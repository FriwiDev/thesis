from dtmf_client.paths.tunnel_deployment.get import ApiForget
from dtmf_client.paths.tunnel_deployment.put import ApiForput
from dtmf_client.paths.tunnel_deployment.delete import ApiFordelete


class TunnelDeployment(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
