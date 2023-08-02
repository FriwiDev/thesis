from typing import Dict

from esmf_server.impl.configuration_util import ConfigurationUtil

from esmf_server.models import Tunnel, Slice, NetworkConfiguration, DeviceConfiguration


class DomainState(object):
    config = ConfigurationUtil.load_configuration_from_disk()
    tunnel_reservations: Dict[int, Tunnel] = {}
    tunnel_deployments: Dict[int, Tunnel] = {}
    slice_reservations: Dict[int, Slice] = {}
    slice_deployments: Dict[int, Slice] = {}

    @classmethod
    def get_network(cls, name: str) -> NetworkConfiguration or None:
        for net in cls.config.networks:
            if net.name == name:
                return net
        return None

    @classmethod
    def get_coordinator_by_network(cls, name: str) -> DeviceConfiguration or None:
        for coordinator in cls.config.coordinators:
            if coordinator.network == name:
                return coordinator
        return None

    @classmethod
    def get_vpn_by_network(cls, fr: str, to: str) -> DeviceConfiguration or None:
        # TODO-FW consider multiple vpn devices per network -> more complex routing
        for net in cls.config.networks:
            if net.name == fr:
                for dev in cls.config.vpn_gateways:
                    if dev.name == net.preferred_vpn[0]:
                        return dev
                break
        return None
