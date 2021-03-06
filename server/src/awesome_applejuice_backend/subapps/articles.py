from aiohttp import web
from pyvalidator import validate, field, InvalidInputError
import sqlalchemy as sa

from awesome_applejuice_backend.models import article, ArticleSerializer


async def handle_articles_fetch(request):
    query = (sa.select('*')
               .select_from(article))
    result = request.app['db_engine'].execute(query)
    articles = list(result)
    return web.json_response(ArticleSerializer.as_dict(articles))


async def handle_article_create(request):
    body = await request.json()
    try:
        validate(body, {
            'title': field.String(),
            'board': field.Integer(nonnegative=True),
            'content': field.String(),
            'created_by': field.Integer(nonnegative=True)
        })
    except InvalidInputError as e:
        return web.Response(text=str(e), status=400)
    # TODO: validate inputs.
    new_article = {
        'title': body['title'],
        'board': body['board'],
        'content': body['content'],
        'created_by': body['created_by'],
    }
    query = (article.insert()
                    .values(new_article))
    result = request.app['db_engine'].execute(query)
    article_id = result.inserted_primary_key
    if not article_id:
        return web.Response(status=500)
    return web.json_response({'id': article_id[0]})


async def handle_article_fetch(request):
    try:
        article_id = int(request.match_info['id'])
    except ValueError:
        return web.Response(text=f'Invalid article id: {article_id}',
                            status=400)
    query = (sa.select('*')
               .select_from(article)
               .where(article.c.row_id == article_id))
    result = request.app['db_engine'].execute(query)
    _article = result.first()
    return web.json_response(ArticleSerializer.as_dict(_article))


async def handle_article_update(request):
    try:
        article_id = int(request.match_info['id'])
    except ValueError:
        return web.Response(text=f'Invalid article id: {article_id}',
                            status=400)
    # TODO: validate inputs.
    body = await request.json()
    article_update = {key: body[key]
                      for key in ['title', 'board', 'content']
                      if key in body.keys()}
    query = (article.update()
                    .values(**article_update)
                    .where(article.c.row_id == article_id))
    result = request.app['db_engine'].execute(query)
    if not result.rowcount:
        return web.Response(text=f'Requested article does not exist: {article_id}',
                            status=400)
    return web.json_response(None, status=204)


async def handle_article_delete(request):
    try:
        article_id = int(request.match_info['id'])
    except ValueError:
        return web.Response(text=f'Invalid article id: {article_id}',
                            status=400)
    query = (article.delete()
                    .where(article.c.row_id == article_id))
    result = request.app['db_engine'].execute(query)
    if not result.rowcount:
        return web.Response(text=f'Requested article does not exist: {article_id}',
                            status=400)
    return web.json_response(None, status=204)


def create_subapp():
    app = web.Application()
    app.add_routes([web.get('/', handle_articles_fetch),
                    web.post('/', handle_article_create),
                    web.get(r'/{id:\d+}', handle_article_fetch),
                    web.put(r'/{id:\d+}', handle_article_update),
                    web.delete(r'/{id:\d+}', handle_article_delete)])
    return app, []
