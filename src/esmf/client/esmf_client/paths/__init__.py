# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from esmf_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    AUTH = "/auth"
    SLICE = "/slice"
    CONFIGURATION = "/configuration"
    SLICE_RESERVATION = "/slice_reservation"
    SLICE_DEPLOYMENT = "/slice_deployment"
    TUNNEL_RESERVATION = "/tunnel_reservation"
    TUNNEL_DEPLOYMENT = "/tunnel_deployment"
