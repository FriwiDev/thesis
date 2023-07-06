from esmf_server.configuration_util import ConfigurationUtil

from esmf_server.models import Tunnel, Slice, NetworkConfiguration


class DomainState(object):
    config = ConfigurationUtil.load_configuration_from_disk()
    tunnel_reservations: dict[int, Tunnel] = {}
    tunnel_deployments: dict[int, Tunnel] = {}
    slice_reservations: dict[int, Slice] = {}
    slice_deployments: dict[int, Slice] = {}

    @classmethod
    def get_network(cls, name: str) -> NetworkConfiguration or None:
        for net in cls.config.networks:
            if net.name == name:
                return net
        return None
