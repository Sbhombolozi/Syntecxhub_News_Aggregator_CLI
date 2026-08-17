import sqlite3

from news_aggregator.database import (
    count_articles,
    get_all_articles,
    initialize_database,
    insert_article,
)


def test_database_initialize(tmp_path, monkeypatch):
    database_path = tmp_path / "test_news.db"

    monkeypatch.setattr(
        "news_aggregator.database.DATABASE_PATH",
        database_path,
    )

    initialize_database()

    assert database_path.exists()


def test_insert_and_count_articles(tmp_path, monkeypatch):
    database_path = tmp_path / "test_news.db"

    monkeypatch.setattr(
        "news_aggregator.database.DATABASE_PATH",
        database_path,
    )

    initialize_database()

    article = {
        "title": "Test News Article",
        "description": "This is a test article.",
        "content": "Test article content.",
        "url": "https://example.com/test",
        "source": "Test Source",
        "author": "Test Author",
        "published_at": "2026-08-17T10:00:00Z",
    }

    inserted = insert_article(article)

    assert inserted == 1
    assert count_articles() == 1


def test_duplicate_article_is_not_inserted(tmp_path, monkeypatch):
    database_path = tmp_path / "test_news.db"

    monkeypatch.setattr(
        "news_aggregator.database.DATABASE_PATH",
        database_path,
    )

    initialize_database()

    article = {
        "title": "Duplicate Test Article",
        "description": "Testing duplicate prevention.",
        "content": "Duplicate test content.",
        "url": "https://example.com/duplicate",
        "source": "Test Source",
        "author": "Test Author",
        "published_at": "2026-08-17T11:00:00Z",
    }

    first_insert = insert_article(article)
    second_insert = insert_article(article)

    assert first_insert == 1
    assert second_insert == 0
    assert count_articles() == 1


def test_get_all_articles(tmp_path, monkeypatch):
    database_path = tmp_path / "test_news.db"

    monkeypatch.setattr(
        "news_aggregator.database.DATABASE_PATH",
        database_path,
    )

    initialize_database()

    article = {
        "title": "Database Retrieval Test",
        "description": "Testing article retrieval.",
        "content": "Test content.",
        "url": "https://example.com/retrieval",
        "source": "Test Source",
        "author": "Test Author",
        "published_at": "2026-08-17T12:00:00Z",
    }

    insert_article(article)

    articles = get_all_articles()

    assert len(articles) == 1
    assert articles[0]["title"] == "Database Retrieval Test"