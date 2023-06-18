import typing_extensions

from esmf_client.paths import PathValues
from esmf_client.apis.paths.auth import Auth
from esmf_client.apis.paths.slice import Slice
from esmf_client.apis.paths.slice_reservation import SliceReservation
from esmf_client.apis.paths.slice_deployment import SliceDeployment
from esmf_client.apis.paths.tunnel_reservation import TunnelReservation
from esmf_client.apis.paths.tunnel_deployment import TunnelDeployment

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.AUTH: Auth,
        PathValues.SLICE: Slice,
        PathValues.SLICE_RESERVATION: SliceReservation,
        PathValues.SLICE_DEPLOYMENT: SliceDeployment,
        PathValues.TUNNEL_RESERVATION: TunnelReservation,
        PathValues.TUNNEL_DEPLOYMENT: TunnelDeployment,
    }
)

path_to_api = PathToApi(
    {
        PathValues.AUTH: Auth,
        PathValues.SLICE: Slice,
        PathValues.SLICE_RESERVATION: SliceReservation,
        PathValues.SLICE_DEPLOYMENT: SliceDeployment,
        PathValues.TUNNEL_RESERVATION: TunnelReservation,
        PathValues.TUNNEL_DEPLOYMENT: TunnelDeployment,
    }
)
