# coding: utf-8

"""
    Controller

    The API used by the DSMF/DTMF to contact the controller. This API is a subset of the API provided by the ryu controller and modelled strictly according to their specification. Currently we only support OpenFlow 1.2 or higher. Please refer to the specification here: <a href=\"https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html\">https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html</a>  # noqa: E501

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

from controller_client import schemas  # noqa: F401


class SwitchFlowMatchV12(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A switch flow match entity (only selected properties, OpenFlow >= v1_2)
    """


    class MetaOapg:
        
        class properties:
            in_port = schemas.IntSchema
            eth_src = schemas.StrSchema
            eth_dst = schemas.StrSchema
            eth_type = schemas.IntSchema
            tcp_src = schemas.IntSchema
            tcp_dst = schemas.IntSchema
            udp_src = schemas.IntSchema
            udp_dst = schemas.IntSchema
            __annotations__ = {
                "in_port": in_port,
                "eth_src": eth_src,
                "eth_dst": eth_dst,
                "eth_type": eth_type,
                "tcp_src": tcp_src,
                "tcp_dst": tcp_dst,
                "udp_src": udp_src,
                "udp_dst": udp_dst,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["in_port"]) -> MetaOapg.properties.in_port: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["eth_src"]) -> MetaOapg.properties.eth_src: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["eth_dst"]) -> MetaOapg.properties.eth_dst: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["eth_type"]) -> MetaOapg.properties.eth_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tcp_src"]) -> MetaOapg.properties.tcp_src: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tcp_dst"]) -> MetaOapg.properties.tcp_dst: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["udp_src"]) -> MetaOapg.properties.udp_src: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["udp_dst"]) -> MetaOapg.properties.udp_dst: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["in_port", "eth_src", "eth_dst", "eth_type", "tcp_src", "tcp_dst", "udp_src", "udp_dst", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["in_port"]) -> typing.Union[MetaOapg.properties.in_port, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["eth_src"]) -> typing.Union[MetaOapg.properties.eth_src, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["eth_dst"]) -> typing.Union[MetaOapg.properties.eth_dst, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["eth_type"]) -> typing.Union[MetaOapg.properties.eth_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tcp_src"]) -> typing.Union[MetaOapg.properties.tcp_src, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tcp_dst"]) -> typing.Union[MetaOapg.properties.tcp_dst, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["udp_src"]) -> typing.Union[MetaOapg.properties.udp_src, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["udp_dst"]) -> typing.Union[MetaOapg.properties.udp_dst, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["in_port", "eth_src", "eth_dst", "eth_type", "tcp_src", "tcp_dst", "udp_src", "udp_dst", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        in_port: typing.Union[MetaOapg.properties.in_port, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        eth_src: typing.Union[MetaOapg.properties.eth_src, str, schemas.Unset] = schemas.unset,
        eth_dst: typing.Union[MetaOapg.properties.eth_dst, str, schemas.Unset] = schemas.unset,
        eth_type: typing.Union[MetaOapg.properties.eth_type, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        tcp_src: typing.Union[MetaOapg.properties.tcp_src, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        tcp_dst: typing.Union[MetaOapg.properties.tcp_dst, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        udp_src: typing.Union[MetaOapg.properties.udp_src, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        udp_dst: typing.Union[MetaOapg.properties.udp_dst, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SwitchFlowMatchV12':
        return super().__new__(
            cls,
            *_args,
            in_port=in_port,
            eth_src=eth_src,
            eth_dst=eth_dst,
            eth_type=eth_type,
            tcp_src=tcp_src,
            tcp_dst=tcp_dst,
            udp_src=udp_src,
            udp_dst=udp_dst,
            _configuration=_configuration,
            **kwargs,
        )
