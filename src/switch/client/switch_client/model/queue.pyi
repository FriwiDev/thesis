# coding: utf-8

"""
    Switch QoS API

    A simple API to manage QoS queues and traffic shaping on arbitrary OpenFlow switches. Does not support listing queues (GET) because this is already part of OpenFlow.  # noqa: E501

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

from switch_client import schemas  # noqa: F401


class Queue(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            queue_id = schemas.Int32Schema
            min_rate = schemas.Int64Schema
            max_rate = schemas.Int64Schema
            burst_rate = schemas.Int64Schema
            priority = schemas.Int32Schema
            port = schemas.StrSchema
            __annotations__ = {
                "queue_id": queue_id,
                "min_rate": min_rate,
                "max_rate": max_rate,
                "burst_rate": burst_rate,
                "priority": priority,
                "port": port,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["queue_id"]) -> MetaOapg.properties.queue_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["min_rate"]) -> MetaOapg.properties.min_rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max_rate"]) -> MetaOapg.properties.max_rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["burst_rate"]) -> MetaOapg.properties.burst_rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priority"]) -> MetaOapg.properties.priority: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["port"]) -> MetaOapg.properties.port: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["queue_id", "min_rate", "max_rate", "burst_rate", "priority", "port", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["queue_id"]) -> typing.Union[MetaOapg.properties.queue_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["min_rate"]) -> typing.Union[MetaOapg.properties.min_rate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max_rate"]) -> typing.Union[MetaOapg.properties.max_rate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["burst_rate"]) -> typing.Union[MetaOapg.properties.burst_rate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priority"]) -> typing.Union[MetaOapg.properties.priority, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["port"]) -> typing.Union[MetaOapg.properties.port, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["queue_id", "min_rate", "max_rate", "burst_rate", "priority", "port", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        queue_id: typing.Union[MetaOapg.properties.queue_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        min_rate: typing.Union[MetaOapg.properties.min_rate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        max_rate: typing.Union[MetaOapg.properties.max_rate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        burst_rate: typing.Union[MetaOapg.properties.burst_rate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        priority: typing.Union[MetaOapg.properties.priority, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        port: typing.Union[MetaOapg.properties.port, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Queue':
        return super().__new__(
            cls,
            *_args,
            queue_id=queue_id,
            min_rate=min_rate,
            max_rate=max_rate,
            burst_rate=burst_rate,
            priority=priority,
            port=port,
            _configuration=_configuration,
            **kwargs,
        )
