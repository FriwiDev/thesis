from esmf_client.paths.tunnel_reservation.delete import ApiFordelete
from esmf_client.paths.tunnel_reservation.get import ApiForget
from esmf_client.paths.tunnel_reservation.put import ApiForput


class TunnelReservation(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
