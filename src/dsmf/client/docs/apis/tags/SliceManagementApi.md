<a id="__pageTop"></a>

# dsmf_client.apis.tags.slice_management_api.SliceManagementApi

All URIs are relative to *http://localhost:8081*

 Method                                                  | HTTP request                 | Description 
---------------------------------------------------------|------------------------------|-------------
 [**slice_deployment_delete**](#slice_deployment_delete) | **delete** /slice_deployment |
 [**slice_deployment_get**](#slice_deployment_get)       | **get** /slice_deployment    |
 [**slice_deployment_put**](#slice_deployment_put)       | **put** /slice_deployment    |

# **slice_deployment_delete**

<a id="slice_deployment_delete"></a>
> slice_deployment_delete(authid)



Deletes a slice

### Example

```python
import dsmf_client
from dsmf_client.apis.tags import slice_management_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = dsmf_client.Configuration(
    host = "http://localhost:8081"
)

# Enter a context with an instance of the API client
with dsmf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slice_management_api.SliceManagementApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'auth': "auth_example",
        'id': 1,
    }
    try:
        api_response = api_instance.slice_deployment_delete(
            query_params=query_params,
        )
    except dsmf_client.ApiException as e:
        print("Exception when calling SliceManagementApi->slice_deployment_delete: %s\n" % e)
```

### Parameters

 Name                 | Type                                             | Description      | Notes                                                                                                                                                                                              
----------------------|--------------------------------------------------|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 query_params         | RequestQueryParams                               |                  |
 stream               | bool                                             | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file 
 timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None  | the timeout used by the rest client                                                                                                                                                                
 skip_deserialization | bool                                             | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         

### query_params

#### RequestQueryParams

 Name | Type       | Description | Notes 
------|------------|-------------|-------
 auth | AuthSchema |             |
 id   | IdSchema   |             |

# AuthSchema

## Model Type Info

 Input Type | Accessed Type | Description | Notes 
------------|---------------|-------------|-------
 str,       | str,          |             |

# IdSchema

## Model Type Info

 Input Type            | Accessed Type    | Description | Notes                          
-----------------------|------------------|-------------|--------------------------------
 decimal.Decimal, int, | decimal.Decimal, |             | value must be a 32 bit integer 

### Return Types, Responses

 Code | Class                                                           | Description                                                 
------|-----------------------------------------------------------------|-------------------------------------------------------------
 n/a  | api_client.ApiResponseWithoutDeserialization                    | When skip_deserialization is True this response is returned 
 200  | [ApiResponseFor200](#slice_deployment_delete.ApiResponseFor200) | The slice was successfully deleted.                         
 403  | [ApiResponseFor403](#slice_deployment_delete.ApiResponseFor403) | Invalid authentication provided.                            
 404  | [ApiResponseFor404](#slice_deployment_delete.ApiResponseFor404) | The slice could not be found.                               

#### slice_deployment_delete.ApiResponseFor200

 Name     | Type                 | Description              | Notes 
----------|----------------------|--------------------------|-------
 response | urllib3.HTTPResponse | Raw response             |
 body     | Unset                | body was not defined     |
 headers  | Unset                | headers were not defined |

#### slice_deployment_delete.ApiResponseFor403

 Name     | Type                 | Description              | Notes 
----------|----------------------|--------------------------|-------
 response | urllib3.HTTPResponse | Raw response             |
 body     | Unset                | body was not defined     |
 headers  | Unset                | headers were not defined |

#### slice_deployment_delete.ApiResponseFor404

 Name     | Type                 | Description              | Notes 
----------|----------------------|--------------------------|-------
 response | urllib3.HTTPResponse | Raw response             |
 body     | Unset                | body was not defined     |
 headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slice_deployment_get**

<a id="slice_deployment_get"></a>
> [Slice] slice_deployment_get(auth)



Lists all current slices

### Example

```python
import dsmf_client
from dsmf_client.apis.tags import slice_management_api
from dsmf_client.model.slice import Slice
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = dsmf_client.Configuration(
    host = "http://localhost:8081"
)

# Enter a context with an instance of the API client
with dsmf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slice_management_api.SliceManagementApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'auth': "auth_example",
    }
    try:
        api_response = api_instance.slice_deployment_get(
            query_params=query_params,
        )
        pprint(api_response)
    except dsmf_client.ApiException as e:
        print("Exception when calling SliceManagementApi->slice_deployment_get: %s\n" % e)
```

### Parameters

 Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              
----------------------|--------------------------------------------------|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 query_params         | RequestQueryParams                               |                                   |
 accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               
 stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file 
 timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                
 skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         

### query_params

#### RequestQueryParams

 Name | Type       | Description | Notes 
------|------------|-------------|-------
 auth | AuthSchema |             |

# AuthSchema

## Model Type Info

 Input Type | Accessed Type | Description | Notes 
------------|---------------|-------------|-------
 str,       | str,          |             |

### Return Types, Responses

 Code | Class                                                        | Description                                                 
------|--------------------------------------------------------------|-------------------------------------------------------------
 n/a  | api_client.ApiResponseWithoutDeserialization                 | When skip_deserialization is True this response is returned 
 200  | [ApiResponseFor200](#slice_deployment_get.ApiResponseFor200) | The current list of slices                                  
 403  | [ApiResponseFor403](#slice_deployment_get.ApiResponseFor403) | Invalid authentication provided                             

#### slice_deployment_get.ApiResponseFor200

 Name     | Type                                                    | Description              | Notes 
----------|---------------------------------------------------------|--------------------------|-------
 response | urllib3.HTTPResponse                                    | Raw response             |
 body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
 headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info

 Input Type   | Accessed Type | Description | Notes 
--------------|---------------|-------------|-------
 list, tuple, | tuple,        |             |

### Tuple Items

 Class Name                                 | Input Type                                 | Accessed Type                              | Description | Notes 
--------------------------------------------|--------------------------------------------|--------------------------------------------|-------------|-------
 [**Slice**]({{complexTypePrefix}}Slice.md) | [**Slice**]({{complexTypePrefix}}Slice.md) | [**Slice**]({{complexTypePrefix}}Slice.md) |             |

#### slice_deployment_get.ApiResponseFor403

 Name     | Type                 | Description              | Notes 
----------|----------------------|--------------------------|-------
 response | urllib3.HTTPResponse | Raw response             |
 body     | Unset                | body was not defined     |
 headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slice_deployment_put**

<a id="slice_deployment_put"></a>
> slice_deployment_put(authid)



Creates a new slice from a reservation

### Example

```python
import dsmf_client
from dsmf_client.apis.tags import slice_management_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = dsmf_client.Configuration(
    host = "http://localhost:8081"
)

# Enter a context with an instance of the API client
with dsmf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slice_management_api.SliceManagementApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'auth': "auth_example",
        'id': 1,
    }
    try:
        api_response = api_instance.slice_deployment_put(
            query_params=query_params,
        )
    except dsmf_client.ApiException as e:
        print("Exception when calling SliceManagementApi->slice_deployment_put: %s\n" % e)
```

### Parameters

 Name                 | Type                                             | Description      | Notes                                                                                                                                                                                              
----------------------|--------------------------------------------------|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 query_params         | RequestQueryParams                               |                  |
 stream               | bool                                             | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file 
 timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None  | the timeout used by the rest client                                                                                                                                                                
 skip_deserialization | bool                                             | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         

### query_params

#### RequestQueryParams

 Name | Type       | Description | Notes 
------|------------|-------------|-------
 auth | AuthSchema |             |
 id   | IdSchema   |             |

# AuthSchema

## Model Type Info

 Input Type | Accessed Type | Description | Notes 
------------|---------------|-------------|-------
 str,       | str,          |             |

# IdSchema

## Model Type Info

 Input Type            | Accessed Type    | Description | Notes                          
-----------------------|------------------|-------------|--------------------------------
 decimal.Decimal, int, | decimal.Decimal, |             | value must be a 32 bit integer 

### Return Types, Responses

 Code | Class                                                        | Description                                                 
------|--------------------------------------------------------------|-------------------------------------------------------------
 n/a  | api_client.ApiResponseWithoutDeserialization                 | When skip_deserialization is True this response is returned 
 200  | [ApiResponseFor200](#slice_deployment_put.ApiResponseFor200) | The slice has been created                                  
 403  | [ApiResponseFor403](#slice_deployment_put.ApiResponseFor403) | Invalid authentication provided                             
 404  | [ApiResponseFor404](#slice_deployment_put.ApiResponseFor404) | The slice reservation could not be found.                   
 500  | [ApiResponseFor500](#slice_deployment_put.ApiResponseFor500) | The deployment to the network failed                        

#### slice_deployment_put.ApiResponseFor200

 Name     | Type                 | Description              | Notes 
----------|----------------------|--------------------------|-------
 response | urllib3.HTTPResponse | Raw response             |
 body     | Unset                | body was not defined     |
 headers  | Unset                | headers were not defined |

#### slice_deployment_put.ApiResponseFor403

 Name     | Type                 | Description              | Notes 
----------|----------------------|--------------------------|-------
 response | urllib3.HTTPResponse | Raw response             |
 body     | Unset                | body was not defined     |
 headers  | Unset                | headers were not defined |

#### slice_deployment_put.ApiResponseFor404

 Name     | Type                 | Description              | Notes 
----------|----------------------|--------------------------|-------
 response | urllib3.HTTPResponse | Raw response             |
 body     | Unset                | body was not defined     |
 headers  | Unset                | headers were not defined |

#### slice_deployment_put.ApiResponseFor500

 Name     | Type                 | Description              | Notes 
----------|----------------------|--------------------------|-------
 response | urllib3.HTTPResponse | Raw response             |
 body     | Unset                | body was not defined     |
 headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

