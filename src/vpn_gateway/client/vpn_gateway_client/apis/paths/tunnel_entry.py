from vpn_gateway_client.paths.tunnel_entry.get import ApiForget
from vpn_gateway_client.paths.tunnel_entry.put import ApiForput
from vpn_gateway_client.paths.tunnel_entry.delete import ApiFordelete


class TunnelEntry(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
