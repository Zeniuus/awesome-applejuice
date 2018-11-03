from aiohttp import web
import pytest

from awesome_applejuice_backend.utils.http import (
    data_missing, validate_body, auth_required)


def test_not_data_missing():
    keys = ['a', 'b']
    body = {'a': 'a', 'b': 'b'}

    assert not data_missing(keys, body)

    keys = ['b']
    body = {'a': 'a', 'b': 'b'}

    assert not data_missing(keys, body)


def test_data_missing():
    keys = ['a', 'b', 'c']
    body = {'a': 'a', 'b': 'b'}

    assert data_missing(keys, body)

    keys = ['c']
    body = {'a': 'a', 'b': 'b'}

    assert data_missing(keys, body)


def test_vaildate_body_not_empty():
    validations = {
        'a': ['not_empty']
    }

    body = {'a': 'a'}
    assert validate_body(body, validations)

    body = {'a': ''}
    assert not validate_body(body, validations)

    body = {'a': []}
    assert not validate_body(body, validations)

    body = {'a': None}
    assert not validate_body(body, validations)

    body = {}
    assert not validate_body(body, validations)


def test_validate_body_number():
    validations = {
        'a': ['number']
    }

    body = {'a': 3}
    assert validate_body(body, validations)

    body = {'a': '3'}
    assert validate_body(body, validations)

    body = {'a': 'a'}
    assert not validate_body(body, validations)

    body = {'a': ''}
    assert not validate_body(body, validations)

    body = {'a': None}
    assert not validate_body(body, validations)

    body = {}
    assert not validate_body(body, validations)


def test_validate_body_invalid_validation_type():
    validations = {
        'a': ['not_implemented']
    }

    body = {'a':'a'}
    with pytest.raises(ValueError):
        validate_body(body, validations)


@pytest.mark.asyncio
async def test_auth_required():

    @auth_required
    async def _dummy_handler(request):
        return 'dummy-response'

    with pytest.raises(web.HTTPUnauthorized):
        await _dummy_handler({})

    res = await _dummy_handler({'user': 'dummy-user'})
    assert res == 'dummy-response'
