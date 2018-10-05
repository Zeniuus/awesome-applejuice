from aiohttp import web
import re
import jwt as _jwt


@web.middleware
async def auth_middleware(request, handler):
    auth_header = request.headers.get('Authorization', None)
    print(auth_header)
    if auth_header:
        user = _parse_auth_header(auth_header)
        if user:
            print('auth')
            request['user'] = user
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


def handle_login(request):
    jwt_byte = _jwt.encode({'name': 'suhwan'},
                           'applejuice-backend-jwt-secret-key',
                           algorithm='HS256')
    jwt = jwt_byte.decode('utf-8')
    return web.json_response({'jwt': jwt})


def authenticated_ping(request):
    user = request.get('user', None)
    if not user:
        return web.Response(status=401)
    return web.Response(text='pong')


def create_subapp():
    app = web.Application()
    app.add_routes([web.get('/login', handle_login),
                    web.get('/ping', authenticated_ping)])
    return app, [auth_middleware]
