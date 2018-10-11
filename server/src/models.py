import sqlalchemy as sa


user = sa.Table(
    'user', sa.MetaData(),
    sa.Column('row_id', sa.Integer, primary_key=True),
    sa.Column('id', sa.String(length=30), unique=True),
    sa.Column('nickname', sa.String(length=30), unique=True),
    sa.Column('password', sa.String(length=30)),
)
