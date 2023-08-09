"""
A small wrapper around the sockperf library.
https://github.com/Mellanox/sockperf
"""
import subprocess
from abc import ABC

from host_client.test_utilities.general import TestUtility

# 18 ETH + 20 to 60 IP + 8 UDP + Payload + 4 CRC (from eth) => 50 to 90 bytes
UDP_PACKET_HEADER_SIZE = 18 + 20 + 8 + 4
# 18 ETH + 20 to 60 IP + 20 to 60 TCP + Payload + 4 CRC (from eth) => 62 to 142 bytes
TCP_PACKET_HEADER_SIZE = 18 + 20 + 20 + 4


class TestResult(object):
    def __init__(self, output: str):
        self.min_latency = -1
        self.max_latency = -1
        self.mean_latency = -1
        self.jitter_ms = -1
        self.dropped_messages = -1
        self.duplicated_messages = -1
        self.out_of_order_messages = -1
        if not output.__contains__("====>"):
            # We are server or received an error
            return
        self.min_latency = float(output.split("<MIN> observation =")[1].split("\n")[0].strip()) / 1000
        self.max_latency = float(output.split("<MAX> observation =")[1].split("\n")[0].strip()) / 1000
        self.mean_latency = float(output.split("avg-latency=")[1].split(" ")[0].strip()) / 1000
        self.jitter_ms = float(output.split("std-dev=")[1].split(",")[0].strip()) / 1000
        self.dropped_messages = int(output.split("dropped messages = ")[1].split(";")[0].strip())
        self.duplicated_messages = int(output.split("duplicated messages = ")[1].split(";")[0].strip())
        self.out_of_order_messages = int(output.split("out-of-order messages = ")[1].split("\n")[0].strip())


class Sockperf(TestUtility, ABC):
    def __init__(self, bind_addr: str, bind_port: int, protocol: str):
        super().__init__()
        self.bind_addr = bind_addr
        self.bind_port = bind_port
        self.protocol = protocol


class SockperfServer(Sockperf):
    def __init__(self, bind_addr: str, bind_port: int, protocol: str):
        super().__init__(bind_addr, bind_port, protocol)

    def run(self) -> TestResult:
        cmd = ['sockperf', 'sr', '--addr', self.bind_addr, '--port', str(self.bind_port), '--dontwarmup']
        if self.protocol == "TCP":
            cmd.append('--tcp')
        return TestResult(_run_command(cmd))


class SockperfClient(Sockperf):
    def __init__(self, bind_addr: str, bind_port: int, protocol: str,
                 client_ip: str or None = None, client_port: str or None = None,
                 bps: int = 1000000, time: int = 1):
        super().__init__(bind_addr, bind_port, protocol)
        self.client_ip = client_ip
        self.client_port = client_port
        self.message_size = 128 - (TCP_PACKET_HEADER_SIZE if protocol == "TCP" else UDP_PACKET_HEADER_SIZE)
        self.bps = bps
        self.mps = int(bps / self.message_size / 8)
        self.time = time

    def run(self) -> TestResult:
        cmd = ['sockperf', 'ul', '--addr', self.bind_addr, '--port', str(self.bind_port), '--dontwarmup',
               '--msg-size', str(self.message_size), '--mps', str(self.mps), '--time', str(self.time)]
        if self.protocol == "TCP":
            cmd.append('--tcp')
        if self.client_ip:
            cmd.append('--client_addr')
            cmd.append(self.client_ip)
        if self.client_port:
            cmd.append('--client_port')
            cmd.append(str(self.client_port))
        return TestResult(_run_command(cmd))


def _run_command(cmd: list[str]) -> str:
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')
