from news_aggregator.filters import (
    apply_filters,
    filter_by_date,
    filter_by_keyword,
    filter_by_source,
)


def test_filter_by_source():
    articles = [
        {"source": "BBC News", "title": "Story One"},
        {"source": "NBC News", "title": "Story Two"},
        {"source": "BBC News", "title": "Story Three"},
    ]

    result = filter_by_source(articles, "BBC News")

    assert len(result) == 2


def test_filter_by_keyword():
    articles = [
        {
            "title": "Cybersecurity Threat Report",
            "description": "New security research",
        },
        {
            "title": "Sports Update",
            "description": "Football results",
        },
        {
            "title": "Cybersecurity Jobs",
            "description": "Technology careers",
        },
    ]

    result = filter_by_keyword(articles, "cybersecurity")

    assert len(result) == 2


def test_filter_by_date():
    articles = [
        {
            "title": "Story One",
            "published_at": "2026-08-16T10:30:00Z",
        },
        {
            "title": "Story Two",
            "published_at": "2026-08-15T14:00:00Z",
        },
        {
            "title": "Story Three",
            "published_at": "2026-08-16T18:00:00Z",
        },
    ]

    result = filter_by_date(articles, "2026-08-16")

    assert len(result) == 2


def test_apply_filters():
    articles = [
        {
            "source": "BBC News",
            "title": "Cybersecurity Attack",
            "description": "Security news",
            "published_at": "2026-08-16T10:00:00Z",
        },
        {
            "source": "BBC News",
            "title": "Sports News",
            "description": "Football",
            "published_at": "2026-08-16T11:00:00Z",
        },
        {
            "source": "NBC News",
            "title": "Cybersecurity Report",
            "description": "Security",
            "published_at": "2026-08-16T12:00:00Z",
        },
    ]

    result = apply_filters(
        articles,
        source="BBC News",
        keyword="cybersecurity",
        date="2026-08-16",
    )

    assert len(result) == 1
    assert result[0]["title"] == "Cybersecurity Attack"