import sqlalchemy as sa

from .base import metadata, SimpleSerializer


article = sa.Table(
    'article', metadata,
    sa.Column('row_id', sa.Integer, primary_key=True),
    sa.Column('title', sa.String(length=256)),
    sa.Column('board', sa.Integer, sa.ForeignKey('board.row_id')),
    sa.Column('content', sa.VARCHAR(length=2048)),
    sa.Column('created_by', sa.Integer, sa.ForeignKey('user.row_id')),
)


class ArticleSerializer(SimpleSerializer):
    @classmethod
    def single_item_as_dict(cls, _article):
        row_id, title, board, content, created_by = _article
        return {
            'title': title,
            'board': board,
            'content': content,
            'created_by': created_by
        }
