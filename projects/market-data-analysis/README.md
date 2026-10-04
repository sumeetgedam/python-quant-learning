# Market Data Analysis

A hands-on project for learning Python data analysis using daily S&P 500 closing values from FRED

## Dataset

- Series : S&P 500(`SP500`)
- Source : FRED, Federal Reserve Bank of St. Louis
- Frequency : Daily close
- Important : This is a price index, not a total-return index; it does not include dividends.


See [data/raw/README.md](data/raw/README.md) for download and data-handling instruction.

This is a **price index**, not a total-return index; it excludes dividends.

## Project goals

Practice loading, checking, cleaning, transforming, summarizing, and exploring real-world time-series data with Python.

## Scripts

Run these frmo project root, in order : 

1. `scripts/01-numpy-market-data.py` - NumPy arrays and returns
2. `scripts/02-pandas-market-data.py` - DataFrames, inspection, and returns
3. `scripts/03-clean-market-data.py` - validation and cleaning report
4. `scripts/04-transform-market-data.py` - returns and rebased prices
5. `scripts/05-aggregate-market-data.py` - monthly summaries
6. `scripts/06-explore-market-data.py` - statistics, charts, and unusual returns
7. `scripts/07-feature-engineering.py` - lagged features, rolling statistics, and a next observation target