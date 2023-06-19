import typing_extensions

from jump_host_client.paths import PathValues
from jump_host_client.apis.paths.auth import Auth
from jump_host_client.apis.paths.tunnel_entry import TunnelEntry

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.AUTH: Auth,
        PathValues.TUNNEL_ENTRY: TunnelEntry,
    }
)

path_to_api = PathToApi(
    {
        PathValues.AUTH: Auth,
        PathValues.TUNNEL_ENTRY: TunnelEntry,
    }
)
