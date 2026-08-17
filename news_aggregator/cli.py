import argparse
from typing import Any

from .database import (
    count_articles,
    get_all_articles,
    initialize_database,
    insert_article,
)
from .deduplication import remove_duplicates
from .fetcher import NewsAPIError, fetch_top_headlines
from .filters import apply_filters
from .exporter import export_to_csv, export_to_excel


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line argument parser."""

    parser = argparse.ArgumentParser(
        prog="news-aggregator",
        description="Syntecxhub News Aggregator CLI",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    # Fetch command
    fetch_parser = subparsers.add_parser(
        "fetch",
        help="Fetch news headlines and store them.",
    )

    fetch_parser.add_argument(
        "--country",
        default="us",
        help="Two-letter country code. Default: us",
    )

    fetch_parser.add_argument(
        "--category",
        help="News category such as technology or business.",
    )

    fetch_parser.add_argument(
        "--keyword",
        help="Keyword to search for.",
    )

    fetch_parser.add_argument(
        "--limit",
        type=int,
        default=20,
        help="Maximum number of articles to request.",
    )

    # Search command
    search_parser = subparsers.add_parser(
        "search",
        help="Search stored articles.",
    )

    search_parser.add_argument(
        "--export",
        choices=["csv", "excel"],
        help="Export search results to CSV or Excel.",
    )

    search_parser.add_argument(
        "--source",
        help="Filter by news source.",
    )

    search_parser.add_argument(
        "--keyword",
        help="Filter by keyword.",
    )

    search_parser.add_argument(
        "--date",
        help="Filter by date in YYYY-MM-DD format.",
    )

    return parser


def handle_fetch(args: argparse.Namespace) -> None:
    """Fetch, deduplicate, and store articles."""

    initialize_database()

    print("Fetching news...")

    try:
        articles = fetch_top_headlines(
            country=args.country,
            category=args.category,
            query=args.keyword,
            page_size=args.limit,
        )

    except NewsAPIError as exc:
        print(f"Error: {exc}")
        return

    unique_articles = remove_duplicates(articles)

    duplicates_removed = len(articles) - len(unique_articles)

    inserted = sum(
        insert_article(article)
        for article in unique_articles
    )

    print()
    print(f"Articles fetched: {len(articles)}")
    print(f"Duplicates removed: {duplicates_removed}")
    print(f"New articles stored: {inserted}")
    print(f"Total articles in database: {count_articles()}")


def _print_articles(
    articles: list[dict[str, Any]],
) -> None:
    """Print articles in a readable CLI format."""

    if not articles:
        print("No articles found.")
        return

    print(f"\nFound {len(articles)} article(s):\n")

    for index, article in enumerate(articles, start=1):
        print(f"[{index}] {article.get('title', 'Untitled')}")
        print(f"    Source: {article.get('source', 'Unknown')}")
        print(f"    Published: {article.get('published_at', 'Unknown')}")
        print(f"    URL: {article.get('url', 'N/A')}")
        print()


def handle_search(args: argparse.Namespace) -> None:
    """Search stored articles using CLI filters."""

    initialize_database()

    articles = get_all_articles()

    results = apply_filters(
        articles,
        source=args.source,
        keyword=args.keyword,
        date=args.date,
    )

    _print_articles(results)

    if args.export == "csv":
        output = export_to_csv(
            results,
            "data/news_export.csv",
        )
        print(f"Exported {len(results)} articles to {output}")

    elif args.export == "excel":
        output = export_to_excel(
            results,
            "data/news_export.xlsx",
        )
        print(f"Exported {len(results)} articles to {output}")


def run_cli() -> None:
    """Run the News Aggregator CLI."""

    parser = build_parser()

    args = parser.parse_args()

    if args.command == "fetch":
        handle_fetch(args)

    elif args.command == "search":
        handle_search(args)