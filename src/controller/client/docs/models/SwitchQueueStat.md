# controller_client.model.switch_queue_stat.SwitchQueueStat

Switch queue stats

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Switch queue stats | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**port_no** | decimal.Decimal, int,  | decimal.Decimal,  | Port number | [optional] 
**queue_id** | decimal.Decimal, int,  | decimal.Decimal,  | Queue ID | [optional] 
**tx_bytes** | decimal.Decimal, int,  | decimal.Decimal,  | Number of transmitted bytes | [optional] 
**tx_packets** | decimal.Decimal, int,  | decimal.Decimal,  | Number of transmitted packets | [optional] 
**tx_errors** | decimal.Decimal, int,  | decimal.Decimal,  | Number of packets dropped due to overrun | [optional] 
**duration_sec** | decimal.Decimal, int,  | decimal.Decimal,  | Time queue has been alive in seconds | [optional] 
**duration_nsec** | decimal.Decimal, int,  | decimal.Decimal,  | Time queue has been alive in nanoseconds beyond duration_sec | [optional] 
**length** | decimal.Decimal, int,  | decimal.Decimal,  | Length of this entry (OpenFlow &gt;&#x3D; 1.4) | [optional] 
**[properties](#properties)** | list, tuple,  | tuple,  | struct ofp_port_desc_prop_header (OpenFlow &gt;&#x3D; 1.4) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# properties

struct ofp_port_desc_prop_header (OpenFlow >= 1.4)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | struct ofp_port_desc_prop_header (OpenFlow &gt;&#x3D; 1.4) | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

