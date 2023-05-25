from aiohttp import web


async def slice_deployment_delete(request: web.Request, auth, id) -> web.Response:
    """slice_deployment_delete

    Deletes a slice from this domain

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param id: The id of the slice to be deleted.
    :type id: int

    """
    return web.Response(status=200)


async def slice_deployment_get(request: web.Request, auth) -> web.Response:
    """slice_deployment_get

    Lists all current slices issued by the requesting ESMF. Used for synchronization purposes.

    :param auth: The authentication token issued by prior login
    :type auth: str

    """
    return web.Response(status=200)


async def slice_deployment_put(request: web.Request, auth, id) -> web.Response:
    """slice_deployment_put

    Creates a new slice on this domain

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param id: The id of the slice to be deployed.
    :type id: int

    """
    return web.Response(status=200)


async def slice_reservation_delete(request: web.Request, auth, id) -> web.Response:
    """slice_reservation_delete

    Deletes a slice reservation

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param id: The id of the slice reservation to be deleted.
    :type id: int

    """
    return web.Response(status=200)


async def slice_reservation_get(request: web.Request, auth) -> web.Response:
    """slice_reservation_get

    Lists all current slice reservations issued by the requesting ESMF. Used for synchronization purposes.

    :param auth: The authentication token issued by prior login
    :type auth: str

    """
    return web.Response(status=200)


async def slice_reservation_put(request: web.Request, auth, slice) -> web.Response:
    """slice_reservation_put

    Creates a new slice reservation on this domain

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param slice: The slice to reserve.
    :type slice: dict | bytes

    """
    slice =.from_dict(slice)
    return web.Response(status=200)
