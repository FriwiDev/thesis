<a id="__pageTop"></a>
# esmf_client.apis.tags.tunnel_synchronization_api.TunnelSynchronizationApi

All URIs are relative to *http://localhost:8080/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tunnel_deployment_delete**](#tunnel_deployment_delete) | **delete** /tunnel_deployment | 
[**tunnel_deployment_get**](#tunnel_deployment_get) | **get** /tunnel_deployment | 
[**tunnel_deployment_put**](#tunnel_deployment_put) | **put** /tunnel_deployment | 
[**tunnel_reservation_delete**](#tunnel_reservation_delete) | **delete** /tunnel_reservation | 
[**tunnel_reservation_get**](#tunnel_reservation_get) | **get** /tunnel_reservation | 
[**tunnel_reservation_put**](#tunnel_reservation_put) | **put** /tunnel_reservation | 

# **tunnel_deployment_delete**
<a id="tunnel_deployment_delete"></a>
> tunnel_deployment_delete(authtunnel_id)



Deletes a tunnel

### Example

```python
import esmf_client
from esmf_client.apis.tags import tunnel_synchronization_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = esmf_client.Configuration(
    host = "http://localhost:8080/v1"
)

# Enter a context with an instance of the API client
with esmf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tunnel_synchronization_api.TunnelSynchronizationApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'auth': "auth_example",
        'tunnel_id': 1,
    }
    try:
        api_response = api_instance.tunnel_deployment_delete(
            query_params=query_params,
        )
    except esmf_client.ApiException as e:
        print("Exception when calling TunnelSynchronizationApi->tunnel_deployment_delete: %s\n" % e)
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
tunnel_id | TunnelIdSchema | | 


# AuthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TunnelIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#tunnel_deployment_delete.ApiResponseFor200) | The tunnel was successfully deleted.
403 | [ApiResponseFor403](#tunnel_deployment_delete.ApiResponseFor403) | Invalid authentication provided.
404 | [ApiResponseFor404](#tunnel_deployment_delete.ApiResponseFor404) | The tunnel could not be found.
412 | [ApiResponseFor412](#tunnel_deployment_delete.ApiResponseFor412) | The tunnel is still being referenced by a deployed slice
500 | [ApiResponseFor500](#tunnel_deployment_delete.ApiResponseFor500) | The deployment to the network failed

#### tunnel_deployment_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### tunnel_deployment_delete.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### tunnel_deployment_delete.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### tunnel_deployment_delete.ApiResponseFor412
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### tunnel_deployment_delete.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **tunnel_deployment_get**
<a id="tunnel_deployment_get"></a>
> [Tunnel] tunnel_deployment_get(auth)



Lists all current tunnels

### Example

```python
import esmf_client
from esmf_client.apis.tags import tunnel_synchronization_api
from esmf_client.model.tunnel import Tunnel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = esmf_client.Configuration(
    host = "http://localhost:8080/v1"
)

# Enter a context with an instance of the API client
with esmf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tunnel_synchronization_api.TunnelSynchronizationApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'auth': "auth_example",
    }
    try:
        api_response = api_instance.tunnel_deployment_get(
            query_params=query_params,
        )
        pprint(api_response)
    except esmf_client.ApiException as e:
        print("Exception when calling TunnelSynchronizationApi->tunnel_deployment_get: %s\n" % e)
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
200 | [ApiResponseFor200](#tunnel_deployment_get.ApiResponseFor200) | The current list of tunnels
403 | [ApiResponseFor403](#tunnel_deployment_get.ApiResponseFor403) | Invalid authentication provided

#### tunnel_deployment_get.ApiResponseFor200
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
[**Tunnel**]({{complexTypePrefix}}Tunnel.md) | [**Tunnel**]({{complexTypePrefix}}Tunnel.md) | [**Tunnel**]({{complexTypePrefix}}Tunnel.md) |  | 

#### tunnel_deployment_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **tunnel_deployment_put**
<a id="tunnel_deployment_put"></a>
> tunnel_deployment_put(authtunnel_id)



Creates a new tunnel or modifies a tunnel from a reservation

### Example

```python
import esmf_client
from esmf_client.apis.tags import tunnel_synchronization_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = esmf_client.Configuration(
    host = "http://localhost:8080/v1"
)

# Enter a context with an instance of the API client
with esmf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tunnel_synchronization_api.TunnelSynchronizationApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'auth': "auth_example",
        'tunnel_id': 1,
    }
    try:
        api_response = api_instance.tunnel_deployment_put(
            query_params=query_params,
        )
    except esmf_client.ApiException as e:
        print("Exception when calling TunnelSynchronizationApi->tunnel_deployment_put: %s\n" % e)
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
tunnel_id | TunnelIdSchema | | 


# AuthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TunnelIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#tunnel_deployment_put.ApiResponseFor200) | The tunnel has been created
403 | [ApiResponseFor403](#tunnel_deployment_put.ApiResponseFor403) | Invalid authentication provided
404 | [ApiResponseFor404](#tunnel_deployment_put.ApiResponseFor404) | The tunnel reservation could not be found.
500 | [ApiResponseFor500](#tunnel_deployment_put.ApiResponseFor500) | The deployment to the network failed

#### tunnel_deployment_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### tunnel_deployment_put.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### tunnel_deployment_put.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### tunnel_deployment_put.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **tunnel_reservation_delete**
<a id="tunnel_reservation_delete"></a>
> tunnel_reservation_delete(authtunnel_id)



Deletes a tunnel reservation

### Example

```python
import esmf_client
from esmf_client.apis.tags import tunnel_synchronization_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = esmf_client.Configuration(
    host = "http://localhost:8080/v1"
)

# Enter a context with an instance of the API client
with esmf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tunnel_synchronization_api.TunnelSynchronizationApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'auth': "auth_example",
        'tunnel_id': 1,
    }
    try:
        api_response = api_instance.tunnel_reservation_delete(
            query_params=query_params,
        )
    except esmf_client.ApiException as e:
        print("Exception when calling TunnelSynchronizationApi->tunnel_reservation_delete: %s\n" % e)
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
tunnel_id | TunnelIdSchema | | 


# AuthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TunnelIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#tunnel_reservation_delete.ApiResponseFor200) | The tunnel reservation was successfully deleted.
403 | [ApiResponseFor403](#tunnel_reservation_delete.ApiResponseFor403) | Invalid authentication provided.
404 | [ApiResponseFor404](#tunnel_reservation_delete.ApiResponseFor404) | The tunnel reservation could not be found.
500 | [ApiResponseFor500](#tunnel_reservation_delete.ApiResponseFor500) | Internal error

#### tunnel_reservation_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### tunnel_reservation_delete.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### tunnel_reservation_delete.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### tunnel_reservation_delete.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **tunnel_reservation_get**
<a id="tunnel_reservation_get"></a>
> [Tunnel] tunnel_reservation_get(auth)



Lists all current tunnel reservations

### Example

```python
import esmf_client
from esmf_client.apis.tags import tunnel_synchronization_api
from esmf_client.model.tunnel import Tunnel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = esmf_client.Configuration(
    host = "http://localhost:8080/v1"
)

# Enter a context with an instance of the API client
with esmf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tunnel_synchronization_api.TunnelSynchronizationApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'auth': "auth_example",
    }
    try:
        api_response = api_instance.tunnel_reservation_get(
            query_params=query_params,
        )
        pprint(api_response)
    except esmf_client.ApiException as e:
        print("Exception when calling TunnelSynchronizationApi->tunnel_reservation_get: %s\n" % e)
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
200 | [ApiResponseFor200](#tunnel_reservation_get.ApiResponseFor200) | The current list of tunnel reservations
403 | [ApiResponseFor403](#tunnel_reservation_get.ApiResponseFor403) | Invalid authentication provided

#### tunnel_reservation_get.ApiResponseFor200
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
[**Tunnel**]({{complexTypePrefix}}Tunnel.md) | [**Tunnel**]({{complexTypePrefix}}Tunnel.md) | [**Tunnel**]({{complexTypePrefix}}Tunnel.md) |  | 

#### tunnel_reservation_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **tunnel_reservation_put**
<a id="tunnel_reservation_put"></a>
> tunnel_reservation_put(auth)



Creates a new tunnel reservation or stages changes to an existing deployed tunnel, as long as source and target of the tunnel match.

### Example

```python
import esmf_client
from esmf_client.apis.tags import tunnel_synchronization_api
from esmf_client.model.tunnel import Tunnel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = esmf_client.Configuration(
    host = "http://localhost:8080/v1"
)

# Enter a context with an instance of the API client
with esmf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tunnel_synchronization_api.TunnelSynchronizationApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'auth': "auth_example",
    }
    try:
        api_response = api_instance.tunnel_reservation_put(
            query_params=query_params,
        )
    except esmf_client.ApiException as e:
        print("Exception when calling TunnelSynchronizationApi->tunnel_reservation_put: %s\n" % e)

    # example passing only optional values
    query_params = {
        'auth': "auth_example",
    }
    body = Tunnel(
        tunnel_id=1,
        min_rate=1,
        max_rate=1,
        burst_rate=1,
        latency=1,
        fr=Endpoint(
            ip="ip_example",
            port=0,
            name="name_example",
            network="network_example",
        ),
,
        private_key="private_key_example",
        public_key="public_key_example",
    )
    try:
        api_response = api_instance.tunnel_reservation_put(
            query_params=query_params,
            body=body,
        )
    except esmf_client.ApiException as e:
        print("Exception when calling TunnelSynchronizationApi->tunnel_reservation_put: %s\n" % e)
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
[**Tunnel**](../../models/Tunnel.md) |  | 


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
200 | [ApiResponseFor200](#tunnel_reservation_put.ApiResponseFor200) | The tunnel has been reserved
403 | [ApiResponseFor403](#tunnel_reservation_put.ApiResponseFor403) | Invalid authentication provided
404 | [ApiResponseFor404](#tunnel_reservation_put.ApiResponseFor404) | The input or output could not be found
406 | [ApiResponseFor406](#tunnel_reservation_put.ApiResponseFor406) | A value exceeds the allowed range
409 | [ApiResponseFor409](#tunnel_reservation_put.ApiResponseFor409) | A tunnel with this id is already known and does not match current source and target
412 | [ApiResponseFor412](#tunnel_reservation_put.ApiResponseFor412) | A value does not match the schema
500 | [ApiResponseFor500](#tunnel_reservation_put.ApiResponseFor500) | Internal error
507 | [ApiResponseFor507](#tunnel_reservation_put.ApiResponseFor507) | Insufficient resources

#### tunnel_reservation_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### tunnel_reservation_put.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### tunnel_reservation_put.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### tunnel_reservation_put.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### tunnel_reservation_put.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### tunnel_reservation_put.ApiResponseFor412
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### tunnel_reservation_put.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### tunnel_reservation_put.ApiResponseFor507
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

