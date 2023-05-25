from esmf_client.paths.slice.delete import ApiFordelete
from esmf_client.paths.slice.get import ApiForget
from esmf_client.paths.slice.put import ApiForput


class Slice(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
