import sqlite3
from pathlib import Path
from typing import Any

from .config import DATABASE_PATH


def get_connection() -> sqlite3.Connection:
    """Create a connection to the SQLite database."""

    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    return connection


def initialize_database() -> None:
    """Create the articles table if it does not already exist."""

    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source TEXT NOT NULL,
                author TEXT,
                title TEXT NOT NULL,
                description TEXT,
                url TEXT UNIQUE,
                image_url TEXT,
                published_at TEXT,
                content TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        connection.commit()


def insert_article(article: dict[str, Any]) -> bool:
    """
    Insert an article into the database.

    Returns:
        True if inserted, False if the article already exists.
    """

    with get_connection() as connection:
        cursor = connection.execute(
            """
            INSERT OR IGNORE INTO articles (
                source,
                author,
                title,
                description,
                url,
                image_url,
                published_at,
                content
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                article.get("source"),
                article.get("author"),
                article.get("title"),
                article.get("description"),
                article.get("url"),
                article.get("image_url"),
                article.get("published_at"),
                article.get("content"),
            ),
        )

        connection.commit()

        return cursor.rowcount > 0


def get_all_articles() -> list[dict[str, Any]]:
    """Return all stored articles."""

    with get_connection() as connection:
        rows = connection.execute(
            """
            SELECT *
            FROM articles
            ORDER BY published_at DESC
            """
        ).fetchall()

    return [dict(row) for row in rows]


def count_articles() -> int:
    """Return the total number of stored articles."""

    with get_connection() as connection:
        row = connection.execute(
            "SELECT COUNT(*) AS total FROM articles"
        ).fetchone()

    return row["total"]