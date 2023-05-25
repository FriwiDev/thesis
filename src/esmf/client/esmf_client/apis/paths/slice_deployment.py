from esmf_client.paths.slice_deployment.delete import ApiFordelete
from esmf_client.paths.slice_deployment.get import ApiForget
from esmf_client.paths.slice_deployment.put import ApiForput


class SliceDeployment(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
