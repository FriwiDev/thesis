# vpn_gateway_client.model.tunnel_entry.TunnelEntry

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**tunnel_entry_id** | decimal.Decimal, int,  | decimal.Decimal,  | The tunnel identifier | [optional] value must be a 32 bit integer
**inner_subnet** | str,  | str,  | The subnet to route towards the inner interface (aka. the edge network/device) | [optional] 
**local_port** | decimal.Decimal, int,  | decimal.Decimal,  | The local port to use to bind the tunnel | [optional] 
**remote_end** | str,  | str,  | The remote address to contact as the other side of the tunnel | [optional] 
**private_key** | str,  | str,  | The private key to use for authentication of the tunnel to the other side | [optional] 
**public_key** | str,  | str,  | The public key to use for authentication of the tunnel from the other side | [optional] 
**local_tunnel_ip** | str,  | str,  | The ip of the local wireguard tunnel end device | [optional] 
**remote_tunnel_ip** | str,  | str,  | The ip of the remote wireguard tunnel end device | [optional] 
**[ingress_matches](#ingress_matches)** | list, tuple,  | tuple,  | A specification for which mpls labels (slice ids) to match, alongside their expected ingress port | [optional] 
**[egress_matches](#egress_matches)** | list, tuple,  | tuple,  | A specification for which mpls labels (slice ids) to match, alongside their supposed egress port | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ingress_matches

A specification for which mpls labels (slice ids) to match, alongside their expected ingress port

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A specification for which mpls labels (slice ids) to match, alongside their expected ingress port | 

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
**intf_name** | str,  | str,  | Specifies the ingress interface | [optional] 
**slice_id** | decimal.Decimal, int,  | decimal.Decimal,  | Specifies the expected mpls label | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# egress_matches

A specification for which mpls labels (slice ids) to match, alongside their supposed egress port

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A specification for which mpls labels (slice ids) to match, alongside their supposed egress port | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | A match entry specifying packets that should be routed to their destination | 

# items

A match entry specifying packets that should be routed to their destination

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A match entry specifying packets that should be routed to their destination | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**intf_name** | str,  | str,  | Specifies the egress interface | [optional] 
**slice_id** | decimal.Decimal, int,  | decimal.Decimal,  | Specifies the expected mpls label | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

