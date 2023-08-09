"""
This is our small library to get some performance metrics via UDP including latency.
Sadly latency is not supported by iperf3, only tcp round trip time can be measured.
We will thus use a token bucket implementation to create a continuous stream of packets towards our target
and then receive reports back from our target that will allow us to derive latency, loss and bandwidth
on the connection.

Warning: Does not consider duplicate packets arriving!

Packet structure:
ETH | IP | UDP | start_time: int64 | packet_num: int64 | seen_packets: int64 | packet_time: int64 | client_rate: int64 | server_rate: int64 | padding to fixed bytes

Where:
start_time: Client start time of our flow. If the server sees a new start time it will inherit it and start a new flow.
                Will be -1 when flow should be finished for computations by the client.
packet_num: The number of this packet within our flow.
seen_packets: Sent by the server to the client to indicate the amount of packets seen in this flow so far. 0 is sent by
                the client.
packet_time: The client always sends current time millis. The server sends the last known client packet time (latency).
client_rate: The rate at which the client sends packets in bps. Server always sends 0.
server_rate: The rate at which the server should respond in bps. Server always sends 0.
padding: Some padding to make packets a bit longer.
"""
import socket
import time
from threading import Thread
from time import sleep

from token_bucket import MemoryStorage, Limiter

from host_client.test_utilities.general import TestUtility

# Somehow udp packets seem to always be 384 byte when we send them.
TARGET_PACKET_SIZE = 384
PACKET_HEADER_SIZE = 256  # This seems not even relevant, as packets seem to get padded to 384 by python anyways.
PRECISION_BITS = 64


class TestResult(object):
    def __init__(self, latency_ms: float,
                 loss: float, loss_rev: float,
                 lost_messages: int, lost_messages_rev: int,
                 bps: float, bps_rev: float):
        self.latency_ms = latency_ms
        self.loss = loss
        self.loss_rev = loss_rev
        self.lost_messages = lost_messages
        self.lost_messages_rev = lost_messages_rev
        self.bps = bps
        self.bps_rev = bps_rev


class UDPPingPacket(object):
    def __init__(self, remote_ip: str, remote_port: int, start_time: int, packet_num: int, seen_packets: int,
                 packet_time: int, client_rate: int, server_rate: int):
        self.remote_ip = remote_ip
        self.remote_port = remote_port
        self.start_time = start_time
        self.packet_num = packet_num
        self.seen_packets = seen_packets
        self.packet_time = packet_time
        self.client_rate = client_rate
        self.server_rate = server_rate

    def __str__(self):
        return f"Packet ({self.start_time}, {self.packet_num}, {self.seen_packets}, {self.packet_time}, {self.client_rate}, {self.server_rate})"


class UDPPingClient(TestUtility):

    def __init__(self, bind_ip: str, bind_port: int, remote_ip: str, remote_port: int, client_rate: int,
                 server_rate: int, time: int):
        self.bind_ip = bind_ip
        self.bind_port = bind_port
        self.token_bucket: Limiter or None = None
        self.remote_ip = remote_ip
        self.remote_port = remote_port
        self.client_rate = client_rate
        self.server_rate = server_rate
        self.token_bucket = Limiter(rate=client_rate, capacity=int(client_rate / 3), storage=MemoryStorage())
        self.current_flow_start = -1
        self.packet_num = 0
        self.seen_packets = 0
        self.sock: socket or None = None
        self.shutdown = False
        self.time = time
        self.sum_latency = 0

    def run(self) -> TestResult:
        # Create and bind socket
        self.sock = socket.socket(socket.AF_INET,  # Internet
                                  socket.SOCK_DGRAM)  # UDP
        if self.bind_ip and self.bind_port:
            self.sock.bind((self.bind_ip, self.bind_port))
        # Run sender thread
        sender_thread = Thread(target=self._run_sender)
        sender_thread.start()
        # Wait a short time to make sure server is reset
        sleep(0.1)
        # Initialize our flow
        self.current_flow_start = time.time_ns()
        # Run listen thread for self.time seconds
        while self.current_flow_start + self.time * 1000000000 > time.time_ns():
            data, addr = self.sock.recvfrom(1024)
            host, port = addr
            packet = parse_packet(host, port, bytearray(data))
            if packet.start_time == self.current_flow_start:
                self.seen_packets += 1
                self.sum_latency += time.time_ns() - packet.packet_time
        # Stop measurement on server side
        self.current_flow_start = -1
        # Wait for a packet from server with flow start -1 to get final values
        final_packet: UDPPingPacket or None = None
        while True:
            data, addr = self.sock.recvfrom(1024)
            host, port = addr
            packet = parse_packet(host, port, bytearray(data))
            if packet.start_time == -1:
                final_packet = packet
                break
            elif packet.start_time == self.current_flow_start:
                self.seen_packets += 1
                self.sum_latency += time.time_ns() - packet.packet_time
        # Shutdown self
        self.shutdown = True
        # Build result from our and origin data
        latency_ms = self.sum_latency / self.seen_packets / 1000000
        loss = 1 - (final_packet.seen_packets + 1) / self.packet_num  # We always "loose" a frame due to our counters
        loss_rev = 1 - self.seen_packets / final_packet.packet_num
        lost_messages = self.packet_num - (final_packet.seen_packets + 1)
        lost_messages_rev = final_packet.packet_num - self.seen_packets
        bps = final_packet.seen_packets * TARGET_PACKET_SIZE * 8 / self.time
        bps_rev = self.seen_packets * TARGET_PACKET_SIZE * 8 / self.time
        return TestResult(latency_ms, loss, loss_rev, lost_messages, lost_messages_rev, bps, bps_rev)

    def _run_sender(self):
        while not self.shutdown:
            if self.token_bucket and self.token_bucket.consume('A', TARGET_PACKET_SIZE * 8):
                # We can send a new packet now
                p = UDPPingPacket(self.remote_ip, self.remote_port, self.current_flow_start, self.packet_num,
                                  self.seen_packets, time.time_ns(), self.client_rate, self.server_rate)
                self.sock.sendto(craft_packet(p), (self.remote_ip, self.remote_port))
                if self.current_flow_start != -1:
                    self.packet_num += 1
            else:
                sleep(0.0001)
        self.sock.close()


class UDPPingServer(TestUtility):

    def __init__(self, bind_ip: str, bind_port: int):
        self.bind_ip = bind_ip
        self.bind_port = bind_port
        self.token_bucket: Limiter or None = None
        self.remote_ip: str or None = None
        self.remote_port: int or None = None
        self.current_flow_start = -1
        self.packet_num = 0
        self.seen_packets = 0
        self.packet_time = 0
        self.sock: socket or None = None
        self.pause_until = 0
        self.last_packet_received = 0

    def run(self) -> TestResult:
        # Create and bind socket
        self.sock = socket.socket(socket.AF_INET,  # Internet
                                  socket.SOCK_DGRAM)  # UDP
        self.sock.bind((self.bind_ip, self.bind_port))
        # Run sender thread
        sender_thread = Thread(target=self._run_sender)
        sender_thread.start()
        # Run listen thread
        while True:
            data, addr = self.sock.recvfrom(1024)  # buffer size is 1024 bytes
            host, port = addr
            packet = parse_packet(host, port, bytearray(data))
            if packet.start_time == -1:
                # Client wishes to clean up, so we freeze our statistics and keep on sending
                if self.current_flow_start != -1:
                    self.pause_until = time.time_ns() + int(300 * 1000 * 1000)
                self.current_flow_start = -1
                continue
            self.last_packet_received = time.time_ns()
            if self.current_flow_start < packet.start_time and self.pause_until < time.time_ns():
                # We are now in a new flow -> reset and apply everything
                self.token_bucket = None
                self.remote_ip = host
                self.remote_port = port
                self.current_flow_start = packet.start_time
                self.packet_num = 0
                self.seen_packets = 0
                self.packet_time = max(self.packet_time, packet.packet_time)
                self.token_bucket = Limiter(rate=packet.server_rate, capacity=int(packet.server_rate / 3),
                                            storage=MemoryStorage())
            else:
                # We continue along our flow and just increase packet counters
                self.seen_packets += 1
                self.packet_time = max(self.packet_time, packet.packet_time)
        self.sock.close()
        return TestResult(0, 0, 0, 0, 0, 0, 0)

    def _run_sender(self):
        while True:
            if self.pause_until > time.time_ns():
                # Wait for packets to trickle in if we should end test
                continue
            if self.token_bucket and self.token_bucket.consume('A', TARGET_PACKET_SIZE * 8):
                # We can send a new packet now
                p = UDPPingPacket(self.remote_ip, self.remote_port, self.current_flow_start, self.packet_num,
                                  self.seen_packets, self.packet_time + (time.time_ns() - self.last_packet_received), 0,
                                  0)
                self.sock.sendto(craft_packet(p), (self.remote_ip, self.remote_port))
                if self.current_flow_start != -1:
                    self.packet_num += 1
            else:
                sleep(0.0001)


def craft_packet(packet: UDPPingPacket) -> bytearray:
    ret = bytearray(TARGET_PACKET_SIZE - PACKET_HEADER_SIZE)
    i = 0
    for add in [packet.start_time, packet.packet_num, packet.seen_packets,
                packet.packet_time, packet.client_rate, packet.server_rate]:
        ret[i * PRECISION_BITS:(i + 1) * PRECISION_BITS] = add.to_bytes(PRECISION_BITS, 'big', signed=True)
        i += 1
    return ret


def parse_packet(remote_ip: str, remote_port: int, in_packet: bytearray) -> UDPPingPacket:
    ret = []
    for i in range(0, 6):
        ret.append(int.from_bytes(in_packet[i * PRECISION_BITS:(i + 1) * PRECISION_BITS], 'big', signed=True))
    return UDPPingPacket(remote_ip, remote_port, ret[0], ret[1], ret[2], ret[3], ret[4], ret[5])
