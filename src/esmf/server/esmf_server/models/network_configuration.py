# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from esmf_server.models.base_model_ import Model
from esmf_server import util


class NetworkConfiguration(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, reachable: List[str]=None, preferred_vpn: List[str]=None, subnet: str=None):
        """NetworkConfiguration - a model defined in OpenAPI

        :param name: The name of this NetworkConfiguration.
        :param reachable: The reachable of this NetworkConfiguration.
        :param preferred_vpn: The preferred_vpn of this NetworkConfiguration.
        :param subnet: The subnet of this NetworkConfiguration.
        """
        self.openapi_types = {
            'name': str,
            'reachable': List[str],
            'preferred_vpn': List[str],
            'subnet': str
        }

        self.attribute_map = {
            'name': 'name',
            'reachable': 'reachable',
            'preferred_vpn': 'preferred_vpn',
            'subnet': 'subnet'
        }

        self._name = name
        self._reachable = reachable
        self._preferred_vpn = preferred_vpn
        self._subnet = subnet

    @classmethod
    def from_dict(cls, dikt: dict) -> 'NetworkConfiguration':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The network_configuration of this NetworkConfiguration.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this NetworkConfiguration.

        The name of the network

        :return: The name of this NetworkConfiguration.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NetworkConfiguration.

        The name of the network

        :param name: The name of this NetworkConfiguration.
        :type name: str
        """

        self._name = name

    @property
    def reachable(self):
        """Gets the reachable of this NetworkConfiguration.

        Networks reachable from this network

        :return: The reachable of this NetworkConfiguration.
        :rtype: List[str]
        """
        return self._reachable

    @reachable.setter
    def reachable(self, reachable):
        """Sets the reachable of this NetworkConfiguration.

        Networks reachable from this network

        :param reachable: The reachable of this NetworkConfiguration.
        :type reachable: List[str]
        """

        self._reachable = reachable

    @property
    def preferred_vpn(self):
        """Gets the preferred_vpn of this NetworkConfiguration.

        VPN gateways to use (in order) to connect to this network

        :return: The preferred_vpn of this NetworkConfiguration.
        :rtype: List[str]
        """
        return self._preferred_vpn

    @preferred_vpn.setter
    def preferred_vpn(self, preferred_vpn):
        """Sets the preferred_vpn of this NetworkConfiguration.

        VPN gateways to use (in order) to connect to this network

        :param preferred_vpn: The preferred_vpn of this NetworkConfiguration.
        :type preferred_vpn: List[str]
        """

        self._preferred_vpn = preferred_vpn

    @property
    def subnet(self):
        """Gets the subnet of this NetworkConfiguration.

        Subnet of this network

        :return: The subnet of this NetworkConfiguration.
        :rtype: str
        """
        return self._subnet

    @subnet.setter
    def subnet(self, subnet):
        """Sets the subnet of this NetworkConfiguration.

        Subnet of this network

        :param subnet: The subnet of this NetworkConfiguration.
        :type subnet: str
        """

        self._subnet = subnet
