# dsmf-client
A simple API to interact with the Domain Slice Management Function. Supports reserving, creating and removing slices and tunnels from one external domain to another external domain or host. Please refer to the topology drawings for further information about the network structures.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python &gt;&#x3D;3.7

## Migration from other generators like python and python-legacy

### Changes
1. This generator uses spec case for all (object) property names and parameter names.
    - So if the spec has a property name like camelCase, it will use camelCase rather than camel_case
    - So you will need to update how you input and read properties to use spec case
2. Endpoint parameters are stored in dictionaries to prevent collisions (explanation below)
    - So you will need to update how you pass data in to endpoints
3. Endpoint responses now include the original response, the deserialized response body, and (todo)the deserialized headers
    - So you will need to update your code to use response.body to access deserialized data
4. All validated data is instantiated in an instance that subclasses all validated Schema classes and Decimal/str/list/tuple/frozendict/NoneClass/BoolClass/bytes/io.FileIO
    - This means that you can use isinstance to check if a payload validated against a schema class
    - This means that no data will be of type None/True/False
        - ingested None will subclass NoneClass
        - ingested True will subclass BoolClass
        - ingested False will subclass BoolClass
        - So if you need to check is True/False/None, instead use instance.is_true_oapg()/.is_false_oapg()/.is_none_oapg()
5. All validated class instances are immutable except for ones based on io.File
    - This is because if properties were changed after validation, that validation would no longer apply
    - So no changing values or property values after a class has been instantiated
6. String + Number types with formats
    - String type data is stored as a string and if you need to access types based on its format like date,
    date-time, uuid, number etc then you will need to use accessor functions on the instance
    - type string + format: See .as_date_oapg, .as_datetime_oapg, .as_decimal_oapg, .as_uuid_oapg
    - type number + format: See .as_float_oapg, .as_int_oapg
    - this was done because openapi/json-schema defines constraints. string data may be type string with no format
    keyword in one schema, and include a format constraint in another schema
    - So if you need to access a string format based type, use as_date_oapg/as_datetime_oapg/as_decimal_oapg/as_uuid_oapg
    - So if you need to access a number format based type, use as_int_oapg/as_float_oapg
7. Property access on AnyType(type unset) or object(dict) schemas
    - Only required keys with valid python names are properties like .someProp and have type hints
    - All optional keys may not exist, so properties are not defined for them
    - One can access optional values with dict_instance['optionalProp'] and KeyError will be raised if it does not exist
    - Use get_item_oapg if you need a way to always get a value whether or not the key exists
        - If the key does not exist, schemas.unset is returned from calling dict_instance.get_item_oapg('optionalProp')
        - All required and optional keys have type hints for this method, and @typing.overload is used
        - A type hint is also generated for additionalProperties accessed using this method
    - So you will need to update you code to use some_instance['optionalProp'] to access optional property
    and additionalProperty values
8. The location of the api classes has changed
    - Api classes are located in your_package.apis.tags.some_api
    - This change was made to eliminate redundant code generation
    - Legacy generators generated the same endpoint twice if it had > 1 tag on it
    - This generator defines an endpoint in one class, then inherits that class to generate
      apis by tags and by paths
    - This change reduces code and allows quicker run time if you use the path apis
        - path apis are at your_package.apis.paths.some_path
    - Those apis will only load their needed models, which is less to load than all of the resources needed in a tag api
    - So you will need to update your import paths to the api classes

### Why are Oapg and _oapg used in class and method names?
Classes can have arbitrarily named properties set on them
Endpoints can have arbitrary operationId method names set
For those reasons, I use the prefix Oapg and _oapg to greatly reduce the likelihood of collisions
on protected + public classes/methods.
oapg stands for OpenApi Python Generator.

### Object property spec case
This was done because when payloads are ingested, they can be validated against N number of schemas.
If the input signature used a different property name then that has mutated the payload.
So SchemaA and SchemaB must both see the camelCase spec named variable.
Also it is possible to send in two properties, named camelCase and camel_case in the same payload.
That use case should be support so spec case is used.

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import dsmf_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import dsmf_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import dsmf_client
from pprint import pprint
from dsmf_client.apis.tags import authentication_api
# Defining the host is optional and defaults to http://localhost:8081/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = dsmf_client.Configuration(
    host = "http://localhost:8081/v1"
)


# Enter a context with an instance of the API client
with dsmf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)
    
    try:
        api_response = api_instance.auth_post()
        pprint(api_response)
    except dsmf_client.ApiException as e:
        print("Exception when calling AuthenticationApi->auth_post: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8081/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationApi* | [**auth_post**](docs/apis/tags/AuthenticationApi.md#auth_post) | **post** /auth | 
*SliceManagementApi* | [**slice_deployment_delete**](docs/apis/tags/SliceManagementApi.md#slice_deployment_delete) | **delete** /slice_deployment | 
*SliceManagementApi* | [**slice_deployment_get**](docs/apis/tags/SliceManagementApi.md#slice_deployment_get) | **get** /slice_deployment | 
*SliceManagementApi* | [**slice_deployment_put**](docs/apis/tags/SliceManagementApi.md#slice_deployment_put) | **put** /slice_deployment | 
*SliceReservationApi* | [**slice_reservation_delete**](docs/apis/tags/SliceReservationApi.md#slice_reservation_delete) | **delete** /slice_reservation | 
*SliceReservationApi* | [**slice_reservation_get**](docs/apis/tags/SliceReservationApi.md#slice_reservation_get) | **get** /slice_reservation | 
*SliceReservationApi* | [**slice_reservation_put**](docs/apis/tags/SliceReservationApi.md#slice_reservation_put) | **put** /slice_reservation | 
*TunnelManagementApi* | [**tunnel_deployment_delete**](docs/apis/tags/TunnelManagementApi.md#tunnel_deployment_delete) | **delete** /tunnel_deployment | 
*TunnelManagementApi* | [**tunnel_deployment_get**](docs/apis/tags/TunnelManagementApi.md#tunnel_deployment_get) | **get** /tunnel_deployment | 
*TunnelManagementApi* | [**tunnel_deployment_put**](docs/apis/tags/TunnelManagementApi.md#tunnel_deployment_put) | **put** /tunnel_deployment | 
*TunnelReservationApi* | [**tunnel_reservation_delete**](docs/apis/tags/TunnelReservationApi.md#tunnel_reservation_delete) | **delete** /tunnel_reservation | 
*TunnelReservationApi* | [**tunnel_reservation_get**](docs/apis/tags/TunnelReservationApi.md#tunnel_reservation_get) | **get** /tunnel_reservation | 
*TunnelReservationApi* | [**tunnel_reservation_put**](docs/apis/tags/TunnelReservationApi.md#tunnel_reservation_put) | **put** /tunnel_reservation | 

## Documentation For Models

 - [Slice](docs/models/Slice.md)
 - [Tunnel](docs/models/Tunnel.md)

## Documentation For Authorization

 Endpoints do not require authorization.


## Author







## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in dsmf_client.apis and dsmf_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from dsmf_client.apis.default_api import DefaultApi`
- `from dsmf_client.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import dsmf_client
from dsmf_client.apis import *
from dsmf_client.models import *
```