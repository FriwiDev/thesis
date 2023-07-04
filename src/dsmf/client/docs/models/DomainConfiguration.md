# dsmf_client.model.domain_configuration.DomainConfiguration

The configuration for this service

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The configuration for this service | 

### Dictionary Keys
 Key                                     | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes                                                                     
-----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------|---------------------------------------------------------------------------
 **type**                                | str,                                                                                                                                        | str,                                                                                    | The service type to be used                                        | [optional] must be one of ["DSMF", "DTMF", ]                              
 **network**                             | str,                                                                                                                                        | str,                                                                                    | Our network name                                                   | [optional]                                                                
 **[controllers](#controllers)**         | list, tuple,                                                                                                                                | tuple,                                                                                  | Specifies the controllers available to us                          | [optional]                                                                
 **[vpn_gateways](#vpn_gateways)**       | list, tuple,                                                                                                                                | tuple,                                                                                  | The vpn gateways known to us                                       | [optional]                                                                
 **[switches](#switches)**               | list, tuple,                                                                                                                                | tuple,                                                                                  | The switches known to us                                           | [optional]                                                                
 **[network_borders](#network_borders)** | list, tuple,                                                                                                                                | tuple,                                                                                  | The routes to other networks known to us                           | [optional]                                                                
 **[networks](#networks)**               | list, tuple,                                                                                                                                | tuple,                                                                                  | The other networks known to us                                     | [optional]                                                                
 **reservable_bitrate**                  | decimal.Decimal, int,                                                                                                                       | decimal.Decimal,                                                                        | The bitrate that can be reserved by hosts on our network           | [optional] if omitted the server will use the default value of 1000000000 
 **any_string_name**                     | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]                                                                

# controllers

Specifies the controllers available to us

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Specifies the controllers available to us | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ControllerConfiguration**](ControllerConfiguration.md) | [**ControllerConfiguration**](ControllerConfiguration.md) | [**ControllerConfiguration**](ControllerConfiguration.md) |  | 

# vpn_gateways

The vpn gateways known to us

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The vpn gateways known to us | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DeviceConfiguration**](DeviceConfiguration.md) | [**DeviceConfiguration**](DeviceConfiguration.md) | [**DeviceConfiguration**](DeviceConfiguration.md) |  | 

# switches

The switches known to us

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The switches known to us | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DeviceConfiguration**](DeviceConfiguration.md) | [**DeviceConfiguration**](DeviceConfiguration.md) | [**DeviceConfiguration**](DeviceConfiguration.md) |  | 

# network_borders

The routes to other networks known to us

## Model Type Info

 Input Type   | Accessed Type | Description                              | Notes 
--------------|---------------|------------------------------------------|-------
 list, tuple, | tuple,        | The routes to other networks known to us |

### Tuple Items

 Class Name                                                      | Input Type                                                      | Accessed Type                                                   | Description | Notes 
-----------------------------------------------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------|-------------|-------
 [**NetworkBorderConfiguration**](NetworkBorderConfiguration.md) | [**NetworkBorderConfiguration**](NetworkBorderConfiguration.md) | [**NetworkBorderConfiguration**](NetworkBorderConfiguration.md) |             |

# networks

The other networks known to us

## Model Type Info

 Input Type   | Accessed Type | Description                    | Notes 
--------------|---------------|--------------------------------|-------
 list, tuple, | tuple,        | The other networks known to us |

### Tuple Items

 Class Name                                          | Input Type                                          | Accessed Type                                       | Description | Notes 
-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-------------|-------
 [**NetworkConfiguration**](NetworkConfiguration.md) | [**NetworkConfiguration**](NetworkConfiguration.md) | [**NetworkConfiguration**](NetworkConfiguration.md) |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

