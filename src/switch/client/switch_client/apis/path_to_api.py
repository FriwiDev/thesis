import typing_extensions
from switch_client.apis.paths.auth import Auth
from switch_client.apis.paths.queue import Queue
from switch_client.paths import PathValues

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.AUTH: Auth,
        PathValues.QUEUE: Queue,
    }
)

path_to_api = PathToApi(
    {
        PathValues.AUTH: Auth,
        PathValues.QUEUE: Queue,
    }
)
