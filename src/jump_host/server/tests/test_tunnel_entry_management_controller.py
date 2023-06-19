# coding: utf-8

import pytest
import json
from aiohttp import web

from jump_host_server.models.tunnel_entry import TunnelEntry


async def test_tunnel_entry_delete(client):
    """Test case for tunnel_entry_delete

    
    """
    params = [('auth', 'auth_example'),
                    ('tunnel_entry_id', 56)]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v1/tunnel_entry',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_tunnel_entry_get(client):
    """Test case for tunnel_entry_get

    
    """
    params = [('auth', 'auth_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/tunnel_entry',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_tunnel_entry_put(client):
    """Test case for tunnel_entry_put

    
    """
    body = jump_host_server.TunnelEntry()
    params = [('auth', 'auth_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/tunnel_entry',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

