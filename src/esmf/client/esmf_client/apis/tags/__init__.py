# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from esmf_client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    AUTHENTICATION = "Authentication"
    SLICE_MANAGEMENT = "Slice Management"
    SLICE_SYNCHRONIZATION = "Slice Synchronization"
    TUNNEL_SYNCHRONIZATION = "Tunnel Synchronization"
