from aiohttp import web
import importlib


def main():
    app = web.Application()

    subapps = [
        'auth',
    ]

    for subapp_name in subapps:
        subapp_module = importlib.import_module(f'.{subapp_name}', 'src')
        subapp, subapp_middlewares = getattr(subapp_module, 'create_subapp', None)()
        app.add_subapp(f'/{subapp_name}', subapp)
        app.middlewares.extend(subapp_middlewares)

    web.run_app(app)


if __name__ == '__main__':
    main()
