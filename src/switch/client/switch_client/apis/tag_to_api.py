import typing_extensions

from switch_client.apis.tags import TagValues
from switch_client.apis.tags.authentication_api import AuthenticationApi
from switch_client.apis.tags.queue_management_api import QueueManagementApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.QUEUE_MANAGEMENT: QueueManagementApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.QUEUE_MANAGEMENT: QueueManagementApi,
    }
)
