# Lesson 7: Feature Engineering

## Learning objectives

- Explain what a feature is.
- Create lagged and rolling festures from time-series data.
- Identity and avoid target leakage.
- Understand the limits of features built from irregular observations.

## Core concepts

A **feature** is an input variable created or selected to help describe a prediction problem. Feature can be raw_values, transformations, or summaries of previous observations.

### Lagged returns

A lagged return moves a past value into the current row  :

```python
df["return_lag_1"] = df["daily_return"].shift(1)
```

At each date. `return_lag_1` contains the previous available observations return, not the return being predicted.

### Rolling statistics

A rolling mean or standard deviation summarizes a window of past observations. Shift the series first so the current row's return is not included.

```python
past_returns = df["daily_return"].shift(1)

df["rolling_mean_20"] = past_returns.rolling(20).mean()
df["rolling_std_20"] = past_returns.rolling(20).std()
```

These use the previous 20 available returns. If observations are missing, that window may span more than 20 trading sessions.

### Define a future target

For an exercise, we can set the next available return as the target : 

```python
df["target_next_return"] = df["daily_return"].shift(-1)
```

This is a target, not a feature : it is the value we might try to predict. Never use it, or information derived from it, as an input feature.

### Avoid target leakage

**Target leakage** occurs when a feature contains information that would not have been known at prediction time. For example, using the current day's return to predict that same return is leakage if the prediction is meant to happen before that return is observed.

When evaluating a time-series model, preserve time order. Do not randomly shuffle dates into training and testing sets.

## Interview questions

1. What is a feature ?
2. Why shift a series before calculating rolling features for prediction ?
3. What is target leakage ?
4. Why should time-series training and test data preserve chronological order ?
5. Does a 20-row rolling window always represent 20 trading sessions ?

## Recap

- Feature are inputs; targets are values to predict.
- Build prediction features only frmo information available at prediction time.
- Shift returns before calculating rolling statistics to avoid inluding the current return.
- Preserve time order and account for missing observations