import re
from typing import List, Dict
from aiohttp import web

from switch_server.command_util import run_command
from switch_server.controllers.authentication_controller import check_auth
from switch_server.models.queue import Queue

MAX_QUEUE = 65535
MAX_RATE = 1000000000000
MAX_PRIORITY = 65535
PORT_PATTERN = re.compile("([A-Z][a-z][0-9]_-)*")


class QueueData:
    current_queue_id = 1
    queues: dict[int, Queue] = {}


async def queue_delete(request: web.Request, auth, queue_id, port) -> web.Response:
    """queue_delete

    Deletes a queue

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param id: The id of the queue to be deleted.
    :type id: int
    :param port: The switch port of the queue to be deleted.
    :type port: str

    """
    if not check_auth(auth):
        return web.Response(status=403, reason="Invalid authentication provided.")
    if queue_id not in QueueData.queues:
        return web.Response(status=404, reason="The queue could not be found.")
    queue = QueueData.queues[queue_id]
    if queue.port != port:
        return web.Response(status=404, reason="The queue could not be found.")
    del QueueData.queues[queue_id]
    flush_queues(queue.port)
    return web.Response(status=200, reason="The queue was successfully deleted.")


async def queue_put(request: web.Request, auth, body=None) -> web.Response:
    """queue_put

    Creates a new queue

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param queue: The queue to create. The id will be set by the service.
    :type queue: dict | bytes

    """
    if not check_auth(auth):
        return web.Response(status=403, reason="Invalid authentication provided.")
    if not body:
        return web.Response(status=400, reason="No body provided.")
    if QueueData.current_queue_id >= MAX_QUEUE:
        return web.Response(status=507, reason="Already too many queues in use.")
    queue = Queue.from_dict(body)
    if queue.min_rate > MAX_RATE or queue.max_rate > MAX_RATE \
            or queue.burst_rate > MAX_RATE or queue.priority > MAX_PRIORITY \
            or queue.min_rate <= 0 or queue.max_rate <= 0 \
            or queue.burst_rate <= 0 or queue.priority <= 0:
        return web.Response(status=406, reason="A value exceeds the allowed range")
    if not check_port(queue.port):
        return web.Response(status=404, reason="The switch port could not be found")
    queue.queue_id = QueueData.current_queue_id
    QueueData.queues[QueueData.current_queue_id] = queue
    QueueData.current_queue_id += 1
    flush_queues(queue.port)
    return web.Response(status=200, content_type="application/json", body=queue.to_str())


def flush_queues(port: str):
    cmd = ['ovs-vsctl', 'set', 'port', port, 'qos=@newqos', '--', '--id=@newqos', 'create', 'qos', 'type=linux-htb']
    for queue in QueueData.queues.values():
        if queue.port == port:
            cmd += ['queues:' + str(queue.queue_id) + "=@queue" + str(queue.queue_id)]
    for queue in QueueData.queues.values():
        if queue.port == port:
            cmd += ['--', '--id=@queue' + str(queue.queue_id), 'create', 'queue',
                    'other-config:min-rate=' + str(queue.min_rate),
                    'other-config:max-rate=' + str(queue.max_rate),
                    'other-config:burst=' + str(queue.burst_rate),
                    'other-config:priority=' + str(queue.priority)]
    run_command(cmd)


def check_port(port: str) -> bool:
    # Validate the port first
    if len(port) > 32 or not PORT_PATTERN.match(port):
        return False
    # Simply check if the list port command returns a zero exit code
    return run_command(['ovs-vsctl', 'list', 'port', port])[0] == 0
