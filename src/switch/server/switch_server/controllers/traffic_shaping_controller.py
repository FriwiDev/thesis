from aiohttp import web

from switch_server.command_util import run_command
from switch_server.controllers.authentication_controller import check_auth
from switch_server.controllers.queue_management_controller import check_port, MAX_RATE


async def policy_put(request: web.Request, auth, port, ingress_policing_rate=None, ingress_policing_burst=None) -> web.Response:
    """policy_put

    Sets the policies on the specified port

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param port: The switch port name to modify.
    :type port: str
    :param ingress_policing_rate: The ingress policing rate to use in Bits/s. Set to 0 to reset/delete.
    :type ingress_policing_rate: int
    :param ingress_policing_burst: The ingress policing burst to use in Bits/s. Set to 0 to reset/delete.
    :type ingress_policing_burst: int

    """
    if not check_auth(auth):
        return web.Response(status=403, reason="Invalid authentication provided.")
    if (ingress_policing_rate and (ingress_policing_rate > MAX_RATE or ingress_policing_rate <= 0)) \
            or (ingress_policing_burst and (ingress_policing_burst > MAX_RATE or ingress_policing_burst <= 0)):
        return web.Response(status=406, reason="A value exceeds the allowed range")
    if not check_port(port):
        return web.Response(status=404, reason="The switch port could not be found")
    if not ingress_policing_rate and not ingress_policing_burst:
        return web.Response(status=200)
    cmd = ['ovs-vsctl', 'set', 'interface', port]
    if ingress_policing_rate:
        cmd += ['ingress_policing_rate='+str(ingress_policing_rate)]
    if ingress_policing_rate:
        cmd += ['ingress_policing_burst=' + str(ingress_policing_burst)]
    run_command(cmd)
    return web.Response(status=200, reason="Traffic policy updated")
