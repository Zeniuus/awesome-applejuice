from aiohttp import web
import jwt as _jwt
from pyvalidator import validate, field, InvalidInputError
import re
import sqlalchemy as sa

from awesome_applejuice_backend.models import user


@web.middleware
async def auth_middleware(request, handler):
    auth_header = request.headers.get('Authorization', None)
    if auth_header:
        user_detail = _parse_auth_header(auth_header)
        if user_detail:
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


async def handle_signup(request):
    body = await request.json()
    try:
        validate(body, {
            'id': field.String(length=30),
            'nickname': field.String(length=32),
            'password': field.String(length=32),
        })
    except InvalidInputError as e:
        return web.Response(text=str(e), status=400)
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


async def handle_signin(request):
    body = await request.json()
    try:
        validate(body, {
            'id': field.String(),
            'password': field.String(),
        })
    except InvalidInputError as e:
        return web.Response(text=str(e), status=400)
    query = (sa.select('*')
               .select_from(user)
               .where((user.c.id == body['id'])
                      & (user.c.password == body['password'])))
    result = request.app['db_engine'].execute(query)
    row = result.first()
    if not row:
        return web.Response(status=401)
    _, user_id, nickname, password = row
    # TODO: get rid of password field from jwt token.
    jwt_byte = _jwt.encode({'id': user_id,
                            'nickname': nickname,
                            'password': password},
                           'applejuice-backend-jwt-secret-key',
                           algorithm='HS256')
    jwt = jwt_byte.decode('utf-8')
    return web.json_response({'id': user_id,
                              'nickname': nickname,
                              'jwt': jwt})


async def authenticated_ping(request):
    user_detail = request.get('user', None)
    # TODO: change as a decorator. (@auth_required)
    if not user_detail:
        return web.Response(status=401)
    return web.Response(text='pong')


def create_subapp():
    app = web.Application()
    app.add_routes([web.post('/signup', handle_signup),
                    web.post('/signin', handle_signin),
                    web.get('/ping', authenticated_ping)])
    return app, [auth_middleware]
