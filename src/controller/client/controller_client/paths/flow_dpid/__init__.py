# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from controller_client.paths.flow_dpid import Api

from controller_client.paths import PathValues

path = PathValues.FLOW_DPID