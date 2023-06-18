from typing import List, Dict
from aiohttp import web

from switch_server import util


async def policy_put(request: web.Request, auth, port, ingress_policing_rate=None, ingress_policing_burst=None) -> web.Response:
    """policy_put

    Sets the policies on the specified port

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param port: The switch port name to modify.
    :type port: str
    :param ingress_policing_rate: The ingress policing rate to use in Bits/s. Set to 0 to reset/delete.
    :type ingress_policing_rate: int
    :param ingress_policing_burst: The ingress policing burst to use in Bits/s. Set to 0 to reset/delete.
    :type ingress_policing_burst: int

    """
    return web.Response(status=200)
