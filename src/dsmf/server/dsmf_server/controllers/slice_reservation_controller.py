from typing import List, Dict
from aiohttp import web

from dsmf_server.models.slice import Slice
from dsmf_server import util


async def slice_reservation_delete(request: web.Request, auth, slice_id) -> web.Response:
    """slice_reservation_delete

    Deletes a slice reservation

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param slice_id: The id of the slice reservation to be deleted.
    :type slice_id: int

    """
    return web.Response(status=200)


async def slice_reservation_get(request: web.Request, auth) -> web.Response:
    """slice_reservation_get

    Lists all current slice reservations

    :param auth: The authentication token issued by prior login
    :type auth: str

    """
    return web.Response(status=200)


async def slice_reservation_put(request: web.Request, auth, body=None) -> web.Response:
    """slice_reservation_put

    Creates a new slice reservation

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param body: The slice to reserve. Will check for issues.
    :type body: dict | bytes

    """
    body = Slice.from_dict(body)
    return web.Response(status=200)
