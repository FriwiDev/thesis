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


class SwitchQueueStat(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Switch queue stats
    """


    class MetaOapg:
        
        class properties:
            port_no = schemas.IntSchema
            queue_id = schemas.IntSchema
            tx_bytes = schemas.IntSchema
            tx_packets = schemas.IntSchema
            tx_errors = schemas.IntSchema
            duration_sec = schemas.IntSchema
            duration_nsec = schemas.IntSchema
            length = schemas.IntSchema
            
            
            class properties(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            additional_properties = schemas.AnyTypeSchema
                        
                        def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                            return super().get_item_oapg(name)
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'properties':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "port_no": port_no,
                "queue_id": queue_id,
                "tx_bytes": tx_bytes,
                "tx_packets": tx_packets,
                "tx_errors": tx_errors,
                "duration_sec": duration_sec,
                "duration_nsec": duration_nsec,
                "length": length,
                "properties": properties,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["port_no"]) -> MetaOapg.properties.port_no: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["queue_id"]) -> MetaOapg.properties.queue_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tx_bytes"]) -> MetaOapg.properties.tx_bytes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tx_packets"]) -> MetaOapg.properties.tx_packets: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tx_errors"]) -> MetaOapg.properties.tx_errors: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration_sec"]) -> MetaOapg.properties.duration_sec: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration_nsec"]) -> MetaOapg.properties.duration_nsec: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["length"]) -> MetaOapg.properties.length: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["properties"]) -> MetaOapg.properties.properties: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["port_no", "queue_id", "tx_bytes", "tx_packets", "tx_errors", "duration_sec", "duration_nsec", "length", "properties", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["port_no"]) -> typing.Union[MetaOapg.properties.port_no, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["queue_id"]) -> typing.Union[MetaOapg.properties.queue_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tx_bytes"]) -> typing.Union[MetaOapg.properties.tx_bytes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tx_packets"]) -> typing.Union[MetaOapg.properties.tx_packets, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tx_errors"]) -> typing.Union[MetaOapg.properties.tx_errors, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration_sec"]) -> typing.Union[MetaOapg.properties.duration_sec, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration_nsec"]) -> typing.Union[MetaOapg.properties.duration_nsec, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["length"]) -> typing.Union[MetaOapg.properties.length, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["properties"]) -> typing.Union[MetaOapg.properties.properties, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["port_no", "queue_id", "tx_bytes", "tx_packets", "tx_errors", "duration_sec", "duration_nsec", "length", "properties", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        port_no: typing.Union[MetaOapg.properties.port_no, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        queue_id: typing.Union[MetaOapg.properties.queue_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        tx_bytes: typing.Union[MetaOapg.properties.tx_bytes, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        tx_packets: typing.Union[MetaOapg.properties.tx_packets, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        tx_errors: typing.Union[MetaOapg.properties.tx_errors, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        duration_sec: typing.Union[MetaOapg.properties.duration_sec, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        duration_nsec: typing.Union[MetaOapg.properties.duration_nsec, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        length: typing.Union[MetaOapg.properties.length, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        properties: typing.Union[MetaOapg.properties.properties, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SwitchQueueStat':
        return super().__new__(
            cls,
            *_args,
            port_no=port_no,
            queue_id=queue_id,
            tx_bytes=tx_bytes,
            tx_packets=tx_packets,
            tx_errors=tx_errors,
            duration_sec=duration_sec,
            duration_nsec=duration_nsec,
            length=length,
            properties=properties,
            _configuration=_configuration,
            **kwargs,
        )