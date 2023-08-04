import ipaddress
import json
import pprint
import re
from typing import List, Dict
from aiohttp import web

from vpn_gateway_server.command_util import run_command
from vpn_gateway_server.controllers.authentication_controller import check_auth
from vpn_gateway_server.models import TunnelEntryIngressMatchesInner, TunnelEntryEgressMatchesInner
from vpn_gateway_server.models.tunnel_entry import TunnelEntry

INTF_PATTERN = re.compile("[A-Za-z0-9_-]+")
KEY_PATTERN = re.compile("[A-Za-z0-9/\\+=]+")

MAX_TUNNEL_ID = 65535
MAX_PORT = 65535


class TunnelEntryData:
    tunnel_entries: Dict[int, TunnelEntry] = {}


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
    # Remove from local impl
    del TunnelEntryData.tunnel_entries[tunnel_entry_id]
    # Delete routing
    wg_intf = "wg" + str(tunnel_entry.local_port)
    tun_intf = "tun" + str(tunnel_entry.local_port)
    ret = apply_routing(None, tunnel_entry, tun_intf)
    if ret != 200:
        return web.Response(status=500, reason="Internal Server Error")
    # Delete the tunnel entry from our local deployment
    if run_command(['ip', 'link', 'del', 'dev', tun_intf])[0] != 0:
        return web.Response(status=500, reason="Internal Server Error")
    if run_command(['ip', 'link', 'del', 'dev', wg_intf])[0] != 0:
        return web.Response(status=500, reason="Internal Server Error")
    if run_command(['rm', '-f', 'pk_wg' + str(tunnel_entry.local_port)])[0] != 0:
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
    return web.Response(status=200, content_type="application/json",
                        body=json.dumps([json.dumps(e.to_dict()) for e in TunnelEntryData.tunnel_entries.values()]))


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
    if tunnel_entry.tunnel_entry_id < 0 or tunnel_entry.tunnel_entry_id > MAX_TUNNEL_ID \
            or tunnel_entry.local_port <= 0 or tunnel_entry.local_port > MAX_PORT:
        return web.Response(status=406, reason="A value exceeds the allowed range")
    # Validate subnets, remote end and keys
    if not validate_ip_network(tunnel_entry.inner_subnet) \
            or len(tunnel_entry.private_key) > 256 or not KEY_PATTERN.match(tunnel_entry.private_key) \
            or len(tunnel_entry.public_key) > 256 or not KEY_PATTERN.match(tunnel_entry.public_key) \
            or len(tunnel_entry.remote_end) > 64:
        return web.Response(status=412, reason="A value does not match the schema")
    remote_end_split = tunnel_entry.remote_end.split(":")
    if len(remote_end_split) != 2 or not validate_ip_address(remote_end_split[0]) \
            or not validate_port_string(remote_end_split[1]):
        return web.Response(status=412, reason="A value does not match the schema")
    if not tunnel_entry.local_tunnel_ip or not validate_ip_address(tunnel_entry.local_tunnel_ip):
        return web.Response(status=412, reason="A value does not match the schema")
    if not tunnel_entry.remote_tunnel_ip or not validate_ip_address(tunnel_entry.remote_tunnel_ip):
        return web.Response(status=412, reason="A value does not match the schema")
    # Validate ingress matches
    for match in tunnel_entry.ingress_matches:
        if not match.intf_name or not check_interface(match.intf_name):
            return web.Response(status=412, reason="A value does not match the schema")
        if not match.slice_id or match.slice_id < 0 or match.slice_id > MAX_TUNNEL_ID:
            return web.Response(status=412, reason="A value does not match the schema")
    # Check for conflicts -> apply routing again if conflict
    wg_intf = "wg" + str(tunnel_entry.local_port)
    tun_intf = "tun" + str(tunnel_entry.local_port)
    if tunnel_entry.tunnel_entry_id in TunnelEntryData.tunnel_entries.keys():
        old = TunnelEntryData.tunnel_entries[tunnel_entry.tunnel_entry_id]
        if (tunnel_entry.inner_subnet != old.inner_subnet
                or tunnel_entry.local_port != old.local_port or tunnel_entry.remote_end != old.remote_end
                or tunnel_entry.private_key != old.private_key or tunnel_entry.public_key != old.public_key
                or tunnel_entry.local_tunnel_ip != old.local_tunnel_ip
                or tunnel_entry.remote_tunnel_ip != old.remote_tunnel_ip):
            return web.Response(status=409, reason="A tunnel entry with this id already exists and information "
                                                   "apart from match entries was changed.")
        ret = apply_routing(tunnel_entry, old, tun_intf)
        TunnelEntryData.tunnel_entries[tunnel_entry.tunnel_entry_id] = tunnel_entry
        if ret == 200:
            return web.Response(status=202, reason="The tunnel entry has been updated")
        else:
            return web.Response(status=500, reason="Internal Server Error")
    if tunnel_entry.local_port in [x.local_port for x in TunnelEntryData.tunnel_entries.values()]:
        return web.Response(status=409, reason="Tunnel entry id or specified ports already in use")
    # Add to local impl
    TunnelEntryData.tunnel_entries[tunnel_entry.tunnel_entry_id] = tunnel_entry
    # Deploy to local
    # Steps: Bootstrap new wireguard interface -> install route for wg interface
    if run_command(['ip', 'link', 'add', 'dev', wg_intf, 'type', 'wireguard'])[0] != 0:
        return web.Response(status=500, reason="Internal Server Error")
    # Write key file
    key_file = open("pk_wg" + str(tunnel_entry.local_port), "w")
    key_file.write(tunnel_entry.private_key)
    key_file.close()
    if run_command(['wg', 'set', wg_intf,
                    'listen-port', str(tunnel_entry.local_port),
                    'private-key', './pk_wg' + str(tunnel_entry.local_port),
                    'peer', tunnel_entry.public_key,
                    'allowed-ips', tunnel_entry.inner_subnet,
                    'endpoint', tunnel_entry.remote_end])[0] != 0:
        return web.Response(status=500, reason="Internal Server Error")
    if run_command(['ip', 'link', 'set', 'dev', wg_intf, 'up'])[0] != 0:
        return web.Response(status=500, reason="Internal Server Error")
    if run_command(['ip', 'addr', 'add', str(tunnel_entry.local_tunnel_ip), 'dev', wg_intf])[0] != 0:
        return web.Response(status=500, reason="Internal Server Error")
    if run_command(['ip', 'route', 'add', str(tunnel_entry.remote_tunnel_ip), 'dev', wg_intf])[0] != 0:
        return web.Response(status=500, reason="Internal Server Error")
    # Install a gretap (L2) tunnel through our wireguard tunnel
    if run_command(['ip', 'link', 'add', tun_intf, 'type', 'gretap',
                    'remote', str(tunnel_entry.remote_tunnel_ip),
                    'local', str(tunnel_entry.local_tunnel_ip),
                    'dev', wg_intf])[0] != 0:
        return web.Response(status=500, reason="Internal Server Error")
    if run_command(['ip', 'link', 'set', 'dev', tun_intf, 'up'])[0] != 0:
        return web.Response(status=500, reason="Internal Server Error")
    # Apply routing as normal
    ret = apply_routing(tunnel_entry, None, tun_intf)
    if ret == 200:
        return web.Response(status=201, reason="The tunnel entry has been created")
    else:
        return web.Response(status=500, reason="Internal Server Error")


def apply_routing(new: TunnelEntry or None, old: TunnelEntry or None, tun_intf: str) -> int:
    # Build match deltas
    ingress_add: [TunnelEntryIngressMatchesInner] = []
    ingress_remove: [TunnelEntryIngressMatchesInner] = []
    egress_add: [TunnelEntryEgressMatchesInner] = []
    egress_remove: [TunnelEntryEgressMatchesInner] = []
    if not old:
        ingress_add = new.ingress_matches.copy()
        egress_add = new.egress_matches.copy()
    elif not new:
        ingress_remove = old.ingress_matches.copy()
        egress_remove = old.egress_matches.copy()
    else:
        for n in new.ingress_matches:
            if n not in old.ingress_matches:
                ingress_add.append(n)
        for o in old.ingress_matches:
            if o not in new.ingress_matches:
                ingress_remove.append(o)

        for n in new.egress_matches:
            if n not in old.egress_matches:
                egress_add.append(n)
        for o in old.egress_matches:
            if o not in new.egress_matches:
                egress_remove.append(o)
    # Remove entries not applicable anymore
    for match in ingress_remove:
        if run_command(['tc', 'filter', 'del', 'dev', match.intf_name, 'root', 'prio', str(match.slice_id)])[0] != 0:
            return 500
    for match in egress_remove:
        if run_command(['tc', 'filter', 'del', 'dev', tun_intf, 'root', 'prio', str(match.slice_id)])[0] != 0:
            return 500
    # Add new entries
    for match in ingress_add:
        # We do not check result of qdisc creation bc it might exist
        run_command(['tc', 'qdisc', 'add', 'dev', match.intf_name, 'ingress'])
        if run_command(['tc', 'filter', 'add', 'dev', match.intf_name, 'ingress',
                        'prio', str(match.slice_id),
                        'protocol', '0x8847',
                        'flower', 'mpls_label', str(match.slice_id),
                        'action', 'mirred', 'egress', 'redirect',
                        'dev', tun_intf])[0] != 0:
            return 500
    for match in egress_add:
        # We do not check result of qdisc creation bc it might exist
        run_command(['tc', 'qdisc', 'add', 'dev', tun_intf, 'ingress'])
        if run_command(['tc', 'filter', 'add', 'dev', tun_intf, 'ingress',
                        'prio', str(match.slice_id),
                        'protocol', '0x8847',
                        'flower', 'mpls_label', str(match.slice_id),
                        'action', 'mirred', 'egress', 'redirect',
                        'dev', match.intf_name])[0] != 0:
            return 500
    # Return success
    return 200


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


def check_interface(port: str) -> bool:
    # Validate the port first
    if len(port) > 32 or not INTF_PATTERN.match(port):
        return False
    # Simply check if the show link command returns a zero exit code
    return run_command(['ip', 'link', 'show', port])[0] == 0
