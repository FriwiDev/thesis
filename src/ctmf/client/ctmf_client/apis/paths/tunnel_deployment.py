from ctmf_client.paths.tunnel_deployment.delete import ApiFordelete
from ctmf_client.paths.tunnel_deployment.get import ApiForget
from ctmf_client.paths.tunnel_deployment.put import ApiForput


class TunnelDeployment(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
