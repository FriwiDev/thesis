# controller_client.model.switch_port_description.SwitchPortDescription

Switch port description

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Switch port description | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[port_no](#port_no)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Port number | [optional] 
**hw_addr** | str,  | str,  | Ethernet hardware address | [optional] 
**name** | str,  | str,  | Name of port | [optional] 
**config** | decimal.Decimal, int,  | decimal.Decimal,  | Bitmap of OFPPC_* flags | [optional] 
**state** | decimal.Decimal, int,  | decimal.Decimal,  | Bitmap of OFPPS_* flags | [optional] 
**curr** | decimal.Decimal, int,  | decimal.Decimal,  | Current features (OpenFlow &lt;&#x3D; 1.4) | [optional] 
**advertised** | decimal.Decimal, int,  | decimal.Decimal,  | Features being advertised by the port (OpenFlow &lt;&#x3D; 1.4) | [optional] 
**supported** | decimal.Decimal, int,  | decimal.Decimal,  | Features being supported by the port (OpenFlow &lt;&#x3D; 1.4) | [optional] 
**peer** | decimal.Decimal, int,  | decimal.Decimal,  | Features advertised by peer (OpenFlow &lt;&#x3D; 1.4) | [optional] 
**curr_speed** | decimal.Decimal, int,  | decimal.Decimal,  | Current port bitrate in kbps (OpenFlow &lt;&#x3D; 1.4) | [optional] 
**max_speed** | decimal.Decimal, int,  | decimal.Decimal,  | Max port bitrate in kbps (OpenFlow &lt;&#x3D; 1.4) | [optional] 
**length** | decimal.Decimal, int,  | decimal.Decimal,  | Length of this entry (OpenFlow &gt;&#x3D; 1.5) | [optional] 
**[properties](#properties)** | list, tuple,  | tuple,  | struct ofp_port_desc_prop_header (OpenFlow &gt;&#x3D; 1.5) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# port_no

Port number

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Port number | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | str,  | str,  |  | 
[one_of_1](#one_of_1) | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# one_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# one_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# properties

struct ofp_port_desc_prop_header (OpenFlow >= 1.5)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | struct ofp_port_desc_prop_header (OpenFlow &gt;&#x3D; 1.5) | 

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

