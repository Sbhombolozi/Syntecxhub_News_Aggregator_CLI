from pathlib import Path
from typing import Any

import pandas as pd


def export_to_csv(
    articles: list[dict[str, Any]],
    output_path: str | Path,
) -> Path:
    """Export articles to a CSV file."""
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    dataframe = pd.DataFrame(articles)
    dataframe.to_csv(output, index=False)

    return output


def export_to_excel(
    articles: list[dict[str, Any]],
    output_path: str | Path,
) -> Path:
    """Export articles to an Excel file."""
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    dataframe = pd.DataFrame(articles)
    dataframe.to_excel(output, index=False)

    return output