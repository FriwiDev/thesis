import typing_extensions
from dtmf_client.apis.paths.auth import Auth
from dtmf_client.apis.paths.tunnel_deployment import TunnelDeployment
from dtmf_client.apis.paths.tunnel_reservation import TunnelReservation
from dtmf_client.paths import PathValues

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.AUTH: Auth,
        PathValues.TUNNEL_RESERVATION: TunnelReservation,
        PathValues.TUNNEL_DEPLOYMENT: TunnelDeployment,
    }
)

path_to_api = PathToApi(
    {
        PathValues.AUTH: Auth,
        PathValues.TUNNEL_RESERVATION: TunnelReservation,
        PathValues.TUNNEL_DEPLOYMENT: TunnelDeployment,
    }
)
