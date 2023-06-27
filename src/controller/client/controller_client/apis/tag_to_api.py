import typing_extensions

from controller_client.apis.tags import TagValues
from controller_client.apis.tags.flow_management_api import FlowManagementApi
from controller_client.apis.tags.general_switch_information_api import GeneralSwitchInformationApi
from controller_client.apis.tags.port_management_api import PortManagementApi
from controller_client.apis.tags.queue_management_api import QueueManagementApi
from controller_client.apis.tags.table_management_api import TableManagementApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.FLOW_MANAGEMENT: FlowManagementApi,
        TagValues.GENERAL_SWITCH_INFORMATION: GeneralSwitchInformationApi,
        TagValues.PORT_MANAGEMENT: PortManagementApi,
        TagValues.QUEUE_MANAGEMENT: QueueManagementApi,
        TagValues.TABLE_MANAGEMENT: TableManagementApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.FLOW_MANAGEMENT: FlowManagementApi,
        TagValues.GENERAL_SWITCH_INFORMATION: GeneralSwitchInformationApi,
        TagValues.PORT_MANAGEMENT: PortManagementApi,
        TagValues.QUEUE_MANAGEMENT: QueueManagementApi,
        TagValues.TABLE_MANAGEMENT: TableManagementApi,
    }
)
