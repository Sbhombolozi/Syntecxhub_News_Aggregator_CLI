import logging
from typing import Any

import requests

from .config import NEWS_API_KEY


logger = logging.getLogger(__name__)

NEWS_API_URL = "https://newsapi.org/v2/top-headlines"


class NewsAPIError(Exception):
    """Raised when NewsAPI returns an error."""


def fetch_top_headlines(
    *,
    country: str = "us",
    category: str | None = None,
    query: str | None = None,
    page_size: int = 20,
) -> list[dict[str, Any]]:
    """
    Fetch top headlines from NewsAPI.

    Args:
        country: Two-letter country code.
        category: Optional news category.
        query: Optional keyword search.
        page_size: Maximum number of articles to request.

    Returns:
        A list of normalized article dictionaries.

    Raises:
        NewsAPIError: If the API returns an error.
        requests.RequestException: If the network request fails.
    """

    if not NEWS_API_KEY:
        raise NewsAPIError(
            "NEWS_API_KEY is missing. Check your .env file."
        )

    params = {
        "apiKey": NEWS_API_KEY,
        "country": country,
        "pageSize": page_size,
    }

    if category:
        params["category"] = category

    if query:
        params["q"] = query

    try:
        response = requests.get(
            NEWS_API_URL,
            params=params,
            timeout=15,
        )

        response.raise_for_status()

    except requests.RequestException as exc:
        logger.exception("Failed to connect to NewsAPI.")
        raise NewsAPIError(
            f"Unable to retrieve news: {exc}"
        ) from exc

    data = response.json()

    if data.get("status") != "ok":
        message = data.get("message", "Unknown NewsAPI error.")
        logger.error("NewsAPI returned an error: %s", message)
        raise NewsAPIError(message)

    articles = data.get("articles", [])

    return [_normalize_article(article) for article in articles]


def _normalize_article(article: dict[str, Any]) -> dict[str, Any]:
    """Convert a NewsAPI article into our application's format."""

    source = article.get("source") or {}

    return {
        "source": source.get("name") or "Unknown",
        "author": article.get("author"),
        "title": article.get("title") or "Untitled",
        "description": article.get("description"),
        "url": article.get("url"),
        "image_url": article.get("urlToImage"),
        "published_at": article.get("publishedAt"),
        "content": article.get("content"),
    }