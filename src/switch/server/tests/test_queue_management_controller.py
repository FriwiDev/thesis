# coding: utf-8

import pytest
import json
from aiohttp import web

from switch_server.models.queue import Queue


async def test_queue_delete(client):
    """Test case for queue_delete

    
    """
    params = [('auth', 'auth_example'),
                    ('id', 56),
                    ('port', 'port_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/queue',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_queue_put(client):
    """Test case for queue_put

    
    """
    params = [('auth', 'auth_example'),
                    ('queue', {'key': switch_server.Queue()})]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/queue',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

