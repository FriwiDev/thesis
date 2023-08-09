from esmf_client.model.endpoint import Endpoint
from esmf_client.model.slice import Slice
from host_client.test_result_mapper import TestResultMapper
from host_client.test_utilities import iperf3, sockperf, udp_ping


class TestSlice(object):
    def __init__(self, data: dict):
        self.name = data["name"]
        self.slice_id = -1
        self.slice_id_rev = -1
        self.data = data

    def get_slices(self, localhost: str, default_slice_rate: int) -> tuple[Slice or None, Slice or None]:
        if self.data["initiator"] != localhost:
            return None, None
        sl = Slice(slice_id=self.slice_id,
                   min_rate=int(self.data["min_rate"]),
                   max_rate=int(self.data["max_rate"]),
                   burst_rate=int(self.data["burst_rate"]),
                   latency=int(self.data["latency"]),
                   tunnel_id=-1,
                   transport_protocol=self.data["transport_protocol"],
                   fr=Endpoint(self.data["fr"]),
                   to=Endpoint(self.data["to"]))
        slice_rev = Slice(slice_id=self.slice_id_rev,
                          min_rate=max(default_slice_rate, int(self.data["reverse_min_rate"])),
                          max_rate=max(int(default_slice_rate * 1.1), int(self.data["reverse_max_rate"])),
                          burst_rate=max(int(default_slice_rate * 1.2), int(self.data["reverse_burst_rate"])),
                          latency=int(self.data["latency"]),
                          tunnel_id=-1,
                          transport_protocol=self.data["transport_protocol"],
                          fr=Endpoint(self.data["to"]),
                          to=Endpoint(self.data["fr"]))
        return sl, slice_rev

    def cosume_slices(self, localhost: str, consume: list[Slice]):
        if self.data["initiator"] != localhost:
            return
        self.slice_id = consume.pop(0)["slice_id"]
        self.slice_id_rev = consume.pop(0)["slice_id"]

    def test_slice_client(self, localhost: str, reverse: bool, suite: str,
                          duration_per_test: int, default_slice_rate: int) -> dict or None:
        if self.data["initiator"] != localhost:
            return None
        if reverse:
            # Check if there even is a reverse slice
            if "reverse_max_rate" not in self.data.keys() or int(self.data["reverse_max_rate"]) <= 0:
                return None
        if suite == "IPERF":
            client = iperf3.IPerf3Client(self.data["to" if self.data["fr"]["name"] == localhost else "fr"]["ip"],
                                         int(self.data["to" if self.data["fr"]["name"] == localhost else "fr"]["port"]),
                                         self.data["transport_protocol"],
                                         self.data["fr" if self.data["fr"]["name"] == localhost else "to"]["ip"],
                                         int(self.data["fr" if self.data["fr"]["name"] == localhost else "to"]["port"]),
                                         int(self.data["reverse_max_rate" if reverse else "max_rate"]),
                                         duration_per_test,
                                         reverse)
            print("Starting an iperf client on " + client.client_ip + ":" + str(
                client.client_port) + " to " + client.bind_addr + ":" + str(
                client.bind_port) + " with protocol " + client.protocol + " (reverse=" + str(client.reverse) + ")...")
            return TestResultMapper.map_test_result(client.run())  # Translate results
        elif suite == "SOCKPERF":
            if reverse:
                print("Warning: Can not use sockperf to test reverse direction (server->client). "
                      "Testing from the other side is required to obtain inverse data!")
                return None
            client = sockperf.SockperfClient(self.data["to" if self.data["fr"]["name"] == localhost else "fr"]["ip"],
                                             int(self.data["to" if self.data["fr"]["name"] == localhost else "fr"][
                                                     "port"]),
                                             self.data["transport_protocol"],
                                             self.data["fr" if self.data["fr"]["name"] == localhost else "to"]["ip"],
                                             int(self.data["fr" if self.data["fr"]["name"] == localhost else "to"][
                                                     "port"]),
                                             int(self.data["reverse_max_rate" if reverse else "max_rate"]),
                                             duration_per_test)
            print("Starting a sockperf client on " + client.client_ip + ":" + str(
                client.client_port) + " to " + client.bind_addr + ":" + str(
                client.bind_port) + " with protocol " + client.protocol + " (reverse=" + str(reverse) + ")...")
            return TestResultMapper.map_test_result(client.run())  # Translate results
        elif suite == "UDP_PING":
            if reverse:
                print("Warning: udp_ping only supports bidirectional testing of slices")
                return None
            if self.data["transport_protocol"] != "UDP":
                print("Warning: udp_ping only supports udp protocol (obviously)")
                return None
            client = udp_ping.UDPPingClient(self.data["fr" if self.data["fr"]["name"] == localhost else "to"]["ip"],
                                            int(self.data["fr" if self.data["fr"]["name"] == localhost else "to"][
                                                    "port"]),
                                            self.data["to" if self.data["fr"]["name"] == localhost else "fr"]["ip"],
                                            int(self.data["to" if self.data["fr"]["name"] == localhost else "fr"][
                                                    "port"]),
                                            self.data["max_rate"],
                                            max(self.data["reverse_max_rate"], default_slice_rate),
                                            duration_per_test)
            print("Starting a udp_ping client on " + client.bind_ip + ":" + str(
                client.bind_port) + " to " + client.remote_ip + ":" + str(
                client.remote_port) + "...")
            return TestResultMapper.map_test_result(client.run())  # Translate results

        else:
            raise Exception("Unknown test suite: " + suite)

    def test_slice_server(self, localhost: str, suite: str):
        if self.data["initiator"] == localhost:
            return
        if suite == "IPERF":
            server = iperf3.IPerf3Server(self.data["fr" if self.data["fr"]["name"] == localhost else "to"]["ip"],
                                         int(self.data["fr" if self.data["fr"]["name"] == localhost else "to"]["port"]))
            print("Starting an iperf server on " + server.bind_addr + ":" + str(server.bind_port) + "...")
            server.run()
        elif suite == "SOCKPERF":
            server = sockperf.SockperfServer(self.data["fr" if self.data["fr"]["name"] == localhost else "to"]["ip"],
                                             int(self.data["fr" if self.data["fr"]["name"] == localhost else "to"][
                                                     "port"]),
                                             self.data["transport_protocol"])
            print("Starting a sockperf server on " + server.bind_addr + ":" + str(server.bind_port) + "...")
            server.run()
        elif suite == "UDP_PING":
            if self.data["transport_protocol"] != "UDP":
                print("Warning: udp_ping only supports udp protocol (obviously)")
                return None
            server = udp_ping.UDPPingServer(self.data["fr" if self.data["fr"]["name"] == localhost else "to"]["ip"],
                                            int(self.data["fr" if self.data["fr"]["name"] == localhost else "to"][
                                                    "port"]))
            print("Starting a udp_ping server on " + server.bind_ip + ":" + str(server.bind_port) + "...")
            server.run()
        else:
            raise Exception("Unknown test suite: " + suite)
