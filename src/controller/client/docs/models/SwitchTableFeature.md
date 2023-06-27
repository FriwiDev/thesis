# controller_client.model.switch_table_feature.SwitchTableFeature

Switch table feature

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Switch table feature | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**table_id** | decimal.Decimal, int,  | decimal.Decimal,  | Table ID | [optional] 
**name** | str,  | str,  | Name of Table | [optional] 
**metadata_match** | decimal.Decimal, int,  | decimal.Decimal,  | Bits of metadata table can match | [optional] 
**metadata_write** | decimal.Decimal, int,  | decimal.Decimal,  | Bits of metadata table can write | [optional] 
**config** | decimal.Decimal, int,  | decimal.Decimal,  | Bitmap of OFPTC_* values | [optional] 
**max_entries** | decimal.Decimal, int,  | decimal.Decimal,  | Max number of entries supported | [optional] 
**[properties](#properties)** | list, tuple,  | tuple,  | struct ofp_table_feature_prop_header | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# properties

struct ofp_table_feature_prop_header

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | struct ofp_table_feature_prop_header | 

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

