# coding: utf-8

import pytest
import json
from aiohttp import web

from switch_server.models.queue import Queue


async def test_queue_delete(client):
    """Test case for queue_delete

    
    """
    params = [('auth', 'auth_example'),
                    ('queue_id', 56),
                    ('port', 'port_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v1/queue',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_queue_put(client):
    """Test case for queue_put

    
    """
    body = switch_server.Queue()
    params = [('auth', 'auth_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/queue',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

