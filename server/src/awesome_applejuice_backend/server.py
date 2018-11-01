from aiohttp import web
from dynaconf import settings
import importlib
import sqlalchemy as sa
import aiohttp_cors


root_app_configs = [
    'db_engine',
]


# TODO: flake8 test
# TODO: travis-ci integration


def init_root_app(app):
    username = settings.USERNAME
    password = settings.PASSWORD
    host = settings.HOST
    dbname = settings.DBNAME
    app['db_engine'] = sa.create_engine(f'mysql+pymysql://{username}:{password}@{host}/{dbname}')


def main():
    # TODO: maybe change into coroutine?
    app = web.Application()
    init_root_app(app)

    # TODO: subapps auto-detection
    # TODO: maybe change name to "routes"?
    subapps = [
        'auth',
        'articles',
        'orders',
    ]

    for subapp_name in subapps:
        subapp_module = importlib.import_module(f'.{subapp_name}', 'awesome_applejuice_backend.subapps')
        subapp, subapp_middlewares = getattr(subapp_module, 'create_subapp', None)()
        app.add_subapp(f'/{subapp_name}', subapp)
        app.middlewares.extend(subapp_middlewares)
        for config in root_app_configs:
            subapp[config] = app[config]

    cors = aiohttp_cors.setup(app, defaults={
        '*': aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers='*',
                allow_headers='*',
            )
    })
    for route in list(app.router.routes()):
        cors.add(route)

    web.run_app(app)


if __name__ == '__main__':
    main()
