import typing_extensions

from ctmf_client.apis.tags import TagValues
from ctmf_client.apis.tags.authentication_api import AuthenticationApi
from ctmf_client.apis.tags.tunnel_synchronization_api import TunnelSynchronizationApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.TUNNEL_SYNCHRONIZATION: TunnelSynchronizationApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.TUNNEL_SYNCHRONIZATION: TunnelSynchronizationApi,
    }
)
