# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from esmf_server.models.base_model_ import Model
from esmf_server import util


class ConnectionConfiguration(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, intf_name: str=None, intf_id: int=None, other_end: str=None):
        """ConnectionConfiguration - a model defined in OpenAPI

        :param intf_name: The intf_name of this ConnectionConfiguration.
        :param intf_id: The intf_id of this ConnectionConfiguration.
        :param other_end: The other_end of this ConnectionConfiguration.
        """
        self.openapi_types = {
            'intf_name': str,
            'intf_id': int,
            'other_end': str
        }

        self.attribute_map = {
            'intf_name': 'intf_name',
            'intf_id': 'intf_id',
            'other_end': 'other_end'
        }

        self._intf_name = intf_name
        self._intf_id = intf_id
        self._other_end = other_end

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ConnectionConfiguration':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The connection_configuration of this ConnectionConfiguration.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def intf_name(self):
        """Gets the intf_name of this ConnectionConfiguration.

        The name of the interface on a switch

        :return: The intf_name of this ConnectionConfiguration.
        :rtype: str
        """
        return self._intf_name

    @intf_name.setter
    def intf_name(self, intf_name):
        """Sets the intf_name of this ConnectionConfiguration.

        The name of the interface on a switch

        :param intf_name: The intf_name of this ConnectionConfiguration.
        :type intf_name: str
        """

        self._intf_name = intf_name

    @property
    def intf_id(self):
        """Gets the intf_id of this ConnectionConfiguration.

        The id of the interface

        :return: The intf_id of this ConnectionConfiguration.
        :rtype: int
        """
        return self._intf_id

    @intf_id.setter
    def intf_id(self, intf_id):
        """Sets the intf_id of this ConnectionConfiguration.

        The id of the interface

        :param intf_id: The intf_id of this ConnectionConfiguration.
        :type intf_id: int
        """

        self._intf_id = intf_id

    @property
    def other_end(self):
        """Gets the other_end of this ConnectionConfiguration.

        The name of the device on the other side

        :return: The other_end of this ConnectionConfiguration.
        :rtype: str
        """
        return self._other_end

    @other_end.setter
    def other_end(self, other_end):
        """Sets the other_end of this ConnectionConfiguration.

        The name of the device on the other side

        :param other_end: The other_end of this ConnectionConfiguration.
        :type other_end: str
        """

        self._other_end = other_end
