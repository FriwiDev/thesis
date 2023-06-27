import typing_extensions

from controller_client.paths import PathValues
from controller_client.apis.paths.switches import Switches
from controller_client.apis.paths.desc_dpid import DescDpid
from controller_client.apis.paths.flow_dpid import FlowDpid
from controller_client.apis.paths.tablefeatures_dpid import TablefeaturesDpid
from controller_client.apis.paths.portdesc_dpid import PortdescDpid
from controller_client.apis.paths.portdesc_dpid_port import PortdescDpidPort
from controller_client.apis.paths.queue_dpid import QueueDpid
from controller_client.apis.paths.queue_dpid_port import QueueDpidPort
from controller_client.apis.paths.queue_dpid_port_queue_id import QueueDpidPortQueueId
from controller_client.apis.paths.flowentry_add import FlowentryAdd
from controller_client.apis.paths.flowentry_delete import FlowentryDelete
from controller_client.apis.paths.flowentry_delete_strict import FlowentryDeleteStrict
from controller_client.apis.paths.flowentry_clear_dpid import FlowentryClearDpid

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.SWITCHES: Switches,
        PathValues.DESC_DPID: DescDpid,
        PathValues.FLOW_DPID: FlowDpid,
        PathValues.TABLEFEATURES_DPID: TablefeaturesDpid,
        PathValues.PORTDESC_DPID: PortdescDpid,
        PathValues.PORTDESC_DPID_PORT: PortdescDpidPort,
        PathValues.QUEUE_DPID: QueueDpid,
        PathValues.QUEUE_DPID_PORT: QueueDpidPort,
        PathValues.QUEUE_DPID_PORT_QUEUE_ID: QueueDpidPortQueueId,
        PathValues.FLOWENTRY_ADD: FlowentryAdd,
        PathValues.FLOWENTRY_DELETE: FlowentryDelete,
        PathValues.FLOWENTRY_DELETE_STRICT: FlowentryDeleteStrict,
        PathValues.FLOWENTRY_CLEAR_DPID: FlowentryClearDpid,
    }
)

path_to_api = PathToApi(
    {
        PathValues.SWITCHES: Switches,
        PathValues.DESC_DPID: DescDpid,
        PathValues.FLOW_DPID: FlowDpid,
        PathValues.TABLEFEATURES_DPID: TablefeaturesDpid,
        PathValues.PORTDESC_DPID: PortdescDpid,
        PathValues.PORTDESC_DPID_PORT: PortdescDpidPort,
        PathValues.QUEUE_DPID: QueueDpid,
        PathValues.QUEUE_DPID_PORT: QueueDpidPort,
        PathValues.QUEUE_DPID_PORT_QUEUE_ID: QueueDpidPortQueueId,
        PathValues.FLOWENTRY_ADD: FlowentryAdd,
        PathValues.FLOWENTRY_DELETE: FlowentryDelete,
        PathValues.FLOWENTRY_DELETE_STRICT: FlowentryDeleteStrict,
        PathValues.FLOWENTRY_CLEAR_DPID: FlowentryClearDpid,
    }
)
