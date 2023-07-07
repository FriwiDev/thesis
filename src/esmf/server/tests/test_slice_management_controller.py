# coding: utf-8

import pytest
import json
from aiohttp import web

from esmf_server.models.slice import Slice


async def test_slice_delete(client):
    """Test case for slice_delete

    
    """
    params = [('auth', 'auth_example'),
                    ('slice_ids', [56])]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v1/slice',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_slice_get(client):
    """Test case for slice_get

    
    """
    params = [('auth', 'auth_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/slice',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_slice_put(client):
    """Test case for slice_put

    
    """
    params = [('auth', 'auth_example'),
                    ('slices', [esmf_server.Slice()])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/slice',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

