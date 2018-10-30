import sqlalchemy as sa

from .base import metadata


board = sa.Table(
    'board', metadata,
    sa.Column('row_id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String(length=32), unique=True)
)
