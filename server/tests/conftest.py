import aiodocker
from aiohttp import web
import alembic.config
import asyncio
from dynaconf import settings
import importlib
import pytest
import sqlalchemy as sa
import time

from awesome_applejuice_backend.server import init_root_app


def wait_db_ready():
    username = settings.USERNAME
    password = settings.PASSWORD
    host = settings.HOST
    dbname = settings.DBNAME
    db_engine = sa.create_engine(f'mysql+pymysql://{username}:{password}@{host}/{dbname}')
    print('Waiting for DB ready...')
    while True:
        try:
            db_engine.execute('SHOW DATABASES;')
        except sa.exc.OperationalError as e:
            time.sleep(3)
        else:
            print('DB is ready now.')
            break


@pytest.fixture(scope='session', autouse=True)
def create_database():
    docker = aiodocker.Docker()
    container = None

    async def _create_database():
        nonlocal container

        container = await docker.containers.create_or_replace(
            config={
                'ExposedPorts': {
                    '3306/tcp': {},
                },
                'Env': [
                    'MYSQL_ROOT_PASSWORD=04220506',
                    'MYSQL_DATABASE=awesome-applejuice-db',
                ],
                'Image': 'mysql:latest',
                'HostConfig': {
                    'PortBindings': {
                        '3306/tcp': [
                            {
                                'HostPort': '3306'
                            }
                        ]
                    },
                }
            },
            name='test-mysql-db',
        )
        await container.start()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(_create_database())

    wait_db_ready()

    alembic_migration_cmd = ['upgrade', 'head']
    alembic.config.main(argv=alembic_migration_cmd)

    yield

    async def _teardown_database():
        nonlocal container

        await container.delete(force=True)
        await docker.close()

    loop.run_until_complete(_teardown_database())


@pytest.fixture
async def prepare_app():

    app = web.Application()
    init_root_app(app)

    root_app_configs = [
        'db_engine',
    ]

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

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()

    yield app

    await runner.cleanup()
