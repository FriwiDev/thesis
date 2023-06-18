# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from dtmf_client.paths.tunnel_reservation import Api

from dtmf_client.paths import PathValues

path = PathValues.TUNNEL_RESERVATION