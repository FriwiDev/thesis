from enum import Enum

from dsmf_server.configuration_util import ConfigurationUtil

SwitchType = Enum('SwitchType',
                  ['SRC_ALL', 'SRC_ENTRY', 'SRC_TP', 'SRC_EXIT', 'BN_ALL', 'BN_BEGIN', 'BN_TP', 'BN_END', 'DST_ALL',
                   'DST_BEGIN', 'DST_TP', 'DST_EXIT'])


class DomainState(object):
    config = ConfigurationUtil.load_configuration_from_disk()


class Tunnel(object):
    def __init__(self, tunnel_id: int):
        self.tunnel_id = tunnel_id
        # switch name -> role, switch forward port num, queue id
        self.switch_roles: dict[str, (SwitchType, int, int)] = {}
        # Network names in order
        self.route: [str] = []


class Slice(object):
    def __init__(self, slice_id: int, tunnel: Tunnel):
        self.slice_id = slice_id
        self.tunnel = tunnel
        # switch name -> role, switch forward port num, queue id
        self.switch_roles: dict[str, (SwitchType, int, int)] = {}
        # Network names in order
        self.route: [str] = []
