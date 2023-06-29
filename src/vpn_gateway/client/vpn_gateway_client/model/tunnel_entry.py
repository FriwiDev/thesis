# coding: utf-8

"""
    VPN Gateway API

    A simple API to manage tunnel entries on a dedicated host within the edges. The VPN Gateway is used to encrypt traffic before it enters the first black network.  # noqa: E501

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

from vpn_gateway_client import schemas  # noqa: F401


class TunnelEntry(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.Int32Schema
            inner_intf = schemas.StrSchema
            outer_intf = schemas.StrSchema
            inner_subnet = schemas.StrSchema
            outer_subnet = schemas.StrSchema
            local_port = schemas.IntSchema
            remote_end = schemas.StrSchema
            private_key = schemas.StrSchema
            public_key = schemas.StrSchema
            
            
            class matches(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                
                                
                                class direction(
                                    schemas.EnumBase,
                                    schemas.StrSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        enum_value_to_name = {
                                            "SRC": "SRC",
                                            "DST": "DST",
                                        }
                                    
                                    @schemas.classproperty
                                    def SRC(cls):
                                        return cls("SRC")
                                    
                                    @schemas.classproperty
                                    def DST(cls):
                                        return cls("DST")
                                
                                
                                class transport_protocol(
                                    schemas.EnumBase,
                                    schemas.StrSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        enum_value_to_name = {
                                            "UDP": "UDP",
                                            "TCP": "TCP",
                                        }
                                    
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
                                    "direction": direction,
                                    "transport_protocol": transport_protocol,
                                    "ip": ip,
                                    "mac": mac,
                                    "port": port,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["direction"]) -> MetaOapg.properties.direction: ...
                        
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
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["direction", "transport_protocol", "ip", "mac", "port", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["direction"]) -> typing.Union[MetaOapg.properties.direction, schemas.Unset]: ...
                        
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
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["direction", "transport_protocol", "ip", "mac", "port", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            direction: typing.Union[MetaOapg.properties.direction, str, schemas.Unset] = schemas.unset,
                            transport_protocol: typing.Union[MetaOapg.properties.transport_protocol, str, schemas.Unset] = schemas.unset,
                            ip: typing.Union[MetaOapg.properties.ip, str, schemas.Unset] = schemas.unset,
                            mac: typing.Union[MetaOapg.properties.mac, str, schemas.Unset] = schemas.unset,
                            port: typing.Union[MetaOapg.properties.port, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                direction=direction,
                                transport_protocol=transport_protocol,
                                ip=ip,
                                mac=mac,
                                port=port,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'matches':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "id": id,
                "inner_intf": inner_intf,
                "outer_intf": outer_intf,
                "inner_subnet": inner_subnet,
                "outer_subnet": outer_subnet,
                "local_port": local_port,
                "remote_end": remote_end,
                "private_key": private_key,
                "public_key": public_key,
                "matches": matches,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inner_intf"]) -> MetaOapg.properties.inner_intf: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["outer_intf"]) -> MetaOapg.properties.outer_intf: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inner_subnet"]) -> MetaOapg.properties.inner_subnet: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["outer_subnet"]) -> MetaOapg.properties.outer_subnet: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["local_port"]) -> MetaOapg.properties.local_port: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["remote_end"]) -> MetaOapg.properties.remote_end: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["private_key"]) -> MetaOapg.properties.private_key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["public_key"]) -> MetaOapg.properties.public_key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["matches"]) -> MetaOapg.properties.matches: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "inner_intf", "outer_intf", "inner_subnet", "outer_subnet", "local_port", "remote_end", "private_key", "public_key", "matches", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inner_intf"]) -> typing.Union[MetaOapg.properties.inner_intf, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["outer_intf"]) -> typing.Union[MetaOapg.properties.outer_intf, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inner_subnet"]) -> typing.Union[MetaOapg.properties.inner_subnet, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["outer_subnet"]) -> typing.Union[MetaOapg.properties.outer_subnet, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["local_port"]) -> typing.Union[MetaOapg.properties.local_port, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["remote_end"]) -> typing.Union[MetaOapg.properties.remote_end, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["private_key"]) -> typing.Union[MetaOapg.properties.private_key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["public_key"]) -> typing.Union[MetaOapg.properties.public_key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["matches"]) -> typing.Union[MetaOapg.properties.matches, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "inner_intf", "outer_intf", "inner_subnet", "outer_subnet", "local_port", "remote_end", "private_key", "public_key", "matches", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        inner_intf: typing.Union[MetaOapg.properties.inner_intf, str, schemas.Unset] = schemas.unset,
        outer_intf: typing.Union[MetaOapg.properties.outer_intf, str, schemas.Unset] = schemas.unset,
        inner_subnet: typing.Union[MetaOapg.properties.inner_subnet, str, schemas.Unset] = schemas.unset,
        outer_subnet: typing.Union[MetaOapg.properties.outer_subnet, str, schemas.Unset] = schemas.unset,
        local_port: typing.Union[MetaOapg.properties.local_port, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        remote_end: typing.Union[MetaOapg.properties.remote_end, str, schemas.Unset] = schemas.unset,
        private_key: typing.Union[MetaOapg.properties.private_key, str, schemas.Unset] = schemas.unset,
        public_key: typing.Union[MetaOapg.properties.public_key, str, schemas.Unset] = schemas.unset,
        matches: typing.Union[MetaOapg.properties.matches, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TunnelEntry':
        return super().__new__(
            cls,
            *_args,
            id=id,
            inner_intf=inner_intf,
            outer_intf=outer_intf,
            inner_subnet=inner_subnet,
            outer_subnet=outer_subnet,
            local_port=local_port,
            remote_end=remote_end,
            private_key=private_key,
            public_key=public_key,
            matches=matches,
            _configuration=_configuration,
            **kwargs,
        )
