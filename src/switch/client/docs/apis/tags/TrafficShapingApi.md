<a id="__pageTop"></a>
# switch_client.apis.tags.traffic_shaping_api.TrafficShapingApi

All URIs are relative to *http://localhost:8082*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policy_put**](#policy_put) | **put** /policy | 

# **policy_put**
<a id="policy_put"></a>
> policy_put(authport)



Sets the policies on the specified port

### Example

```python
import switch_client
from switch_client.apis.tags import traffic_shaping_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8082
# See configuration.py for a list of all supported configuration parameters.
configuration = switch_client.Configuration(
    host = "http://localhost:8082"
)

# Enter a context with an instance of the API client
with switch_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = traffic_shaping_api.TrafficShapingApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'auth': "auth_example",
        'port': "port_example",
    }
    try:
        api_response = api_instance.policy_put(
            query_params=query_params,
        )
    except switch_client.ApiException as e:
        print("Exception when calling TrafficShapingApi->policy_put: %s\n" % e)

    # example passing only optional values
    query_params = {
        'auth': "auth_example",
        'port': "port_example",
        'ingress_policing_rate': 1,
        'ingress_policing_burst': 1,
    }
    try:
        api_response = api_instance.policy_put(
            query_params=query_params,
        )
    except switch_client.ApiException as e:
        print("Exception when calling TrafficShapingApi->policy_put: %s\n" % e)
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
port | PortSchema | | 
ingress_policing_rate | IngressPolicingRateSchema | | optional
ingress_policing_burst | IngressPolicingBurstSchema | | optional


# AuthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IngressPolicingRateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# IngressPolicingBurstSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#policy_put.ApiResponseFor200) | Traffic policy updated
403 | [ApiResponseFor403](#policy_put.ApiResponseFor403) | Invalid authentication provided
404 | [ApiResponseFor404](#policy_put.ApiResponseFor404) | The switch port could not be found
406 | [ApiResponseFor406](#policy_put.ApiResponseFor406) | A value exceeds the allowed range

#### policy_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### policy_put.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### policy_put.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### policy_put.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

