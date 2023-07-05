<a id="__pageTop"></a>
# switch_client.apis.tags.queue_management_api.QueueManagementApi

All URIs are relative to *http://localhost:8082/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**queue_delete**](#queue_delete) | **delete** /queue | 
[**queue_put**](#queue_put) | **put** /queue | 

# **queue_delete**
<a id="queue_delete"></a>
> queue_delete(authqueue_idport)



Deletes a queue

### Example

```python
import switch_client
from switch_client.apis.tags import queue_management_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8082/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = switch_client.Configuration(
    host = "http://localhost:8082/v1"
)

# Enter a context with an instance of the API client
with switch_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = queue_management_api.QueueManagementApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'auth': "auth_example",
        'queue_id': 1,
        'port': "port_example",
    }
    try:
        api_response = api_instance.queue_delete(
            query_params=query_params,
        )
    except switch_client.ApiException as e:
        print("Exception when calling QueueManagementApi->queue_delete: %s\n" % e)
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
queue_id | QueueIdSchema | | 
port | PortSchema | | 


# AuthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# QueueIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# PortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#queue_delete.ApiResponseFor200) | The queue was successfully deleted.
403 | [ApiResponseFor403](#queue_delete.ApiResponseFor403) | Invalid authentication provided.
404 | [ApiResponseFor404](#queue_delete.ApiResponseFor404) | The queue could not be found.

#### queue_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### queue_delete.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### queue_delete.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **queue_put**
<a id="queue_put"></a>
> Queue queue_put(auth)



Creates a new queue

### Example

```python
import switch_client
from switch_client.apis.tags import queue_management_api
from switch_client.model.queue import Queue
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8082/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = switch_client.Configuration(
    host = "http://localhost:8082/v1"
)

# Enter a context with an instance of the API client
with switch_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = queue_management_api.QueueManagementApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'auth': "auth_example",
    }
    try:
        api_response = api_instance.queue_put(
            query_params=query_params,
        )
        pprint(api_response)
    except switch_client.ApiException as e:
        print("Exception when calling QueueManagementApi->queue_put: %s\n" % e)

    # example passing only optional values
    query_params = {
        'auth': "auth_example",
    }
    body = Queue(
        queue_id=1,
        min_rate=1,
        max_rate=1,
        burst_rate=1,
        priority=1,
        port="port_example",
    )
    try:
        api_response = api_instance.queue_put(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except switch_client.ApiException as e:
        print("Exception when calling QueueManagementApi->queue_put: %s\n" % e)
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
Type | Description  | Notes
------------- | ------------- | -------------
[**Queue**](../../models/Queue.md) |  | 


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
200 | [ApiResponseFor200](#queue_put.ApiResponseFor200) | The queue object
400 | [ApiResponseFor400](#queue_put.ApiResponseFor400) | No body provided.
403 | [ApiResponseFor403](#queue_put.ApiResponseFor403) | Invalid authentication provided.
404 | [ApiResponseFor404](#queue_put.ApiResponseFor404) | The switch port could not be found
406 | [ApiResponseFor406](#queue_put.ApiResponseFor406) | A value exceeds the allowed range
507 | [ApiResponseFor507](#queue_put.ApiResponseFor507) | Already too many queues in use

#### queue_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Queue**](../../models/Queue.md) |  | 


#### queue_put.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### queue_put.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### queue_put.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### queue_put.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### queue_put.ApiResponseFor507
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

