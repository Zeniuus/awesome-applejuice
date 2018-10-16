import enum
import sqlalchemy as sa

from .base import metadata


class OrderType(enum.Enum):
    APPLEJUICE = enum.auto()


class OrderStatus(enum.Enum):
    BEFORE_SEND = enum.auto()
    ON_DELIVERY = enum.auto()
    DELIVERY_COMPLETE = enum.auto()


order = sa.Table(
    'order', metadata,
    sa.Column('row_id', sa.Integer, primary_key=True),
    sa.Column('order_number', sa.String(length=32), unique=True),
    sa.Column('order_type', sa.Enum(OrderType)),
    sa.Column('sender_name', sa.Unicode(length=32)),
    sa.Column('receiver_name', sa.Unicode(length=32)),
    sa.Column('receiver_addr', sa.Unicode(length=512)),
    sa.Column('amount', sa.Integer),
    sa.Column('status', sa.Enum(OrderStatus), default=OrderStatus.BEFORE_SEND),
    sa.Column('paid', sa.Boolean, default=False),
)


class OrderSerializer:
    @staticmethod
    def as_dict(orders):
        if not orders:
            return {}
        if not isinstance(orders, list):
            _order = orders
            (
                row_id, order_number, order_type,
                sender_name, receiver_name, receiver_addr,
                amount, status, paid
            ) = _order
            return {
                'order_number': order_number,
                'order_type': order_type,
                'sender_name': sender_name,
                'receiver_name': receiver_name,
                'receiver_addr': receiver_addr,
                'amount': amount,
                'status': status,
                'paid': paid,
            }
        if len(orders) == 0:
            return {}
        return list(map(OrderSerializer.as_dict, orders))
