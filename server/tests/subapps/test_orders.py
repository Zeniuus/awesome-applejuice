import aiohttp
import pytest

from awesome_applejuice_backend.models import order


@pytest.mark.integration
@pytest.mark.asyncio
async def test_handle_order_create(prepare_app):
    async with aiohttp.ClientSession() as session:
        body = {
            'sender_name': 'test-sender-name',
            'amount': 3,
            'receiver_name': 'test-receiver-name',
            'receiver_phone': '01000000000',
            'receiver_addr': 'test-receiver-addr'
        }
        res = await session.post('http://localhost:8080/orders/',
                                 json=body)
        assert res.status == 200
        res_json = await res.json()
        assert 'id' in res_json
        assert 'order_number' in res_json


@pytest.fixture
async def prepare_order(prepare_app):
    app = prepare_app

    async with aiohttp.ClientSession() as session:
        body = {
            'sender_name': 'test-sender-name',
            'amount': 3,
            'receiver_name': 'test-receiver-name',
            'receiver_phone': '01000000000',
            'receiver_addr': 'test-receiver-addr'
        }
        res = await session.post('http://localhost:8080/orders/',
                                 json=body)
        print(await res.text())
        res_json = await res.json()

        yield res_json['order_number'], body

        query = (order.delete())
        app['db_engine'].execute(query)


@pytest.mark.integration
@pytest.mark.asyncio
async def test_handle_order_delete(prepare_order):
    order_number, _ = prepare_order

    async with aiohttp.ClientSession() as session:
        res = await session.delete(f'http://localhost:8080/orders/{order_number}')
        assert res.status == 204


@pytest.mark.integration
@pytest.mark.asyncio
async def test_handle_orders_fetch_auth_failed(prepare_app):
    async with aiohttp.ClientSession() as session:
        res = await session.get('http://localhost:8080/orders/')
        assert res.status == 401


@pytest.mark.integration
@pytest.mark.asyncio
async def test_handle_orders_fetch(prepare_order, auth_header):
    order_number, order_info = prepare_order

    async with aiohttp.ClientSession() as session:
        res = await session.get('http://localhost:8080/orders/', headers=auth_header)
        assert res.status == 200
        res_json = await res.json()
        assert len(res_json) == 1
        _order = res_json[0]
        assert _order['order_number'] == order_number
        assert _order['order_type'] == 'APPLEJUICE'
        assert _order['sender_name'] == order_info['sender_name']
        assert _order['receiver_name'] == order_info['receiver_name']
        assert _order['receiver_phone'] == order_info['receiver_phone']
        assert _order['receiver_addr'] == order_info['receiver_addr']
        assert _order['amount'] == order_info['amount']
        assert _order['status'] == 'BEFORE_SEND'
        assert not _order['paid']


@pytest.mark.integration
@pytest.mark.asyncio
async def test_handle_order_fetch(prepare_order):
    order_number, order_info = prepare_order

    async with aiohttp.ClientSession() as session:
        res = await session.get(f'http://localhost:8080/orders/{order_number}')
        assert res.status == 200
        _order = await res.json()
        print(_order)
        assert _order['order_number'] == order_number
        assert _order['order_type'] == 'APPLEJUICE'
        assert _order['sender_name'] == order_info['sender_name']
        assert _order['receiver_name'] == order_info['receiver_name']
        assert _order['receiver_phone'] == order_info['receiver_phone']
        assert _order['receiver_addr'] == order_info['receiver_addr']
        assert _order['amount'] == order_info['amount']
        assert _order['status'] == 'BEFORE_SEND'
        assert not _order['paid']


@pytest.mark.integration
@pytest.mark.asyncio
async def test_handle_order_update(prepare_order):
    order_number, order_info = prepare_order

    async with aiohttp.ClientSession() as session:
        body = {
            'status': 'ON_DELIVERY',
            'receiver_name': 'updated-receiver-name',
            'paid': True,
        }
        res = await session.put(f'http://localhost:8080/orders/{order_number}',
                                json=body)
        assert res.status == 204

        res = await session.get(f'http://localhost:8080/orders/{order_number}')
        res_json = await res.json()
        _order = res_json
        assert _order['order_number'] == order_number
        assert _order['order_type'] == 'APPLEJUICE'
        assert _order['sender_name'] == order_info['sender_name']
        assert _order['receiver_name'] == body['receiver_name']
        assert _order['receiver_phone'] == order_info['receiver_phone']
        assert _order['receiver_addr'] == order_info['receiver_addr']
        assert _order['amount'] == order_info['amount']
        assert _order['status'] == body['status']
        assert _order['paid']


