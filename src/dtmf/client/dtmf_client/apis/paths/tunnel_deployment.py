from dtmf_client.paths.tunnel_deployment.delete import ApiFordelete
from dtmf_client.paths.tunnel_deployment.get import ApiForget
from dtmf_client.paths.tunnel_deployment.put import ApiForput


class TunnelDeployment(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
