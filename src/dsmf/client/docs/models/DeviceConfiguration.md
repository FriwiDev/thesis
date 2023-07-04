# dsmf_client.model.device_configuration.DeviceConfiguration

A device/switch configuration element

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A device/switch configuration element | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ip** | str,  | str,  | The ip or name the device can be reached on | [optional] if omitted the server will use the default value of "localhost"
**port** | decimal.Decimal, int,  | decimal.Decimal,  | The port that the device REST API can be reached on | [optional] if omitted the server will use the default value of 8082
**[connections](#connections)** | list, tuple,  | tuple,  | The (relevant) interface definitions for this device | [optional] 
**network** | str,  | str,  | The network name this device is assigned to | [optional] 
**name** | str,  | str,  | The name of the device | [optional] 
**dpid** | decimal.Decimal, int,  | decimal.Decimal,  | The datapath id in case this is a switch | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# connections

The (relevant) interface definitions for this device

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The (relevant) interface definitions for this device | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ConnectionConfiguration**](ConnectionConfiguration.md) | [**ConnectionConfiguration**](ConnectionConfiguration.md) | [**ConnectionConfiguration**](ConnectionConfiguration.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

