# vpn_gateway_client.model.tunnel_entry.TunnelEntry

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
**[matches](#matches)** | list, tuple,  | tuple,  | A specification for which packets to transport through the tunnel | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# matches

A specification for which packets to transport through the tunnel

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A specification for which packets to transport through the tunnel | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | A match entry specifying packets that should be routed through the tunnel | 

# items

A match entry specifying packets that should be routed through the tunnel

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A match entry specifying packets that should be routed through the tunnel | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**direction** | str,  | str,  | Specifies the fields of the packets that need to be matched | [optional] must be one of ["SRC", "DST", ] 
**transport_protocol** | str,  | str,  | The protocol to be expected | [optional] must be one of ["UDP", "TCP", ] 
**ip** | str,  | str,  | Specifies the source or target ip to be matched. Leave empty for no matching. | [optional] 
**mac** | str,  | str,  | Specifies the source or target mac to be matched. Leave empty for no matching. | [optional] 
**port** | decimal.Decimal, int,  | decimal.Decimal,  | Specifies the source or target port to be matched. Leave empty or on 0 for no matching. | [optional] if omitted the server will use the default value of 0
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

