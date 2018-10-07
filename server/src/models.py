import sqlalchemy as sa


user = sa.Table(
    'user', sa.MetaData(),
    sa.Column('id', sa.String(length=30), primary_key=True),
    sa.Column('nickname', sa.String(length=30)),
    sa.Column('password', sa.String(length=30)),
)
