# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import uuid  # noqa: F401
from dataclasses import dataclass
from datetime import date, datetime  # noqa: F401

import frozendict  # noqa: F401
import typing_extensions  # noqa: F401
import urllib3
from switch_client import api_client, exceptions
from switch_client import schemas  # noqa: F401

# Query params
AuthSchema = schemas.StrSchema
IdSchema = schemas.Int32Schema
PortSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'auth': typing.Union[AuthSchema, str,],
        'id': typing.Union[IdSchema, decimal.Decimal, int,],
        'port': typing.Union[PortSchema, str,],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_auth = api_client.QueryParameter(
    name="auth",
    style=api_client.ParameterStyle.FORM,
    schema=AuthSchema,
    required=True,
    explode=True,
)
request_query_id = api_client.QueryParameter(
    name="id",
    style=api_client.ParameterStyle.FORM,
    schema=IdSchema,
    required=True,
    explode=True,
)
request_query_port = api_client.QueryParameter(
    name="port",
    style=api_client.ParameterStyle.FORM,
    schema=PortSchema,
    required=True,
    explode=True,
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
)


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
)


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
)


class BaseApi(api_client.Api):
    @typing.overload
    def _queue_delete_oapg(
            self,
            query_params: RequestQueryParams = frozendict.frozendict(),
            stream: bool = False,
            timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
            skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]:
        ...

    @typing.overload
    def _queue_delete_oapg(
            self,
            skip_deserialization: typing_extensions.Literal[True],
            query_params: RequestQueryParams = frozendict.frozendict(),
            stream: bool = False,
            timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization:
        ...

    @typing.overload
    def _queue_delete_oapg(
            self,
            query_params: RequestQueryParams = frozendict.frozendict(),
            stream: bool = False,
            timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
            skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        ...

    def _queue_delete_oapg(
            self,
            query_params: RequestQueryParams = frozendict.frozendict(),
            stream: bool = False,
            timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
            skip_deserialization: bool = False,
    ):
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
                request_query_auth,
                request_query_id,
                request_query_port,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
        # TODO add cookie handling

        response = self.api_client.call_api(
            resource_path=used_path,
            method='delete'.upper(),
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class QueueDelete(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def queue_delete(
            self,
            query_params: RequestQueryParams = frozendict.frozendict(),
            stream: bool = False,
            timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
            skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def queue_delete(
            self,
            skip_deserialization: typing_extensions.Literal[True],
            query_params: RequestQueryParams = frozendict.frozendict(),
            stream: bool = False,
            timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def queue_delete(
            self,
            query_params: RequestQueryParams = frozendict.frozendict(),
            stream: bool = False,
            timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
            skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def queue_delete(
            self,
            query_params: RequestQueryParams = frozendict.frozendict(),
            stream: bool = False,
            timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
            skip_deserialization: bool = False,
    ):
        return self._queue_delete_oapg(
            query_params=query_params,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiFordelete(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def delete(
            self,
            query_params: RequestQueryParams = frozendict.frozendict(),
            stream: bool = False,
            timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
            skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def delete(
            self,
            skip_deserialization: typing_extensions.Literal[True],
            query_params: RequestQueryParams = frozendict.frozendict(),
            stream: bool = False,
            timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def delete(
            self,
            query_params: RequestQueryParams = frozendict.frozendict(),
            stream: bool = False,
            timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
            skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def delete(
            self,
            query_params: RequestQueryParams = frozendict.frozendict(),
            stream: bool = False,
            timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
            skip_deserialization: bool = False,
    ):
        return self._queue_delete_oapg(
            query_params=query_params,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )
