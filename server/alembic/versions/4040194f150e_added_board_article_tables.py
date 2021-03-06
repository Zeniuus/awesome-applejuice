"""Added board, article tables

Revision ID: 4040194f150e
Revises: 29ddcceecc11
Create Date: 2018-10-15 16:47:49.392727

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4040194f150e'
down_revision = '29ddcceecc11'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'board',
        sa.Column('row_id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=32), nullable=True),
        sa.PrimaryKeyConstraint('row_id'),
        sa.UniqueConstraint('name')
    )
    op.create_table(
        'article',
        sa.Column('row_id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=256), nullable=True),
        sa.Column('board', sa.Integer(), nullable=True),
        sa.Column('content', sa.VARCHAR(length=2048), nullable=True),
        sa.Column('created_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['board'], ['board.row_id'], ),
        sa.ForeignKeyConstraint(['created_by'], ['user.row_id'], ),
        sa.PrimaryKeyConstraint('row_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('article')
    op.drop_table('board')
    # ### end Alembic commands ###
