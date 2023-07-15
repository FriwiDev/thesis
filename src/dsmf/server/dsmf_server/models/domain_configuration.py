# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from dsmf_server.models.base_model_ import Model
from dsmf_server.models.controller_configuration import ControllerConfiguration
from dsmf_server.models.device_configuration import DeviceConfiguration
from dsmf_server.models.network_border_configuration import NetworkBorderConfiguration
from dsmf_server.models.network_configuration import NetworkConfiguration
from dsmf_server import util


class DomainConfiguration(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type: str=None, network: str=None, controllers: List[ControllerConfiguration]=None, vpn_gateways: List[DeviceConfiguration]=None, switches: List[DeviceConfiguration]=None, network_borders: List[NetworkBorderConfiguration]=None, networks: List[NetworkConfiguration]=None, reservable_bitrate: int=1000000000):
        """DomainConfiguration - a model defined in OpenAPI

        :param type: The type of this DomainConfiguration.
        :param network: The network of this DomainConfiguration.
        :param controllers: The controllers of this DomainConfiguration.
        :param vpn_gateways: The vpn_gateways of this DomainConfiguration.
        :param switches: The switches of this DomainConfiguration.
        :param network_borders: The network_borders of this DomainConfiguration.
        :param networks: The networks of this DomainConfiguration.
        :param reservable_bitrate: The reservable_bitrate of this DomainConfiguration.
        """
        self.openapi_types = {
            'type': str,
            'network': str,
            'controllers': List[ControllerConfiguration],
            'vpn_gateways': List[DeviceConfiguration],
            'switches': List[DeviceConfiguration],
            'network_borders': List[NetworkBorderConfiguration],
            'networks': List[NetworkConfiguration],
            'reservable_bitrate': int
        }

        self.attribute_map = {
            'type': 'type',
            'network': 'network',
            'controllers': 'controllers',
            'vpn_gateways': 'vpn_gateways',
            'switches': 'switches',
            'network_borders': 'network_borders',
            'networks': 'networks',
            'reservable_bitrate': 'reservable_bitrate'
        }

        self._type = type
        self._network = network
        self._controllers = controllers
        self._vpn_gateways = vpn_gateways
        self._switches = switches
        self._network_borders = network_borders
        self._networks = networks
        self._reservable_bitrate = reservable_bitrate

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DomainConfiguration':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The domain_configuration of this DomainConfiguration.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self):
        """Gets the type of this DomainConfiguration.

        The service type to be used

        :return: The type of this DomainConfiguration.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DomainConfiguration.

        The service type to be used

        :param type: The type of this DomainConfiguration.
        :type type: str
        """
        allowed_values = ["DSMF", "DTMF"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def network(self):
        """Gets the network of this DomainConfiguration.

        Our network name

        :return: The network of this DomainConfiguration.
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this DomainConfiguration.

        Our network name

        :param network: The network of this DomainConfiguration.
        :type network: str
        """

        self._network = network

    @property
    def controllers(self):
        """Gets the controllers of this DomainConfiguration.

        Specifies the controllers available to us

        :return: The controllers of this DomainConfiguration.
        :rtype: List[ControllerConfiguration]
        """
        return self._controllers

    @controllers.setter
    def controllers(self, controllers):
        """Sets the controllers of this DomainConfiguration.

        Specifies the controllers available to us

        :param controllers: The controllers of this DomainConfiguration.
        :type controllers: List[ControllerConfiguration]
        """

        self._controllers = controllers

    @property
    def vpn_gateways(self):
        """Gets the vpn_gateways of this DomainConfiguration.

        The vpn gateways known to us

        :return: The vpn_gateways of this DomainConfiguration.
        :rtype: List[DeviceConfiguration]
        """
        return self._vpn_gateways

    @vpn_gateways.setter
    def vpn_gateways(self, vpn_gateways):
        """Sets the vpn_gateways of this DomainConfiguration.

        The vpn gateways known to us

        :param vpn_gateways: The vpn_gateways of this DomainConfiguration.
        :type vpn_gateways: List[DeviceConfiguration]
        """

        self._vpn_gateways = vpn_gateways

    @property
    def switches(self):
        """Gets the switches of this DomainConfiguration.

        The switches known to us

        :return: The switches of this DomainConfiguration.
        :rtype: List[DeviceConfiguration]
        """
        return self._switches

    @switches.setter
    def switches(self, switches):
        """Sets the switches of this DomainConfiguration.

        The switches known to us

        :param switches: The switches of this DomainConfiguration.
        :type switches: List[DeviceConfiguration]
        """

        self._switches = switches

    @property
    def network_borders(self):
        """Gets the network_borders of this DomainConfiguration.

        The routes to other networks known to us

        :return: The network_borders of this DomainConfiguration.
        :rtype: List[NetworkBorderConfiguration]
        """
        return self._network_borders

    @network_borders.setter
    def network_borders(self, network_borders):
        """Sets the network_borders of this DomainConfiguration.

        The routes to other networks known to us

        :param network_borders: The network_borders of this DomainConfiguration.
        :type network_borders: List[NetworkBorderConfiguration]
        """

        self._network_borders = network_borders

    @property
    def networks(self):
        """Gets the networks of this DomainConfiguration.

        The other networks known to us

        :return: The networks of this DomainConfiguration.
        :rtype: List[NetworkConfiguration]
        """
        return self._networks

    @networks.setter
    def networks(self, networks):
        """Sets the networks of this DomainConfiguration.

        The other networks known to us

        :param networks: The networks of this DomainConfiguration.
        :type networks: List[NetworkConfiguration]
        """

        self._networks = networks

    @property
    def reservable_bitrate(self):
        """Gets the reservable_bitrate of this DomainConfiguration.

        The bitrate that can be reserved by hosts on our network

        :return: The reservable_bitrate of this DomainConfiguration.
        :rtype: int
        """
        return self._reservable_bitrate

    @reservable_bitrate.setter
    def reservable_bitrate(self, reservable_bitrate):
        """Sets the reservable_bitrate of this DomainConfiguration.

        The bitrate that can be reserved by hosts on our network

        :param reservable_bitrate: The reservable_bitrate of this DomainConfiguration.
        :type reservable_bitrate: int
        """

        self._reservable_bitrate = reservable_bitrate