# dsmf_client.model.network_configuration.NetworkConfiguration

A network configuration element

## Model Type Info

 Input Type                   | Accessed Type          | Description                     | Notes 
------------------------------|------------------------|---------------------------------|-------
 dict, frozendict.frozendict, | frozendict.frozendict, | A network configuration element |

### Dictionary Keys

 Key                                 | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes      
-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------|------------
 **name**                            | str,                                                                                                                                        | str,                                                                                    | The name of the network                                            | [optional] 
 **[reachable](#reachable)**         | list, tuple,                                                                                                                                | tuple,                                                                                  | Networks reachable from this network                               | [optional] 
 **[preferred_vpn](#preferred_vpn)** | list, tuple,                                                                                                                                | tuple,                                                                                  | VPN gateways to use (in order) to connect to this network          | [optional] 
 **any_string_name**                 | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional] 

# reachable

Networks reachable from this network

## Model Type Info

 Input Type   | Accessed Type | Description                          | Notes 
--------------|---------------|--------------------------------------|-------
 list, tuple, | tuple,        | Networks reachable from this network |

### Tuple Items

 Class Name | Input Type | Accessed Type | Description | Notes 
------------|------------|---------------|-------------|-------
 items      | str,       | str,          |             |

# preferred_vpn

VPN gateways to use (in order) to connect to this network

## Model Type Info

 Input Type   | Accessed Type | Description                                               | Notes 
--------------|---------------|-----------------------------------------------------------|-------
 list, tuple, | tuple,        | VPN gateways to use (in order) to connect to this network |

### Tuple Items

 Class Name | Input Type | Accessed Type | Description | Notes 
------------|------------|---------------|-------------|-------
 items      | str,       | str,          |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

