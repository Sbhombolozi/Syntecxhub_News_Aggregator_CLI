import os
from pathlib import Path

from dotenv import load_dotenv


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env
load_dotenv(BASE_DIR / ".env")

# NewsAPI configuration
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Database configuration
DATABASE_PATH = BASE_DIR / "data" / "news.db"

# Logging configuration
LOG_DIRECTORY = BASE_DIR / "logs"
LOG_FILE = LOG_DIRECTORY / "news_aggregator.log"


def validate_config():
    """Validate required application configuration."""

    if not NEWS_API_KEY:
        raise ValueError(
            "NEWS_API_KEY is missing. "
            "Please add it to the .env file."
        )

    return True