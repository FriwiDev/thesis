import typing_extensions

from dsmf_client.apis.tags import TagValues
from dsmf_client.apis.tags.authentication_api import AuthenticationApi
from dsmf_client.apis.tags.slice_management_api import SliceManagementApi
from dsmf_client.apis.tags.slice_reservation_api import SliceReservationApi
from dsmf_client.apis.tags.tunnel_management_api import TunnelManagementApi
from dsmf_client.apis.tags.tunnel_reservation_api import TunnelReservationApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.SLICE_MANAGEMENT: SliceManagementApi,
        TagValues.SLICE_RESERVATION: SliceReservationApi,
        TagValues.TUNNEL_MANAGEMENT: TunnelManagementApi,
        TagValues.TUNNEL_RESERVATION: TunnelReservationApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.SLICE_MANAGEMENT: SliceManagementApi,
        TagValues.SLICE_RESERVATION: SliceReservationApi,
        TagValues.TUNNEL_MANAGEMENT: TunnelManagementApi,
        TagValues.TUNNEL_RESERVATION: TunnelReservationApi,
    }
)
