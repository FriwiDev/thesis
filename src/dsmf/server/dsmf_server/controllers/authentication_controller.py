from typing import List, Dict
from aiohttp import web

from dsmf_server import util


async def auth_post(request: web.Request, ) -> web.Response:
    """auth_post

    Issues a new authentication token in exchange for credentials. Currently requires no credentials, this is up to future implementations.


    """
    return web.Response(status=200)
