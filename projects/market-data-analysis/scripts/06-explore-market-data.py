"""
Explore FRED S&P500 closing values and returns.

Expected input: 
    project/market-data-analysis/data/raw/sp500.csv

Install Pandas if needed : 
    python -m pip install pandas matplotlib
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = PROJECT_DIR / "data" / "raw" / "sp500.csv"
OUTPUT_DIR = PROJECT_DIR / "outputs"
LARGE_RETURN_THRESHOLD = 0.03 # 3%; an inspection hueristic, not an error rule

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

def explore_data(df):
    """Summarize returns and flag large observations for investigation."""

    returns = df["daily_return"].dropna()
    return_summary = returns.describe()

    flagged_returns = df.loc[
        df["daily_return"].abs() > LARGE_RETURN_THRESHOLD,
        ["close", "daily_return"]
    ]

    return return_summary, flagged_returns


def save_plots(df, output_dir):
    """Save price, return and return distribution plots."""

    output_dir.mkdir(parents=True, exist_ok=True)

    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(12, 12))

    df["close"].plot(ax=axes[0], title="S&P 500 Closing value")
    axes[0].set_ylabel("Index value")

    df["daily_return"].plot(ax=axes[1], title="Return Between Available Observations")
    axes[1].set_ylabel("Fractional return")

    df["daily_return"].dropna().hist(bins=50, ax=axes[2])
    axes[2].set_title("Distribution of Returns")
    axes[2].set_xlabel("Fractional return")
    axes[2].set_ylabel("Frequency")

    fig.tight_layout()
    output_file = output_dir / "market-date-eda.png"
    fig.savefig(output_file, dpi=150)
    plt.close(fig)
    return output_file


def main():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found : {DATA_FILE}\n"
            "Download the FRED CSV and save it at that location."
        )
    
    df = load_market_data(DATA_FILE)
    return_summary, flagged_returns = explore_data(df)
    plot_file = save_plots(df, OUTPUT_DIR)

    print("Dataset shape : ", df.shape)
    print("\nClosing value summary : ")
    print(df["close"].describe())

    print("\nReturn summary : ")
    print(return_summary)

    print(
        f"\nReturns exceeding +/-{LARGE_RETURN_THRESHOLD:.1%}"
        "(inspect; not automatically errors):"
    )

    print(flagged_returns)

    print(f"\nSaved chart to : {plot_file}")


if __name__ == "__main__":
    main()