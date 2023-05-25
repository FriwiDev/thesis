import typing_extensions

from dtmf_client.apis.tags import TagValues
from dtmf_client.apis.tags.authentication_api import AuthenticationApi
from dtmf_client.apis.tags.tunnel_management_api import TunnelManagementApi
from dtmf_client.apis.tags.tunnel_reservation_api import TunnelReservationApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.TUNNEL_MANAGEMENT: TunnelManagementApi,
        TagValues.TUNNEL_RESERVATION: TunnelReservationApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.TUNNEL_MANAGEMENT: TunnelManagementApi,
        TagValues.TUNNEL_RESERVATION: TunnelReservationApi,
    }
)
