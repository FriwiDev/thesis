<a id="__pageTop"></a>

# switch_client.apis.tags.authentication_api.AuthenticationApi

All URIs are relative to *http://localhost:8082*

 Method                    | HTTP request  | Description 
---------------------------|---------------|-------------
 [**auth_put**](#auth_put) | **put** /auth |

# **auth_put**

<a id="auth_put"></a>
> str auth_put()



Issues a new authentication token in exchange for credentials. Currently requires no credentials, this is up to future
implementations.

### Example

```python
import switch_client
from switch_client.apis.tags import authentication_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8082
# See configuration.py for a list of all supported configuration parameters.
configuration = switch_client.Configuration(
    host = "http://localhost:8082"
)

# Enter a context with an instance of the API client
with switch_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.auth_put()
        pprint(api_response)
    except switch_client.ApiException as e:
        print("Exception when calling AuthenticationApi->auth_put: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return Types, Responses

 Code | Class                                            | Description                                                 
------|--------------------------------------------------|-------------------------------------------------------------
 n/a  | api_client.ApiResponseWithoutDeserialization     | When skip_deserialization is True this response is returned 
 200  | [ApiResponseFor200](#auth_put.ApiResponseFor200) | The authentication token as string                          
 403  | [ApiResponseFor403](#auth_put.ApiResponseFor403) | Wrong credentials were specified                            

#### auth_put.ApiResponseFor200

 Name     | Type                                                    | Description              | Notes 
----------|---------------------------------------------------------|--------------------------|-------
 response | urllib3.HTTPResponse                                    | Raw response             |
 body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
 headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info

 Input Type | Accessed Type | Description | Notes 
------------|---------------|-------------|-------
 str,       | str,          |             |

#### auth_put.ApiResponseFor403

 Name     | Type                 | Description              | Notes 
----------|----------------------|--------------------------|-------
 response | urllib3.HTTPResponse | Raw response             |
 body     | Unset                | body was not defined     |
 headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

