import os

import aiohttp_cors
import connexion


def main():
    options = {
        "swagger_ui": True
    }
    specification_dir = os.path.join(os.path.dirname(__file__), 'openapi')
    app = connexion.AioHttpApp(__name__, specification_dir=specification_dir, options=options)
    app.add_api('openapi.yaml',
                arguments={'title': 'DTMF'},
                pythonic_params=True,
                pass_context_arg_name='request')

    # Enable CORS for all origins.
    cors = aiohttp_cors.setup(app.app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    })

    # Register all routers for CORS.
    for route in list(app.app.router.routes()):
        cors.add(route)

    app.run(port=8081)
