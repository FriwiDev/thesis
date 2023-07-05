# dsmf_client.model.endpoint.Endpoint

Specifying an endpoint to be matched for source or target

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Specifying an endpoint to be matched for source or target | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ip** | str,  | str,  | Specifies the source or target ip to be matched. Leave empty for no matching. | [optional] 
**port** | decimal.Decimal, int,  | decimal.Decimal,  | Specifies the source or target port to be matched. Leave empty or on 0 for no matching. | [optional] if omitted the server will use the default value of 0
**name** | str,  | str,  | Specifies the name of this entry to look up in our configuration. | [optional] 
**network** | str,  | str,  | Specifies the network name of this endpoint. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

