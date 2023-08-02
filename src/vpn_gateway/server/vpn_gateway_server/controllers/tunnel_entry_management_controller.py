import ipaddress
import json
import pprint
import re
from typing import List, Dict
from aiohttp import web

from vpn_gateway_server.command_util import run_command
from vpn_gateway_server.controllers.authentication_controller import check_auth
from vpn_gateway_server.models import TunnelEntryMatchesInner
from vpn_gateway_server.models.tunnel_entry import TunnelEntry
from vpn_gateway_server import util

INTF_PATTERN = re.compile("[A-Za-z0-9_-]+")
KEY_PATTERN = re.compile("[A-Za-z0-9/\\+=]+")
MAC_PATTERN = re.compile("[0-9A-Fa-f][0-9A-Fa-f]:[0-9A-Fa-f][0-9A-Fa-f]:[0-9A-Fa-f][0-9A-Fa-f]"
                         ":[0-9A-Fa-f][0-9A-Fa-f]:[0-9A-Fa-f][0-9A-Fa-f]:[0-9A-Fa-f][0-9A-Fa-f]")

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
    ret = apply_routing(None, tunnel_entry, wg_intf)
    if ret != 200:
        return web.Response(status=500, reason="Internal Server Error")
    # Delete the tunnel entry from our local deployment
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
    return web.Response(status=200, content_type="application/json", body=json.dumps([json.dumps(e.to_dict()) for e in TunnelEntryData.tunnel_entries.values()]))


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
    # Validate matches
    for match in tunnel_entry.matches:
        if not match.transport_protocol or (match.transport_protocol != "UDP" and match.transport_protocol != "TCP"):
            return web.Response(status=412, reason="A value does not match the schema")
        if match.source_ip and not validate_ip_address(match.source_ip):
            return web.Response(status=412, reason="A value does not match the schema")
        if match.target_ip and not validate_ip_address(match.target_ip):
            return web.Response(status=412, reason="A value does not match the schema")
        if match.source_mac and not check_mac(match.source_mac):
            return web.Response(status=412, reason="A value does not match the schema")
        if match.source_port and (match.source_port < 0 or match.source_port > MAX_PORT):
            return web.Response(status=412, reason="A value does not match the schema")
        if match.target_port and (match.target_port < 0 or match.target_port > MAX_PORT):
            return web.Response(status=412, reason="A value does not match the schema")
    # Check for conflicts -> apply routing again if conflict
    wg_intf = "wg" + str(tunnel_entry.local_port)
    if tunnel_entry.tunnel_entry_id in TunnelEntryData.tunnel_entries.keys():
        old = TunnelEntryData.tunnel_entries[tunnel_entry.tunnel_entry_id]
        if tunnel_entry.inner_subnet != old.inner_subnet \
                or tunnel_entry.local_port != old.local_port or tunnel_entry.remote_end != old.remote_end \
                or tunnel_entry.private_key != old.private_key or tunnel_entry.public_key != old.public_key:
            return web.Response(status=409, reason="A tunnel entry with this id already exists and information "
                                                   "apart from match entries was changed.")
        ret = apply_routing(tunnel_entry, old, wg_intf)
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
    key_file = open("pk_wg"+str(tunnel_entry.local_port), "w")
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
    # Apply routing
    # if run_command(['ip', 'route', 'add', 'default', 'dev', wg_intf, 'table', str(tunnel_entry.tunnel_entry_id)])[0] != 0:
    #     return web.Response(status=500, reason="Internal Server Error")
    ret = apply_routing(tunnel_entry, None, wg_intf)
    if ret == 200:
        return web.Response(status=201, reason="The tunnel entry has been created")
    else:
        return web.Response(status=500, reason="Internal Server Error")


def apply_routing(new: TunnelEntry or None, old: TunnelEntry or None, wg_intf: str) -> int:
    # Build match deltas
    add: [TunnelEntryMatchesInner] = []
    remove: [TunnelEntryMatchesInner] = []
    if not old:
        add = new.matches.copy()
        # if run_command(['ip', 'rule', 'add', 'fwmark', str(new.tunnel_entry_id), 'lookup', str(new.tunnel_entry_id)])[0] != 0:
        #     return 500
    elif not new:
        remove = old.matches.copy()
        # if run_command(['ip', 'rule', 'del', 'fwmark', str(old.tunnel_entry_id), 'lookup', str(old.tunnel_entry_id)])[0] != 0:
        #     return 500
    else:
        for n in new.matches:
            if n not in old.matches:
                add.append(n)
        for o in old.matches:
            if o not in new.matches:
                remove.append(o)
    # Remove entries not applicable anymore
    for match in remove:
        ret = deploy_iptables_rule(tunnel_entry_id=old.tunnel_entry_id, match=match, add=False, wg_intf=wg_intf)
        if ret != 200:
            return ret
    # Add new entries
    for match in add:
        ret = deploy_iptables_rule(tunnel_entry_id=new.tunnel_entry_id, match=match, add=True, wg_intf=wg_intf)
        if ret != 200:
            return ret
    # Return success
    return 200


def deploy_iptables_rule(tunnel_entry_id: int, match: TunnelEntryMatchesInner, add: bool, wg_intf: str) -> int:
    # Build iptables command
    cmd = ['iptables', # '-t', 'mangle',
           '-A' if add else '-D', 'FORWARD']
    # Append source and destination ip
    if match.source_ip:
        cmd.append("-s")
        cmd.append(match.source_ip)
    if match.target_ip:
        cmd.append("-d")
        cmd.append(match.target_ip)
    # Append mac
    if match.source_mac:
        cmd.append("-m")
        cmd.append("mac")
        cmd.append("--mac-source")
        cmd.append(match.source_mac)
    # Append protocol
    cmd.append("-p")
    cmd.append(match.transport_protocol.lower())
    # Append ports
    if match.source_port and match.source_port != 0:
        cmd.append("--sport")
        cmd.append(str(match.source_port))
    if match.target_port and match.target_port != 0:
        cmd.append("--dport")
        cmd.append(str(match.target_port))
    # Set output port to our wg port
    cmd.append("-o")
    cmd.append(wg_intf)
    # Append mark
    cmd.append("-j")
    cmd.append("ACCEPT")
    # cmd.append("MARK")
    # cmd.append("--set-mark")
    # cmd.append(str(tunnel_entry_id))
    if run_command(cmd)[0] != 0:
        return 500
    return 200

def check_mac(mac: str) -> bool:
    # Validate pattern
    return mac and not len(mac) > 17 and MAC_PATTERN.match(mac)


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
