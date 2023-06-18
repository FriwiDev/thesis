# coding: utf-8

import pytest
import json
from aiohttp import web

from dsmf_server.models.slice import Slice


async def test_slice_reservation_delete(client):
    """Test case for slice_reservation_delete

    
    """
    params = [('auth', 'auth_example'),
                    ('id', 56)]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/slice_reservation',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_slice_reservation_get(client):
    """Test case for slice_reservation_get

    
    """
    params = [('auth', 'auth_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/slice_reservation',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_slice_reservation_put(client):
    """Test case for slice_reservation_put

    
    """
    params = [('auth', 'auth_example'),
                    ('slice', {'key': dsmf_server.Slice()})]
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/slice_reservation',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

