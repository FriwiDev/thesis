from typing import List, Dict
from aiohttp import web

from switch_server.models.queue import Queue
from switch_server import util


async def queue_delete(request: web.Request, auth, id, port) -> web.Response:
    """queue_delete

    Deletes a queue

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param id: The id of the queue to be deleted.
    :type id: int
    :param port: The switch port of the queue to be deleted.
    :type port: str

    """
    return web.Response(status=200)


async def queue_put(request: web.Request, auth, queue) -> web.Response:
    """queue_put

    Creates a new queue

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param queue: The queue to create. The id will be set by the service.
    :type queue: dict | bytes

    """
    queue = .from_dict(queue)
    return web.Response(status=200)
