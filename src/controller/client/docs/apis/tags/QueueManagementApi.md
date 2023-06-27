<a id="__pageTop"></a>
# controller_client.apis.tags.queue_management_api.QueueManagementApi

All URIs are relative to *http://localhost:8080/stats*

Method | HTTP request | Description
------------- | ------------- | -------------
[**queue_dpid_get**](#queue_dpid_get) | **get** /queue/{dpid} | 
[**queue_dpid_port_get**](#queue_dpid_port_get) | **get** /queue/{dpid}/{port} | 
[**queue_dpid_port_queue_id_get**](#queue_dpid_port_queue_id_get) | **get** /queue/{dpid}/{port}/{queue_id} | 

# **queue_dpid_get**
<a id="queue_dpid_get"></a>
> {str: ([SwitchQueueStat],)} queue_dpid_get(dpid)



Fetch the queue stats of a switch.

### Example

```python
import controller_client
from controller_client.apis.tags import queue_management_api
from controller_client.model.switch_queue_stat import SwitchQueueStat
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/stats
# See configuration.py for a list of all supported configuration parameters.
configuration = controller_client.Configuration(
    host = "http://localhost:8080/stats"
)

# Enter a context with an instance of the API client
with controller_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = queue_management_api.QueueManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dpid': 1,
    }
    try:
        api_response = api_instance.queue_dpid_get(
            path_params=path_params,
        )
        pprint(api_response)
    except controller_client.ApiException as e:
        print("Exception when calling QueueManagementApi->queue_dpid_get: %s\n" % e)
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
200 | [ApiResponseFor200](#queue_dpid_get.ApiResponseFor200) | The queue stats
404 | [ApiResponseFor404](#queue_dpid_get.ApiResponseFor404) | Switch not found

#### queue_dpid_get.ApiResponseFor200
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
**[any_string_name](#any_string_name)** | list, tuple,  | tuple,  | any string name can be used but the value must be the correct type | [optional] 

# any_string_name

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SwitchQueueStat**]({{complexTypePrefix}}SwitchQueueStat.md) | [**SwitchQueueStat**]({{complexTypePrefix}}SwitchQueueStat.md) | [**SwitchQueueStat**]({{complexTypePrefix}}SwitchQueueStat.md) |  | 

#### queue_dpid_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **queue_dpid_port_get**
<a id="queue_dpid_port_get"></a>
> {str: ([SwitchQueueStat],)} queue_dpid_port_get(dpid)



Fetch the queue stats of a switch.

### Example

```python
import controller_client
from controller_client.apis.tags import queue_management_api
from controller_client.model.switch_queue_stat import SwitchQueueStat
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/stats
# See configuration.py for a list of all supported configuration parameters.
configuration = controller_client.Configuration(
    host = "http://localhost:8080/stats"
)

# Enter a context with an instance of the API client
with controller_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = queue_management_api.QueueManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dpid': 1,
    }
    try:
        api_response = api_instance.queue_dpid_port_get(
            path_params=path_params,
        )
        pprint(api_response)
    except controller_client.ApiException as e:
        print("Exception when calling QueueManagementApi->queue_dpid_port_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'dpid': 1,
        'port': 1,
    }
    try:
        api_response = api_instance.queue_dpid_port_get(
            path_params=path_params,
        )
        pprint(api_response)
    except controller_client.ApiException as e:
        print("Exception when calling QueueManagementApi->queue_dpid_port_get: %s\n" % e)
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
port | PortSchema | | optional

# DpidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#queue_dpid_port_get.ApiResponseFor200) | The queue stats
404 | [ApiResponseFor404](#queue_dpid_port_get.ApiResponseFor404) | Switch or port not found

#### queue_dpid_port_get.ApiResponseFor200
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
**[any_string_name](#any_string_name)** | list, tuple,  | tuple,  | any string name can be used but the value must be the correct type | [optional] 

# any_string_name

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SwitchQueueStat**]({{complexTypePrefix}}SwitchQueueStat.md) | [**SwitchQueueStat**]({{complexTypePrefix}}SwitchQueueStat.md) | [**SwitchQueueStat**]({{complexTypePrefix}}SwitchQueueStat.md) |  | 

#### queue_dpid_port_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **queue_dpid_port_queue_id_get**
<a id="queue_dpid_port_queue_id_get"></a>
> {str: ([SwitchQueueStat],)} queue_dpid_port_queue_id_get(dpid)



Fetch the queue stats of a switch.

### Example

```python
import controller_client
from controller_client.apis.tags import queue_management_api
from controller_client.model.switch_queue_stat import SwitchQueueStat
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/stats
# See configuration.py for a list of all supported configuration parameters.
configuration = controller_client.Configuration(
    host = "http://localhost:8080/stats"
)

# Enter a context with an instance of the API client
with controller_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = queue_management_api.QueueManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dpid': 1,
    }
    try:
        api_response = api_instance.queue_dpid_port_queue_id_get(
            path_params=path_params,
        )
        pprint(api_response)
    except controller_client.ApiException as e:
        print("Exception when calling QueueManagementApi->queue_dpid_port_queue_id_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'dpid': 1,
        'port': None,
        'queue_id': 1,
    }
    try:
        api_response = api_instance.queue_dpid_port_queue_id_get(
            path_params=path_params,
        )
        pprint(api_response)
    except controller_client.ApiException as e:
        print("Exception when calling QueueManagementApi->queue_dpid_port_queue_id_get: %s\n" % e)
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
port | PortSchema | | optional
queue_id | QueueIdSchema | | optional

# DpidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | decimal.Decimal, int,  | decimal.Decimal,  |  | 
[one_of_1](#one_of_1) | str,  | str,  |  | must be one of ["ALL", ] 

# one_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# one_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["ALL", ] 

# QueueIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#queue_dpid_port_queue_id_get.ApiResponseFor200) | The queue stats
404 | [ApiResponseFor404](#queue_dpid_port_queue_id_get.ApiResponseFor404) | Switch, port or queue id not found

#### queue_dpid_port_queue_id_get.ApiResponseFor200
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
**[any_string_name](#any_string_name)** | list, tuple,  | tuple,  | any string name can be used but the value must be the correct type | [optional] 

# any_string_name

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SwitchQueueStat**]({{complexTypePrefix}}SwitchQueueStat.md) | [**SwitchQueueStat**]({{complexTypePrefix}}SwitchQueueStat.md) | [**SwitchQueueStat**]({{complexTypePrefix}}SwitchQueueStat.md) |  | 

#### queue_dpid_port_queue_id_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

