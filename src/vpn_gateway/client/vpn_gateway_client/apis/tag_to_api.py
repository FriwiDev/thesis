import typing_extensions

from vpn_gateway_client.apis.tags import TagValues
from vpn_gateway_client.apis.tags.authentication_api import AuthenticationApi
from vpn_gateway_client.apis.tags.tunnel_entry_management_api import TunnelEntryManagementApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.TUNNEL_ENTRY_MANAGEMENT: TunnelEntryManagementApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.TUNNEL_ENTRY_MANAGEMENT: TunnelEntryManagementApi,
    }
)
