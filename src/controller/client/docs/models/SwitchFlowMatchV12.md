# controller_client.model.switch_flow_match_v12.SwitchFlowMatchV12

A switch flow match entity (only selected properties, OpenFlow >= v1_2)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A switch flow match entity (only selected properties, OpenFlow &gt;&#x3D; v1_2) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**in_port** | decimal.Decimal, int,  | decimal.Decimal,  | Input switch port | [optional] 
**eth_src** | str,  | str,  | Ethernet source address | [optional] 
**eth_dst** | str,  | str,  | Ethernet destination address | [optional] 
**eth_type** | decimal.Decimal, int,  | decimal.Decimal,  | Ethernet frame type | [optional] 
**tcp_src** | decimal.Decimal, int,  | decimal.Decimal,  | TCP source port | [optional] 
**tcp_dst** | decimal.Decimal, int,  | decimal.Decimal,  | TCP destination port | [optional] 
**udp_src** | decimal.Decimal, int,  | decimal.Decimal,  | UDP source port | [optional] 
**udp_dst** | decimal.Decimal, int,  | decimal.Decimal,  | UDP destination port | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

