# Lesson 5: Aggregations

## Learning objectives

- Explain why data is aggregated.
- Group observations into calendar periods
- Calculate multiple summary statistics for each group.
- Interpret counts and returns carefully.


## Core concepts

An **aggregation** summarizes multiple observations. For example, daily prices can be grouped by month to calculate each month's average or final available price.

### Grouping and aggregating

Pandas `groupby()` splits rows into groups. An aggregation such as `mean`, `min`, or `max` summarizes each group.

```python
monthly_average = df.groupby(df.index.to_period("M"))["close"].mean()
```

Here, `to_period("M")` labels each date with its calendar month.

You can calculate several statistics at once :

```python
monthly_summary = df.groupby(df.index.to_period("M"))["close"].agg(
    first_close = "first",
    last_close = "last",
    average_close="mean",
    minimum_close="min",
    maximum_close="max",
    observation_count="count",
)
```

Since the data is sorted by date, `first` and `last` refer to the first and last available observations in each month.

### Monthly returns

A Monthly return can be calculated from consecutive months' last available closing values : 

```python
monthly_summary["monthly_return"] = (
    monthly_summary["last_close"].pct_change(fill_method=None)
)
```

The first month has no previous month's close, so its return is missing. If a calendar month has no observations and is absent from the data, a return may span multiple calendar months. Check the month labels before interpreting returns as month-to-month.

### Interpret summaries carefully

A monthly average price is not the same as the month-end price. The observation count indicates how many daily records contributed to that month's summary; it may vary because of weekends, holidays, or missing data.

## Interview questions

1. What does `groupby()` do ?
2. Why is a monthly average different from a month end price ?
3. What dies the observation count tell you ?
4. Why should you inspect month labels before interpreting monthly returns ?

## Recap

- Aggregations summarize group of observations.
- Grouping by calendar month enables monthly statistics.
- Keep monthly averages distrinct from last available monthly prices.
- Check for missing periods before interpreting calculated returns.