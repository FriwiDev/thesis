# coding: utf-8

import pytest
import json
from aiohttp import web

from dsmf_server.models.slice import Slice


async def test_slice_reservation_delete(client):
    """Test case for slice_reservation_delete

    
    """
    params = [('auth', 'auth_example'),
                    ('slice_id', 56)]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v1/slice_reservation',
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
        path='/v1/slice_reservation',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_slice_reservation_put(client):
    """Test case for slice_reservation_put

    
    """
    body = dsmf_server.Slice()
    params = [('auth', 'auth_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/slice_reservation',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

