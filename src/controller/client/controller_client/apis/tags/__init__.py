# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from controller_client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    FLOW_MANAGEMENT = "Flow management"
    GENERAL_SWITCH_INFORMATION = "General Switch Information"
    PORT_MANAGEMENT = "Port management"
    QUEUE_MANAGEMENT = "Queue management"
    TABLE_MANAGEMENT = "Table management"
