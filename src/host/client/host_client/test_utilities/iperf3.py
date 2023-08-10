"""
A small wapper around the iperf3 library.
https://github.com/esnet/iperf

The test result parsing is taken (and modified) from the iperf3-python library by Mathijs Mortimer <mathijs@mortimer.nl>
but the client and server implementations have been recreated to use the CLI of iperf3 instead of the library.
The problem with the library: Starting multiple servers at once is not possible - the library freezes.
https://github.com/thiezn/iperf3-python
"""
import json
import subprocess
from abc import ABC
from typing import List

from host_client.test_utilities.general import TestUtility


class TestResult(object):
    """Class containing iperf3 test results.

    :param text: The raw result from libiperf as text
    :param json: The raw result from libiperf asjson/dict
    :param error: Error captured during test, None if all ok

    :param time: Start time
    :param timesecs: Start time in seconds

    :param system_info: System info
    :param version: Iperf Version

    :param local_host: Local host ip
    :param local_port: Local port number
    :param remote_host: Remote host ip
    :param remote_port: Remote port number

    :param reverse: Test ran in reverse direction
    :param protocol: 'TCP' or 'UDP'
    :param num_streams: Number of test streams
    :param blksize:
    :param omit: Test duration to omit in the beginning in seconds
    :param duration: Test duration (following omit duration) in seconds

    :param local_cpu_total: The local total CPU load
    :param local_cpu_user: The local user CPU load
    :param local_cpu_system: The local system CPU load
    :param remote_cpu_total: The remote total CPU load
    :param remote_cpu_user: The remote user CPU load
    :param remote_cpu_system: The remote system CPU load


    TCP test specific

    :param tcp_mss_default:
    :param retransmits: amount of retransmits (Only returned from client)

    :param sent_bytes: Sent bytes
    :param sent_bps: Sent bits per second
    :param sent_kbps: sent kilobits per second
    :param sent_Mbps: Sent Megabits per second
    :param sent_kB_s: Sent kiloBytes per second
    :param sent_MB_s: Sent MegaBytes per second

    :param received_bytes:  Received bytes
    :param received_bps: Received bits per second
    :param received_kbps: Received kilobits per second
    :param received_Mbps: Received Megabits per second
    :param received_kB_s: Received kiloBytes per second
    :param received_MB_s: Received MegaBytes per second

    :param min_rtt: The minimal round trip time in milliseconds
    :param max_rtt: The maximum round trip time in milliseconds
    :param mean_rtt: The average round trip time in milliseconds


    UDP test specific

    :param bytes:
    :param bps:
    :param jitter_ms:
    :param kbps:
    :param Mbps:
    :param kB_s:
    :param MB_s:
    :param packets:
    :param lost_packets:
    :param lost_percent:
    :param seconds:
    """

    def __init__(self, result: str):
        """Initialise TestResult

        :param result: raw json output from :class:`Client` and :class:`Server`
        """
        # The full result data
        self.text = result
        self.json = json.loads(result)

        self.protocol = None

        if 'error' in self.json:
            self.error = self.json['error']
        else:
            self.error = None
            if 'start' not in self.json:
                return

            # start time
            self.time = self.json['start']['timestamp']['time']
            self.timesecs = self.json['start']['timestamp']['timesecs']

            # generic info
            self.system_info = self.json['start']['system_info']
            self.version = self.json['start']['version']

            # connection details
            connection_details = self.json['start']['connected'][0]
            self.local_host = connection_details['local_host']
            self.local_port = connection_details['local_port']
            self.remote_host = connection_details['remote_host']
            self.remote_port = connection_details['remote_port']

            # test setup
            self.tcp_mss_default = self.json['start'].get('tcp_mss_default')
            self.protocol = self.json['start']['test_start']['protocol']
            self.num_streams = self.json['start']['test_start']['num_streams']
            self.blksize = self.json['start']['test_start']['blksize']
            self.omit = self.json['start']['test_start']['omit']
            self.duration = self.json['start']['test_start']['duration']

            # system performance
            cpu_utilization_perc = self.json['end']['cpu_utilization_percent']
            self.local_cpu_total = cpu_utilization_perc['host_total']
            self.local_cpu_user = cpu_utilization_perc['host_user']
            self.local_cpu_system = cpu_utilization_perc['host_system']
            self.remote_cpu_total = cpu_utilization_perc['remote_total']
            self.remote_cpu_user = cpu_utilization_perc['remote_user']
            self.remote_cpu_system = cpu_utilization_perc['remote_system']

            # TCP specific test results
            if self.protocol == 'TCP':
                sent_json = self.json['end']['sum_sent']
                self.sent_bytes = sent_json['bytes']
                self.sent_bps = sent_json['bits_per_second']

                recv_json = self.json['end']['sum_received']
                self.received_bytes = recv_json['bytes']
                self.received_bps = recv_json['bits_per_second']

                # Bits are measured in 10**3 terms
                # Bytes are measured in 2**10 terms
                # kbps = Kilobits per second
                # Mbps = Megabits per second
                # kB_s = kiloBytes per second
                # MB_s = MegaBytes per second

                self.sent_kbps = self.sent_bps / 1000
                self.sent_Mbps = self.sent_kbps / 1000
                self.sent_kB_s = self.sent_bps / (8 * 1024)
                self.sent_MB_s = self.sent_kB_s / 1024

                self.received_kbps = self.received_bps / 1000
                self.received_Mbps = self.received_kbps / 1000
                self.received_kB_s = self.received_bps / (8 * 1024)
                self.received_MB_s = self.received_kB_s / 1024

                # retransmits only returned from client
                self.retransmits = sent_json.get('retransmits')

                # get rtt from streams
                self.max_rtt = 0
                self.min_rtt = 0
                self.mean_rtt = 0
                mean_div = 0
                for x in self.json['end']['streams']:
                    self.max_rtt = max(self.max_rtt, x['sender']['max_rtt'])
                    if self.min_rtt == 0:
                        self.min_rtt = x['sender']['min_rtt']
                    elif x['sender']['min_rtt'] > 0:
                        self.min_rtt = min(self.min_rtt, x['sender']['min_rtt'])
                    if x['sender']['mean_rtt'] > 0:
                        self.mean_rtt += x['sender']['mean_rtt']
                        mean_div += 1
                if mean_div > 0:
                    self.mean_rtt /= mean_div

            # UDP specific test results
            elif self.protocol == 'UDP':
                self.bytes = self.json['end']['sum']['bytes']
                self.bps = self.json['end']['sum']['bits_per_second']
                self.jitter_ms = self.json['end']['sum']['jitter_ms']
                self.kbps = self.bps / 1000
                self.Mbps = self.kbps / 1000
                self.kB_s = self.bps / (8 * 1024)
                self.MB_s = self.kB_s / 1024
                self.packets = self.json['end']['sum']['packets']
                self.lost_packets = self.json['end']['sum']['lost_packets']
                self.lost_percent = self.json['end']['sum']['lost_percent']
                self.seconds = self.json['end']['sum']['seconds']

    @property
    def reverse(self):
        if self.json['start']['test_start']['reverse']:
            return True
        else:
            return False

    @property
    def type(self):
        if 'connecting_to' in self.json['start']:
            return 'client'
        else:
            return 'server'

    def __repr__(self):
        """Print the result as received from iperf3"""
        return self.text


class IPerf3(TestUtility, ABC):
    def __init__(self, bind_addr: str, bind_port: int):
        super().__init__()
        self.bind_addr = bind_addr
        self.bind_port = bind_port


class IPerf3Server(IPerf3):
    def __init__(self, bind_addr: str, bind_port: int):
        super().__init__(bind_addr, bind_port)

    def run(self) -> TestResult:
        cmd = ['iperf3', '-s', '--bind', self.bind_addr, '--port', str(self.bind_port)]
        return TestResult(_run_command(cmd))


class IPerf3Client(IPerf3):
    def __init__(self, bind_addr: str, bind_port: int, protocol: str,
                 client_ip: str or None = None, client_port: str or None = None,
                 bps: int = 1000000, time: int = 1, reverse: bool = False):
        super().__init__(bind_addr, bind_port)
        self.protocol = protocol
        self.client_ip = client_ip
        self.client_port = client_port
        self.bps = bps
        self.time = time
        self.reverse = reverse

    def run(self) -> TestResult:
        cmd = ['iperf3', '-c', self.bind_addr, '--port', str(self.bind_port), '--bitrate', str(self.bps),
               '--time', str(self.time), '--json']
        if self.protocol == "UDP":
            cmd.append('--udp')
        if self.reverse:
            cmd.append('--reverse')
        if self.client_ip:
            cmd.append('--bind')
            cmd.append(self.client_ip)
        if self.client_port:
            cmd.append('--cport')
            cmd.append(str(self.client_port))
        return TestResult(_run_command(cmd))


def _run_command(cmd: List[str]) -> str:
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')
