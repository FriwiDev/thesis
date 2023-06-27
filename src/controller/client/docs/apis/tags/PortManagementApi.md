<a id="__pageTop"></a>
# controller_client.apis.tags.port_management_api.PortManagementApi

All URIs are relative to *http://localhost:8080/stats*

Method | HTTP request | Description
------------- | ------------- | -------------
[**portdesc_dpid_get**](#portdesc_dpid_get) | **get** /portdesc/{dpid} | 
[**portdesc_dpid_port_get**](#portdesc_dpid_port_get) | **get** /portdesc/{dpid}/{port} | 

# **portdesc_dpid_get**
<a id="portdesc_dpid_get"></a>
> {str: ([SwitchPortDescription],)} portdesc_dpid_get(dpid)



Fetch the port descriptions of a switch.

### Example

```python
import controller_client
from controller_client.apis.tags import port_management_api
from controller_client.model.switch_port_description import SwitchPortDescription
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/stats
# See configuration.py for a list of all supported configuration parameters.
configuration = controller_client.Configuration(
    host = "http://localhost:8080/stats"
)

# Enter a context with an instance of the API client
with controller_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = port_management_api.PortManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dpid': 1,
    }
    try:
        api_response = api_instance.portdesc_dpid_get(
            path_params=path_params,
        )
        pprint(api_response)
    except controller_client.ApiException as e:
        print("Exception when calling PortManagementApi->portdesc_dpid_get: %s\n" % e)
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
200 | [ApiResponseFor200](#portdesc_dpid_get.ApiResponseFor200) | The port descriptions
404 | [ApiResponseFor404](#portdesc_dpid_get.ApiResponseFor404) | Switch not found

#### portdesc_dpid_get.ApiResponseFor200
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
[**SwitchPortDescription**]({{complexTypePrefix}}SwitchPortDescription.md) | [**SwitchPortDescription**]({{complexTypePrefix}}SwitchPortDescription.md) | [**SwitchPortDescription**]({{complexTypePrefix}}SwitchPortDescription.md) |  | 

#### portdesc_dpid_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **portdesc_dpid_port_get**
<a id="portdesc_dpid_port_get"></a>
> {str: ([SwitchPortDescription],)} portdesc_dpid_port_get(dpid)



Fetch the port descriptions of a switch.

### Example

```python
import controller_client
from controller_client.apis.tags import port_management_api
from controller_client.model.switch_port_description import SwitchPortDescription
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/stats
# See configuration.py for a list of all supported configuration parameters.
configuration = controller_client.Configuration(
    host = "http://localhost:8080/stats"
)

# Enter a context with an instance of the API client
with controller_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = port_management_api.PortManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dpid': 1,
    }
    try:
        api_response = api_instance.portdesc_dpid_port_get(
            path_params=path_params,
        )
        pprint(api_response)
    except controller_client.ApiException as e:
        print("Exception when calling PortManagementApi->portdesc_dpid_port_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'dpid': 1,
        'port': 1,
    }
    try:
        api_response = api_instance.portdesc_dpid_port_get(
            path_params=path_params,
        )
        pprint(api_response)
    except controller_client.ApiException as e:
        print("Exception when calling PortManagementApi->portdesc_dpid_port_get: %s\n" % e)
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
200 | [ApiResponseFor200](#portdesc_dpid_port_get.ApiResponseFor200) | The port descriptions
404 | [ApiResponseFor404](#portdesc_dpid_port_get.ApiResponseFor404) | Switch or port not found

#### portdesc_dpid_port_get.ApiResponseFor200
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
[**SwitchPortDescription**]({{complexTypePrefix}}SwitchPortDescription.md) | [**SwitchPortDescription**]({{complexTypePrefix}}SwitchPortDescription.md) | [**SwitchPortDescription**]({{complexTypePrefix}}SwitchPortDescription.md) |  | 

#### portdesc_dpid_port_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

