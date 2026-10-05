"""
Fit a simple line to S&P 500 and VIX changes on shared dates.

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

def fit_regression(changes):
    """Fit a simple leat-squares line and return key results."""
    x = changes["vix_pct_change"].to_numpy(dtype=float)
    y = changes["sp500_return"].to_numpy(dtype=float)

    if len(x) < 3:
        raise ValueError("Need at least three paired observations.")
    if not np.isfinite(x).all() or not np.isfinite(y).all():
        raise ValueError("Regression inputs must contain only finit values.")
    
    if np.ptp(x) == 0:
        raise ValueError("VIX changes have no variation; slope is undefined.")
    
    result = stats.linregress(x, y)

    return {
        "slope" : float(result.slope),
        "intercept" : float(result.intercept),
        "r_squared" : float(result.rvalue ** 2),
        "p_value" : float(result.pvalue),
        "slope_stderr" : float(result.stderr),
    }

def save_regression_plot(changes, regression, output_dir):
    """Save a scatter plot and fitted line"""
    output_dir.mkdir(parents=True, exist_ok=True)

    x = changes["vix_pct_change"].to_numpy(dtype=float)
    y = changes["sp500_return"].to_numpy(dtype=float)

    line_x = np.linspace(x.min(), x.max(), 200)
    line_y = regression["intercept"] + regression["slope"] * line_x

    fig, ax = plt.subplots(figsize=(9, 6))
    ax.scatter(x, y, alpha=0.45, s = 10, label="Observed paired changes")
    ax.plot(line_x, line_y, color="darkred", linewidth=2, label="Fitted line")
    ax.set_title("S&P 500 Return vs VIX Percentage Change")
    ax.set_xlabel("VIC fractional change")
    ax.set_ylabel("S&P 500 fractional return")
    ax.legend()
    fig.tight_layout()

    output_file = output_dir / "sp500-vix-regression.png"
    fig.savefig(output_file, dpi=150)
    plt.close(fig)

    return output_file

def main():
    for file_path in (SP500_FILE, VIX_FILE):
        if not file_path.exists():
            raise FileNotFoundError(
                f"Dataset not found : {file_path}\n"
                "Download the required FRED CSV and save it there."
            )
        
    changes = load_aligned_changes(SP500_FILE, VIX_FILE)
    regression = fit_regression(changes)
    plot_file = save_regression_plot(changes, regression, OUTPUT_DIR)

    print(f"Paired change obseravtions : {len(changes)}")
    print(
        f"Date range : {changes.index.min().date()} to "
        f"{changes.index.max().date()}"
    )
    print("Model : S&P 500 return = interpret + slope * VIX change")
    print(f"Slope         : {regression['slope']:.6f}")
    print(f"Intercept     : {regression['intercept']:.6f}")
    print(f"R-squared     : {regression['r_squared']:.6f}")
    print(f"Slope p-value : {regression['p_value']:.6f}")
    print(f"Saved plot    : {plot_file}")
    print(
        "\nThis is a contemporaneous historixal association, not evidence "
        "of causation or a future-prediction result."
    )

if __name__ == "__main__":
    main()