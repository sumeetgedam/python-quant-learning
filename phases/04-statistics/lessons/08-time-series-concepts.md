# Lesson 8: Time-Series Concepts

## Learning objectives

- Explain why time order matters in time-series data.
- Describce trends, lags, and autocorrelation.
- Calculate rolling statistics frmo past observations.
- Split time-series data chronologically

## Core concepts

A **time series** is a sequence of observations indexed by time. Unlike a dataset whose rows can be freely shuffled, the order of time series often contains important information.

### Trend and changes

A **trend** is a longer-term direction or pattern in a series. Prices may trend over time, so their levels can behave differently frmo their changes.

A first difference subtracts the previous available value from the current one : 

```python
df["price_change"] = df["close"].diff()
```

A percentage change expresses that difference relative to the previous value : 

```python
df["return"] = df["close"].pct_change(fill_method=None)
```

Changes can be easier to compare across different price levels. This does not guarantee that returns are stationary or predictable.

### Lags and autocorrelation

A **lag** is past observation brought forward to the current row :

```python
df["return_lag_1"] = df["return"].shift(1)
```

***Autocorrelation** measures the linear relationship between a series and  between a series and a lagged version of itself. A lag-1 autocorrelation compares each value with the previous available value.

Autocorrelation is a descriptive statistic. It does not, by itself, prove a useful forecasting relationship

### Rolling statistics

A rolling statistic summarizes a fixed number of observations at a time. For a prediction featuer, calculate it using only values available beforehand : 

```python
past_returns = df["return"].shift(1)
df["rolling_mean_20"] = past_returns.rolling(20).mean()
```

This is a 20-observation window, not necessarily 20 calendar days. Missing dates can make its time span longer.

### Chronological train/test split.

When testing a forecasting idea, keep earlier observations in the training set and later observations in the test set. Randomly shuffling time-series rows can let future information influence training.

A chronological split helps preserve time order, but it does not by itself prevent every form of leakage. Each feature must still use only information that would have been available at its prediction time.

## Interview questions

1. Why does row order matter in a time series ?
2. What does a lag represent ?
3. What does autocorrelation measure ?
4. Why shift returns before calculation a rolling feature for prediction ?
5. Why should time-series data generally not be randomly chuffled into train and test sets ?


## Recap 

- Time order is part of the information in a time series.
- Lags and autocorrelation describe relationships with past observations.
- Prediction features must not include information from the future.
- Rolling windows count observations, which may nt equal calendar days.
- Preserve chronological order when splitting data for validation.