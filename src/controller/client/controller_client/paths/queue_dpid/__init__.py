# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from controller_client.paths.queue_dpid import Api

from controller_client.paths import PathValues

path = PathValues.QUEUE_DPID