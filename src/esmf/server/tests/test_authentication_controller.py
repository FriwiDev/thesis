# coding: utf-8

import pytest
import json
from aiohttp import web



async def test_auth_put(client):
    """Test case for auth_put

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/auth',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

