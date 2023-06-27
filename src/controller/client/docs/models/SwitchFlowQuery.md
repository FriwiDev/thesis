# controller_client.model.switch_flow_query.SwitchFlowQuery

A switch flow query

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A switch flow query | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**table_id** | decimal.Decimal, int,  | decimal.Decimal,  | Table ID | [optional] 
**out_port** | decimal.Decimal, int,  | decimal.Decimal,  | Require matching entries to include this as an output port | [optional] 
**out_group** | decimal.Decimal, int,  | decimal.Decimal,  | Require matching entries to include this as an output group | [optional] 
**cookie** | decimal.Decimal, int,  | decimal.Decimal,  | Require matching entries to contain this cookie value | [optional] 
**cookie_mask** | decimal.Decimal, int,  | decimal.Decimal,  | Mask used to restrict the cookie bits that must match | [optional] 
**match** | [**SwitchFlowMatchV12**](SwitchFlowMatchV12.md) | [**SwitchFlowMatchV12**](SwitchFlowMatchV12.md) |  | [optional] 
**priority** | decimal.Decimal, int,  | decimal.Decimal,  | Priority of the entry | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

