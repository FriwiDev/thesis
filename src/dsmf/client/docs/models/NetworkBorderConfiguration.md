# dsmf_client.model.network_border_configuration.NetworkBorderConfiguration

A network border configuration element (telling us where to route traffic to when wanting to reach a different network)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A network border configuration element (telling us where to route traffic to when wanting to reach a different network) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**network_name** | str,  | str,  | The network this border leads to | [optional] 
**device_name** | str,  | str,  | The name of the device that has a direct connection to the other network (our side) | [optional] 
**device_type** | str,  | str,  | The type of the remote device | [optional] must be one of ["SWITCH", "VPN", "HOST", ] 
**connection** | [**ConnectionConfiguration**](ConnectionConfiguration.md) | [**ConnectionConfiguration**](ConnectionConfiguration.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

