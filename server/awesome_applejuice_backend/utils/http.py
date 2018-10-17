from aiohttp import web
import functools


def data_missing(keys, body):
    return not all([key in body
                    for key in keys])


# TODO: organize 4xx error messages hierarchically.
def bad_request_missing_data(keys):
    quoted_keys = list(map(lambda x: f'"{x}"', keys))
    return f'Missing key among {", ".join(quoted_keys)}'


def auth_required(handler):
    @functools.wraps(handler)
    async def wrapped_handler(request):
        if 'user' not in request:
            raise web.HTTPUnauthorized
        return await handler(request)
    return wrapped_handler
