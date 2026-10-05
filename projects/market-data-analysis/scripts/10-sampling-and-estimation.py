"""
Estimate the mean of returns between available observations.

Expected input: 
    project/market-data-analysis/data/raw/sp500.csv

Install Pandas if needed : 
    python -m pip install numpy pandas 
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


def estimate_mean(returns, n_resamples=2000, seed=42):
    """Calculate mean uncertainty estimates with an IID bootstrap illustration"""
    values = np.asarray(returns, dtype=float)

    if values.ndim != 1 or values.size < 2 :
        raise ValueError("Provide at least two one-dimensional observation.")
    
    if n_resamples < 1:
        raise ValueError("n_resamples must be atleast 1.")
    
    estimate = float(np.mean(values))
    sample_std = float(np.std(values, ddof=1))
    standard_error = sample_std / np.sqrt(values.size)

    # This resamples individual observatins independently. It does not
    # preserve chronological dependence in the original time series.
    rng = np.random.default_rng(seed)
    bootstrap_samples = rng.choice(
        values, 
        size=(n_resamples, values.size),
        replace=True
    )
    bootstrap_means = bootstrap_samples.mean(axis=1)
    bootstrap_low, bootstrap_high = np.percentile(
        bootstrap_means, [2.5, 97.5]
    )

    normal_low = estimate - 1.96 * standard_error
    normal_high = estimate + 1.96 * standard_error

    return {
        "sample_size" : int(values.size),
        "mean" : estimate,
        "standard_error_iid" : float(standard_error),
        "normal_approx_low_iid" : float(normal_low),
        "normal_approx_high_iid" : float(normal_high),
        "bootstrap_low_iid" : float(bootstrap_low),
        "bootstrap_high_iid" : float(bootstrap_high),
        "n_resamples" : int(n_resamples)
    }

def main():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found : {DATA_FILE}\n"
            "Download the FRED CSV and save it at that location."
        )
    
    returns = load_returns(DATA_FILE)
    results = estimate_mean(returns)

    print(f"Return observations : {results['sample_size']}")
    print("Returns are changes between available observations.")
    print(f"Sample mean : {results['mean']:.6f}")
    print(f"IID standard error : {results['standard_error_iid']:.6f}")
    print(
        "Normal apprximation interval under IID assumptions"
        f"[{results['normal_approx_low_iid']:.6f}, "
        f"{results['normal_approx_high_iid']:.6f}]"
    )
    print(
        "Individual resampling bootstrap interval : "
        f"[{results['bootstrap_low_iid']:.6f}, "
        f"{results['bootstrap_high_iid']}]"
    )
    print(
        "\nCaution : these simple estimates treat observations as independent; "
        "they do not account for time-series dependence or chaning volatility."
    )


if __name__ == "__main__":
    main()