"""
Compare S&P 500 changes with VIX changes on shared dates

Expected inputs:
    projects/market-data-analysis/data/raw/sp500.csv
    projects/market-data-analysis/data/raw/vix.csv
    
Install dependencies if needed :
    python -m pip install pandas matplotlib
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

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

def calculate_relationship(changes):
    """Return sample covariance and Pearson correlation matrices."""

    paired_changes = changes[["sp500_return", "vix_pct_change"]]

    coveriance = paired_changes.cov()
    correlation = paired_changes.corr(method="pearson")

    return coveriance, correlation

def save_scatter_plot(changes, output_dir):
    """Save a scatter plot of aligned S&P500 and VIX percentage changes."""

    output_dir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(
        changes["sp500_return"],
        changes["vix_pct_change"],
        alpha=0.45,
        s=18
    )

    ax.set_title("S&P 500 and VIX Percentage changes")
    ax.set_xlabel("S&P 500 fractional change")
    ax.set_ylabel("VIX fractional changes")
    ax.axhline(0, color="gray", linewidth=0.8)
    fig.tight_layout()

    output_file = output_dir / "sp500-vix-changes.png"
    fig.savefig(output_file, dpi=150)
    plt.close()

    return output_file

def main():
    for file_path in (SP500_FILE, VIX_FILE):
        if not file_path.exists():
            raise FileNotFoundError(
                f"Dataset not found : {file_path}\n"
                "Download the required FRED CSV and save it at that location"
            )
        
    changes = load_aligned_changes(SP500_FILE, VIX_FILE)
    covariance, correlation = calculate_relationship(changes)

    plot_file = save_scatter_plot(changes, OUTPUT_DIR)

    print(f"Aligned change obseravtions : {len(changes)}")
    print(f"Date range : {changes.index.min().date()} to "
              f"{changes.index.max().date()}")
    print("\nSample covariance matrix : ")
    print(covariance)
    print("\nPearson correlation matrix : ")
    print(correlation)
    print(f"\nSaved scatter plot to : {plot_file}")
    print(
        "\nThese are histrical associations between changes on shared dates; "
        "they do not establidh causation"
    )

if __name__ == "__main__":
    main() 