<a id="__pageTop"></a>
# controller_client.apis.tags.flow_management_api.FlowManagementApi

All URIs are relative to *http://localhost:8080/stats*

Method | HTTP request | Description
------------- | ------------- | -------------
[**flow_dpid_get**](#flow_dpid_get) | **get** /flow/{dpid} | 
[**flow_dpid_post**](#flow_dpid_post) | **post** /flow/{dpid} | 
[**flowentry_add_post**](#flowentry_add_post) | **post** /flowentry/add | 
[**flowentry_clear_dpid_delete**](#flowentry_clear_dpid_delete) | **delete** /flowentry/clear/{dpid} | 
[**flowentry_delete_post**](#flowentry_delete_post) | **post** /flowentry/delete | 
[**flowentry_delete_strict_post**](#flowentry_delete_strict_post) | **post** /flowentry/delete_strict | 

# **flow_dpid_get**
<a id="flow_dpid_get"></a>
> {str: (SwitchFlow,)} flow_dpid_get(dpid)



Fetch the flow stats of a switch.

### Example

```python
import controller_client
from controller_client.apis.tags import flow_management_api
from controller_client.model.switch_flow import SwitchFlow
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/stats
# See configuration.py for a list of all supported configuration parameters.
configuration = controller_client.Configuration(
    host = "http://localhost:8080/stats"
)

# Enter a context with an instance of the API client
with controller_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flow_management_api.FlowManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dpid': 1,
    }
    try:
        api_response = api_instance.flow_dpid_get(
            path_params=path_params,
        )
        pprint(api_response)
    except controller_client.ApiException as e:
        print("Exception when calling FlowManagementApi->flow_dpid_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
dpid | DpidSchema | | 

# DpidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#flow_dpid_get.ApiResponseFor200) | The switch stats
404 | [ApiResponseFor404](#flow_dpid_get.ApiResponseFor404) | Switch not found

#### flow_dpid_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**SwitchFlow**]({{complexTypePrefix}}SwitchFlow.md) | [**SwitchFlow**]({{complexTypePrefix}}SwitchFlow.md) | any string name can be used but the value must be the correct type | [optional] 

#### flow_dpid_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **flow_dpid_post**
<a id="flow_dpid_post"></a>
> {str: (SwitchFlow,)} flow_dpid_post(dpid)



Fetch the flow stats of a switch.

### Example

```python
import controller_client
from controller_client.apis.tags import flow_management_api
from controller_client.model.switch_flow_query import SwitchFlowQuery
from controller_client.model.switch_flow import SwitchFlow
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/stats
# See configuration.py for a list of all supported configuration parameters.
configuration = controller_client.Configuration(
    host = "http://localhost:8080/stats"
)

# Enter a context with an instance of the API client
with controller_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flow_management_api.FlowManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dpid': 1,
    }
    try:
        api_response = api_instance.flow_dpid_post(
            path_params=path_params,
        )
        pprint(api_response)
    except controller_client.ApiException as e:
        print("Exception when calling FlowManagementApi->flow_dpid_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'dpid': 1,
    }
    body = SwitchFlowQuery(
        table_id=0,
        out_port=2,
        out_group=1,
        cookie=1,
        cookie_mask=1,
        match=SwitchFlowMatchV12(
            in_port=7,
            eth_src="aa:bb:cc:11:22:33",
            eth_dst="aa:bb:cc:11:22:33",
            eth_type=123,
            tcp_src=1,
            tcp_dst=2,
            udp_src=1,
            udp_dst=2,
        ),
        priority=0,
    )
    try:
        api_response = api_instance.flow_dpid_post(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except controller_client.ApiException as e:
        print("Exception when calling FlowManagementApi->flow_dpid_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SwitchFlowQuery**](../../models/SwitchFlowQuery.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
dpid | DpidSchema | | 

# DpidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#flow_dpid_post.ApiResponseFor200) | The switch stats
404 | [ApiResponseFor404](#flow_dpid_post.ApiResponseFor404) | Switch not found

#### flow_dpid_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**SwitchFlow**]({{complexTypePrefix}}SwitchFlow.md) | [**SwitchFlow**]({{complexTypePrefix}}SwitchFlow.md) | any string name can be used but the value must be the correct type | [optional] 

#### flow_dpid_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **flowentry_add_post**
<a id="flowentry_add_post"></a>
> flowentry_add_post()



Add a new flow entry to a switch. Needs to be confirmed afterwards.

### Example

```python
import controller_client
from controller_client.apis.tags import flow_management_api
from controller_client.model.switch_flow import SwitchFlow
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/stats
# See configuration.py for a list of all supported configuration parameters.
configuration = controller_client.Configuration(
    host = "http://localhost:8080/stats"
)

# Enter a context with an instance of the API client
with controller_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flow_management_api.FlowManagementApi(api_client)

    # example passing only optional values
    body = SwitchFlow(
        dpid=1,
        length=88,
        buffer_id=1,
        table_id=0,
        duration_sec=2,
        duration_nsec=688768767,
        priority=11111,
        idle_timeout=0,
        hard_timeout=0,
        flags=1,
        cookie=1,
        packet_count=0,
        byte_count=0,
        match=SwitchFlowMatchV12(
            in_port=7,
            eth_src="aa:bb:cc:11:22:33",
            eth_dst="aa:bb:cc:11:22:33",
            eth_type=123,
            tcp_src=1,
            tcp_dst=2,
            udp_src=1,
            udp_dst=2,
        ),
        actions=["OUTPUT:2"],
        instructions=[
            SwitchFlowInstruction(
                type="APPLY_ACTIONS",
                actions=[{"port":2,"max_len":0,"type":"OUTPUT"}],
            )
        ],
    )
    try:
        api_response = api_instance.flowentry_add_post(
            body=body,
        )
    except controller_client.ApiException as e:
        print("Exception when calling FlowManagementApi->flowentry_add_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SwitchFlow**](../../models/SwitchFlow.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#flowentry_add_post.ApiResponseFor200) | The creation of the flow entry was attempted
404 | [ApiResponseFor404](#flowentry_add_post.ApiResponseFor404) | Switch not found

#### flowentry_add_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### flowentry_add_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **flowentry_clear_dpid_delete**
<a id="flowentry_clear_dpid_delete"></a>
> flowentry_clear_dpid_delete(dpid)



Delete all flow entries from a switch. Needs to be confirmed afterwards.

### Example

```python
import controller_client
from controller_client.apis.tags import flow_management_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/stats
# See configuration.py for a list of all supported configuration parameters.
configuration = controller_client.Configuration(
    host = "http://localhost:8080/stats"
)

# Enter a context with an instance of the API client
with controller_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flow_management_api.FlowManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dpid': 1,
    }
    try:
        api_response = api_instance.flowentry_clear_dpid_delete(
            path_params=path_params,
        )
    except controller_client.ApiException as e:
        print("Exception when calling FlowManagementApi->flowentry_clear_dpid_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
dpid | DpidSchema | | 

# DpidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#flowentry_clear_dpid_delete.ApiResponseFor200) | The deletion of all flow entries was attempted
404 | [ApiResponseFor404](#flowentry_clear_dpid_delete.ApiResponseFor404) | Switch not found

#### flowentry_clear_dpid_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### flowentry_clear_dpid_delete.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **flowentry_delete_post**
<a id="flowentry_delete_post"></a>
> flowentry_delete_post()



Delete all matching flow entries from a switch. Needs to be confirmed afterwards.

### Example

```python
import controller_client
from controller_client.apis.tags import flow_management_api
from controller_client.model.switch_flow import SwitchFlow
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/stats
# See configuration.py for a list of all supported configuration parameters.
configuration = controller_client.Configuration(
    host = "http://localhost:8080/stats"
)

# Enter a context with an instance of the API client
with controller_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flow_management_api.FlowManagementApi(api_client)

    # example passing only optional values
    body = SwitchFlow(
        dpid=1,
        length=88,
        buffer_id=1,
        table_id=0,
        duration_sec=2,
        duration_nsec=688768767,
        priority=11111,
        idle_timeout=0,
        hard_timeout=0,
        flags=1,
        cookie=1,
        packet_count=0,
        byte_count=0,
        match=SwitchFlowMatchV12(
            in_port=7,
            eth_src="aa:bb:cc:11:22:33",
            eth_dst="aa:bb:cc:11:22:33",
            eth_type=123,
            tcp_src=1,
            tcp_dst=2,
            udp_src=1,
            udp_dst=2,
        ),
        actions=["OUTPUT:2"],
        instructions=[
            SwitchFlowInstruction(
                type="APPLY_ACTIONS",
                actions=[{"port":2,"max_len":0,"type":"OUTPUT"}],
            )
        ],
    )
    try:
        api_response = api_instance.flowentry_delete_post(
            body=body,
        )
    except controller_client.ApiException as e:
        print("Exception when calling FlowManagementApi->flowentry_delete_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SwitchFlow**](../../models/SwitchFlow.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#flowentry_delete_post.ApiResponseFor200) | The deletion of all matching flow entries was attempted
404 | [ApiResponseFor404](#flowentry_delete_post.ApiResponseFor404) | Switch not found

#### flowentry_delete_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### flowentry_delete_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **flowentry_delete_strict_post**
<a id="flowentry_delete_strict_post"></a>
> flowentry_delete_strict_post()



Delete one strictly matching flow entry from a switch. Needs to be confirmed afterwards.

### Example

```python
import controller_client
from controller_client.apis.tags import flow_management_api
from controller_client.model.switch_flow import SwitchFlow
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/stats
# See configuration.py for a list of all supported configuration parameters.
configuration = controller_client.Configuration(
    host = "http://localhost:8080/stats"
)

# Enter a context with an instance of the API client
with controller_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flow_management_api.FlowManagementApi(api_client)

    # example passing only optional values
    body = SwitchFlow(
        dpid=1,
        length=88,
        buffer_id=1,
        table_id=0,
        duration_sec=2,
        duration_nsec=688768767,
        priority=11111,
        idle_timeout=0,
        hard_timeout=0,
        flags=1,
        cookie=1,
        packet_count=0,
        byte_count=0,
        match=SwitchFlowMatchV12(
            in_port=7,
            eth_src="aa:bb:cc:11:22:33",
            eth_dst="aa:bb:cc:11:22:33",
            eth_type=123,
            tcp_src=1,
            tcp_dst=2,
            udp_src=1,
            udp_dst=2,
        ),
        actions=["OUTPUT:2"],
        instructions=[
            SwitchFlowInstruction(
                type="APPLY_ACTIONS",
                actions=[{"port":2,"max_len":0,"type":"OUTPUT"}],
            )
        ],
    )
    try:
        api_response = api_instance.flowentry_delete_strict_post(
            body=body,
        )
    except controller_client.ApiException as e:
        print("Exception when calling FlowManagementApi->flowentry_delete_strict_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SwitchFlow**](../../models/SwitchFlow.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#flowentry_delete_strict_post.ApiResponseFor200) | The deletion of one strictly matching flow entry was attempted
404 | [ApiResponseFor404](#flowentry_delete_strict_post.ApiResponseFor404) | Switch not found

#### flowentry_delete_strict_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### flowentry_delete_strict_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

