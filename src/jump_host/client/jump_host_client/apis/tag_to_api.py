import typing_extensions

from jump_host_client.apis.tags import TagValues
from jump_host_client.apis.tags.authentication_api import AuthenticationApi
from jump_host_client.apis.tags.tunnel_entry_management_api import TunnelEntryManagementApi

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
