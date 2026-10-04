"""
Aggregate FRED S&P500 closing values by calendar month.

Expected input: 
    project/market-data-analysis/data/raw/sp500.csv

Install Pandas if needed : 
    python -m pip install pandas
"""

from pathlib import Path

import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = PROJECT_DIR / "data" / "raw" / "sp500.csv"

def load_clean_data(file_path):
    """Load, validate, and sort the date and closing price columns."""

    df = pd.read_csv(file_path, na_values=["."])

    expected_columns = {"observation_date", "SP500"}
    missing_columns = expected_columns - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing expected columns : {sorted(missing_columns)}"
        )
    
    df = df.rename(
        columns={
            "observation_date" : "date",
            "SP500" : "close"
        }
    ).copy()

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["close"] = pd.to_numeric(df["close"], errors="coerce")
    df = df.dropna(subset=["date", "close"])
    df = df[df["close"] > 0].sort_values("date")

    if df["date"].duplicated().any():
        raise ValueError("Duplicate dates found; inspect before transforming.")
    
    return df.set_index("date")


def aggregate_monthly(df):
    """Summarize closes by month and calculate returns from monthly closes."""

    monthly = df.groupby(df.index.to_period("M"))["close"].agg(
        first_close = "first",
        last_close  = "last",
        average_close = "mean",
        minimum_close = "min",
        maximum_close = "max",
        observation_count = "count",
    )

    monthly["monthly_return"] = monthly["last_close"].pct_change(
        fill_method = None
    )

    return monthly

def main():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found : {DATA_FILE}\n"
            "Download the FRED CSV and save it at that location."
        )
    
    daily = load_clean_data(DATA_FILE)
    monthly = aggregate_monthly(daily)

    print("Monthly summary : ")
    print(monthly.head())

    print("\nLatest months : ")
    print(monthly.tail())

    print("\nMonths with no available closing value are not shown.")
    print("Monthly returns : ")
    print(monthly["monthly_return"].dropna().describe())

if __name__ == "__main__":
    main()
