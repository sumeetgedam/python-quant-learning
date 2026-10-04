"""
Explore FRED S&P 500 closing values with NumPy.

Expected input : 
    project/market-data-analysis/data/raw/sp500.csv

Install NumPy is needed : 
    python -m pip install numpy
"""

import csv
from pathlib import Path


import numpy as np

PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = PROJECT_DIR / "data" / "raw" / "sp500.csv"


def load_market_data(file_path):
    """
    Load valid dates and index values from the FRED CSV.
    """

    dates = []
    prices = []

    with file_path.open("r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            date = row["observation_date"]
            value = row["SP500"]

            # FRED uses "." for a missing observation.
            if not value or value == ".":
                continue

            dates.append(date)
            prices.append(float(value))

    return dates, np.array(prices, dtype=float)


def calculate_returns(prices):
    """Calculate simple returns using NumPy array operations"""
    return (prices[1:] - prices[:-1]) / prices[:-1]


def main():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_FILE}\n"
            "Download the FRED CSV and save it at that location."
        )
    
    dates, prices = load_market_data(DATA_FILE)

    if len(prices) < 2:
        raise ValueError("Need at least two valid prices to calculate returns.")
    
    daily_returns = calculate_returns(prices)

    print(f"Valid price observations  : {len(prices)}")
    print(f"First date and close      : {dates[0]} - {prices[0]:,.2f}")
    print(f"Last date and close       : {dates[-1]} - {prices[-1]:,.2f}")
    print(f"Minimum close             : {np.min(prices):,.2f}")
    print(f"Maximum close             : {np.max(prices):,.2f}")
    print(f"Average daily return      : {np.mean(daily_returns):.6f}")
    print(f"Daily return std dev      : {np.std(daily_returns):.6f}")



if __name__ == "__main__":
    main()