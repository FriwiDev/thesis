# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from dtmf_server.models.base_model_ import Model
from dtmf_server import util


class Tunnel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, rate: int=None, latency: int=None, _from: str=None, to: str=None):
        """Tunnel - a model defined in OpenAPI

        :param id: The id of this Tunnel.
        :param rate: The rate of this Tunnel.
        :param latency: The latency of this Tunnel.
        :param _from: The _from of this Tunnel.
        :param to: The to of this Tunnel.
        """
        self.openapi_types = {
            'id': int,
            'rate': int,
            'latency': int,
            '_from': str,
            'to': str
        }

        self.attribute_map = {
            'id': 'id',
            'rate': 'rate',
            'latency': 'latency',
            '_from': 'from',
            'to': 'to'
        }

        self._id = id
        self._rate = rate
        self._latency = latency
        self.__from = _from
        self._to = to

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Tunnel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The tunnel of this Tunnel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Tunnel.

        The tunnel identifier

        :return: The id of this Tunnel.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Tunnel.

        The tunnel identifier

        :param id: The id of this Tunnel.
        :type id: int
        """

        self._id = id

    @property
    def rate(self):
        """Gets the rate of this Tunnel.

        The transmission rate as bits/s

        :return: The rate of this Tunnel.
        :rtype: int
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this Tunnel.

        The transmission rate as bits/s

        :param rate: The rate of this Tunnel.
        :type rate: int
        """

        self._rate = rate

    @property
    def latency(self):
        """Gets the latency of this Tunnel.

        The required maximum latency

        :return: The latency of this Tunnel.
        :rtype: int
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        """Sets the latency of this Tunnel.

        The required maximum latency

        :param latency: The latency of this Tunnel.
        :type latency: int
        """

        self._latency = latency

    @property
    def _from(self):
        """Gets the _from of this Tunnel.

        The name of the input domain or host

        :return: The _from of this Tunnel.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this Tunnel.

        The name of the input domain or host

        :param _from: The _from of this Tunnel.
        :type _from: str
        """

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this Tunnel.

        The name of the output domain or host

        :return: The to of this Tunnel.
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this Tunnel.

        The name of the output domain or host

        :param to: The to of this Tunnel.
        :type to: str
        """

        self._to = to
