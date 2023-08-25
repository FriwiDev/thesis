from aiohttp import web


async def auth_post(request: web.Request, ) -> web.Response:
    """auth_post

    Issues a new authentication token in exchange for credentials. Currently requires no credentials, this is up to future implementations.


    """
    return web.Response(status=200, content_type="application/json", body="\"token\"")


def check_auth(token: str) -> bool:
    # adv_token is the token of our spamming adversary so that we can distinguish it from our host
    return token == "token" or token == "adv_token"
