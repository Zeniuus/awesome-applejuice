import sqlalchemy as sa

from .base import metadata


article = sa.Table(
    'article', metadata,
    sa.Column('row_id', sa.Integer, primary_key=True),
    sa.Column('title', sa.String(length=256)),
    sa.Column('board', sa.Integer, sa.ForeignKey('board.row_id')),
    sa.Column('content', sa.VARCHAR(length=2048)),
    sa.Column('created_by', sa.Integer, sa.ForeignKey('user.row_id')),
)


class ArticleSerializer:
    @staticmethod
    def as_dict(articles):
        if not articles:
            return {}
        if not isinstance(articles, list):
            _article = articles
            row_id, title, board, content, created_by = _article
            return {
                'title': title,
                'board': board,
                'content': content,
                'created_by': created_by
            }
        if len(articles) == 0:
            return {}
        return list(map(ArticleSerializer.as_dict, articles))
