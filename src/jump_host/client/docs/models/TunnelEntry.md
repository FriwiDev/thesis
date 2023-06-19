# jump_host_client.model.tunnel_entry.TunnelEntry

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The tunnel identifier | [optional] value must be a 32 bit integer
**inner_intf** | str,  | str,  | The name of the network interface that faces towards the edge network | [optional] 
**outer_intf** | str,  | str,  | The name of the network interface that faces towards the first black network | [optional] 
**inner_subnet** | str,  | str,  | The subnet to route towards the inner interface (aka. the edge network/device) | [optional] 
**outer_subnet** | str,  | str,  | The subnet to route towards the tunnel (aka. the other edge network/device) | [optional] 
**local_port** | decimal.Decimal, int,  | decimal.Decimal,  | The local port to use to bind the tunnel | [optional] 
**remote_end** | str,  | str,  | The remote address to contact as the other side of the tunnel | [optional] 
**private_key** | str,  | str,  | The private key to use for authentication of the tunnel to the other side | [optional] 
**public_key** | str,  | str,  | The public key to use for authentication of the tunnel from the other side | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

