from enum import Enum

from dsmf_server.configuration_util import ConfigurationUtil
from dsmf_server.models import Tunnel, Slice, DeviceConfiguration, NetworkConfiguration

DeviceType = Enum('SwitchType',
                  ['SRC', 'DST', 'TUN_ENTRY', 'TUN_EXIT', 'SRC_ALL', 'SRC_ENTRY', 'SRC_TP', 'SRC_EXIT', 'BN_ALL',
                   'BN_BEGIN', 'BN_TP', 'BN_END', 'DST_ALL',
                   'DST_BEGIN', 'DST_TP', 'DST_EXIT'])


class DomainState(object):
    config = ConfigurationUtil.load_configuration_from_disk()
    tunnel_reservations: dict[int, Tunnel] = {}
    tunnel_deployments: dict[int, Tunnel] = {}
    slice_reservations: dict[int, Slice] = {}
    slice_deployments: dict[int, Slice] = {}

    @classmethod
    def get_device(cls, name: str) -> DeviceConfiguration or None:
        for device in cls.config.vpn_gateways + cls.config.switches:
            if device.name == name:
                return device
        return None

    @classmethod
    def get_network(cls, name: str) -> NetworkConfiguration or None:
        for net in cls.config.networks:
            if net.name == name:
                return net
        return None


class Tunnel(object):
    def __init__(self, tunnel_id: int):
        self.tunnel_id = tunnel_id
        # switch name -> role, switch forward port num, queue id
        self.switch_roles: dict[str, (DeviceType, int, int)] = {}
        # Network names in order
        self.route: [str] = []


class Slice(object):
    def __init__(self, slice_id: int, tunnel: Tunnel):
        self.slice_id = slice_id
        self.tunnel = tunnel
        # switch name -> role, switch forward port num, queue id
        self.switch_roles: dict[str, (DeviceType, int, int)] = {}
        # Network names in order
        self.route: [str] = []
