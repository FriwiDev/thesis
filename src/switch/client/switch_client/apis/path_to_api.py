import typing_extensions

from switch_client.paths import PathValues
from switch_client.apis.paths.auth import Auth
from switch_client.apis.paths.queue import Queue
from switch_client.apis.paths.policy import Policy

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.AUTH: Auth,
        PathValues.QUEUE: Queue,
        PathValues.POLICY: Policy,
    }
)

path_to_api = PathToApi(
    {
        PathValues.AUTH: Auth,
        PathValues.QUEUE: Queue,
        PathValues.POLICY: Policy,
    }
)
