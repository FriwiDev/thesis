# dsmf_client.model.tunnel.Tunnel

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**tunnel_id** | decimal.Decimal, int,  | decimal.Decimal,  | The tunnel identifier | [optional] value must be a 32 bit integer
**min_rate** | decimal.Decimal, int,  | decimal.Decimal,  | The minimum transmission rate as bits/s | [optional] value must be a 64 bit integer
**max_rate** | decimal.Decimal, int,  | decimal.Decimal,  | The maximum transmission rate as bits/s | [optional] value must be a 64 bit integer
**burst_rate** | decimal.Decimal, int,  | decimal.Decimal,  | The burst transmission rate as bits/s | [optional] value must be a 64 bit integer
**latency** | decimal.Decimal, int,  | decimal.Decimal,  | The required maximum latency | [optional] 
**fr** | [**Endpoint**](Endpoint.md) | [**Endpoint**](Endpoint.md) |  | [optional] 
**to** | [**Endpoint**](Endpoint.md) | [**Endpoint**](Endpoint.md) |  | [optional] 
**private_key** | str,  | str,  | The tunnel private key | [optional] 
**public_key** | str,  | str,  | The tunnel public key (of the other side) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

