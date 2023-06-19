from typing import List, Dict
from aiohttp import web

from jump_host_server.models.tunnel_entry import TunnelEntry
from jump_host_server import util


async def tunnel_entry_delete(request: web.Request, auth, tunnel_entry_id) -> web.Response:
    """tunnel_entry_delete

    Deletes a tunnel entry

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param tunnel_entry_id: The id of the tunnel entry to be deleted.
    :type tunnel_entry_id: int

    """
    return web.Response(status=200)


async def tunnel_entry_get(request: web.Request, auth) -> web.Response:
    """tunnel_entry_get

    Lists all current tunnel entries

    :param auth: The authentication token issued by prior login
    :type auth: str

    """
    return web.Response(status=200)


async def tunnel_entry_put(request: web.Request, auth, body=None) -> web.Response:
    """tunnel_entry_put

    Creates a new tunnel entry

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param body: The tunnel entry to create. The id will be checked for conflicts and inherited from the request.
    :type body: dict | bytes

    """
    body = TunnelEntry.from_dict(body)
    return web.Response(status=200)
