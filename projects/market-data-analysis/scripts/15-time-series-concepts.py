"""
Explore basic time-series features in S&P500 closing values.

Expected inputs:
    projects/market-data-analysis/data/raw/sp500.csv
    
Install dependencies if needed :
    python -m pip install pandas matplotlib
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = PROJECT_DIR / "data" / "raw"  / "sp500.csv"
OUTPUT_DIR = PROJECT_DIR / "outputs"
ROLLING_WINDOW = 20

def load_market_data(file_path):
    """Load, validation and sort the date and closing-price columns."""
    df = pd.read_csv(file_path, na_values=["."])

    expected_columns = {"observation_date", "SP500"}
    missing_columns = expected_columns - set(df.columns)

    if missing_columns:
        raise ValueError(f"Missing expected columns : {sorted(missing_columns)}")
    
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
        raise ValueError("Duplicate dates found; inspect them before analysis")
    
    return df.set_index("date")

def add_time_series_features(df):
    """Add returns and rolling features based only on prior returns."""
    featured = df.copy()
    featured["return"] = featured["close"].pct_change(fill_method=None)
    featured["return_lag_1"] = featured["return"].shift(1)

    past_returns = featured["return"].shift(1)

    featured["rolling_mean_20"] = past_returns.rolling(
        ROLLING_WINDOW,
        min_periods=ROLLING_WINDOW
    ).mean()

    featured["rolling_std_20"] = past_returns.rolling(
        ROLLING_WINDOW,
        min_periods=ROLLING_WINDOW
    ).std()

    return featured

def chronological_split(df, train_fraction=0.8):
    """split rows in time order, without shuffling"""

    if not 0 < train_fraction < 1:
        raise ValueError("train_fraction must be beetween 0 and 1.")
    
    split_at = int(len(df) * train_fraction)
    if split_at == 0 or split_at == len(df):
        raise ValueError("Not enough rows for both train and test sets.")
    
    return df.iloc[:split_at].copy(), df.iloc[split_at:].copy()

def save_plots(df, output_dir):
    """Save plots of the closing index level and calculated reutrn"""
    output_dir.mkdir(parents=True, exist_ok=True)

    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(11, 9))
    df["close"].plot(ax=axes[0], title="S&P 500 Closing Value")
    axes[0].set_ylabel("Index value")

    df["return"].plot(ax=axes[1], title="Return Between Available Observations")
    axes[1].set_ylabel("Fractional return")
    axes[1].axhline(0, color="gray", linewidth=0.8)

    fig.tight_layout()
    output_file = output_dir / "time-series-concepts.png"
    fig.savefig(output_file, dpi=150)
    plt.close(fig)

    return output_file


def main():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_FILE}\n"
            "Download the required FRED CSV and save it there."
        )
    
    prices = load_market_data(DATA_FILE)
    featured = add_time_series_features(prices)
    train, test = chronological_split(featured)

    autocorrelation = featured["return"].autocorr(lag=1)
    plot_file = save_plots(featured, OUTPUT_DIR)

    print(f"Valid price observations : {len(prices)}")
    print(
        f"Date range : {prices.index.min().date()} to "
        f"{prices.index.max().date()}"
    )
    print(f"Training rows : {len(train)}")
    print(
        f"Training dates : {train.index.min().date()} to"
        f"{train.index.max().date()}"
    )
    print(f"Test rows : {len(test)}")
    print(
        f"Test dates : {test.index.min().date()} to"
        f"{test.index.max().date()}"
    )

    print(f"Lag-1 return autocorrelation : {autocorrelation:.6f}")
    print("\nRecent features : ")
    print(
        featured[
            [
                "close",
                "return",
                "return_lag_1",
                "rolling_mean_20",
                "rolling_std_20"
            ]
        ].tail()
    )
    print(f"\nSaved plots to : {plot_file}")

        

if __name__ == '__main__':
    main()