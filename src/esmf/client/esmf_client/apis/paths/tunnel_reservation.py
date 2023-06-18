from esmf_client.paths.tunnel_reservation.get import ApiForget
from esmf_client.paths.tunnel_reservation.put import ApiForput
from esmf_client.paths.tunnel_reservation.delete import ApiFordelete


class TunnelReservation(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
