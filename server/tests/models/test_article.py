from awesome_applejuice_backend.models import ArticleSerializer


def test_article_single_item_as_dict():
    row_id = 0
    title = 'test-article-title'
    board = 0
    content = 'test-article-content'
    created_by = 0
    row = (row_id, title, board, content, created_by)

    article = ArticleSerializer.single_item_as_dict(row)
    assert article['title'] == title
    assert article['board'] == board
    assert article['content'] == content
    assert article['created_by'] == created_by


def test_article_as_dict():
    row_id_1 = 0
    title_1 = 'test-article-title-1'
    board_1 = 0
    content_1 = 'test-article-content-1'
    created_by_1 = 0

    row_id_2 = 1
    title_2 = 'test-article-title-2'
    board_2 = 1
    content_2 = 'test-article-content-2'
    created_by_2 = 1

    row1 = (row_id_1, title_1, board_1, content_1, created_by_1)
    row2 = (row_id_2, title_2, board_2, content_2, created_by_2)

    # Empty item test
    article = ArticleSerializer.as_dict(None)
    assert article == {}

    # Single item test
    article = ArticleSerializer.as_dict(row1)
    assert article['title'] == title_1
    assert article['board'] == board_1
    assert article['content'] == content_1
    assert article['created_by'] == created_by_1

    # Empty item list test
    articles = ArticleSerializer.as_dict([])
    assert articles == []

    # Item list with length 1 test
    articles = ArticleSerializer.as_dict([row1])
    assert articles[0]['title'] == title_1
    assert articles[0]['board'] == board_1
    assert articles[0]['content'] == content_1
    assert articles[0]['created_by'] == created_by_1

    # Item list with length > 1 test
    articles = ArticleSerializer.as_dict([row1, row2])
    assert articles[0]['title'] == title_1
    assert articles[0]['board'] == board_1
    assert articles[0]['content'] == content_1
    assert articles[0]['created_by'] == created_by_1
    assert articles[1]['title'] == title_2
    assert articles[1]['board'] == board_2
    assert articles[1]['content'] == content_2
    assert articles[1]['created_by'] == created_by_2
