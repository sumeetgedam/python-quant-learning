"""
Summarize returns between available S&P500 observations.

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

def load_returns(file_path):
    """Read the FRED CSV and calculate returns between available prices."""

    df = pd.read_csv(file_path, na_values=["."])

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
    

    return df["close"].pct_change(fill_method=None).dropna()



def summarize_returns(returns):
    """Calculate common descriptive statistics for the observed retuns"""
    values = np.asarray(returns, dtype=float)

    if values.size < 2:
        raise ValueError("At least two return observations are needed.")
    
    return {
        "mean" : float(np.mean(values)),
        "median" : float(np.median(values)),
        "population_std" : float(np.std(values, ddof=0)),
        "sample_std" : float(np.std(values, ddof=1)),
    }


def main():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found : {DATA_FILE}\n"
            "Download the FRED CSV and save it at that location."
        )
    
    returns = load_returns(DATA_FILE)
    stats = summarize_returns(returns)

    print(f"Return observations : {len(returns)}")
    print("Returns are fractional changes between available observations.")
    print(f"Mean                    : {stats['mean']:.6f}")
    print(f"Median                  : {stats['median']:.6f}")
    print(f"Population std (ddof=0) : {stats['population_std']:.6f}")
    print(f"Sample std (ddof=1)     : {stats['sample_std']:.6f}")

if __name__ == "__main__":
    main()    