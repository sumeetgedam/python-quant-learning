"""
Demonstrate a one-sample t-test on available observation returns.

Expected input: 
    project/market-data-analysis/data/raw/sp500.csv

Install Pandas if needed : 
    python -m pip install numpy pandas scipy
"""

from pathlib import Path

from scipy import stats
import numpy as np
import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = PROJECT_DIR / "data" / "raw" / "sp500.csv"
ALPHA = 0.05

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


def test_mean(returns, alpha = 0.05):
    """Run a two-sided one-sample t-test against a zero mean."""
    values = np.asarray(returns)

    if values.ndim != 1 or values.size < 2 :
        raise ValueError("Provide at least two one dimentional observations.")
    
    if not np.isfinite(values).all():
        raise ValueError("Returns must contain only finite values.")
    
    if not 0 < alpha < 1:
        raise ValueError("alpha must be between 0 and 1")
    
    result = stats.ttest_1samp(
        values,
        popmean=0.0,
        alternative="two-sided",
    )

    return {
        "sample_size" : int(values.size),
        "sample_mean" : float(np.mean(values)),
        "t_statistic" : float(result.statistic),
        "p_value" : float(result.pvalue),
        "alpha" : float(alpha),
        "reject_null" : bool(result.pvalue < alpha)
    }


def main():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found : {DATA_FILE}\n"
            "Download the FRED CSV and save it at that location."
        )
    
    returns = load_returns(DATA_FILE)
    result = test_mean(returns, alpha=ALPHA)

    print("Test : two sided one sample t test")
    print("J0: population mean return = 0")
    print("H1: population mean return != 0")
    print(f"Observations : {result['sample_size']}")
    print(f"Sample mean  : {result['sample_mean']:.8f}")
    print(f"t statistic  : {result['t_statistic']:.6f}")
    print(f"p-value      : {result['p_value']:.8g}")
    print(f"alpha        : {result['alpha']:.2f}")

    if result["reject_null"]:
        print("Decision: rejeect H0 under this test and its assumptions")
    else:
        print("Decision:  fail to reject H0 under this test and its assumptions.")

    
    
if __name__ == "__main__":
    main()