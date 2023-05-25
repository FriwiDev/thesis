# coding: utf-8


async def test_slice_delete(client):
    """Test case for slice_delete

    
    """
    params = [('auth', 'auth_example'),
              ('ids', [56])]
    headers = {
    }
    response = await client.request(
        method='DELETE',
        path='/slice',
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
        path='/slice',
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
        path='/slice',
        headers=headers,
        params=params,
    )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')
