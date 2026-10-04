# Lesson 2: Pandas

## Learning objectives

- Explain what a `DataFrame` and `Series` are.
- Load a CSV file into Pandas.
- Inspect columns, data types, and missing values.
- Calculate daily returns from a price column.

## Core concepts

### DataFrame and Series

A **DataFrame** is a table with rows and columns. A **Series** is one labeled column from a DataFrame.

```python
import pandas as pd
data = {
    "symbol" : ["AAPL" , "MSFT"],
    "price" : [200.0, 400.0],
}

df = pd.DataFrame(data)
price = df["price"]
```

### Read and inspect a CSV

```python
df = pd.read_csv("data.csv")

print(df.head())
print(df.columns)
print(df.dtypes)
print(df.isna().sum())
```

`head()` previews rows. `dtypes` shows column types, and `isna().sum()` counts missing values in each column.

When reading a CSV, `na_values` lets us specify strings such as `"."` that should be treated as missing data.

### Dates and sorting

Convert a date column to Pandas' datetime type, then sort by date before calculating changes : 

```python
df["date"] = pd.to_datetime(df["observation_date"])
df = df.sort_values("date")
```

### Daily returns

`pct_change()` calculates the fractional change from the previous row. For example, `0.02` means a 2% return. The first row has no previous price, so its return is missing.

```python
df["daily_return"] = df["close"].pct_change(fill_method=None)
```

The result is a fraction; multiply by 100 if you want a percentage number.

## Interview questions

1. What is the difference between a Pandas `DataFrame` and a `Series` ?
2. How can you inspect a DataFrame's columns and datatypes ?
3. Why should market data be sorted by date before calculating returns ?
4. Why is the first row's return missing ?

## Recap

- A DataFrame is a labeled table; a series is one labeled column.
- Inspect daa before analyzing it.
- Convert dates and sort observations into time order.
- `pct_change()` returns fractional changes between rows.