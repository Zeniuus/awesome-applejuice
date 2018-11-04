from aiohttp import web
import pytest

from awesome_applejuice_backend.utils.http import auth_required


@pytest.mark.asyncio
async def test_auth_required():

    @auth_required
    async def _dummy_handler(request):
        return 'dummy-response'

    with pytest.raises(web.HTTPUnauthorized):
        await _dummy_handler({})

    res = await _dummy_handler({'user': 'dummy-user'})
    assert res == 'dummy-response'
