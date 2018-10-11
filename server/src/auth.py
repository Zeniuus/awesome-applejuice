from aiohttp import web
import re
import jwt as _jwt
import sqlalchemy as sa

from .models import user
from .utils import data_missing, bad_request_missing_data


@web.middleware
async def auth_middleware(request, handler):
    auth_header = request.headers.get('Authorization', None)
    if auth_header:
        user_detail = _parse_auth_header(auth_header)
        if user:
            request['user'] = user_detail
    return await handler(request)


def _parse_auth_header(auth_header):
    auth_header_regex = re.compile(r'Bearer (?P<jwt>\w+\.\w+\.\w+)')
    match = auth_header_regex.match(auth_header)
    if not match:
        return None
    jwt = match.group('jwt')
    return _jwt.decode(jwt,
                       'applejuice-backend-jwt-secret-key',
                       algorithm='HS256')


async def handle_signin(request):
    body = await request.json()
    mandatory_keys = ['id', 'nickname', 'password']
    if data_missing(mandatory_keys, body):
        return web.Response(text=bad_request_missing_data(mandatory_keys), status=400)
    # TODO: check length of id, nickname, password.
    # TODO: check if duplicate.
    # TODO: encrypt password.
    new_user = {
        'id': body['id'],
        'nickname': body['nickname'],
        'password': body['password'],
    }
    query = (user.insert()
                 .values(new_user))
    request.app['db_engine'].execute(query)
    return web.Response(status=204)


async def handle_login(request):
    body = await request.json()
    mandatory_keys = ['id', 'password']
    if data_missing(mandatory_keys, body):
        return web.Response(text=bad_request_missing_data(mandatory_keys), status=400)
    query = (sa.select('*')
               .select_from(user)
               .where((user.c.id == body['id'])
                      & (user.c.password == body['password'])))
    result = request.app['db_engine'].execute(query)
    row = result.first()
    if not row:
        return web.Response(status=401)
    _, user_id, nickname, password = row
    jwt_byte = _jwt.encode({'id': user_id,
                            'nickname': nickname,
                            'password': password},
                           'applejuice-backend-jwt-secret-key',
                           algorithm='HS256')
    jwt = jwt_byte.decode('utf-8')
    return web.json_response({'jwt': jwt})


async def authenticated_ping(request):
    user_detail = request.get('user', None)
    # TODO: change as a decorator. (@auth_required)
    if not user_detail:
        return web.Response(status=401)
    return web.Response(text='pong')


def create_subapp():
    app = web.Application()
    app.add_routes([web.post('/login', handle_login),
                    web.post('/signin', handle_signin),
                    web.get('/ping', authenticated_ping)])
    return app, [auth_middleware]
