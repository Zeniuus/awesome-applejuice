from aiohttp import web
import importlib
import sqlalchemy as sa


root_app_configs = [
    'db_engine',
]


def init_root_app(app):
    # TODO: move configs to config file and .gitignore it.
    username = 'root'
    password = '04220506'
    host = 'localhost:3306'
    dbname = 'awesome-applejuice-db'
    app['db_engine'] = sa.create_engine(f'mysql+pymysql://{username}:{password}@{host}/{dbname}')
    # TODO: use docker-compose to setup MySQL DB container.


def main():
    # TODO: maybe change into coroutine?
    app = web.Application()
    init_root_app(app)

    subapps = [
        'auth',
    ]

    for subapp_name in subapps:
        subapp_module = importlib.import_module(f'.{subapp_name}', 'awesome_applejuice_backend')
        subapp, subapp_middlewares = getattr(subapp_module, 'create_subapp', None)()
        app.add_subapp(f'/{subapp_name}', subapp)
        app.middlewares.extend(subapp_middlewares)
        for config in root_app_configs:
            subapp[config] = app[config]

    web.run_app(app)


if __name__ == '__main__':
    main()

# TODO: dockerize application.
