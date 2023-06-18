# coding: utf-8

import pytest
import json
from aiohttp import web



async def test_policy_put(client):
    """Test case for policy_put

    
    """
    params = [('auth', 'auth_example'),
                    ('port', 'port_example'),
                    ('ingress_policing_rate', 56),
                    ('ingress_policing_burst', 56)]
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/policy',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

