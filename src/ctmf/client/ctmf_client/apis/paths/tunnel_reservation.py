from ctmf_client.paths.tunnel_reservation.get import ApiForget
from ctmf_client.paths.tunnel_reservation.put import ApiForput
from ctmf_client.paths.tunnel_reservation.delete import ApiFordelete


class TunnelReservation(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
