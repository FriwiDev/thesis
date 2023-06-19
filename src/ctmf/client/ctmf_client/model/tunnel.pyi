# coding: utf-8

"""
    CTMF

    A simple API to interact with the Core Tunnel Management Function. Supports creating and removing tunnels on this domains. Is advised to allocate resources by external ESMFs. The CTMF is a subset of the ESMF. Please refer to the topology drawings for further information about the network structures.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from ctmf_client import schemas  # noqa: F401


class Tunnel(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.Int32Schema
            min_rate = schemas.Int64Schema
            max_rate = schemas.Int64Schema
            burst_rate = schemas.Int64Schema
            latency = schemas.IntSchema
            _from = schemas.StrSchema
            to = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "min_rate": min_rate,
                "max_rate": max_rate,
                "burst_rate": burst_rate,
                "latency": latency,
                "from": _from,
                "to": to,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["min_rate"]) -> MetaOapg.properties.min_rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max_rate"]) -> MetaOapg.properties.max_rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["burst_rate"]) -> MetaOapg.properties.burst_rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["latency"]) -> MetaOapg.properties.latency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from"]) -> MetaOapg.properties._from: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to"]) -> MetaOapg.properties.to: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "min_rate", "max_rate", "burst_rate", "latency", "from", "to", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["min_rate"]) -> typing.Union[MetaOapg.properties.min_rate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max_rate"]) -> typing.Union[MetaOapg.properties.max_rate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["burst_rate"]) -> typing.Union[MetaOapg.properties.burst_rate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["latency"]) -> typing.Union[MetaOapg.properties.latency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from"]) -> typing.Union[MetaOapg.properties._from, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to"]) -> typing.Union[MetaOapg.properties.to, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "min_rate", "max_rate", "burst_rate", "latency", "from", "to", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        min_rate: typing.Union[MetaOapg.properties.min_rate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        max_rate: typing.Union[MetaOapg.properties.max_rate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        burst_rate: typing.Union[MetaOapg.properties.burst_rate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        latency: typing.Union[MetaOapg.properties.latency, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        to: typing.Union[MetaOapg.properties.to, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Tunnel':
        return super().__new__(
            cls,
            *_args,
            id=id,
            min_rate=min_rate,
            max_rate=max_rate,
            burst_rate=burst_rate,
            latency=latency,
            to=to,
            _configuration=_configuration,
            **kwargs,
        )
