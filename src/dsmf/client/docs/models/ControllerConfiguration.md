# dsmf_client.model.controller_configuration.ControllerConfiguration

A controller configuration element

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A controller configuration element | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ip** | str,  | str,  | The ip or name the controller can be reached on | [optional] if omitted the server will use the default value of "localhost"
**port** | decimal.Decimal, int,  | decimal.Decimal,  | The port that the controller REST API can be reached on | [optional] if omitted the server will use the default value of 8080
**name** | str,  | str,  | The name of this controller | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

