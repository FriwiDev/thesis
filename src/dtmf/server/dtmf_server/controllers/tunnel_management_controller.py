from typing import List, Dict
from aiohttp import web

from dtmf_server.models.tunnel import Tunnel
from dtmf_server import util


async def tunnel_deployment_delete(request: web.Request, auth, tunnel_id) -> web.Response:
    """tunnel_deployment_delete

    Deletes a tunnel

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param tunnel_id: The id of the tunnel to be deleted.
    :type tunnel_id: int

    """
    return web.Response(status=200)


async def tunnel_deployment_get(request: web.Request, auth) -> web.Response:
    """tunnel_deployment_get

    Lists all current tunnels

    :param auth: The authentication token issued by prior login
    :type auth: str

    """
    return web.Response(status=200)


async def tunnel_deployment_put(request: web.Request, auth, tunnel_id) -> web.Response:
    """tunnel_deployment_put

    Creates a new tunnel or modifies a tunnel from a reservation

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param tunnel_id: The tunnel to create from the corresponding reservation id
    :type tunnel_id: int

    """
    return web.Response(status=200)
