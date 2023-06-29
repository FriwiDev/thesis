# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from vpn_gateway_server.models.base_model_ import Model
from vpn_gateway_server import util


class TunnelEntryMatchesInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, direction: str=None, transport_protocol: str=None, ip: str=None, mac: str=None, port: int=0):
        """TunnelEntryMatchesInner - a model defined in OpenAPI

        :param direction: The direction of this TunnelEntryMatchesInner.
        :param transport_protocol: The transport_protocol of this TunnelEntryMatchesInner.
        :param ip: The ip of this TunnelEntryMatchesInner.
        :param mac: The mac of this TunnelEntryMatchesInner.
        :param port: The port of this TunnelEntryMatchesInner.
        """
        self.openapi_types = {
            'direction': str,
            'transport_protocol': str,
            'ip': str,
            'mac': str,
            'port': int
        }

        self.attribute_map = {
            'direction': 'direction',
            'transport_protocol': 'transport_protocol',
            'ip': 'ip',
            'mac': 'mac',
            'port': 'port'
        }

        self._direction = direction
        self._transport_protocol = transport_protocol
        self._ip = ip
        self._mac = mac
        self._port = port

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TunnelEntryMatchesInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The tunnel_entry_matches_inner of this TunnelEntryMatchesInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def direction(self):
        """Gets the direction of this TunnelEntryMatchesInner.

        Specifies the fields of the packets that need to be matched

        :return: The direction of this TunnelEntryMatchesInner.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this TunnelEntryMatchesInner.

        Specifies the fields of the packets that need to be matched

        :param direction: The direction of this TunnelEntryMatchesInner.
        :type direction: str
        """
        allowed_values = ["SRC", "DST"]  # noqa: E501
        if direction not in allowed_values:
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def transport_protocol(self):
        """Gets the transport_protocol of this TunnelEntryMatchesInner.

        The protocol to be expected

        :return: The transport_protocol of this TunnelEntryMatchesInner.
        :rtype: str
        """
        return self._transport_protocol

    @transport_protocol.setter
    def transport_protocol(self, transport_protocol):
        """Sets the transport_protocol of this TunnelEntryMatchesInner.

        The protocol to be expected

        :param transport_protocol: The transport_protocol of this TunnelEntryMatchesInner.
        :type transport_protocol: str
        """
        allowed_values = ["UDP", "TCP"]  # noqa: E501
        if transport_protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `transport_protocol` ({0}), must be one of {1}"
                .format(transport_protocol, allowed_values)
            )

        self._transport_protocol = transport_protocol

    @property
    def ip(self):
        """Gets the ip of this TunnelEntryMatchesInner.

        Specifies the source or target ip to be matched. Leave empty for no matching.

        :return: The ip of this TunnelEntryMatchesInner.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this TunnelEntryMatchesInner.

        Specifies the source or target ip to be matched. Leave empty for no matching.

        :param ip: The ip of this TunnelEntryMatchesInner.
        :type ip: str
        """

        self._ip = ip

    @property
    def mac(self):
        """Gets the mac of this TunnelEntryMatchesInner.

        Specifies the source or target mac to be matched. Leave empty for no matching.

        :return: The mac of this TunnelEntryMatchesInner.
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """Sets the mac of this TunnelEntryMatchesInner.

        Specifies the source or target mac to be matched. Leave empty for no matching.

        :param mac: The mac of this TunnelEntryMatchesInner.
        :type mac: str
        """

        self._mac = mac

    @property
    def port(self):
        """Gets the port of this TunnelEntryMatchesInner.

        Specifies the source or target port to be matched. Leave empty or on 0 for no matching.

        :return: The port of this TunnelEntryMatchesInner.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this TunnelEntryMatchesInner.

        Specifies the source or target port to be matched. Leave empty or on 0 for no matching.

        :param port: The port of this TunnelEntryMatchesInner.
        :type port: int
        """

        self._port = port
