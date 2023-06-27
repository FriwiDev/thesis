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


class SwitchFlow(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A switch flow
    """


    class MetaOapg:
        
        class properties:
            dpid = schemas.IntSchema
            length = schemas.IntSchema
            buffer_id = schemas.IntSchema
            table_id = schemas.IntSchema
            duration_sec = schemas.IntSchema
            duration_nsec = schemas.IntSchema
            priority = schemas.IntSchema
            idle_timeout = schemas.IntSchema
            hard_timeout = schemas.IntSchema
            flags = schemas.IntSchema
            cookie = schemas.IntSchema
            packet_count = schemas.IntSchema
            byte_count = schemas.IntSchema
        
            @staticmethod
            def match() -> typing.Type['SwitchFlowMatchV12']:
                return SwitchFlowMatchV12
            
            
            class actions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'actions':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class instructions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SwitchFlowInstruction']:
                        return SwitchFlowInstruction
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['SwitchFlowInstruction'], typing.List['SwitchFlowInstruction']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'instructions':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SwitchFlowInstruction':
                    return super().__getitem__(i)
            __annotations__ = {
                "dpid": dpid,
                "length": length,
                "buffer_id": buffer_id,
                "table_id": table_id,
                "duration_sec": duration_sec,
                "duration_nsec": duration_nsec,
                "priority": priority,
                "idle_timeout": idle_timeout,
                "hard_timeout": hard_timeout,
                "flags": flags,
                "cookie": cookie,
                "packet_count": packet_count,
                "byte_count": byte_count,
                "match": match,
                "actions": actions,
                "instructions": instructions,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dpid"]) -> MetaOapg.properties.dpid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["length"]) -> MetaOapg.properties.length: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["buffer_id"]) -> MetaOapg.properties.buffer_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["table_id"]) -> MetaOapg.properties.table_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration_sec"]) -> MetaOapg.properties.duration_sec: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration_nsec"]) -> MetaOapg.properties.duration_nsec: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priority"]) -> MetaOapg.properties.priority: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idle_timeout"]) -> MetaOapg.properties.idle_timeout: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hard_timeout"]) -> MetaOapg.properties.hard_timeout: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flags"]) -> MetaOapg.properties.flags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cookie"]) -> MetaOapg.properties.cookie: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["packet_count"]) -> MetaOapg.properties.packet_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["byte_count"]) -> MetaOapg.properties.byte_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["match"]) -> 'SwitchFlowMatchV12': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actions"]) -> MetaOapg.properties.actions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["instructions"]) -> MetaOapg.properties.instructions: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["dpid", "length", "buffer_id", "table_id", "duration_sec", "duration_nsec", "priority", "idle_timeout", "hard_timeout", "flags", "cookie", "packet_count", "byte_count", "match", "actions", "instructions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dpid"]) -> typing.Union[MetaOapg.properties.dpid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["length"]) -> typing.Union[MetaOapg.properties.length, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["buffer_id"]) -> typing.Union[MetaOapg.properties.buffer_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["table_id"]) -> typing.Union[MetaOapg.properties.table_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration_sec"]) -> typing.Union[MetaOapg.properties.duration_sec, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration_nsec"]) -> typing.Union[MetaOapg.properties.duration_nsec, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priority"]) -> typing.Union[MetaOapg.properties.priority, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idle_timeout"]) -> typing.Union[MetaOapg.properties.idle_timeout, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hard_timeout"]) -> typing.Union[MetaOapg.properties.hard_timeout, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flags"]) -> typing.Union[MetaOapg.properties.flags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cookie"]) -> typing.Union[MetaOapg.properties.cookie, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["packet_count"]) -> typing.Union[MetaOapg.properties.packet_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["byte_count"]) -> typing.Union[MetaOapg.properties.byte_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["match"]) -> typing.Union['SwitchFlowMatchV12', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actions"]) -> typing.Union[MetaOapg.properties.actions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["instructions"]) -> typing.Union[MetaOapg.properties.instructions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["dpid", "length", "buffer_id", "table_id", "duration_sec", "duration_nsec", "priority", "idle_timeout", "hard_timeout", "flags", "cookie", "packet_count", "byte_count", "match", "actions", "instructions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        dpid: typing.Union[MetaOapg.properties.dpid, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        length: typing.Union[MetaOapg.properties.length, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        buffer_id: typing.Union[MetaOapg.properties.buffer_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        table_id: typing.Union[MetaOapg.properties.table_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        duration_sec: typing.Union[MetaOapg.properties.duration_sec, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        duration_nsec: typing.Union[MetaOapg.properties.duration_nsec, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        priority: typing.Union[MetaOapg.properties.priority, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        idle_timeout: typing.Union[MetaOapg.properties.idle_timeout, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        hard_timeout: typing.Union[MetaOapg.properties.hard_timeout, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        flags: typing.Union[MetaOapg.properties.flags, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        cookie: typing.Union[MetaOapg.properties.cookie, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        packet_count: typing.Union[MetaOapg.properties.packet_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        byte_count: typing.Union[MetaOapg.properties.byte_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        match: typing.Union['SwitchFlowMatchV12', schemas.Unset] = schemas.unset,
        actions: typing.Union[MetaOapg.properties.actions, list, tuple, schemas.Unset] = schemas.unset,
        instructions: typing.Union[MetaOapg.properties.instructions, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SwitchFlow':
        return super().__new__(
            cls,
            *_args,
            dpid=dpid,
            length=length,
            buffer_id=buffer_id,
            table_id=table_id,
            duration_sec=duration_sec,
            duration_nsec=duration_nsec,
            priority=priority,
            idle_timeout=idle_timeout,
            hard_timeout=hard_timeout,
            flags=flags,
            cookie=cookie,
            packet_count=packet_count,
            byte_count=byte_count,
            match=match,
            actions=actions,
            instructions=instructions,
            _configuration=_configuration,
            **kwargs,
        )

from controller_client.model.switch_flow_instruction import SwitchFlowInstruction
from controller_client.model.switch_flow_match_v12 import SwitchFlowMatchV12
