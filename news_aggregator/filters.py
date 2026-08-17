from typing import Any


def filter_by_source(
    articles: list[dict[str, Any]],
    source: str,
) -> list[dict[str, Any]]:
    """Filter articles by source name."""

    source = source.strip().lower()

    return [
        article
        for article in articles
        if (article.get("source") or "").strip().lower() == source
    ]


def filter_by_keyword(
    articles: list[dict[str, Any]],
    keyword: str,
) -> list[dict[str, Any]]:
    """Filter articles containing a keyword."""

    keyword = keyword.strip().lower()

    if not keyword:
        return articles

    results = []

    for article in articles:
        searchable_text = " ".join(
            str(article.get(field) or "")
            for field in (
                "title",
                "description",
                "content",
                "author",
                "source",
            )
        ).lower()

        if keyword in searchable_text:
            results.append(article)

    return results


def filter_by_date(
    articles: list[dict[str, Any]],
    date: str,
) -> list[dict[str, Any]]:
    """
    Filter articles by publication date.

    Expected format:
        YYYY-MM-DD
    """

    date = date.strip()

    return [
        article
        for article in articles
        if (article.get("published_at") or "").startswith(date)
    ]


def apply_filters(
    articles: list[dict[str, Any]],
    source: str | None = None,
    keyword: str | None = None,
    date: str | None = None,
) -> list[dict[str, Any]]:
    """Apply source, keyword, and date filters."""

    filtered_articles = articles

    if source:
        filtered_articles = filter_by_source(
            filtered_articles,
            source,
        )

    if keyword:
        filtered_articles = filter_by_keyword(
            filtered_articles,
            keyword,
        )

    if date:
        filtered_articles = filter_by_date(
            filtered_articles,
            date,
        )

    return filtered_articles