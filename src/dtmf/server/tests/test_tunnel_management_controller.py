# coding: utf-8

import pytest
import json
from aiohttp import web

from dtmf_server.models.tunnel import Tunnel


async def test_tunnel_deployment_delete(client):
    """Test case for tunnel_deployment_delete

    
    """
    params = [('auth', 'auth_example'),
                    ('tunnel_id', 56)]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v1/tunnel_deployment',
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
        path='/v1/tunnel_deployment',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_tunnel_deployment_put(client):
    """Test case for tunnel_deployment_put

    
    """
    params = [('auth', 'auth_example'),
                    ('tunnel_id', 56)]
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v1/tunnel_deployment',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

