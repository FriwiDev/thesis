from ctmf_client.paths.tunnel_reservation.delete import ApiFordelete
from ctmf_client.paths.tunnel_reservation.get import ApiForget
from ctmf_client.paths.tunnel_reservation.put import ApiForput


class TunnelReservation(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
