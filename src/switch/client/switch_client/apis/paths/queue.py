from switch_client.paths.queue.delete import ApiFordelete
from switch_client.paths.queue.put import ApiForput


class Queue(
    ApiForput,
    ApiFordelete,
):
    pass
