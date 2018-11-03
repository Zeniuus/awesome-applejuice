import aiohttp
import pytest
import sqlalchemy as sa

from awesome_applejuice_backend.subapps.auth import (
    auth_middleware, _parse_auth_header)
from awesome_applejuice_backend.models import user


class MockRequest:
    def __init__(self, **kwargs):
        self._dict = {}

        for key, item in kwargs.items():
            setattr(self, key, item)

    def __setitem__(self, key, value):
        self._dict[key] = value

    def get(self, key, default=None):
        return self._dict.get(key, default)

    def __getitem__(self, key):
        return self._dict[key]

    def __contains__(self, val):
        return val in self._dict


def test__parse_auth_header(auth_header):
    user_detail = _parse_auth_header('fake-auth-header')
    assert user_detail is None

    user_detail = _parse_auth_header(auth_header['Authorization'])
    assert 'id' in user_detail
    assert 'nickname' in user_detail
    assert 'password' in user_detail


@pytest.mark.asyncio
async def test_auth_middleware(auth_header):

    async def _request_proxy_handler(request):
        return request

    headers = {}
    request = MockRequest(headers=headers)
    res = await auth_middleware(request, _request_proxy_handler)

    assert res.get('user', None) is None

    headers.update(auth_header)
    res = await auth_middleware(request, _request_proxy_handler)
    assert 'user' in res
    user = res['user']
    assert 'id' in user
    assert 'nickname' in user
    assert 'password' in user


@pytest.mark.integration
@pytest.mark.asyncio
async def test_authenticated_ping(prepare_app, auth_header):
    async with aiohttp.ClientSession() as session:
        res = await session.get('http://localhost:8080/auth/ping')
        assert res.status == 401

        res = await session.get('http://localhost:8080/auth/ping',
                                headers=auth_header)
        assert res.status == 200
        res_text = await res.text()
        assert res_text == 'pong'


@pytest.mark.integration
@pytest.mark.asyncio
async def test_handle_signup(prepare_app):
    app = prepare_app

    async with aiohttp.ClientSession() as session:
        body = {
            'id': 'test-id',
            'nickname': 'test-nickname',
            'password': 'test-password',
        }
        res = await session.post('http://localhost:8080/auth/signup',
                                 json=body)
        assert res.status == 204
        query = (sa.select('*')
                   .select_from(user)
                   .where(user.c.id == body['id']))
        result = app['db_engine'].execute(query)
        row = result.first()
        assert row is not None


@pytest.mark.integration
@pytest.mark.asyncio
async def test_handle_signin(prepare_app, test_user):
    async with aiohttp.ClientSession() as session:
        body = {
            'id': test_user['id'],
            'password': test_user['password'],
        }
        res = await session.post('http://localhost:8080/auth/signin',
                                 json=body)
        assert res.status == 200
        res_json = await res.json()
        assert res_json.get('id', None) == test_user['id']
        assert res_json.get('nickname', None) == test_user['nickname']
        assert 'jwt' in res_json
