"""
Create hostorical features and a next observation target.

Expected input: 
    project/market-data-analysis/data/raw/sp500.csv

Install Pandas if needed : 
    python -m pip install pandas 
"""

from pathlib import Path

import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = PROJECT_DIR / "data" / "raw" / "sp500.csv"
ROLLING_WINDOW = 20

def load_market_data(file_path):
    """Load, validate, adn sort the date and closing price columns"""

    df = pd.read_csv(file_path)

    expected_columns = {"observation_date", "SP500"}
    missing_columns = expected_columns - set(df.columns)

    if missing_columns:
        raise ValueError(f"Missing expected columns : {sorted(missing_columns)}")
    
    df = df.rename(
        columns={"observation_date" : "date", "SP500" : "close"}
    ).copy()

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["close"] = pd.to_numeric(df["close"], errors="coerce")

    df = df.dropna(subset=["date", "close"])
    df = df[df["close"] > 0].sort_values("date")

    if df["date"].duplicated().any():
        raise ValueError("Duplicate dates found; inspect before analyzing.")
    
    df = df.set_index("date")
    df["daily_return"] = df["close"].pct_change(fill_method=None)

    return df

def build_features(df):
    """Create past only features and the next available return target."""

    featured = df.copy()

    featured["return_lag_1"] = featured["daily_return"].shift(1)

    past_returns = featured["daily_return"].shift(1)
    featured["rolling_mean_20"] = past_returns.rolling(ROLLING_WINDOW).mean()
    featured["rolling_std_20"] = past_returns.rolling(ROLLING_WINDOW).std()

    featured["target_next_return"] = featured["daily_return"].shift(-1)

    return featured

def main():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found : {DATA_FILE}\n"
            "Download the FRED CSV and save it at that location."
        )
    
    df = load_market_data(DATA_FILE)
    featured = build_features(df)

    columns = [
        "close",
        "daily_return",
        "return_lag_1",
        "rolling_mean_20",
        "rolling_std_20",
        "target_next_return",
    ]

    print("Feature preview : ")
    print(featured[columns].tail(10))

    complete_rows = featured.dropna(subset=columns[2:])
    print(f"\nRows with complete features and target : {len(complete_rows)}")
    print(
        "Note : the target is the next available observation's return; "
        "missing dates may make that interval longer than one session"
    )
    

if __name__ == "__main__":
    main()