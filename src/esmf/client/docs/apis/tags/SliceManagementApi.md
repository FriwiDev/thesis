<a id="__pageTop"></a>
# esmf_client.apis.tags.slice_management_api.SliceManagementApi

All URIs are relative to *http://localhost:8080/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slice_delete**](#slice_delete) | **delete** /slice | 
[**slice_get**](#slice_get) | **get** /slice | 
[**slice_put**](#slice_put) | **put** /slice | 

# **slice_delete**
<a id="slice_delete"></a>
> slice_delete(authslice_ids)



Deletes one or multiple slices

### Example

```python
import esmf_client
from esmf_client.apis.tags import slice_management_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = esmf_client.Configuration(
    host = "http://localhost:8080/v1"
)

# Enter a context with an instance of the API client
with esmf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slice_management_api.SliceManagementApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'auth': "auth_example",
        'slice_ids': [
        1
    ],
    }
    try:
        api_response = api_instance.slice_delete(
            query_params=query_params,
        )
    except esmf_client.ApiException as e:
        print("Exception when calling SliceManagementApi->slice_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
auth | AuthSchema | | 
slice_ids | SliceIdsSchema | | 


# AuthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SliceIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slice_delete.ApiResponseFor200) | The slices were successfully deleted.
403 | [ApiResponseFor403](#slice_delete.ApiResponseFor403) | Invalid or insufficient authentication provided.
429 | [ApiResponseFor429](#slice_delete.ApiResponseFor429) | Please slow down. You may only use slice actions every couple of seconds.
404 | [ApiResponseFor404](#slice_delete.ApiResponseFor404) | One or multiple of the slices could not be found.
417 | [ApiResponseFor417](#slice_delete.ApiResponseFor417) | No slice ids were provided.
421 | [ApiResponseFor421](#slice_delete.ApiResponseFor421) | Slice management is not supported by this service
500 | [ApiResponseFor500](#slice_delete.ApiResponseFor500) | Internal error

#### slice_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### slice_delete.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### slice_delete.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### slice_delete.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### slice_delete.ApiResponseFor417
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### slice_delete.ApiResponseFor421
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### slice_delete.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slice_get**
<a id="slice_get"></a>
> [Slice] slice_get(auth)



Lists all current slices by this requester

### Example

```python
import esmf_client
from esmf_client.apis.tags import slice_management_api
from esmf_client.model.slice import Slice
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = esmf_client.Configuration(
    host = "http://localhost:8080/v1"
)

# Enter a context with an instance of the API client
with esmf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slice_management_api.SliceManagementApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'auth': "auth_example",
    }
    try:
        api_response = api_instance.slice_get(
            query_params=query_params,
        )
        pprint(api_response)
    except esmf_client.ApiException as e:
        print("Exception when calling SliceManagementApi->slice_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
auth | AuthSchema | | 


# AuthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slice_get.ApiResponseFor200) | The current list of slices assigned to this requester
403 | [ApiResponseFor403](#slice_get.ApiResponseFor403) | Invalid authentication provided
421 | [ApiResponseFor421](#slice_get.ApiResponseFor421) | Slice management is not supported by this service

#### slice_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Slice**]({{complexTypePrefix}}Slice.md) | [**Slice**]({{complexTypePrefix}}Slice.md) | [**Slice**]({{complexTypePrefix}}Slice.md) |  | 

#### slice_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### slice_get.ApiResponseFor421
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slice_put**
<a id="slice_put"></a>
> [Slice] slice_put(auth)



Creates one or multiple new slices from one host to another. Will either create all slices if feasible or none at all.

### Example

```python
import esmf_client
from esmf_client.apis.tags import slice_management_api
from esmf_client.model.slice import Slice
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = esmf_client.Configuration(
    host = "http://localhost:8080/v1"
)

# Enter a context with an instance of the API client
with esmf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slice_management_api.SliceManagementApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'auth': "auth_example",
    }
    try:
        api_response = api_instance.slice_put(
            query_params=query_params,
        )
        pprint(api_response)
    except esmf_client.ApiException as e:
        print("Exception when calling SliceManagementApi->slice_put: %s\n" % e)

    # example passing only optional values
    query_params = {
        'auth': "auth_example",
    }
    body = [
        Slice(
            slice_id=1,
            min_rate=1,
            max_rate=1,
            burst_rate=1,
            latency=1,
            tunnel_id=1,
            transport_protocol="UDP",
            fr=Endpoint(
                ip="ip_example",
                port=0,
                name="name_example",
                network="network_example",
            ),
,
        )
    ]
    try:
        api_response = api_instance.slice_put(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except esmf_client.ApiException as e:
        print("Exception when calling SliceManagementApi->slice_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Slice**]({{complexTypePrefix}}Slice.md) | [**Slice**]({{complexTypePrefix}}Slice.md) | [**Slice**]({{complexTypePrefix}}Slice.md) |  | 

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
auth | AuthSchema | | 


# AuthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slice_put.ApiResponseFor200) | The slices have been deployed. Returns the parameters of the deployed slices, including the fresh ids.
403 | [ApiResponseFor403](#slice_put.ApiResponseFor403) | Invalid or insufficient authentication provided
429 | [ApiResponseFor429](#slice_put.ApiResponseFor429) | Please slow down. You may only use slice actions every couple of seconds.
404 | [ApiResponseFor404](#slice_put.ApiResponseFor404) | The input or output of one or multiple of the slices could not be found
417 | [ApiResponseFor417](#slice_put.ApiResponseFor417) | No slices were requested
421 | [ApiResponseFor421](#slice_put.ApiResponseFor421) | Slice management is not supported by this service
422 | [ApiResponseFor422](#slice_put.ApiResponseFor422) | Can not handle slices not originating from or to our network
500 | [ApiResponseFor500](#slice_put.ApiResponseFor500) | Internal error
507 | [ApiResponseFor507](#slice_put.ApiResponseFor507) | Insufficient resources by participating domain or requester

#### slice_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Slice**]({{complexTypePrefix}}Slice.md) | [**Slice**]({{complexTypePrefix}}Slice.md) | [**Slice**]({{complexTypePrefix}}Slice.md) |  | 

#### slice_put.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### slice_put.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### slice_put.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### slice_put.ApiResponseFor417
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### slice_put.ApiResponseFor421
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### slice_put.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### slice_put.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### slice_put.ApiResponseFor507
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

