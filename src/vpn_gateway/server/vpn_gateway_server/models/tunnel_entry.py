# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from vpn_gateway_server.models.base_model_ import Model
from vpn_gateway_server import util


class TunnelEntry(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, inner_intf: str=None, outer_intf: str=None, inner_subnet: str=None, outer_subnet: str=None, local_port: int=None, remote_end: str=None, private_key: str=None, public_key: str=None):
        """TunnelEntry - a model defined in OpenAPI

        :param id: The id of this TunnelEntry.
        :param inner_intf: The inner_intf of this TunnelEntry.
        :param outer_intf: The outer_intf of this TunnelEntry.
        :param inner_subnet: The inner_subnet of this TunnelEntry.
        :param outer_subnet: The outer_subnet of this TunnelEntry.
        :param local_port: The local_port of this TunnelEntry.
        :param remote_end: The remote_end of this TunnelEntry.
        :param private_key: The private_key of this TunnelEntry.
        :param public_key: The public_key of this TunnelEntry.
        """
        self.openapi_types = {
            'id': int,
            'inner_intf': str,
            'outer_intf': str,
            'inner_subnet': str,
            'outer_subnet': str,
            'local_port': int,
            'remote_end': str,
            'private_key': str,
            'public_key': str
        }

        self.attribute_map = {
            'id': 'id',
            'inner_intf': 'inner_intf',
            'outer_intf': 'outer_intf',
            'inner_subnet': 'inner_subnet',
            'outer_subnet': 'outer_subnet',
            'local_port': 'local_port',
            'remote_end': 'remote_end',
            'private_key': 'private_key',
            'public_key': 'public_key'
        }

        self._id = id
        self._inner_intf = inner_intf
        self._outer_intf = outer_intf
        self._inner_subnet = inner_subnet
        self._outer_subnet = outer_subnet
        self._local_port = local_port
        self._remote_end = remote_end
        self._private_key = private_key
        self._public_key = public_key

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TunnelEntry':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The tunnel_entry of this TunnelEntry.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this TunnelEntry.

        The tunnel identifier

        :return: The id of this TunnelEntry.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TunnelEntry.

        The tunnel identifier

        :param id: The id of this TunnelEntry.
        :type id: int
        """

        self._id = id

    @property
    def inner_intf(self):
        """Gets the inner_intf of this TunnelEntry.

        The name of the network interface that faces towards the edge network

        :return: The inner_intf of this TunnelEntry.
        :rtype: str
        """
        return self._inner_intf

    @inner_intf.setter
    def inner_intf(self, inner_intf):
        """Sets the inner_intf of this TunnelEntry.

        The name of the network interface that faces towards the edge network

        :param inner_intf: The inner_intf of this TunnelEntry.
        :type inner_intf: str
        """

        self._inner_intf = inner_intf

    @property
    def outer_intf(self):
        """Gets the outer_intf of this TunnelEntry.

        The name of the network interface that faces towards the first black network

        :return: The outer_intf of this TunnelEntry.
        :rtype: str
        """
        return self._outer_intf

    @outer_intf.setter
    def outer_intf(self, outer_intf):
        """Sets the outer_intf of this TunnelEntry.

        The name of the network interface that faces towards the first black network

        :param outer_intf: The outer_intf of this TunnelEntry.
        :type outer_intf: str
        """

        self._outer_intf = outer_intf

    @property
    def inner_subnet(self):
        """Gets the inner_subnet of this TunnelEntry.

        The subnet to route towards the inner interface (aka. the edge network/device)

        :return: The inner_subnet of this TunnelEntry.
        :rtype: str
        """
        return self._inner_subnet

    @inner_subnet.setter
    def inner_subnet(self, inner_subnet):
        """Sets the inner_subnet of this TunnelEntry.

        The subnet to route towards the inner interface (aka. the edge network/device)

        :param inner_subnet: The inner_subnet of this TunnelEntry.
        :type inner_subnet: str
        """

        self._inner_subnet = inner_subnet

    @property
    def outer_subnet(self):
        """Gets the outer_subnet of this TunnelEntry.

        The subnet to route towards the tunnel (aka. the other edge network/device)

        :return: The outer_subnet of this TunnelEntry.
        :rtype: str
        """
        return self._outer_subnet

    @outer_subnet.setter
    def outer_subnet(self, outer_subnet):
        """Sets the outer_subnet of this TunnelEntry.

        The subnet to route towards the tunnel (aka. the other edge network/device)

        :param outer_subnet: The outer_subnet of this TunnelEntry.
        :type outer_subnet: str
        """

        self._outer_subnet = outer_subnet

    @property
    def local_port(self):
        """Gets the local_port of this TunnelEntry.

        The local port to use to bind the tunnel

        :return: The local_port of this TunnelEntry.
        :rtype: int
        """
        return self._local_port

    @local_port.setter
    def local_port(self, local_port):
        """Sets the local_port of this TunnelEntry.

        The local port to use to bind the tunnel

        :param local_port: The local_port of this TunnelEntry.
        :type local_port: int
        """

        self._local_port = local_port

    @property
    def remote_end(self):
        """Gets the remote_end of this TunnelEntry.

        The remote address to contact as the other side of the tunnel

        :return: The remote_end of this TunnelEntry.
        :rtype: str
        """
        return self._remote_end

    @remote_end.setter
    def remote_end(self, remote_end):
        """Sets the remote_end of this TunnelEntry.

        The remote address to contact as the other side of the tunnel

        :param remote_end: The remote_end of this TunnelEntry.
        :type remote_end: str
        """

        self._remote_end = remote_end

    @property
    def private_key(self):
        """Gets the private_key of this TunnelEntry.

        The private key to use for authentication of the tunnel to the other side

        :return: The private_key of this TunnelEntry.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this TunnelEntry.

        The private key to use for authentication of the tunnel to the other side

        :param private_key: The private_key of this TunnelEntry.
        :type private_key: str
        """

        self._private_key = private_key

    @property
    def public_key(self):
        """Gets the public_key of this TunnelEntry.

        The public key to use for authentication of the tunnel from the other side

        :return: The public_key of this TunnelEntry.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this TunnelEntry.

        The public key to use for authentication of the tunnel from the other side

        :param public_key: The public_key of this TunnelEntry.
        :type public_key: str
        """

        self._public_key = public_key