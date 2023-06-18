from dsmf_client.paths.slice_deployment.get import ApiForget
from dsmf_client.paths.slice_deployment.put import ApiForput
from dsmf_client.paths.slice_deployment.delete import ApiFordelete


class SliceDeployment(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
