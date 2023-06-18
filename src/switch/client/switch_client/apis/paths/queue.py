from switch_client.paths.queue.put import ApiForput
from switch_client.paths.queue.delete import ApiFordelete


class Queue(
    ApiForput,
    ApiFordelete,
):
    pass
