from dsmf_client.paths.tunnel_deployment.delete import ApiFordelete
from dsmf_client.paths.tunnel_deployment.get import ApiForget
from dsmf_client.paths.tunnel_deployment.put import ApiForput


class TunnelDeployment(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
