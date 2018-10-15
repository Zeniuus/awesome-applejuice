import sqlalchemy as sa


metadata = sa.MetaData()


user = sa.Table(
    'user', metadata,
    sa.Column('row_id', sa.Integer, primary_key=True),
    sa.Column('id', sa.String(length=30), unique=True),
    sa.Column('nickname', sa.String(length=32), unique=True),
    sa.Column('password', sa.String(length=32)),
)

board = sa.Table(
    'board', metadata,
    sa.Column('row_id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String(length=32), unique=True)
)

article = sa.Table(
    'article', metadata,
    sa.Column('row_id', sa.Integer, primary_key=True),
    sa.Column('title', sa.String(length=256)),
    sa.Column('board', sa.Integer, sa.ForeignKey('board.row_id')),
    sa.Column('content', sa.VARCHAR(length=2048)),
    sa.Column('created_by', sa.Integer, sa.ForeignKey('user.row_id')),
)

# TODO: add row_id, created_at, updated_at, deleted_at
# columns automatically for every tables.
# TODO: wrap models with API for CRUD operations.
