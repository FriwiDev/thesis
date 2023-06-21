import ipaddress
import pprint
import re
from typing import List, Dict
from aiohttp import web

from vpn_gateway_server.command_util import run_command
from vpn_gateway_server.controllers.authentication_controller import check_auth
from vpn_gateway_server.models.tunnel_entry import TunnelEntry
from vpn_gateway_server import util

INTF_PATTERN = re.compile("([A-Z][a-z][0-9]_-)*")
KEY_PATTERN = re.compile("([A-Z][a-z][0-9]/\\+=)*")

MAX_TUNNEL_ID = 65535
MAX_PORT = 65535


class TunnelEntryData:
    tunnel_entries: dict[int, TunnelEntry] = {}


async def tunnel_entry_delete(request: web.Request, auth, tunnel_entry_id) -> web.Response:
    """tunnel_entry_delete

    Deletes a tunnel entry

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param tunnel_entry_id: The id of the tunnel entry to be deleted.
    :type tunnel_entry_id: int

    """
    if not check_auth(auth):
        return web.Response(status=403, reason="Invalid authentication provided.")
    # Check for existence of entry
    if tunnel_entry_id not in TunnelEntryData.tunnel_entries.keys():
        return web.Response(status=404, reason="The tunnel entry could not be found.")
    tunnel_entry = TunnelEntryData.tunnel_entries[tunnel_entry_id]
    # Remove from local state
    del TunnelEntryData.tunnel_entries[tunnel_entry_id]
    # Delete the tunnel entry from our local deployment
    wg_intf = "wg" + str(tunnel_entry.local_port)
    if run_command(['ip', 'link', 'del', 'dev', wg_intf]) != 0:
        return web.Response(status=500, reason="Internal Server Error")
    if run_command(['rm', '-f', 'pk_wg'+str(tunnel_entry.local_port)]) != 0:
        return web.Response(status=500, reason="Internal Server Error")
    return web.Response(status=200, reason="The tunnel entry was successfully deleted.")


async def tunnel_entry_get(request: web.Request, auth) -> web.Response:
    """tunnel_entry_get

    Lists all current tunnel entries

    :param auth: The authentication token issued by prior login
    :type auth: str

    """
    if not check_auth(auth):
        return web.Response(status=403, reason="Invalid authentication provided.")
    return web.Response(status=200, body=pprint.pformat(TunnelEntryData.tunnel_entries.values()))


async def tunnel_entry_put(request: web.Request, auth, body=None) -> web.Response:
    """tunnel_entry_put

    Creates a new tunnel entry

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param body: The tunnel entry to create. The id will be checked for conflicts and inherited from the request.
    :type body: dict | bytes

    """
    if not check_auth(auth):
        return web.Response(status=403, reason="Invalid authentication provided.")
    if not body:
        return web.Response(status=400, reason="No body provided.")
    tunnel_entry = TunnelEntry.from_dict(body)
    # Check ranges
    if tunnel_entry.id < 0 or tunnel_entry.id > MAX_TUNNEL_ID \
            or tunnel_entry.local_port <= 0 or tunnel_entry.local_port > MAX_PORT:
        return web.Response(status=406, reason="A value exceeds the allowed range")
    # Validate subnets, remote end and keys
    if not validate_ip_network(tunnel_entry.inner_subnet) or not validate_ip_network(tunnel_entry.outer_subnet) \
            or len(tunnel_entry.private_key) > 256 or not KEY_PATTERN.match(tunnel_entry.private_key) \
            or len(tunnel_entry.public_key) > 256 or not KEY_PATTERN.match(tunnel_entry.public_key) \
            or len(tunnel_entry.remote_end) > 64:
        return web.Response(status=412, reason="A value does not match the schema")
    remote_end_split = tunnel_entry.remote_end.split(":")
    if len(remote_end_split) != 2 or not validate_ip_address(remote_end_split[0]) \
            or not validate_port_string(remote_end_split[1]):
        return web.Response(status=412, reason="A value does not match the schema")
    # Check for conflicts
    if tunnel_entry.id in TunnelEntryData.tunnel_entries.keys():
        return web.Response(status=409, reason="Tunnel entry id or specified ports already in use")
    if tunnel_entry.local_port in [x.local_port for x in TunnelEntryData.tunnel_entries.values()]:
        return web.Response(status=409, reason="Tunnel entry id or specified ports already in use")
    # Validate interfaces
    if not check_interface(tunnel_entry.inner_intf) or not check_interface(tunnel_entry.outer_intf):
        return web.Response(status=404, reason="A specified interface could not be found")
    # Add to local state
    TunnelEntryData.tunnel_entries[tunnel_entry.id] = tunnel_entry
    # Deploy to local
    # Steps: Bootstrap new wireguard interface -> install route for wg interface
    wg_intf = "wg"+str(tunnel_entry.local_port)
    if run_command(['ip', 'link', 'add', 'dev', wg_intf, 'type', 'wireguard']) != 0:
        return web.Response(status=500, reason="Internal Server Error")
    if run_command(['sh', '-c', f'\"echo \\\"{tunnel_entry.private_key}\\\"', '>',
                    'pk_wg'+str(tunnel_entry.local_port)]) != 0:
        return web.Response(status=500, reason="Internal Server Error")
    if run_command(['wg', 'set', wg_intf,
                    'listen-port', str(tunnel_entry.local_port),
                    'private-key', './pk_wg'+str(tunnel_entry.local_port),
                    'peer', tunnel_entry.public_key,
                    'allowed-ips', tunnel_entry.inner_subnet,
                    'endpoint', tunnel_entry.remote_end]) != 0:
        return web.Response(status=500, reason="Internal Server Error")
    if run_command(['ip', 'link', 'set', 'dev', wg_intf, 'up']) != 0:
        return web.Response(status=500, reason="Internal Server Error")
    if run_command(['ip', 'route', 'add', tunnel_entry.outer_subnet, 'dev', wg_intf]) != 0:
        return web.Response(status=500, reason="Internal Server Error")
    # Return success
    return web.Response(status=200, reason="The tunnel entry has been created")


def check_interface(intf: str) -> bool:
    # Validate the port first
    if len(intf) > 32 or not INTF_PATTERN.match(intf):
        return False
    # Simply check if the directory for the network interface exists
    return run_command(['test', '-d', '/sys/class/net/'+intf])[0] == 0


def validate_ip_address(ip: str) -> bool:
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def validate_ip_network(net: str) -> bool:
    try:
        ipaddress.ip_network(net)
        return True
    except ValueError:
        return False


def validate_port_string(port: str) -> bool:
    try:
        port = int(port)
        return 0 < port <= MAX_PORT
    except ValueError:
        return False
