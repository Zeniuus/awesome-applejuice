import sqlalchemy as sa


metadata = sa.MetaData()


user = sa.Table(
    'user', metadata,
    sa.Column('row_id', sa.Integer, primary_key=True),
    sa.Column('id', sa.String(length=30), unique=True),
    sa.Column('nickname', sa.String(length=32), unique=True),
    sa.Column('password', sa.String(length=32)),
)
