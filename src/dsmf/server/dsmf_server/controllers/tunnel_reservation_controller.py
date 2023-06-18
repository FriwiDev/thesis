from typing import List, Dict
from aiohttp import web

from dsmf_server.models.tunnel import Tunnel
from dsmf_server import util


async def tunnel_reservation_delete(request: web.Request, auth, id) -> web.Response:
    """tunnel_reservation_delete

    Deletes a tunnel reservation

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param id: The id of the tunnel reservation to be deleted.
    :type id: int

    """
    return web.Response(status=200)


async def tunnel_reservation_get(request: web.Request, auth) -> web.Response:
    """tunnel_reservation_get

    Lists all current tunnel reservations

    :param auth: The authentication token issued by prior login
    :type auth: str

    """
    return web.Response(status=200)


async def tunnel_reservation_put(request: web.Request, auth, tunnel) -> web.Response:
    """tunnel_reservation_put

    Creates a new tunnel reservation or stages changes to an existing deployed tunnel, as long as source and target of the tunnel match.

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param tunnel: The tunnel to reserve. Will check for issues.
    :type tunnel: dict | bytes

    """
    tunnel = .from_dict(tunnel)
    return web.Response(status=200)
