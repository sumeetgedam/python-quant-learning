"""
Inspect residuals from a simple S&P 500 / VIX regression.

Expected inputs:
    projects/market-data-analysis/data/raw/sp500.csv
    projects/market-data-analysis/data/raw/vix.csv
    
Install dependencies if needed :
    python -m pip install pandas matplotlib scipy numpy
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_DIR / "data" / "raw" 
SP500_FILE = DATA_DIR / "sp500.csv"
VIX_FILE = DATA_DIR / "vix.csv"
OUTPUT_DIR = PROJECT_DIR / "outputs"

def load_series(file_path, date_column, value_column, output_name):
    """Load one FRED series, normalize its columns ad validate dates."""

    df = pd.read_csv(file_path, na_values=["."])

    expected_columns = {date_column, value_column}
    missing_columns = expected_columns - set(df.columns)
    if missing_columns:
        raise ValueError(
            f"{file_path.name} is missing {sorted(missing_columns)}"
            f"found coluns {list(df.columns)}"
        )
    
    df = df[[date_column, value_column]].rename(
        columns={
            date_column: "date",
            value_column : output_name
        }
    )

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df[output_name] = pd.to_numeric(df[output_name], errors="coerce")

    df = df.dropna(subset=["date", output_name]).sort_values("date")

    if df["date"].duplicated().any():
        raise ValueError(f"Duplicated daets found in : {file_path.name}")
    
    return df.set_index("date")

def load_aligned_changes(sp500_file, vix_file):
    """Align closing values, then calculate changes over shared dates"""
    sp500 = load_series(
        sp500_file, "observation_date", "SP500", "sp500_close"
    )
    vix = load_series(
        vix_file, "observation_date", "VIXCLS", "vix_close"
    )

    # Inner join keeps dates present in both data source.
    prices = sp500.join(vix, how="inner").sort_index()

    if len(prices) < 3:
        raise ValueError("Need at least three shared dates to compare changes")
    
    changes = prices.pct_change(fill_method=None).dropna()
    changes = changes.rename(
        columns={
            "sp500_close" : "sp500_return",
            "vix_close" : "vix_pct_change",
        }
    )

    return changes

def fit_line(changes):
    """Fit a simple least-squares line and return corfficients."""
    x = changes["vix_pct_change"].to_numpy(dtype=float)
    y = changes["sp500_return"].to_numpy(dtype=float)

    if len(x) < 3:
        raise ValueError("Need at least three paired observations.")
    if not np.isfinite(x).all() or not np.isfinite(y).all():
        raise ValueError("Regression inputs must contain only finit values.")
    
    if np.ptp(x) == 0:
        raise ValueError("VIX changes have no variation; slope is undefined.")
    
    result = stats.linregress(x, y)

    return float(result.slope), float(result.intercept)

def calculate_diagnostics(changes, slope, intercept):
    """Calculate fitted values, residuals and descriptive summaries."""

    result = changes.copy()

    result["fitted"] = (
        intercept + slope * result["vix_pct_change"]
    )
    result["residual"] = result["sp500_return"] - result["fitted"]

    residuals = result["residual"]
    lag1_correlation = residuals.corr(residuals.shift(1))

    summary = {
        "residual_mean" : float(residuals.mean()),
        "residual_sample_std" : float(residuals.std(ddof=1)),
        "lag1_residual_correlation" : float(lag1_correlation)
    }

    return result, summary


def save_diagnostic_plots(result, output_dir):
    """Save residual-versus-fitted, Q-Q and time-order plots"""
    output_dir.mkdir(parents=True, exist_ok=True)

    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(11, 14))

    axes[0].scatter(result["fitted"], result["residual"], alpha=0.45, s=18)
    axes[0].axhline(0, color="darkred", linewidth=1)
    axes[0].set_title("Residual vs Fitted values")
    axes[0].set_xlabel("Fitted S&P 500 return")
    axes[0].set_ylabel("Residual")

    stats.probplot(result["residual"], dist="norm", plot = axes[1])
    axes[1].set_title("Normal Q-Q Plot of Residuals")

    axes[2].plot(result.index, result["residual"], linewidth=0.8)
    axes[2].axhline(0, color="darkred", linewidth=1)
    axes[2].set_title("Residuals in Date Order")
    axes[2].set_xlabel("Date")
    axes[2].set_ylabel("Residual")

    fig.tight_layout()
    output_file = output_dir / "sp500-vix-regression-diagnostics.png"
    fig.savefig(output_file, dpi=150)
    plt.close(fig)

    return output_file

def main():
    for file_path in (SP500_FILE, VIX_FILE):
        if not file_path.exists():
            raise FileNotFoundError(
                f"Dataset not found: {file_path}\n"
                "Download the required FRED CSV and save it there."
            )
        

    changes = load_aligned_changes(SP500_FILE, VIX_FILE)
    slope, intercept = fit_line(changes)
    result, summary = calculate_diagnostics(changes, slope, intercept)

    plot_file = save_diagnostic_plots(result, OUTPUT_DIR)

    print(f"Paired change observations : {len(result)}")
    print(
        f"Date range : {result.index.min().date()} to "
        f"{result.index.max().date()}"
    )

    print(f"Regression slope : {slope:.6f}")
    print(f"Regressio intercept : {intercept:.6f}")
    print(f"Residual mean : {summary['residual_mean']:.8f}")
    print(
        "Residual sample std : "
        f"{summary['residual_sample_std']:.6f}"
    )
    print(
        "Lag-1 residual correlations : "
        f"{summary['lag1_residual_correlation']:.6f}"
    )
    print(f"Saved diagnostic plot to; {plot_file}")


if __name__ == "__main__":
    main()