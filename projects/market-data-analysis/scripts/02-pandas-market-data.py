"""
Inspect FRED S&P500 closing values with Pandas.

Expected input: 
    project/market-data-analysis/data/raw/sp500.csv

Install Pandas if needed : 
    python -m pip install pandas
"""

from pathlib import Path

import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = PROJECT_DIR / "data" / "raw" / "sp500.csv"

def load_market_data(file_path):
    """Read the CSV and prepare its data and closing price columns"""
    df = pd.read_csv(file_path, na_values=["."])

    expected_columns = {"observation_date", "SP500"}
    missing_columns = expected_columns - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Expecte columns {sorted(expected_columns)}, "
            f"but found {list(df.columns)}"
        )
    
    df = df.rename(
        columns={
            "observation_date" : "date",
            "SP500" : "close", 
        }
    )

    df["date"] = pd.to_datetime(df["date"])
    df["close"] = pd.to_numeric(df["close"], errors="coerce")

    return df.sort_values("date").set_index("date")

def add_returns(df):
    """Add fractional daily returns, without filling missing prices"""

    df = df.copy()
    df["daily_return"] = df["close"].pct_change(fill_method=None)
    return df

def main():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_FILE}\n"
            "Download the FRED CSV and save it at that location."
        )
    
    df = load_market_data(DATA_FILE)

    print("First rows : ")
    print(df.head())

    print("\nData types : ")
    print(df.dtypes)

    print("\nMissing values vefore dropping rows: ")
    print(df.isna().sum())

    df = df.dropna(subset=["close"])
    df = add_returns(df)

    print("\nFirst rows with returns :")
    print(df.head())

    print("\nSummary statistics : ")
    print(df[["close", "daily_return"]].describe())



if __name__ == "__main__":
    main()