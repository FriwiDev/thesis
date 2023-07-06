from dsmf_server.impl.domain_state import DomainState
from esmf_server.impl.domain_util import DomainUtil
from esmf_server.models import Tunnel, Slice, NetworkConfiguration, Endpoint


class EdgeState(object):
    slices: dict[int, Slice] = {}
    slices_per_owner: dict[str, [Slice]] = {}
    tunnels: dict[int, Tunnel] = {}
    tunnels_per_src_net: dict[str, [Tunnel]] = {}
    tunnels_per_dst_net: dict[str, [Tunnel]] = {}


    @classmethod
    def handle_slice_request(cls, slices: [Slice], owner: str) -> bool:
        # TODO-FW Resource limits per owner?
        for sl in slices:
            if sl.fr.network != DomainState.config.network and sl.to.network != DomainState.config.network:
                return False
        # Calculate the required capacity per target (to and from)
        to_cap = {}  # network -> min_rate, max_rate, burst_rate, latency
        from_cap = {}  # network -> min_rate, max_rate, burst_rate, latency
        for sl in slices:
            if sl.fr.network != DomainState.config.network:
                min_rate, max_rate, burst_rate, latency = (100, 100, 100, 20000)
                if sl.fr.network in from_cap.keys():
                    min_rate, max_rate, burst_rate, latency = from_cap[sl.fr.network]
                min_rate += sl.min_rate
                max_rate += sl.max_rate
                burst_rate += sl.burst_rate
                latency = min(latency, sl.latency)
                from_cap[sl.fr.network] = (min_rate, max_rate, burst_rate, latency)
            elif sl.to.network != DomainState.config.network:
                min_rate, max_rate, burst_rate, latency = (100, 100, 100, 20000)
                if sl.to.network in to_cap.keys():
                    min_rate, max_rate, burst_rate, latency = to_cap[sl.to.network]
                min_rate += sl.min_rate
                max_rate += sl.max_rate
                burst_rate += sl.burst_rate
                latency = min(latency, sl.latency)
                to_cap[sl.to.network] = (min_rate, max_rate, burst_rate, latency)

        # Now we know how much traffic we will require - now lets build some adequate tunnels
        # TODO-FW Grow and shrink existing tunnels. For now we will just deploy tunnels for all our slices here.
        to_tunnels = {}  # network -> tunnel
        from_tunnels = {}  # network -> tunnel
        staged_tunnels = []  # tunnel, [networks]
        # FROM tunnels
        for fr, values in from_cap.items():
            min_rate, max_rate, burst_rate, latency = values
            tunnel_id = 3  # TODO-NOW
            vpn_fr = DomainState.get_vpn_by_network(fr, DomainState.config.network)
            vpn_to = DomainState.get_vpn_by_network(DomainState.config.network, fr)
            networks = DomainUtil.route_network(fr, DomainState.config.network)
            tunnel = Tunnel(tunnel_id=tunnel_id,
                            min_rate=min_rate,
                            max_rate=max_rate,
                            burst_rate=burst_rate,
                            latency=latency,
                            fr=Endpoint(
                                ip=vpn_fr.ip,
                                port=0,
                                name=vpn_fr.name,
                                network=vpn_fr.network
                            ),
                            to=Endpoint(
                                ip=vpn_to.ip,
                                port=0,
                                name=vpn_to.name,
                                network=vpn_to.network
                            ),
                            private_key=None,  # TODO-NOW
                            public_key=None  # TODO-NOW
                            )
            staged_tunnels.append((tunnel, networks))
            from_tunnels[fr] = tunnel
            if not cls.reserve_tunnel(tunnel, networks):
                # Roll back everything if we failed
                for t, nets in staged_tunnels:
                    cls.delete_reserved_tunnel(t, nets)
                return False

        # TO tunnels
        for to, values in to_cap.items():
            min_rate, max_rate, burst_rate, latency = values
            tunnel_id = 3  # TODO-NOW
            vpn_fr = DomainState.get_vpn_by_network(DomainState.config.network, to)
            vpn_to = DomainState.get_vpn_by_network(to, DomainState.config.network)
            networks = DomainUtil.route_network(DomainState.config.network, to)
            tunnel = Tunnel(tunnel_id=tunnel_id,
                            min_rate=min_rate,
                            max_rate=max_rate,
                            burst_rate=burst_rate,
                            latency=latency,
                            fr=Endpoint(
                                ip=vpn_fr.ip,
                                port=0,
                                name=vpn_fr.name,
                                network=vpn_fr.network
                            ),
                            to=Endpoint(
                                ip=vpn_to.ip,
                                port=0,
                                name=vpn_to.name,
                                network=vpn_to.network
                            ),
                            private_key=None,  # TODO-NOW
                            public_key=None  # TODO-NOW
                            )
            staged_tunnels.append((tunnel, networks))
            to_tunnels[to] = tunnel
            if not cls.reserve_tunnel(tunnel, networks):
                # Roll back everything if we failed
                for t, nets in staged_tunnels:
                    cls.delete_reserved_tunnel(t, nets)
                return False

        staged_slices = []  # slice, [networks]
        # Slices
        for sl in slices:
            tunnel = None
            if sl.fr.network != DomainState.config.network:
                tunnel = from_tunnels[sl.fr.network]
            elif sl.to.network != DomainState.config.network:
                tunnel = to_tunnels[sl.to.network]
            networks = DomainUtil.route_network(sl.fr.network, sl.to.network)
            slice_id = 3  # TODO-NOW
            sl.slice_id = slice_id
            sl.tunnel_id = tunnel.tunnel_id
            staged_slices.append((sl, networks))
            if not cls.reserve_slice(sl, networks):
                # Roll back everything if we failed
                for s, nets in staged_slices:
                    cls.delete_reserved_slice(s, nets)
                for t, nets in staged_tunnels:
                    cls.delete_reserved_tunnel(t, nets)
                return False

        # Now everything is reserved. Let us deploy everything - tunnels first
        deployed_tunnels = []  # tunnel, [networks]
        deployed_slices = []  # slice, [networks]

        for tu, netws in staged_tunnels.copy():
            if not cls.deploy_tunnel(tu, netws):
                # Roll back everything if we failed
                for t, nets in deployed_tunnels:
                    cls.delete_deployed_tunnel(t, nets)
                for s, nets in staged_slices:
                    cls.delete_reserved_slice(s, nets)
                for t, nets in staged_tunnels:
                    cls.delete_reserved_tunnel(t, nets)
                return False
            staged_tunnels.remove((tu, netws))
            deployed_tunnels.append((tu, netws))

        for sl, netws in staged_slices.copy():
            if not cls.deploy_slice(sl, netws):
                # Roll back everything if we failed
                for s, nets in deployed_slices:
                    cls.delete_deployed_slice(s, nets)
                for t, nets in deployed_tunnels:
                    cls.delete_deployed_tunnel(t, nets)
                for s, nets in staged_slices:
                    cls.delete_reserved_slice(s, nets)
                for t, nets in staged_tunnels:
                    cls.delete_reserved_tunnel(t, nets)
                return False
            staged_slices.remove((sl, netws))
            deployed_slices.append((sl, netws))

        # TODO-NOW Integrate new tunnels and slices into data structure above

        return True

    @classmethod
    def reserve_tunnel(cls, tunnel: Tunnel, networks: [str]) -> bool:
        # TODO-NOW implement
        return True

    @classmethod
    def delete_reserved_tunnel(cls, tunnel: Tunnel, networks: [str]) -> bool:
        # TODO-NOW implement
        return True

    @classmethod
    def deploy_tunnel(cls, tunnel: Tunnel, networks: [str]) -> bool:
        # TODO-NOW implement
        return True

    @classmethod
    def delete_deployed_tunnel(cls, tunnel: Tunnel, networks: [str]) -> bool:
        # TODO-NOW implement
        return True

    @classmethod
    def reserve_slice(cls, sl: Slice, networks: [str]) -> bool:
        # TODO-NOW implement
        return True

    @classmethod
    def delete_reserved_slice(cls, sl: Slice, networks: [str]) -> bool:
        # TODO-NOW implement
        return True

    @classmethod
    def deploy_slice(cls, sl: Slice, networks: [str]) -> bool:
        # TODO-NOW implement
        return True

    @classmethod
    def delete_deployed_slice(cls, sl: Slice, networks: [str]) -> bool:
        # TODO-NOW implement
        return True
