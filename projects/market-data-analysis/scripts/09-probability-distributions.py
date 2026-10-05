"""
INspect the empirical distribution of available observation returns.

Expected input: 
    project/market-data-analysis/data/raw/sp500.csv

Install Pandas if needed : 
    python -m pip install numpy pandas matplotlib
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = PROJECT_DIR / "data" / "raw" / "sp500.csv"
OUTPUT_DIR = PROJECT_DIR / "outputs"

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

def calculate_quantiles(returns):
    """Calculate selected empirical quantiles"""
    values = np.asarray(returns, dtype=float)

    if values.size == 0:
        raise ValueError("At least one return observation is required.")
    
    q05, q50, q95 = np.quantile(values, [0.05, 0.50, 0.95])
    return {
        "q05" : float(q05),
        "q50" : float(q50),
        "q95" : float(q95),
    }

def save_distribution_plot(returns, output_dir):
    """save histogram with a normal curve as a visual reference."""
    values = np.asarray(returns, dtype=float)

    if values.size < 2:
        raise ValueError("At least tw return observations are needed.")
    
    mean =float(np.mean(values))
    std = float(np.std(values, ddof=1))

    if std == 0:
        raise ValueError("Cannot draw a normal reference curve for zero spread.")
    
    output_dir.mkdir(parents=True, exist_ok=True)

    x_values = np.linspace(values.min(), values.max(), 500)
    normal_density = (
        np.exp(-0.5 * ((x_values - mean) / std) ** 2)
        / (std * np.sqrt(2 * np.pi))
    )
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(values, bins=50, density=True, alpha=0.65, label="Observed returns")
    ax.plot(
        x_values,
        normal_density,
        color = "darkred",
        linewidth = 2,
        label = "Normal reference using sample mean and std",
    )

    ax.set_title("Empirical Return Distribution")
    ax.set_xlabel("Fractional return betwen available observations")
    ax.set_ylabel("Density")
    ax.legend()
    fig.tight_layout()

    output_file = output_dir / "return-distribution.png"
    fig.savefig(output_file, dpi=150)
    plt.close(fig)

    return output_file

def main():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found : {DATA_FILE}\n"
            "Download the FRED CSV and save it at that location."
        )
    
    returns = load_returns(DATA_FILE)
    quantiles = calculate_quantiles(returns)
    plot_file = save_distribution_plot(returns, OUTPUT_DIR)

    print(f"Return observations : {len(returns)}")
    print("Empirical quantities : ")
    print(f" 5th percentile  : {quantiles['q05']:.6f}")
    print(f" 50th percential : {quantiles['q50']:.6f}")
    print(f" 95th percentile : {quantiles['q95']:.6f}")
    print(f"\nSaved comparison plot to : {plot_file}")
    print(
        "The normal curve is a visual reference, not evidence that "
        "returns follows a normal distribution."
    )


if __name__ == "__main__":
    main()