from esmf_client.paths.slice_reservation.get import ApiForget
from esmf_client.paths.slice_reservation.put import ApiForput
from esmf_client.paths.slice_reservation.delete import ApiFordelete


class SliceReservation(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
