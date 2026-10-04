# Lesson 3: Data Cleaning

## Learning objectives

- Inspect data for missing and invalid values.
- Convert coumns to the correct types.
- Detect duplictes date.
- Keep a record of cleaning decisions.

## Core concepts

Real datasets may contain missing values, unexpected types, duplicate rows, or invalid values. Cleaning makes these issues visible and applies explicit, repeatable rules.

### Inspect before changing data

Start by checking the shape, types, and missing value : 

```python
print(df.shape)
print(df.dtypes)
print(df.isna().sum())
```

Do not immediately drop every row with a missing value. First ask what is missing and whether removing that row is appropriate.

### Convert and validate types

Dates should be parsed as dates, and prices should be numeric. Values that cannot be parsed should be investigated rather than mistaken for valid data.

```python
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["close"] = pd.to_numeric(df["close"], errors="coerce")
```

With `errors="coerce"`, unparsable values become missing values (`NaT` for dates and `NaN` for numbers).

### Check duplicates

Duplicate dates may indicate duplicated records or a data source issue. Do not arbitrarily keep one row unless you have a clear rule for resolving duplicates.

### Keep a cleaning report

Record how many rows were removed at each step and why. This makes the process auditable and easier to revise.

### Market-date caution

If a price observation is missing and you drop that row, the next calculated percentage change may span more than one trading session. Do not automatically treat it as one day return. 


## Interview questions

1. Why should you inspect data before cleaning it ?
2. What does `errors="coerce"` do ?
3. Why might silently dropping duplicate dates be risky ?
4. Why can dropping a missing market observation affect return calculations ?

## Recap

- Make cleaning rules explicit.
- Track what changes and how many rows are affected.
- Investigate duplicates rather than removing them blindly.
- Missing market observations can affect the time interval between returns.