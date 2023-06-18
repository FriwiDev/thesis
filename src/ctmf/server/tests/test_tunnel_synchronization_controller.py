# coding: utf-8

import pytest
import json
from aiohttp import web

from ctmf_server.models.tunnel import Tunnel


async def test_tunnel_deployment_delete(client):
    """Test case for tunnel_deployment_delete

    
    """
    params = [('auth', 'auth_example'),
                    ('id', 56)]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/tunnel_deployment',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_tunnel_deployment_get(client):
    """Test case for tunnel_deployment_get

    
    """
    params = [('auth', 'auth_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/tunnel_deployment',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_tunnel_deployment_put(client):
    """Test case for tunnel_deployment_put

    
    """
    params = [('auth', 'auth_example'),
                    ('id', 56)]
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/tunnel_deployment',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_tunnel_reservation_delete(client):
    """Test case for tunnel_reservation_delete

    
    """
    params = [('auth', 'auth_example'),
                    ('id', 56)]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/tunnel_reservation',
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
        path='/tunnel_reservation',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_tunnel_reservation_put(client):
    """Test case for tunnel_reservation_put

    
    """
    params = [('auth', 'auth_example'),
                    ('tunnel', {'key': ctmf_server.Tunnel()})]
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/tunnel_reservation',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

