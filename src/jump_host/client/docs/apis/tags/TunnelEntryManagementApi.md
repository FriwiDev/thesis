<a id="__pageTop"></a>
# jump_host_client.apis.tags.tunnel_entry_management_api.TunnelEntryManagementApi

All URIs are relative to *http://localhost:8083/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tunnel_entry_delete**](#tunnel_entry_delete) | **delete** /tunnel_entry | 
[**tunnel_entry_get**](#tunnel_entry_get) | **get** /tunnel_entry | 
[**tunnel_entry_put**](#tunnel_entry_put) | **put** /tunnel_entry | 

# **tunnel_entry_delete**
<a id="tunnel_entry_delete"></a>
> tunnel_entry_delete(authtunnel_entry_id)



Deletes a tunnel entry

### Example

```python
import jump_host_client
from jump_host_client.apis.tags import tunnel_entry_management_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8083/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = jump_host_client.Configuration(
    host = "http://localhost:8083/v1"
)

# Enter a context with an instance of the API client
with jump_host_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tunnel_entry_management_api.TunnelEntryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'auth': "auth_example",
        'tunnel_entry_id': 1,
    }
    try:
        api_response = api_instance.tunnel_entry_delete(
            query_params=query_params,
        )
    except jump_host_client.ApiException as e:
        print("Exception when calling TunnelEntryManagementApi->tunnel_entry_delete: %s\n" % e)
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
tunnel_entry_id | TunnelEntryIdSchema | | 


# AuthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TunnelEntryIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#tunnel_entry_delete.ApiResponseFor200) | The tunnel entry was successfully deleted.
403 | [ApiResponseFor403](#tunnel_entry_delete.ApiResponseFor403) | Invalid authentication provided.
404 | [ApiResponseFor404](#tunnel_entry_delete.ApiResponseFor404) | The tunnel entry could not be found.

#### tunnel_entry_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### tunnel_entry_delete.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### tunnel_entry_delete.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **tunnel_entry_get**
<a id="tunnel_entry_get"></a>
> [TunnelEntry] tunnel_entry_get(auth)



Lists all current tunnel entries

### Example

```python
import jump_host_client
from jump_host_client.apis.tags import tunnel_entry_management_api
from jump_host_client.model.tunnel_entry import TunnelEntry
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8083/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = jump_host_client.Configuration(
    host = "http://localhost:8083/v1"
)

# Enter a context with an instance of the API client
with jump_host_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tunnel_entry_management_api.TunnelEntryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'auth': "auth_example",
    }
    try:
        api_response = api_instance.tunnel_entry_get(
            query_params=query_params,
        )
        pprint(api_response)
    except jump_host_client.ApiException as e:
        print("Exception when calling TunnelEntryManagementApi->tunnel_entry_get: %s\n" % e)
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
200 | [ApiResponseFor200](#tunnel_entry_get.ApiResponseFor200) | The current list of tunnel entries
403 | [ApiResponseFor403](#tunnel_entry_get.ApiResponseFor403) | Invalid authentication provided

#### tunnel_entry_get.ApiResponseFor200
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
[**TunnelEntry**]({{complexTypePrefix}}TunnelEntry.md) | [**TunnelEntry**]({{complexTypePrefix}}TunnelEntry.md) | [**TunnelEntry**]({{complexTypePrefix}}TunnelEntry.md) |  | 

#### tunnel_entry_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **tunnel_entry_put**
<a id="tunnel_entry_put"></a>
> tunnel_entry_put(auth)



Creates a new tunnel entry

### Example

```python
import jump_host_client
from jump_host_client.apis.tags import tunnel_entry_management_api
from jump_host_client.model.tunnel_entry import TunnelEntry
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8083/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = jump_host_client.Configuration(
    host = "http://localhost:8083/v1"
)

# Enter a context with an instance of the API client
with jump_host_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tunnel_entry_management_api.TunnelEntryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'auth': "auth_example",
    }
    try:
        api_response = api_instance.tunnel_entry_put(
            query_params=query_params,
        )
    except jump_host_client.ApiException as e:
        print("Exception when calling TunnelEntryManagementApi->tunnel_entry_put: %s\n" % e)

    # example passing only optional values
    query_params = {
        'auth': "auth_example",
    }
    body = TunnelEntry(
        id=1,
        inner_intf="inner_intf_example",
        outer_intf="outer_intf_example",
        inner_subnet="inner_subnet_example",
        outer_subnet="outer_subnet_example",
        local_port=1,
        remote_end="remote_end_example",
        private_key="private_key_example",
        public_key="public_key_example",
    )
    try:
        api_response = api_instance.tunnel_entry_put(
            query_params=query_params,
            body=body,
        )
    except jump_host_client.ApiException as e:
        print("Exception when calling TunnelEntryManagementApi->tunnel_entry_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TunnelEntry**](../../models/TunnelEntry.md) |  | 


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
200 | [ApiResponseFor200](#tunnel_entry_put.ApiResponseFor200) | The tunnel entry has been created
400 | [ApiResponseFor400](#tunnel_entry_put.ApiResponseFor400) | No body provided.
403 | [ApiResponseFor403](#tunnel_entry_put.ApiResponseFor403) | Invalid authentication provided.
404 | [ApiResponseFor404](#tunnel_entry_put.ApiResponseFor404) | A specified interface could not be found
406 | [ApiResponseFor406](#tunnel_entry_put.ApiResponseFor406) | A value exceeds the allowed range
409 | [ApiResponseFor409](#tunnel_entry_put.ApiResponseFor409) | Tunnel entry id or specified ports already in use
507 | [ApiResponseFor507](#tunnel_entry_put.ApiResponseFor507) | Already too many tunnel entries in use

#### tunnel_entry_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### tunnel_entry_put.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### tunnel_entry_put.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### tunnel_entry_put.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### tunnel_entry_put.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### tunnel_entry_put.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### tunnel_entry_put.ApiResponseFor507
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

