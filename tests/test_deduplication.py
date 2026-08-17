from news_aggregator.deduplication import remove_duplicates


def test_remove_duplicates_by_url():
    articles = [
        {
            "title": "Article One",
            "url": "https://example.com/1",
        },
        {
            "title": "Article One Duplicate",
            "url": "https://example.com/1",
        },
        {
            "title": "Article Two",
            "url": "https://example.com/2",
        },
    ]

    result = remove_duplicates(articles)

    assert len(result) == 2
    assert result[0]["title"] == "Article One"
    assert result[1]["title"] == "Article Two"


def test_remove_duplicates_by_title():
    articles = [
        {
            "title": "Same Story",
        },
        {
            "title": "Same Story",
        },
        {
            "title": "Different Story",
        },
    ]

    result = remove_duplicates(articles)

    assert len(result) == 2
    assert result[0]["title"] == "Same Story"
    assert result[1]["title"] == "Different Story"