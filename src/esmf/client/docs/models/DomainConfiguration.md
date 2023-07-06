# esmf_client.model.domain_configuration.DomainConfiguration

The configuration for this service

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The configuration for this service | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | The service type to be used | [optional] must be one of ["ESMF", "CTMF", ] 
**network** | str,  | str,  | Our network name | [optional] 
**[vpn_gateways](#vpn_gateways)** | list, tuple,  | tuple,  | The vpn gateways known to us | [optional] 
**[networks](#networks)** | list, tuple,  | tuple,  | The other networks known to us | [optional] 
**[coordinators](#coordinators)** | list, tuple,  | tuple,  | A list of the other ESMF/CTMF services | [optional] 
**domain_controller** | [**DeviceConfiguration**](DeviceConfiguration.md) | [**DeviceConfiguration**](DeviceConfiguration.md) |  | [optional] 
**reservable_bitrate** | decimal.Decimal, int,  | decimal.Decimal,  | The bitrate that can be reserved by hosts on our network | [optional] if omitted the server will use the default value of 1000000000
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

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

# networks

The other networks known to us

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The other networks known to us | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**NetworkConfiguration**](NetworkConfiguration.md) | [**NetworkConfiguration**](NetworkConfiguration.md) | [**NetworkConfiguration**](NetworkConfiguration.md) |  | 

# coordinators

A list of the other ESMF/CTMF services

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of the other ESMF/CTMF services | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DeviceConfiguration**](DeviceConfiguration.md) | [**DeviceConfiguration**](DeviceConfiguration.md) | [**DeviceConfiguration**](DeviceConfiguration.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

