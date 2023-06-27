import typing_extensions

from ctmf_client.paths import PathValues
from ctmf_client.apis.paths.auth import Auth
from ctmf_client.apis.paths.tunnel_reservation import TunnelReservation
from ctmf_client.apis.paths.tunnel_deployment import TunnelDeployment

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