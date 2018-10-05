from aiohttp import web


def handle_login(request):
    return web.Response(status=204)


def create_subapp():
    app = web.Application()
    app.add_routes([web.get('/login', handle_login)])
    return app, []
