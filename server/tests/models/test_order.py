import uuid

from awesome_applejuice_backend.models import (
    OrderSerializer, OrderStatus, OrderType)


def test_order_single_item_as_dict():
    row_id = 0
    order_number = uuid.uuid4().hex
    order_type = OrderType.APPLEJUICE
    sender_name = 'Suhwan Jee'
    receiver_name = 'Zeniuus'
    receiver_phone = '01000000000'
    receiver_addr = 'Seoul somewhere'
    amount = 3
    status = OrderStatus.BEFORE_SEND
    paid = False
    row = (row_id, order_number, order_type,
           sender_name, receiver_name, receiver_phone, receiver_addr,
           amount, status, paid)

    order = OrderSerializer.single_item_as_dict(row)
    assert order['order_number'] == order_number
    assert order['order_type'] == order_type
    assert order['sender_name'] == sender_name
    assert order['receiver_name'] == receiver_name
    assert order['receiver_phone'] == receiver_phone
    assert order['receiver_addr'] == receiver_addr
    assert order['amount'] == amount
    assert order['status'] == status
    assert order['paid'] == paid


def test_order_as_dict():
    row_id_1 = 0
    order_number_1 = uuid.uuid4().hex
    order_type_1 = OrderType.APPLEJUICE
    sender_name_1 = 'Suhwan Jee'
    receiver_name_1 = 'Zeniuus'
    receiver_phone_1 = '01000000000'
    receiver_addr_1 = 'Seoul somewhere'
    amount_1 = 3
    status_1 = OrderStatus.BEFORE_SEND
    paid_1 = False

    row_id_2 = 1
    order_number_2 = uuid.uuid4().hex
    order_type_2 = OrderType.APPLEJUICE
    sender_name_2 = 'Zeniuus'
    receiver_name_2 = 'Suhwan Jee'
    receiver_phone_2 = '01011111111'
    receiver_addr_2 = 'Seoul elsewhere'
    amount_2 = 2
    status_2 = OrderStatus.ON_DELIVERY
    paid_2 = True

    row1 = (row_id_1, order_number_1, order_type_1,
            sender_name_1, receiver_name_1, receiver_phone_1, receiver_addr_1,
            amount_1, status_1, paid_1)
    row2 = (row_id_2, order_number_2, order_type_2,
            sender_name_2, receiver_name_2, receiver_phone_2, receiver_addr_2,
            amount_2, status_2, paid_2)

    # Empty item test
    order = OrderSerializer.as_dict(None)
    assert order == {}

    # Single item test
    order = OrderSerializer.as_dict(row1)
    assert order['order_number'] == order_number_1
    assert order['order_type'] == order_type_1
    assert order['sender_name'] == sender_name_1
    assert order['receiver_name'] == receiver_name_1
    assert order['receiver_phone'] == receiver_phone_1
    assert order['receiver_addr'] == receiver_addr_1
    assert order['amount'] == amount_1
    assert order['status'] == status_1
    assert order['paid'] == paid_1

    # Empty item list test
    orders = OrderSerializer.as_dict([])
    assert orders == []

    # Item list with length 1 test
    orders = OrderSerializer.as_dict([row1])
    assert orders[0]['order_number'] == order_number_1
    assert orders[0]['order_type'] == order_type_1
    assert orders[0]['sender_name'] == sender_name_1
    assert orders[0]['receiver_name'] == receiver_name_1
    assert orders[0]['receiver_phone'] == receiver_phone_1
    assert orders[0]['receiver_addr'] == receiver_addr_1
    assert orders[0]['amount'] == amount_1
    assert orders[0]['status'] == status_1
    assert orders[0]['paid'] == paid_1

    # Item list with length > 1 test
    orders = OrderSerializer.as_dict([row1, row2])
    assert orders[0]['order_number'] == order_number_1
    assert orders[0]['order_type'] == order_type_1
    assert orders[0]['sender_name'] == sender_name_1
    assert orders[0]['receiver_name'] == receiver_name_1
    assert orders[0]['receiver_phone'] == receiver_phone_1
    assert orders[0]['receiver_addr'] == receiver_addr_1
    assert orders[0]['amount'] == amount_1
    assert orders[0]['status'] == status_1
    assert orders[0]['paid'] == paid_1
    assert orders[1]['order_number'] == order_number_2
    assert orders[1]['order_type'] == order_type_2
    assert orders[1]['sender_name'] == sender_name_2
    assert orders[1]['receiver_name'] == receiver_name_2
    assert orders[1]['receiver_phone'] == receiver_phone_2
    assert orders[1]['receiver_addr'] == receiver_addr_2
    assert orders[1]['amount'] == amount_2
    assert orders[1]['status'] == status_2
    assert orders[1]['paid'] == paid_2
