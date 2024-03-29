# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from vpn_gateway_server.models.base_model_ import Model
from vpn_gateway_server import util


class TunnelEntryEgressMatchesInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, intf_name: str=None, slice_id: int=None):
        """TunnelEntryEgressMatchesInner - a model defined in OpenAPI

        :param intf_name: The intf_name of this TunnelEntryEgressMatchesInner.
        :param slice_id: The slice_id of this TunnelEntryEgressMatchesInner.
        """
        self.openapi_types = {
            'intf_name': str,
            'slice_id': int
        }

        self.attribute_map = {
            'intf_name': 'intf_name',
            'slice_id': 'slice_id'
        }

        self._intf_name = intf_name
        self._slice_id = slice_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TunnelEntryEgressMatchesInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The tunnel_entry_egress_matches_inner of this TunnelEntryEgressMatchesInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def intf_name(self):
        """Gets the intf_name of this TunnelEntryEgressMatchesInner.

        Specifies the egress interface

        :return: The intf_name of this TunnelEntryEgressMatchesInner.
        :rtype: str
        """
        return self._intf_name

    @intf_name.setter
    def intf_name(self, intf_name):
        """Sets the intf_name of this TunnelEntryEgressMatchesInner.

        Specifies the egress interface

        :param intf_name: The intf_name of this TunnelEntryEgressMatchesInner.
        :type intf_name: str
        """

        self._intf_name = intf_name

    @property
    def slice_id(self):
        """Gets the slice_id of this TunnelEntryEgressMatchesInner.

        Specifies the expected mpls label

        :return: The slice_id of this TunnelEntryEgressMatchesInner.
        :rtype: int
        """
        return self._slice_id

    @slice_id.setter
    def slice_id(self, slice_id):
        """Sets the slice_id of this TunnelEntryEgressMatchesInner.

        Specifies the expected mpls label

        :param slice_id: The slice_id of this TunnelEntryEgressMatchesInner.
        :type slice_id: int
        """

        self._slice_id = slice_id
