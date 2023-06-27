# controller_client.model.switch_flow.SwitchFlow

A switch flow

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A switch flow | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**dpid** | decimal.Decimal, int,  | decimal.Decimal,  | Datapath ID. Only set when using this object to create or modify a flow entry. | [optional] 
**length** | decimal.Decimal, int,  | decimal.Decimal,  | Length of this entry. Not in use when using this object to create or modify a flow entry. | [optional] 
**buffer_id** | decimal.Decimal, int,  | decimal.Decimal,  | Buffered packet to apply to, or OFP_NO_BUFFER. Only used when writing flow entries. | [optional] 
**table_id** | decimal.Decimal, int,  | decimal.Decimal,  | Table ID | [optional] 
**duration_sec** | decimal.Decimal, int,  | decimal.Decimal,  | Time flow has been alive in seconds | [optional] 
**duration_nsec** | decimal.Decimal, int,  | decimal.Decimal,  | Time flow has been alive in nanoseconds beyond duration_sec | [optional] 
**priority** | decimal.Decimal, int,  | decimal.Decimal,  | Priority of the entry | [optional] 
**idle_timeout** | decimal.Decimal, int,  | decimal.Decimal,  | Number of seconds idle before expiration | [optional] 
**hard_timeout** | decimal.Decimal, int,  | decimal.Decimal,  | Number of seconds before expiration | [optional] 
**flags** | decimal.Decimal, int,  | decimal.Decimal,  | Bitmap of OFPFF_* flags | [optional] 
**cookie** | decimal.Decimal, int,  | decimal.Decimal,  | Opaque controller-issued identifier | [optional] 
**packet_count** | decimal.Decimal, int,  | decimal.Decimal,  | Number of packets in flow | [optional] 
**byte_count** | decimal.Decimal, int,  | decimal.Decimal,  | Number of bytes in flow | [optional] 
**match** | [**SwitchFlowMatchV12**](SwitchFlowMatchV12.md) | [**SwitchFlowMatchV12**](SwitchFlowMatchV12.md) |  | [optional] 
**[actions](#actions)** | list, tuple,  | tuple,  | Instruction set (OpenFlow &lt;&#x3D; v1_3) | [optional] 
**[instructions](#instructions)** | list, tuple,  | tuple,  | struct ofp_instruction_header (OpenFlow &gt;&#x3D; v1_4) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# actions

Instruction set (OpenFlow <= v1_3)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Instruction set (OpenFlow &lt;&#x3D; v1_3) | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# instructions

struct ofp_instruction_header (OpenFlow >= v1_4)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | struct ofp_instruction_header (OpenFlow &gt;&#x3D; v1_4) | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SwitchFlowInstruction**](SwitchFlowInstruction.md) | [**SwitchFlowInstruction**](SwitchFlowInstruction.md) | [**SwitchFlowInstruction**](SwitchFlowInstruction.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

