from jump_host_client.paths.tunnel_entry.get import ApiForget
from jump_host_client.paths.tunnel_entry.put import ApiForput
from jump_host_client.paths.tunnel_entry.delete import ApiFordelete


class TunnelEntry(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
