<a id="__pageTop"></a>
# dsmf_client.apis.tags.configuration_api.ConfigurationApi

All URIs are relative to *http://localhost:8081/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configuration_get**](#configuration_get) | **get** /configuration | 
[**configuration_put**](#configuration_put) | **put** /configuration | 

# **configuration_get**
<a id="configuration_get"></a>
> DomainConfiguration configuration_get(auth)



Fetch the current configuration of this service

### Example

```python
import dsmf_client
from dsmf_client.apis.tags import configuration_api
from dsmf_client.model.domain_configuration import DomainConfiguration
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = dsmf_client.Configuration(
    host = "http://localhost:8081/v1"
)

# Enter a context with an instance of the API client
with dsmf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'auth': "auth_example",
    }
    try:
        api_response = api_instance.configuration_get(
            query_params=query_params,
        )
        pprint(api_response)
    except dsmf_client.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_get: %s\n" % e)
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
200 | [ApiResponseFor200](#configuration_get.ApiResponseFor200) | The current configuration
403 | [ApiResponseFor403](#configuration_get.ApiResponseFor403) | Invalid authentication provided

#### configuration_get.ApiResponseFor200

 Name     | Type                                                    | Description              | Notes 
----------|---------------------------------------------------------|--------------------------|-------
 response | urllib3.HTTPResponse                                    | Raw response             |
 body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
 headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

 Type                                                           | Description | Notes 
----------------------------------------------------------------|-------------|-------
 [**DomainConfiguration**](../../models/DomainConfiguration.md) |             |

#### configuration_get.ApiResponseFor403

 Name     | Type                 | Description              | Notes 
----------|----------------------|--------------------------|-------
 response | urllib3.HTTPResponse | Raw response             |
 body     | Unset                | body was not defined     |
 headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **configuration_put**
<a id="configuration_put"></a>
> configuration_put(auth)



Installs a new configuration for this service

### Example

```python
import dsmf_client
from dsmf_client.apis.tags import configuration_api
from dsmf_client.model.domain_configuration import DomainConfiguration
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = dsmf_client.Configuration(
    host = "http://localhost:8081/v1"
)

# Enter a context with an instance of the API client
with dsmf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'auth': "auth_example",
    }
    try:
        api_response = api_instance.configuration_put(
            query_params=query_params,
        )
    except dsmf_client.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_put: %s\n" % e)

    # example passing only optional values
    query_params = {
        'auth': "auth_example",
    }
    body = DomainConfiguration(
        type="DSMF",
        network="network_example",
        controllers=[
            ControllerConfiguration(
                ip="localhost",
                port=8080,
                name="name_example",
            )
        ],
        vpn_gateways=[
            DeviceConfiguration(
                ip="localhost",
                port=8082,
                connections=[
                    ConnectionConfiguration(
                        intf_name="intf_name_example",
                        intf_id=1,
                        other_end="other_end_example",
                    )
                ],
                network="network_example",
                name="name_example",
                dpid=1,
            )
        ],
        switches=[
            DeviceConfiguration()
        ],
        network_borders=[
            NetworkBorderConfiguration(
                network_name="network_name_example",
                device_name="device_name_example",
                device_type="SWITCH",
                connection=ConnectionConfiguration(),
            )
        ],
        networks=[
            NetworkConfiguration(
                name="name_example",
                reachable=[
                    "reachable_example"
                ],
                preferred_vpn=[
                    "preferred_vpn_example"
                ],
            )
        ],
        reservable_bitrate=1000000000,
    )
    try:
        api_response = api_instance.configuration_put(
            query_params=query_params,
            body=body,
        )
    except dsmf_client.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_put: %s\n" % e)
```
### Parameters

 Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              
----------------------|----------------------------------------------------------|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
 query_params         | RequestQueryParams                                       |                                         |
 content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           
 stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file 
 timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                
 skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         

### body

# SchemaForRequestBodyApplicationJson

 Type                                                           | Description | Notes 
----------------------------------------------------------------|-------------|-------
 [**DomainConfiguration**](../../models/DomainConfiguration.md) |             |

### query_params

#### RequestQueryParams

 Name | Type       | Description | Notes 
------|------------|-------------|-------
 auth | AuthSchema |             |

# AuthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#configuration_put.ApiResponseFor200) | The configuration has been installed
403 | [ApiResponseFor403](#configuration_put.ApiResponseFor403) | Invalid authentication provided
406 | [ApiResponseFor406](#configuration_put.ApiResponseFor406) | A value exceeds the allowed range
409 | [ApiResponseFor409](#configuration_put.ApiResponseFor409) | There are slices currently running. Reconfiguring is not supported while slices are open.
412 | [ApiResponseFor412](#configuration_put.ApiResponseFor412) | The provided configuration is invalid

#### configuration_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### configuration_put.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### configuration_put.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### configuration_put.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### configuration_put.ApiResponseFor412
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

