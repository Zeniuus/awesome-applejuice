"""Inserted default boards to board table

Revision ID: 7d58def78fdd
Revises: 4040194f150e
Create Date: 2018-10-15 17:26:04.683862

"""
from alembic import op
import sqlalchemy as sa
from pathlib import Path
import sys
sys.path.append(str(Path().parent.absolute()))
from awesome_applejuice_backend.models import board


# revision identifiers, used by Alembic.
revision = '7d58def78fdd'
down_revision = '4040194f150e'
branch_labels = None
depends_on = None


def upgrade():
    op.get_bind().execute(
        board.insert().values(name='rural_life')
    )
    op.get_bind().execute(
        board.insert().values(name='apple_story')
    )
    op.get_bind().execute(
        board.insert().values(name='qna')
    )


def downgrade():
    pass
