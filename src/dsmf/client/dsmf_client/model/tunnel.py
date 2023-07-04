# coding: utf-8

"""
    DSMF

    A simple API to interact with the Domain Slice Management Function. Supports reserving, creating and removing slices and tunnels from one external domain to another external domain or host. Please refer to the topology drawings for further information about the network structures.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401
from datetime import date, datetime  # noqa: F401

import frozendict  # noqa: F401
from dsmf_client import schemas  # noqa: F401


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

            @staticmethod
            def _from() -> typing.Type['Endpoint']:
                return Endpoint

            @staticmethod
            def to() -> typing.Type['Endpoint']:
                return Endpoint

            private_key = schemas.StrSchema
            public_key = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "min_rate": min_rate,
                "max_rate": max_rate,
                "burst_rate": burst_rate,
                "latency": latency,
                "from": _from,
                "to": to,
                "private_key": private_key,
                "public_key": public_key,
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
    def __getitem__(self, name: typing_extensions.Literal["from"]) -> 'Endpoint': ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to"]) -> 'Endpoint': ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["private_key"]) -> MetaOapg.properties.private_key: ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["public_key"]) -> MetaOapg.properties.public_key: ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...

    def __getitem__(self, name: typing.Union[typing_extensions.Literal[
        "id", "min_rate", "max_rate", "burst_rate", "latency", "from", "to", "private_key", "public_key",], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[
        MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["min_rate"]) -> typing.Union[MetaOapg.properties.min_rate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max_rate"]) -> typing.Union[MetaOapg.properties.max_rate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["burst_rate"]) -> typing.Union[MetaOapg.properties.burst_rate, schemas.Unset]: ...

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["latency"]) -> typing.Union[
        MetaOapg.properties.latency, schemas.Unset]: ...

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from"]) -> typing.Union['Endpoint', schemas.Unset]: ...

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to"]) -> typing.Union['Endpoint', schemas.Unset]: ...

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["private_key"]) -> typing.Union[
        MetaOapg.properties.private_key, schemas.Unset]: ...

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["public_key"]) -> typing.Union[
        MetaOapg.properties.public_key, schemas.Unset]: ...

    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...

    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal[
        "id", "min_rate", "max_rate", "burst_rate", "latency", "from", "to", "private_key", "public_key",], str]):
        return super().get_item_oapg(name)

    def __new__(
            cls,
            *_args: typing.Union[dict, frozendict.frozendict,],
            id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
            min_rate: typing.Union[MetaOapg.properties.min_rate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
            max_rate: typing.Union[MetaOapg.properties.max_rate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
            burst_rate: typing.Union[
                MetaOapg.properties.burst_rate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
            latency: typing.Union[MetaOapg.properties.latency, decimal.Decimal, int, schemas.Unset] = schemas.unset,
            to: typing.Union['Endpoint', schemas.Unset] = schemas.unset,
            private_key: typing.Union[MetaOapg.properties.private_key, str, schemas.Unset] = schemas.unset,
            public_key: typing.Union[MetaOapg.properties.public_key, str, schemas.Unset] = schemas.unset,
            _configuration: typing.Optional[schemas.Configuration] = None,
            **kwargs: typing.Union[
                schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
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
            private_key=private_key,
            public_key=public_key,
            _configuration=_configuration,
            **kwargs,
        )

from dsmf_client.model.endpoint import Endpoint
