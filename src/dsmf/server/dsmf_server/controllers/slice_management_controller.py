from typing import List, Dict
from aiohttp import web

from dsmf_server.models.slice import Slice
from dsmf_server import util


async def slice_deployment_delete(request: web.Request, auth, id) -> web.Response:
    """slice_deployment_delete

    Deletes a slice

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param id: The id of the slice to be deleted.
    :type id: int

    """
    return web.Response(status=200)


async def slice_deployment_get(request: web.Request, auth) -> web.Response:
    """slice_deployment_get

    Lists all current slices

    :param auth: The authentication token issued by prior login
    :type auth: str

    """
    return web.Response(status=200)


async def slice_deployment_put(request: web.Request, auth, id) -> web.Response:
    """slice_deployment_put

    Creates a new slice from a reservation

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param id: The slice to create from the corresponding reservation id
    :type id: int

    """
    return web.Response(status=200)
