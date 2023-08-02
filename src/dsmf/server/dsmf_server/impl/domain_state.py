from enum import Enum
from typing import Dict, Tuple

from dsmf_server.impl.configuration_util import ConfigurationUtil
from dsmf_server.models import Tunnel, Slice, DeviceConfiguration, NetworkConfiguration, ConnectionConfiguration
from switch_client.model.queue import Queue

DeviceType = Enum('SwitchType',
                  ['SRC', 'DST', 'TUN_ENTRY', 'TUN_EXIT', 'SRC_ALL', 'SRC_BEGIN', 'SRC_TP', 'SRC_END', 'BN_ALL',
                   'BN_BEGIN', 'BN_TP', 'BN_END', 'DST_ALL',
                   'DST_BEGIN', 'DST_TP', 'DST_END'])


class DomainState(object):
    config = ConfigurationUtil.load_configuration_from_disk()
    tunnel_reservations: Dict[int, Tunnel] = {}
    tunnel_deployments: Dict[int, Tunnel] = {}
    slice_reservations: Dict[int, Slice] = {}
    slice_deployments: Dict[int, Slice] = {}
    tunnel_queue_pools: Dict[int, Dict[str, Tuple[Queue, Queue or None]]] = {}
    slice_queue_pools: Dict[int, Dict[str, Queue]] = {}

    @classmethod
    def get_device(cls, name: str) -> DeviceConfiguration or None:
        for device in cls.config.vpn_gateways + cls.config.switches:
            if device.name == name:
                return device
        # TODO-FW This could be replaced with real device config data in the future
        for switch in cls.config.switches:
            for connection in switch.connections:
                if connection.other_end == name:
                    return DeviceConfiguration(ip=None, port=None, connections=[ConnectionConfiguration(other_end=switch.name)], network=switch.network, name=name, dpid=None)
        return None

    @classmethod
    def get_network(cls, name: str) -> NetworkConfiguration or None:
        for net in cls.config.networks:
            if net.name == name:
                return net
        return None

