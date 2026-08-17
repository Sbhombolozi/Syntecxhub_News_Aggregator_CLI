import hashlib
from typing import Any


def generate_article_key(article: dict[str, Any]) -> str:
    """
    Generate a stable unique key for an article.

    The URL is preferred because it is normally unique.
    If no URL exists, the title is used as a fallback.
    """

    identifier = article.get("url") or article.get("title") or ""

    normalized = identifier.strip().lower()

    return hashlib.sha256(
        normalized.encode("utf-8")
    ).hexdigest()


def remove_duplicates(
    articles: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """
    Remove duplicate articles from a list.

    Articles with the same URL or fallback title
    are considered duplicates.
    """

    unique_articles = []
    seen_keys = set()

    for article in articles:
        key = generate_article_key(article)

        if not key or key in seen_keys:
            continue

        seen_keys.add(key)
        unique_articles.append(article)

    return unique_articles