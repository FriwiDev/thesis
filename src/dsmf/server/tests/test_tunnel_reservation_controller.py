# coding: utf-8

import pytest
import json
from aiohttp import web

from dsmf_server.models.tunnel import Tunnel


async def test_tunnel_reservation_delete(client):
    """Test case for tunnel_reservation_delete

    
    """
    params = [('auth', 'auth_example'),
                    ('tunnel_id', 56)]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v1/tunnel_reservation',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_tunnel_reservation_get(client):
    """Test case for tunnel_reservation_get

    
    """
    params = [('auth', 'auth_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/tunnel_reservation',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_tunnel_reservation_put(client):
    """Test case for tunnel_reservation_put

    
    """
    body = dsmf_server.Tunnel()
    params = [('auth', 'auth_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/tunnel_reservation',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

