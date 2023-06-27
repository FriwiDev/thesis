# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from controller_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    SWITCHES = "/switches"
    DESC_DPID = "/desc/{dpid}"
    FLOW_DPID = "/flow/{dpid}"
    TABLEFEATURES_DPID = "/tablefeatures/{dpid}"
    PORTDESC_DPID = "/portdesc/{dpid}"
    PORTDESC_DPID_PORT = "/portdesc/{dpid}/{port}"
    QUEUE_DPID = "/queue/{dpid}"
    QUEUE_DPID_PORT = "/queue/{dpid}/{port}"
    QUEUE_DPID_PORT_QUEUE_ID = "/queue/{dpid}/{port}/{queue_id}"
    FLOWENTRY_ADD = "/flowentry/add"
    FLOWENTRY_DELETE = "/flowentry/delete"
    FLOWENTRY_DELETE_STRICT = "/flowentry/delete_strict"
    FLOWENTRY_CLEAR_DPID = "/flowentry/clear/{dpid}"
