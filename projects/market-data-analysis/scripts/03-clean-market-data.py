"""
Clean and audit FRED S&P500 closing value data.

Expected input: 
    project/market-data-analysis/data/raw/sp500.csv

Install Pandas if needed : 
    python -m pip install pandas
"""

from pathlib import Path

import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = PROJECT_DIR / "data" / "raw" / "sp500.csv"


def clean_market_data(raw_df):
    """Clean records and report how many were excluded at each step."""

    expected_columns = {"observation_date", "SP500"}
    missing_columns = expected_columns - set(raw_df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing expected columns: {sorted(missing_columns)}"
        )
    
    df = raw_df.rename(
        columns={
            "observation_date" :"date",
            "SP500" : "close",
        }
    ).copy()

    row_count = len(df)

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    invalid_date_count = int(df["date"].isna().sum())
    df = df.dropna(subset=["date"])

    df["close"] = pd.to_numeric(df["close"], errors="coerce")
    invalid_close_count = int(df["close"].isna().sum())
    df = df.dropna(subset=["close"])

    non_positive_count = int((df["close"] <= 0).sum())
    df = df[df["close"] > 0].copy()

    duplicate_date_count = int(df["date"].duplicated().sum())
    if duplicate_date_count:
        raise ValueError(
            f"Found {duplicate_date_count} duplicate valid dates; "
            "inspect then before deciding how to resolve them."
        )
    
    df = df.sort_values("date").set_index("date")

    report = {
        "input_rows" : row_count,
        "invalid_dates" : invalid_date_count,
        "missing_or_invalid_closes" : invalid_close_count,
        "non_positive_closes" : non_positive_count,
        "output_rows" : len(df),
    }

    return df, report



def main():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found : {DATA_FILE}\n"
            "Download the FRED CSV and save it at that location"
        )
    
    raw_df = pd.read_csv(DATA_FILE, na_values=["."])
    cleaned_df, report = clean_market_data(raw_df)

    print("Cleaning report : ")
    for name, count in report.items():
        print(f" {name}: {count}")

    print("\nCleaned data preview : ")
    print(cleaned_df.head())

    print("\nDate range : ")
    print(cleaned_df.index.min(), "to", cleaned_df.index.max())

if __name__ == "__main__":
    main()