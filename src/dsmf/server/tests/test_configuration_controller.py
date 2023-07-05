# coding: utf-8

import pytest
import json
from aiohttp import web

from dsmf_server.models.domain_configuration import DomainConfiguration


async def test_configuration_get(client):
    """Test case for configuration_get

    
    """
    params = [('auth', 'auth_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/configuration',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_configuration_put(client):
    """Test case for configuration_put

    
    """
    body = dsmf_server.DomainConfiguration()
    params = [('auth', 'auth_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/configuration',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

