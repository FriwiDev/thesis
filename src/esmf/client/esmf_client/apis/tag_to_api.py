import typing_extensions

from esmf_client.apis.tags import TagValues
from esmf_client.apis.tags.authentication_api import AuthenticationApi
from esmf_client.apis.tags.slice_management_api import SliceManagementApi
from esmf_client.apis.tags.slice_synchronization_api import SliceSynchronizationApi
from esmf_client.apis.tags.tunnel_synchronization_api import TunnelSynchronizationApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.SLICE_MANAGEMENT: SliceManagementApi,
        TagValues.SLICE_SYNCHRONIZATION: SliceSynchronizationApi,
        TagValues.TUNNEL_SYNCHRONIZATION: TunnelSynchronizationApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.SLICE_MANAGEMENT: SliceManagementApi,
        TagValues.SLICE_SYNCHRONIZATION: SliceSynchronizationApi,
        TagValues.TUNNEL_SYNCHRONIZATION: TunnelSynchronizationApi,
    }
)
