# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from jump_host_client.paths.tunnel_entry import Api

from jump_host_client.paths import PathValues

path = PathValues.TUNNEL_ENTRY