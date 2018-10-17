from aiohttp import web
import sqlalchemy as sa
import uuid

from awesome_applejuice_backend.models import (
    order, OrderType, OrderSerializer)
from awesome_applejuice_backend.utils.http import (
    data_missing, bad_request_missing_data, auth_required)


@auth_required
async def handle_orders_fetch(request):
    query = (sa.select('*')
               .select_from(order))
    result = request.app['db_engine'].execute(query)
    orders = list(result)
    return web.json_response(OrderSerializer.as_dict(orders))


async def handle_order_create(request):
    body = await request.json()
    mandatory_keys = ['sender_name', 'amount', 'receiver_name', 'receiver_addr']
    if data_missing(mandatory_keys, body):
        return web.Response(text=bad_request_missing_data(mandatory_keys),
                            status=400)
    # TODO: validate inputs
    order_number = uuid.uuid4().hex
    new_order = {
        'order_number': order_number,
        'order_type': OrderType.APPLEJUICE,  # Default order type
        'sender_name': body['sender_name'],
        'amount': body['amount'],
        'receiver_name': body['receiver_name'],
        'receiver_addr': body['receiver_addr'],
    }
    query = (order.insert()
                  .values(new_order))
    result = request.app['db_engine'].execute(query)
    order_id = result.inserted_primary_key
    if not order_id:
        return web.Response(status=500)
    return web.json_response({'id': order_id[0],
                              'order_number': order_number})


async def handle_order_fetch(request):
    order_number = request.match_info['order_number']
    query = (sa.select('*')
               .select_from(order)
               .where(order.c.order_number == order_number))
    result = request.app['db_engine'].execute(query)
    _order = result.first()
    return web.json_response(OrderSerializer.as_dict(_order))


async def handle_order_update(request):
    body = await request.json()
    # TODO: validate inputs.
    order_number = request.match_info['order_number']
    order_update = {key: body[key]
                    for key in ['sender_name', 'amount', 'receiver_name', 'receiver_addr']
                    if key in body.keys()}
    query = (order.update()
                  .values(**order_update)
                  .where(order.c.order_number == order_number))
    result = request.app['db_engine'].execute(query)
    if not result.rowcount:
        return web.Response(text=f'Requested order does not exist: {order_number}',
                            status=400)
    return web.json_response(None, status=204)


async def handle_order_delete(request):
    order_number = request.match_info['order_number']
    query = (order.delete()
                  .where(order.c.order_number == order_number))
    result = request.app['db_engine'].execute(query)
    if not result.rowcount:
        return web.Response(text=f'Requested order does not exist: {order_number}',
                            status=400)
    return web.json_response(None, status=204)


def create_subapp():
    app = web.Application()
    app.add_routes([web.get('/', handle_orders_fetch),
                    web.post('/', handle_order_create),
                    web.get(r'/{order_number:[0-9a-f]+}', handle_order_fetch),
                    web.put(r'/{order_number:[0-9a-f]+}', handle_order_update),
                    web.delete(r'/{order_number:[0-9a-f]+}', handle_order_delete)])
    return app, []
