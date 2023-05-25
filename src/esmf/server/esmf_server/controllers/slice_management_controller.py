from typing import List

from aiohttp import web

from esmf_server.models.slice import Slice


async def slice_delete(request: web.Request, auth, id) -> web.Response:
    """slice_delete

    Deletes one or multiple slices

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param id: The ids of the slices to be deleted.
    :type id: List[int]

    """
    return web.Response(status=200)


async def slice_get(request: web.Request, auth) -> web.Response:
    """slice_get

    Lists all current slices by this requester

    :param auth: The authentication token issued by prior login
    :type auth: str

    """
    return web.Response(status=200)


async def slice_put(request: web.Request, auth, slice) -> web.Response:
    """slice_put

    Creates one or multiple new slices from one host to another. Will either create all slices if feasible or none at all.

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param slice: The slices to reserve. The service will set the slice ids.
    :type slice: list | bytes

    """
    slice = [Slice.from_dict(d) for d in slice]
    return web.Response(status=200)
