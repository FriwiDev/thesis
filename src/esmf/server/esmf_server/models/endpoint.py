# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from esmf_server.models.base_model_ import Model
from esmf_server import util


class Endpoint(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, transport_protocol: str=None, ip: str=None, mac: str=None, port: int=0):
        """Endpoint - a model defined in OpenAPI

        :param transport_protocol: The transport_protocol of this Endpoint.
        :param ip: The ip of this Endpoint.
        :param mac: The mac of this Endpoint.
        :param port: The port of this Endpoint.
        """
        self.openapi_types = {
            'transport_protocol': str,
            'ip': str,
            'mac': str,
            'port': int
        }

        self.attribute_map = {
            'transport_protocol': 'transport_protocol',
            'ip': 'ip',
            'mac': 'mac',
            'port': 'port'
        }

        self._transport_protocol = transport_protocol
        self._ip = ip
        self._mac = mac
        self._port = port

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Endpoint':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The endpoint of this Endpoint.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def transport_protocol(self):
        """Gets the transport_protocol of this Endpoint.

        The protocol to be expected

        :return: The transport_protocol of this Endpoint.
        :rtype: str
        """
        return self._transport_protocol

    @transport_protocol.setter
    def transport_protocol(self, transport_protocol):
        """Sets the transport_protocol of this Endpoint.

        The protocol to be expected

        :param transport_protocol: The transport_protocol of this Endpoint.
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
        """Gets the ip of this Endpoint.

        Specifies the source or target ip to be matched. Leave empty for no matching.

        :return: The ip of this Endpoint.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this Endpoint.

        Specifies the source or target ip to be matched. Leave empty for no matching.

        :param ip: The ip of this Endpoint.
        :type ip: str
        """

        self._ip = ip

    @property
    def mac(self):
        """Gets the mac of this Endpoint.

        Specifies the source or target mac to be matched. Leave empty for no matching. We currently can not match the destination mac address, it will be ignored.

        :return: The mac of this Endpoint.
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """Sets the mac of this Endpoint.

        Specifies the source or target mac to be matched. Leave empty for no matching. We currently can not match the destination mac address, it will be ignored.

        :param mac: The mac of this Endpoint.
        :type mac: str
        """

        self._mac = mac

    @property
    def port(self):
        """Gets the port of this Endpoint.

        Specifies the source or target port to be matched. Leave empty or on 0 for no matching.

        :return: The port of this Endpoint.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this Endpoint.

        Specifies the source or target port to be matched. Leave empty or on 0 for no matching.

        :param port: The port of this Endpoint.
        :type port: int
        """

        self._port = port