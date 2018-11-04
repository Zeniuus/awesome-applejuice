from aiohttp import web
import functools


def auth_required(handler):
    @functools.wraps(handler)
    async def wrapped_handler(request):
        if 'user' not in request:
            raise web.HTTPUnauthorized
        return await handler(request)
    return wrapped_handler
