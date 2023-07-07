from esmf_server.impl.domain_state import DomainState
from esmf_server.impl.domain_util import DomainUtil

from esmf_server.impl.dsmf_communicator import DSMFCommunicator

from esmf_server.impl.esmf_communicator import ESMFCommunicator
from esmf_server.models import Tunnel, Slice, NetworkConfiguration, Endpoint


class DeployedSlice(object):
    def __init__(self, sl: Slice, owner: str, networks: [str]):
        self.sl = sl
        self.owner = owner
        self.networks = networks


class DeployedTunnel(object):
    def __init__(self, tunnel: Tunnel, networks: [str]):
        self.tunnel = tunnel
        self.networks = networks


class EdgeState(object):
    current_slice_id = DomainState.config.slice_id_range.fr
    current_tunnel_id = DomainState.config.tunnel_id_range.fr
    slices: dict[int, DeployedSlice] = {}
    tunnels: dict[int, DeployedTunnel] = {}

    @classmethod
    def handle_slice_request(cls, slices: [Slice], owner: str) -> int or [Slice]:
        # TODO-FW Resource limits per owner?
        for sl in slices:
            if sl.fr.network != DomainState.config.network and sl.to.network != DomainState.config.network:
                return 422
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
            tunnel_id = cls.current_tunnel_id
            cls.current_tunnel_id += 1
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
                return 500

        # TO tunnels
        for to, values in to_cap.items():
            min_rate, max_rate, burst_rate, latency = values
            tunnel_id = cls.current_tunnel_id
            cls.current_tunnel_id += 1
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
                return 500

        staged_slices = []  # slice, [networks]
        # Slices
        for sl in slices:
            tunnel = None
            if sl.fr.network != DomainState.config.network:
                tunnel = from_tunnels[sl.fr.network]
            elif sl.to.network != DomainState.config.network:
                tunnel = to_tunnels[sl.to.network]
            networks = DomainUtil.route_network(sl.fr.network, sl.to.network)
            slice_id = cls.current_slice_id
            cls.current_slice_id += 1
            sl.slice_id = slice_id
            sl.tunnel_id = tunnel.tunnel_id
            staged_slices.append((sl, networks))
            if not cls.reserve_slice(sl, networks):
                # Roll back everything if we failed
                for s, nets in staged_slices:
                    cls.delete_reserved_slice(s, nets)
                for t, nets in staged_tunnels:
                    cls.delete_reserved_tunnel(t, nets)
                return 500

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

        # Add to our state
        for t, nets in deployed_tunnels:
            cls.tunnels[t.tunnel_id] = DeployedTunnel(t, nets)
        for sl, nets in deployed_slices:
            cls.slices[sl.slice_id] = DeployedSlice(sl, owner, nets)

        # Return the deployed slices
        ret = []
        for sl, nets in deployed_slices:
            ret.append(sl)

        return ret

    @classmethod
    def get_slices_by_owner(cls, owner: str) -> [Slice]:
        ret = []
        for sl in cls.slices.values():
            if sl.owner == owner:
                ret.append(sl.sl)
        return ret

    @classmethod
    def handle_slice_revoke(cls, slice_ids: [int], owner: str) -> int:
        sd = []
        # Find all requested slices
        for i in slice_ids:
            if i not in cls.slices.keys() or cls.slices[i].owner != owner:
                return 404
            sd.append(cls.slices[i])

        # Delete all found slices
        for s in sd:
            if not cls.delete_deployed_slice(s.sl, s.networks):
                return 500
            del cls.slices[s.sl.slice_id]

        # Delete all unused tunnels
        for t in cls.tunnels.copy().values():
            if not cls.is_used(t.tunnel.tunnel_id):
                if not cls.delete_deployed_tunnel(t.tunnel, t.networks):
                    return 500
                del cls.tunnels[t.tunnel.tunnel_id]

        return 200

    @classmethod
    def is_used(cls, tunnel_id: int) -> bool:
        for sl in cls.slices.values():
            if sl.sl.tunnel_id == tunnel_id:
                return True
        return False

    @classmethod
    def reserve_tunnel(cls, tunnel: Tunnel, networks: [str]) -> bool:
        for net in networks:
            if net == DomainState.config.network:
                if not DSMFCommunicator.reserve_tunnel(tunnel):
                    return False
            else:
                if not ESMFCommunicator.reserve_tunnel(tunnel, net):
                    return False
        return True

    @classmethod
    def delete_reserved_tunnel(cls, tunnel: Tunnel, networks: [str]) -> bool:
        for net in networks:
            if net == DomainState.config.network:
                if not DSMFCommunicator.delete_reserved_tunnel(tunnel):
                    return False
            else:
                if not ESMFCommunicator.delete_reserved_tunnel(tunnel, net):
                    return False
        return True

    @classmethod
    def deploy_tunnel(cls, tunnel: Tunnel, networks: [str]) -> bool:
        for net in networks:
            if net == DomainState.config.network:
                if not DSMFCommunicator.deploy_tunnel(tunnel):
                    return False
            else:
                if not ESMFCommunicator.deploy_tunnel(tunnel, net):
                    return False
        return True

    @classmethod
    def delete_deployed_tunnel(cls, tunnel: Tunnel, networks: [str]) -> bool:
        for net in networks:
            if net == DomainState.config.network:
                if not DSMFCommunicator.delete_deployed_tunnel(tunnel):
                    return False
            else:
                if not ESMFCommunicator.delete_deployed_tunnel(tunnel, net):
                    return False
        return True

    @classmethod
    def reserve_slice(cls, sl: Slice, networks: [str]) -> bool:
        networks = [networks[0], networks[len(networks)-1]]
        for net in networks:
            if net == DomainState.config.network:
                if not DSMFCommunicator.reserve_slice(sl):
                    return False
            else:
                if not ESMFCommunicator.reserve_slice(sl, net):
                    return False
        return True

    @classmethod
    def delete_reserved_slice(cls, sl: Slice, networks: [str]) -> bool:
        networks = [networks[0], networks[len(networks) - 1]]
        for net in networks:
            if net == DomainState.config.network:
                if not DSMFCommunicator.delete_reserved_slice(sl):
                    return False
            else:
                if not ESMFCommunicator.delete_reserved_slice(sl, net):
                    return False
        return True

    @classmethod
    def deploy_slice(cls, sl: Slice, networks: [str]) -> bool:
        networks = [networks[0], networks[len(networks) - 1]]
        for net in networks:
            if net == DomainState.config.network:
                if not DSMFCommunicator.deploy_slice(sl):
                    return False
            else:
                if not ESMFCommunicator.deploy_slice(sl, net):
                    return False
        return True

    @classmethod
    def delete_deployed_slice(cls, sl: Slice, networks: [str]) -> bool:
        networks = [networks[0], networks[len(networks) - 1]]
        for net in networks:
            if net == DomainState.config.network:
                if not DSMFCommunicator.delete_deployed_slice(sl):
                    return False
            else:
                if not ESMFCommunicator.delete_deployed_slice(sl, net):
                    return False
        return True
