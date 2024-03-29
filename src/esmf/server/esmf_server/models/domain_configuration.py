# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from esmf_server.models.base_model_ import Model
from esmf_server.models.device_configuration import DeviceConfiguration
from esmf_server.models.domain_configuration_slice_id_range import DomainConfigurationSliceIdRange
from esmf_server.models.domain_configuration_tunnel_id_range import DomainConfigurationTunnelIdRange
from esmf_server.models.network_configuration import NetworkConfiguration
from esmf_server import util


class DomainConfiguration(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type: str=None, network: str=None, vpn_gateways: List[DeviceConfiguration]=None, networks: List[NetworkConfiguration]=None, coordinators: List[DeviceConfiguration]=None, domain_controller: DeviceConfiguration=None, reservable_bitrate: int=1000000000, slice_id_range: DomainConfigurationSliceIdRange=None, tunnel_id_range: DomainConfigurationTunnelIdRange=None):
        """DomainConfiguration - a model defined in OpenAPI

        :param type: The type of this DomainConfiguration.
        :param network: The network of this DomainConfiguration.
        :param vpn_gateways: The vpn_gateways of this DomainConfiguration.
        :param networks: The networks of this DomainConfiguration.
        :param coordinators: The coordinators of this DomainConfiguration.
        :param domain_controller: The domain_controller of this DomainConfiguration.
        :param reservable_bitrate: The reservable_bitrate of this DomainConfiguration.
        :param slice_id_range: The slice_id_range of this DomainConfiguration.
        :param tunnel_id_range: The tunnel_id_range of this DomainConfiguration.
        """
        self.openapi_types = {
            'type': str,
            'network': str,
            'vpn_gateways': List[DeviceConfiguration],
            'networks': List[NetworkConfiguration],
            'coordinators': List[DeviceConfiguration],
            'domain_controller': DeviceConfiguration,
            'reservable_bitrate': int,
            'slice_id_range': DomainConfigurationSliceIdRange,
            'tunnel_id_range': DomainConfigurationTunnelIdRange
        }

        self.attribute_map = {
            'type': 'type',
            'network': 'network',
            'vpn_gateways': 'vpn_gateways',
            'networks': 'networks',
            'coordinators': 'coordinators',
            'domain_controller': 'domain_controller',
            'reservable_bitrate': 'reservable_bitrate',
            'slice_id_range': 'slice_id_range',
            'tunnel_id_range': 'tunnel_id_range'
        }

        self._type = type
        self._network = network
        self._vpn_gateways = vpn_gateways
        self._networks = networks
        self._coordinators = coordinators
        self._domain_controller = domain_controller
        self._reservable_bitrate = reservable_bitrate
        self._slice_id_range = slice_id_range
        self._tunnel_id_range = tunnel_id_range

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
        allowed_values = ["ESMF", "CTMF"]  # noqa: E501
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
    def coordinators(self):
        """Gets the coordinators of this DomainConfiguration.

        A list of the other ESMF/CTMF services

        :return: The coordinators of this DomainConfiguration.
        :rtype: List[DeviceConfiguration]
        """
        return self._coordinators

    @coordinators.setter
    def coordinators(self, coordinators):
        """Sets the coordinators of this DomainConfiguration.

        A list of the other ESMF/CTMF services

        :param coordinators: The coordinators of this DomainConfiguration.
        :type coordinators: List[DeviceConfiguration]
        """

        self._coordinators = coordinators

    @property
    def domain_controller(self):
        """Gets the domain_controller of this DomainConfiguration.


        :return: The domain_controller of this DomainConfiguration.
        :rtype: DeviceConfiguration
        """
        return self._domain_controller

    @domain_controller.setter
    def domain_controller(self, domain_controller):
        """Sets the domain_controller of this DomainConfiguration.


        :param domain_controller: The domain_controller of this DomainConfiguration.
        :type domain_controller: DeviceConfiguration
        """

        self._domain_controller = domain_controller

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

    @property
    def slice_id_range(self):
        """Gets the slice_id_range of this DomainConfiguration.


        :return: The slice_id_range of this DomainConfiguration.
        :rtype: DomainConfigurationSliceIdRange
        """
        return self._slice_id_range

    @slice_id_range.setter
    def slice_id_range(self, slice_id_range):
        """Sets the slice_id_range of this DomainConfiguration.


        :param slice_id_range: The slice_id_range of this DomainConfiguration.
        :type slice_id_range: DomainConfigurationSliceIdRange
        """

        self._slice_id_range = slice_id_range

    @property
    def tunnel_id_range(self):
        """Gets the tunnel_id_range of this DomainConfiguration.


        :return: The tunnel_id_range of this DomainConfiguration.
        :rtype: DomainConfigurationTunnelIdRange
        """
        return self._tunnel_id_range

    @tunnel_id_range.setter
    def tunnel_id_range(self, tunnel_id_range):
        """Sets the tunnel_id_range of this DomainConfiguration.


        :param tunnel_id_range: The tunnel_id_range of this DomainConfiguration.
        :type tunnel_id_range: DomainConfigurationTunnelIdRange
        """

        self._tunnel_id_range = tunnel_id_range
