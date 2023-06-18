from typing import List, Dict
from aiohttp import web

from dtmf_server.models.tunnel import Tunnel
from dtmf_server import util


async def tunnel_reservation_delete(request: web.Request, auth, tunnel_id) -> web.Response:
    """tunnel_reservation_delete

    Deletes a tunnel reservation

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param tunnel_id: The id of the tunnel reservation to be deleted.
    :type tunnel_id: int

    """
    return web.Response(status=200)


async def tunnel_reservation_get(request: web.Request, auth) -> web.Response:
    """tunnel_reservation_get

    Lists all current tunnel reservations

    :param auth: The authentication token issued by prior login
    :type auth: str

    """
    return web.Response(status=200)


async def tunnel_reservation_put(request: web.Request, auth, body=None) -> web.Response:
    """tunnel_reservation_put

    Creates a new tunnel reservation or stages changes to an existing deployed tunnel, as long as source and target of the tunnel match.

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param body: The tunnel to reserve. Will check for issues.
    :type body: dict | bytes

    """
    body = Tunnel.from_dict(body)
    return web.Response(status=200)
