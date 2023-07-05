import heapq as hq
import math

from dsmf_server.models import DeviceConfiguration, ConnectionConfiguration
from dsmf_server.impl.domain_state import DomainState, DeviceType


class DomainUtil(object):
    @classmethod
    def route_network(cls, fr: str, to: str) -> [str]:
        # index -> index with weight
        graph: [[(int, int)]] = [[(DomainUtil.network_index_of(y), 1) for y in x.reachable] for x in
                                 DomainState.config.networks]
        t = DomainUtil.network_index_of(to)

        # Perform dijkstra on graph with start node "to"
        path, weights = DomainUtil.dijkstra(graph, t)

        # Now traverse the path to get our result. Each element in the path array refers to the node index closer to the
        # destination node on the shortest path.
        s = DomainUtil.network_index_of(fr)
        ret = []
        while s != t:
            ret.append(DomainState.config.networks[s].name)
            s = path[s]
        ret.append(DomainState.config.networks[t].name)

        # Return the resulting dumped data. Will contain elements [fr, ..., to]
        return ret

    @classmethod
    def route_slice(cls, host: str, vpn_gateway: str, begin: bool) -> ([str], [DeviceType]):
        # Builds the route from host to vpn or from vpn to host

        # Build a device list using our host, our vpn gateway and all our available switches
        devs = [DeviceConfiguration(name=host, connections=[ConnectionConfiguration(other_end=s.name) for s in
                                                            DomainUtil.find_switches_with_connection_to(host)]),
                DeviceConfiguration(name=vpn_gateway, connections=[ConnectionConfiguration(other_end=s.name) for s in
                                                                   DomainUtil.find_switches_with_connection_to(
                                                                       vpn_gateway)])]
        for s in DomainState.config.switches:
            devs.append(s)

        # index -> index with weight
        graph: [[(int, int)]] = [[(DomainUtil.device_index_of(y.other_end, devs), 1) for y in x.connections] for x in
                                 devs]
        t_name = vpn_gateway if begin else host
        t = DomainUtil.device_index_of(t_name, devs)

        # Perform dijkstra on graph with start node "to"
        path, weights = DomainUtil.dijkstra(graph, t)

        # Now traverse the path to get our result. Each element in the path array refers to the node index closer to the
        # destination node on the shortest path.
        s = DomainUtil.device_index_of(host if begin else vpn_gateway, devs)
        ret = []
        while s != t:
            ret.append(devs[s].name)
            s = path[s]
        ret.append(t_name)

        # Build the roles
        roles = [DeviceType.SRC if begin else DeviceType.TUN_EXIT]
        if len(ret) == 3:
            # In this case we use an ALL type switch in the middle, as we need to merge ENTRY and EXIT switches
            if begin:
                roles.append(DeviceType.SRC_ALL)
            else:
                roles.append(DeviceType.DST_ALL)
        else:
            # Generate a switch cascade with <SRC/DST>_ENTRY -> <SRC/DST>_TP* -> <SRC/DST>_EXIT
            if begin:
                roles.append(DeviceType.SRC_ENTRY)
                for i in range(len(ret) - 4):
                    roles.append(DeviceType.SRC_TP)
                roles.append(DeviceType.SRC_EXIT)
            else:
                roles.append(DeviceType.DST_ENTRY)
                for i in range(len(ret) - 4):
                    roles.append(DeviceType.DST_TP)
                roles.append(DeviceType.DST_EXIT)
        # Add our ending devices
        if begin:
            roles.append(DeviceType.TUN_ENTRY)
        else:
            roles.append(DeviceType.DST)

        # Return the resulting dumped data. Will contain elements [host, ..., vpn_gateway] or [vpn_gateway, ..., host]
        # The second array will contain the roles with same indexes
        return ret, roles

    @classmethod
    def route_tunnel(cls, tun_entry: str, tun_exit: str, previous_network: str, next_network: str) -> (
            [str], [DeviceType]):
        # Builds the route from vpn entry to exit

        # Determine our actual source and target (we have partial view)
        src = tun_entry
        first_dev = None  # The first device on our territory
        if previous_network != DomainState.config.network:
            # Select a device name that is a border to the target network
            for border in DomainState.config.network_borders:
                if border.network_name == previous_network:
                    first_dev = border.device_name
                    src = border.connection.other_end
                    break
            if not first_dev:
                raise Exception("Could not reach network " + previous_network + " from our POV - please adjust config")

        dst = tun_exit
        last_dev = None  # The last device on our territory
        if next_network != DomainState.config.network:
            # Select a device name that is a border to the target network
            for border in DomainState.config.network_borders:
                if border.network_name == next_network:
                    last_dev = border.device_name
                    dst = border.connection.other_end
                    break
            if not first_dev:
                raise Exception("Could not reach network " + next_network + " from our POV - please adjust config")

        # Build a device list using first and last out of view devices, along with our available switches
        devs = []

        if first_dev:
            # We have a previous network, so we insert a virtual device connected to first_dev
            devs.append(DeviceConfiguration(name=src, connections=[ConnectionConfiguration(other_end=first_dev)]))

        if last_dev:
            # We have a next network, so we insert a virtual device connected to last_dev
            devs.append(DeviceConfiguration(name=dst, connections=[ConnectionConfiguration(other_end=last_dev)]))

        # Add all other devices (including vpn gateways to allow us to be first/final network)
        for s in DomainState.config.switches:
            devs.append(s)

        for s in DomainState.config.vpn_gateways:
            devs.append(s)

        # index -> index with weight
        graph: [[(int, int)]] = [[(DomainUtil.device_index_of(y.other_end, devs), 1) for y in x.connections] for x in
                                 devs]
        t = DomainUtil.device_index_of(dst, devs)

        # Perform dijkstra on graph with start node "to"
        path, weights = DomainUtil.dijkstra(graph, t)

        # Now traverse the path to get our result. Each element in the path array refers to the node index closer to the
        # destination node on the shortest path.
        s = DomainUtil.device_index_of(src, devs)
        ret = []
        while s != t:
            ret.append(devs[s].name)
            s = path[s]
        ret.append(dst)

        # Build the roles
        roles = []
        if src == tun_entry and dst == tun_exit and len(ret) == 3:
            # We see everything and definitly manage the middle switch. Mark it as ALL here (it is enough if we know)
            roles.append(DeviceType.TUN_ENTRY)
            roles.append(DeviceType.BN_ALL)
            roles.append(DeviceType.TUN_EXIT)
        else:
            if src == tun_entry:
                # Our first device is a begin switch
                roles.append(DeviceType.TUN_ENTRY)
                roles.append(DeviceType.BN_BEGIN)
            else:
                # Our first device is a tp switch
                roles.append(DeviceType.BN_BEGIN)  # We do not care if it is a TP or BEGIN switch
                roles.append(DeviceType.BN_TP)

            # Fill all but last two with transport switches (also substract the first two from range)
            for i in range(len(ret) - 4):
                roles.append(DeviceType.BN_TP)

            if dst == tun_exit:
                # Our last device is an end switch
                roles.append(DeviceType.BN_END)
                roles.append(DeviceType.TUN_EXIT)
            else:
                # Our last device is a tp switch
                roles.append(DeviceType.BN_TP)
                roles.append(DeviceType.BN_END)  # We do not care if it is a TP or END switch

        # Return the resulting dumped data. Will contain elements [src, ..., dst], where src and dst are either
        # a) The previous or next device in another network
        # b) The tunnel entry or exit themselves if on our network (or matching a)
        # The second array will contain the roles with same indexes
        return ret, roles

    @classmethod
    def find_switches_with_connection_to(cls, to: str) -> [str]:
        ret = []
        for switch in DomainState.config.switches:
            for connection in switch.connections:
                if connection.other_end == to:
                    ret.append(switch.name)
                    break
        return ret

    @classmethod
    def network_index_of(cls, net: str) -> int:
        i = 0
        for network in DomainState.config.networks:
            if network.name == net:
                return i
            i += 1
        return -1

    @classmethod
    def device_index_of(cls, device: str, devs: [DeviceConfiguration]) -> int:
        i = 0
        for dev in devs:
            if dev.name == device:
                return i
            i += 1
        return -1

    @classmethod
    def port_index_of_switch(cls, device: DeviceConfiguration, other: str) -> int:
        for conn in device.connections:
            if conn.other_end == other:
                return conn.intf_id
        return -1

    @classmethod
    def port_name_of_switch(cls, device: DeviceConfiguration, other: str) -> str or None:
        for conn in device.connections:
            if conn.other_end == other:
                return conn.intf_name
        return None

    @classmethod
    def switch_index_of(cls, name: str) -> int:
        i = 0
        for switch in DomainState.config.switches:
            if switch.name == name:
                return i
            i += 1
        return -1

    @classmethod
    # https://stackoverflow.com/a/56740241
    def dijkstra(cls, graph: list[list[(int, int)]], s: int):
        n = len(graph)
        visited = [False] * n
        weights = [math.inf] * n
        path = [None] * n
        queue = []
        weights[s] = 0
        hq.heappush(queue, (0, s))
        while len(queue) > 0:
            g, u = hq.heappop(queue)
            visited[u] = True
            for v, w in graph[u]:
                if not visited[v]:
                    f = g + w
                    if f < weights[v]:
                        weights[v] = f
                        path[v] = u
                        hq.heappush(queue, (f, v))
        return path, weights
