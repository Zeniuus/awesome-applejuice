import enum
import sqlalchemy as sa

from .base import metadata, SimpleSerializer


class OrderType(enum.Enum):
    APPLEJUICE = 'APPLEJUICE'


class OrderStatus(enum.Enum):
    BEFORE_SEND = 'BEFORE_SEND'
    ON_DELIVERY = 'ON_DELIVERY'
    DELIVERY_COMPLETE = 'DELIVERY_COMPLETE'


order = sa.Table(
    'order', metadata,
    sa.Column('row_id', sa.Integer, primary_key=True),
    sa.Column('order_number', sa.String(length=32), unique=True),
    sa.Column('order_type', sa.Enum(OrderType)),
    sa.Column('sender_name', sa.Unicode(length=32)),
    sa.Column('receiver_name', sa.Unicode(length=32)),
    sa.Column('receiver_phone', sa.String(length=16)),
    sa.Column('receiver_addr', sa.Unicode(length=512)),
    sa.Column('amount', sa.Integer),
    sa.Column('status', sa.Enum(OrderStatus), default=OrderStatus.BEFORE_SEND),
    sa.Column('paid', sa.Boolean, default=False),
)


class OrderSerializer(SimpleSerializer):
    @classmethod
    def single_item_as_dict(cls, _order):
        (
            row_id, order_number, order_type,
            sender_name, receiver_name, receiver_phone, receiver_addr,
            amount, status, paid
        ) = _order
        return {
            'order_number': order_number,
            'order_type': order_type,
            'sender_name': sender_name,
            'receiver_name': receiver_name,
            'receiver_phone': receiver_phone,
            'receiver_addr': receiver_addr,
            'amount': amount,
            'status': status,
            'paid': paid,
        }
