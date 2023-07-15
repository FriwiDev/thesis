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


class DomainConfiguration(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The configuration for this service
    """


    class MetaOapg:
        
        class properties:
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def DSMF(cls):
                    return cls("DSMF")
                
                @schemas.classproperty
                def DTMF(cls):
                    return cls("DTMF")
            network = schemas.StrSchema
            
            
            class controllers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ControllerConfiguration']:
                        return ControllerConfiguration
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ControllerConfiguration'], typing.List['ControllerConfiguration']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'controllers':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ControllerConfiguration':
                    return super().__getitem__(i)
            
            
            class vpn_gateways(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['DeviceConfiguration']:
                        return DeviceConfiguration
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['DeviceConfiguration'], typing.List['DeviceConfiguration']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'vpn_gateways':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'DeviceConfiguration':
                    return super().__getitem__(i)
            
            
            class switches(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['DeviceConfiguration']:
                        return DeviceConfiguration
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['DeviceConfiguration'], typing.List['DeviceConfiguration']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'switches':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'DeviceConfiguration':
                    return super().__getitem__(i)
            
            
            class network_borders(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['NetworkBorderConfiguration']:
                        return NetworkBorderConfiguration
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['NetworkBorderConfiguration'], typing.List['NetworkBorderConfiguration']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'network_borders':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'NetworkBorderConfiguration':
                    return super().__getitem__(i)
            
            
            class networks(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['NetworkConfiguration']:
                        return NetworkConfiguration
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['NetworkConfiguration'], typing.List['NetworkConfiguration']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'networks':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'NetworkConfiguration':
                    return super().__getitem__(i)
            reservable_bitrate = schemas.IntSchema
            __annotations__ = {
                "type": type,
                "network": network,
                "controllers": controllers,
                "vpn_gateways": vpn_gateways,
                "switches": switches,
                "network_borders": network_borders,
                "networks": networks,
                "reservable_bitrate": reservable_bitrate,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["network"]) -> MetaOapg.properties.network: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["controllers"]) -> MetaOapg.properties.controllers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vpn_gateways"]) -> MetaOapg.properties.vpn_gateways: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["switches"]) -> MetaOapg.properties.switches: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["network_borders"]) -> MetaOapg.properties.network_borders: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["networks"]) -> MetaOapg.properties.networks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reservable_bitrate"]) -> MetaOapg.properties.reservable_bitrate: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "network", "controllers", "vpn_gateways", "switches", "network_borders", "networks", "reservable_bitrate", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["network"]) -> typing.Union[MetaOapg.properties.network, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["controllers"]) -> typing.Union[MetaOapg.properties.controllers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vpn_gateways"]) -> typing.Union[MetaOapg.properties.vpn_gateways, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["switches"]) -> typing.Union[MetaOapg.properties.switches, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["network_borders"]) -> typing.Union[MetaOapg.properties.network_borders, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["networks"]) -> typing.Union[MetaOapg.properties.networks, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reservable_bitrate"]) -> typing.Union[MetaOapg.properties.reservable_bitrate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "network", "controllers", "vpn_gateways", "switches", "network_borders", "networks", "reservable_bitrate", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        network: typing.Union[MetaOapg.properties.network, str, schemas.Unset] = schemas.unset,
        controllers: typing.Union[MetaOapg.properties.controllers, list, tuple, schemas.Unset] = schemas.unset,
        vpn_gateways: typing.Union[MetaOapg.properties.vpn_gateways, list, tuple, schemas.Unset] = schemas.unset,
        switches: typing.Union[MetaOapg.properties.switches, list, tuple, schemas.Unset] = schemas.unset,
        network_borders: typing.Union[MetaOapg.properties.network_borders, list, tuple, schemas.Unset] = schemas.unset,
        networks: typing.Union[MetaOapg.properties.networks, list, tuple, schemas.Unset] = schemas.unset,
        reservable_bitrate: typing.Union[MetaOapg.properties.reservable_bitrate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DomainConfiguration':
        return super().__new__(
            cls,
            *_args,
            type=type,
            network=network,
            controllers=controllers,
            vpn_gateways=vpn_gateways,
            switches=switches,
            network_borders=network_borders,
            networks=networks,
            reservable_bitrate=reservable_bitrate,
            _configuration=_configuration,
            **kwargs,
        )

from dsmf_client.model.controller_configuration import ControllerConfiguration
from dsmf_client.model.device_configuration import DeviceConfiguration
from dsmf_client.model.network_border_configuration import NetworkBorderConfiguration
from dsmf_client.model.network_configuration import NetworkConfiguration