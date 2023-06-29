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


class Endpoint(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Specifying an endpoint to be matched for source or target
    """


    class MetaOapg:
        
        class properties:
            
            
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
            ip = schemas.StrSchema
            mac = schemas.StrSchema
            port = schemas.IntSchema
            __annotations__ = {
                "transport_protocol": transport_protocol,
                "ip": ip,
                "mac": mac,
                "port": port,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transport_protocol"]) -> MetaOapg.properties.transport_protocol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ip"]) -> MetaOapg.properties.ip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mac"]) -> MetaOapg.properties.mac: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["port"]) -> MetaOapg.properties.port: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["transport_protocol", "ip", "mac", "port", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transport_protocol"]) -> typing.Union[MetaOapg.properties.transport_protocol, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ip"]) -> typing.Union[MetaOapg.properties.ip, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mac"]) -> typing.Union[MetaOapg.properties.mac, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["port"]) -> typing.Union[MetaOapg.properties.port, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["transport_protocol", "ip", "mac", "port", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        transport_protocol: typing.Union[MetaOapg.properties.transport_protocol, str, schemas.Unset] = schemas.unset,
        ip: typing.Union[MetaOapg.properties.ip, str, schemas.Unset] = schemas.unset,
        mac: typing.Union[MetaOapg.properties.mac, str, schemas.Unset] = schemas.unset,
        port: typing.Union[MetaOapg.properties.port, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Endpoint':
        return super().__new__(
            cls,
            *_args,
            transport_protocol=transport_protocol,
            ip=ip,
            mac=mac,
            port=port,
            _configuration=_configuration,
            **kwargs,
        )
