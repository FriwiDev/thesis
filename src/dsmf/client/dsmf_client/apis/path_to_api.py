import typing_extensions
from dsmf_client.apis.paths.auth import Auth
from dsmf_client.apis.paths.slice_deployment import SliceDeployment
from dsmf_client.apis.paths.slice_reservation import SliceReservation
from dsmf_client.apis.paths.tunnel_deployment import TunnelDeployment
from dsmf_client.apis.paths.tunnel_reservation import TunnelReservation
from dsmf_client.paths import PathValues

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.AUTH: Auth,
        PathValues.SLICE_RESERVATION: SliceReservation,
        PathValues.SLICE_DEPLOYMENT: SliceDeployment,
        PathValues.TUNNEL_RESERVATION: TunnelReservation,
        PathValues.TUNNEL_DEPLOYMENT: TunnelDeployment,
    }
)

path_to_api = PathToApi(
    {
        PathValues.AUTH: Auth,
        PathValues.SLICE_RESERVATION: SliceReservation,
        PathValues.SLICE_DEPLOYMENT: SliceDeployment,
        PathValues.TUNNEL_RESERVATION: TunnelReservation,
        PathValues.TUNNEL_DEPLOYMENT: TunnelDeployment,
    }
)
