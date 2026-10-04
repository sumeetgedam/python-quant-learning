"""
Transform FRED S&P500 closing values.

Expected input: 
    project/market-data-analysis/data/raw/sp500.csv

Install Pandas if needed : 
    python -m pip install pandas numpy
"""

from pathlib import Path

import numpy as np
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

def transform_data(df):
    """Add returns between available observations and a rebased price."""

    transformed = df.copy()

    previous_close = transformed["close"].shift(1)
    transformed["simple_return"] = (
        transformed["close"].div(previous_close).sub(1)
    )
    transformed["log_return"] = np.log(
        transformed["close"].div(previous_close)
    )
    transformed["rebased_close"] = (
        transformed["close"].div(transformed["close"].iloc[0]) * 100
    )

    return transformed

def main():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found : {DATA_FILE}\n"
            "Download the FRED CSV and save it at that location."
        )
    
    prices = load_clean_data(DATA_FILE)
    transformed = transform_data(prices)

    print("Transformed data : ")
    print(
        transformed[
            ["close", "simple_return", "log_return", "rebased_close"]
        ].head()
    )

    print("\nAvailable simple returns : ", transformed["simple_return"].count())
    print("First rebased value : ", transformed["rebased_close"].iloc[0])
    print("Last revased value : ", transformed["rebased_close"].iloc[-1])
    

if __name__ == "__main__":
    main()