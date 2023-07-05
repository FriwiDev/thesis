# coding: utf-8

"""
    DSMF

    A simple API to interact with the Domain Slice Management Function. Supports reserving, creating and removing slices and tunnels from one external domain to another external domain or host. Please refer to the topology drawings for further information about the network structures.  # noqa: E501

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

from dsmf_client import schemas  # noqa: F401


class Slice(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            slice_id = schemas.Int32Schema
            min_rate = schemas.Int64Schema
            max_rate = schemas.Int64Schema
            burst_rate = schemas.Int64Schema
            latency = schemas.IntSchema
            tunnel_id = schemas.Int32Schema
            
            
            class transport_protocol(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def UDP(cls):
                    return cls("UDP")
                
                @schemas.classproperty
                def TCP(cls):
                    return cls("TCP")
        
            @staticmethod
            def fr() -> typing.Type['Endpoint']:
                return Endpoint
        
            @staticmethod
            def to() -> typing.Type['Endpoint']:
                return Endpoint
            __annotations__ = {
                "slice_id": slice_id,
                "min_rate": min_rate,
                "max_rate": max_rate,
                "burst_rate": burst_rate,
                "latency": latency,
                "tunnel_id": tunnel_id,
                "transport_protocol": transport_protocol,
                "fr": fr,
                "to": to,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["slice_id"]) -> MetaOapg.properties.slice_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["min_rate"]) -> MetaOapg.properties.min_rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max_rate"]) -> MetaOapg.properties.max_rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["burst_rate"]) -> MetaOapg.properties.burst_rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["latency"]) -> MetaOapg.properties.latency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tunnel_id"]) -> MetaOapg.properties.tunnel_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transport_protocol"]) -> MetaOapg.properties.transport_protocol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fr"]) -> 'Endpoint': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to"]) -> 'Endpoint': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["slice_id", "min_rate", "max_rate", "burst_rate", "latency", "tunnel_id", "transport_protocol", "fr", "to", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["slice_id"]) -> typing.Union[MetaOapg.properties.slice_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["min_rate"]) -> typing.Union[MetaOapg.properties.min_rate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max_rate"]) -> typing.Union[MetaOapg.properties.max_rate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["burst_rate"]) -> typing.Union[MetaOapg.properties.burst_rate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["latency"]) -> typing.Union[MetaOapg.properties.latency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tunnel_id"]) -> typing.Union[MetaOapg.properties.tunnel_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transport_protocol"]) -> typing.Union[MetaOapg.properties.transport_protocol, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fr"]) -> typing.Union['Endpoint', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to"]) -> typing.Union['Endpoint', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["slice_id", "min_rate", "max_rate", "burst_rate", "latency", "tunnel_id", "transport_protocol", "fr", "to", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        slice_id: typing.Union[MetaOapg.properties.slice_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        min_rate: typing.Union[MetaOapg.properties.min_rate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        max_rate: typing.Union[MetaOapg.properties.max_rate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        burst_rate: typing.Union[MetaOapg.properties.burst_rate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        latency: typing.Union[MetaOapg.properties.latency, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        tunnel_id: typing.Union[MetaOapg.properties.tunnel_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        transport_protocol: typing.Union[MetaOapg.properties.transport_protocol, str, schemas.Unset] = schemas.unset,
        fr: typing.Union['Endpoint', schemas.Unset] = schemas.unset,
        to: typing.Union['Endpoint', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Slice':
        return super().__new__(
            cls,
            *_args,
            slice_id=slice_id,
            min_rate=min_rate,
            max_rate=max_rate,
            burst_rate=burst_rate,
            latency=latency,
            tunnel_id=tunnel_id,
            transport_protocol=transport_protocol,
            fr=fr,
            to=to,
            _configuration=_configuration,
            **kwargs,
        )

from dsmf_client.model.endpoint import Endpoint
