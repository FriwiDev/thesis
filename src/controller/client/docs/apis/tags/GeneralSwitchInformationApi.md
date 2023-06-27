<a id="__pageTop"></a>
# controller_client.apis.tags.general_switch_information_api.GeneralSwitchInformationApi

All URIs are relative to *http://localhost:8080/stats*

Method | HTTP request | Description
------------- | ------------- | -------------
[**desc_dpid_get**](#desc_dpid_get) | **get** /desc/{dpid} | 
[**switches_get**](#switches_get) | **get** /switches | 

# **desc_dpid_get**
<a id="desc_dpid_get"></a>
> {str: (SwitchDescription,)} desc_dpid_get(dpid)



Fetch the description of a switch.

### Example

```python
import controller_client
from controller_client.apis.tags import general_switch_information_api
from controller_client.model.switch_description import SwitchDescription
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/stats
# See configuration.py for a list of all supported configuration parameters.
configuration = controller_client.Configuration(
    host = "http://localhost:8080/stats"
)

# Enter a context with an instance of the API client
with controller_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = general_switch_information_api.GeneralSwitchInformationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dpid': 1,
    }
    try:
        api_response = api_instance.desc_dpid_get(
            path_params=path_params,
        )
        pprint(api_response)
    except controller_client.ApiException as e:
        print("Exception when calling GeneralSwitchInformationApi->desc_dpid_get: %s\n" % e)
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
200 | [ApiResponseFor200](#desc_dpid_get.ApiResponseFor200) | The switch description
404 | [ApiResponseFor404](#desc_dpid_get.ApiResponseFor404) | Switch not found

#### desc_dpid_get.ApiResponseFor200
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
**any_string_name** | [**SwitchDescription**]({{complexTypePrefix}}SwitchDescription.md) | [**SwitchDescription**]({{complexTypePrefix}}SwitchDescription.md) | any string name can be used but the value must be the correct type | [optional] 

#### desc_dpid_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **switches_get**
<a id="switches_get"></a>
> [int] switches_get()



Get the list of all switches which connected to the controller.

### Example

```python
import controller_client
from controller_client.apis.tags import general_switch_information_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/stats
# See configuration.py for a list of all supported configuration parameters.
configuration = controller_client.Configuration(
    host = "http://localhost:8080/stats"
)

# Enter a context with an instance of the API client
with controller_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = general_switch_information_api.GeneralSwitchInformationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.switches_get()
        pprint(api_response)
    except controller_client.ApiException as e:
        print("Exception when calling GeneralSwitchInformationApi->switches_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#switches_get.ApiResponseFor200) | A list of DPIDs.

#### switches_get.ApiResponseFor200
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
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

