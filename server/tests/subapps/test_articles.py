import aiohttp
import json
import pytest

from awesome_applejuice_backend.models import board, user, article


@pytest.fixture
async def prepare_articles_test_db(prepare_app):
    app = prepare_app
    query = (board.insert()
                  .values(name='test-board'))
    result = app['db_engine'].execute(query)
    board_id = result.inserted_primary_key[0]

    new_user = {
        'id': 'test-id',
        'nickname': 'test-nickname',
        'password': 'test-password',
    }
    query = (user.insert()
                 .values(new_user))
    result = app['db_engine'].execute(query)
    user_id = result.inserted_primary_key[0]

    yield board_id, user_id

    query = (article.delete())
    app['db_engine'].execute(query)
    query = (board.delete()
                  .where(board.c.row_id == board_id))
    app['db_engine'].execute(query)
    query = (user.delete()
                 .where(user.c.row_id == user_id))
    app['db_engine'].execute(query)


@pytest.mark.integration
@pytest.mark.asyncio
async def test_handle_article_create(prepare_articles_test_db):
    board_id, user_id = prepare_articles_test_db

    async with aiohttp.ClientSession() as session:
        body = {
            'title': 'test-title',
            'board': board_id,
            'content': 'test-content',
            'created_by': user_id,
        }
        res = await session.post('http://localhost:8080/articles/',
                                 data=json.dumps(body).encode())
        assert res.status == 200
        res_json = await res.json()
        assert 'id' in res_json


@pytest.fixture
async def prepare_article(prepare_articles_test_db):
    board_id, user_id = prepare_articles_test_db
    async with aiohttp.ClientSession() as session:
        body = {
            'title': 'test-title',
            'board': board_id,
            'content': 'test-content',
            'created_by': user_id,
        }
        res = await session.post('http://localhost:8080/articles/',
                                 data=json.dumps(body).encode())
        res_json = await res.json()
        return res_json['id'], body


@pytest.mark.integration
@pytest.mark.asyncio
async def test_handle_article_delete(prepare_article):
    article_id, _ = prepare_article

    async with aiohttp.ClientSession() as session:
        res = await session.delete(f'http://localhost:8080/articles/{article_id}')
        assert res.status == 204


@pytest.mark.integration
@pytest.mark.asyncio
async def test_handle_articles_fetch(prepare_article):
    article_id, article_info = prepare_article

    async with aiohttp.ClientSession() as session:
        res = await session.get('http://localhost:8080/articles/')
        assert res.status == 200
        res_json = await res.json()
        assert len(res_json) == 1
        _article = res_json[0]
        assert _article['id'] == article_id
        assert _article['title'] == article_info['title']
        assert _article['board'] == article_info['board']
        assert _article['content'] == article_info['content']
        assert _article['created_by'] == article_info['created_by']


@pytest.mark.integration
@pytest.mark.asyncio
async def test_handle_article_fetch(prepare_article):
    article_id, article_info = prepare_article

    async with aiohttp.ClientSession() as session:
        res = await session.get(f'http://localhost:8080/articles/{article_id}')
        assert res.status == 200
        _article = await res.json()
        assert _article['id'] == article_id
        assert _article['title'] == article_info['title']
        assert _article['board'] == article_info['board']
        assert _article['content'] == article_info['content']
        assert _article['created_by'] == article_info['created_by']


@pytest.mark.integration
@pytest.mark.asyncio
async def test_handle_article_update(prepare_article):
    article_id, article_info = prepare_article

    async with aiohttp.ClientSession() as session:
        body = {
            'title': 'updated-title',
            'content': 'updated-content',
        }
        res = await session.put(f'http://localhost:8080/articles/{article_id}',
                                data=json.dumps(body).encode())
        assert res.status == 204

        res = await session.get(f'http://localhost:8080/articles/{article_id}')
        res_json = await res.json()
        _article = res_json
        assert _article['id'] == article_id
        assert _article['title'] == body['title']
        assert _article['board'] == article_info['board']
        assert _article['content'] == body['content']
        assert _article['created_by'] == article_info['created_by']


