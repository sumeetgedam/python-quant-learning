# Lesson 6: Exploratory Data Analysis

## Learning objectives

- Summarize a dataset using descriptive statistics.
- Plot price and return time series.
- Inspect the distribution returns.
- Identify observations for further investigation without automatically deleting them.

## Core concepts

**Exploratory Data Analysis (EDA)** is the practice of inspecting and visualizing data to understand its structure, patterns, and potential issues before drawing conclusion.

### Descriptive statistics

For a numerical column, `describe()` reports statistics such as count, mean, standard deviation, minimum, quartiles, and maximum :

```python
prit(df["close"].describe())
```

Summary statistics provide a compact view, but they do not show every pattern in the data.

### Visualize values over time

A time-series line plot can reveal long-term movement, sudden changes, and possible data problems : 

```python
df["close"].plot()
```

Price levels and returns answer different questions. A price chart shows the index level; a return chart shows changes between available observations.

### Inspect the return distribution

A histogram groups retuns into bins so you can see where values are concentrated and whether the distribution appears asymmetric or has large observations : 

```python
df["daily_return"].dropna().hist(bins=50)
```

Pandas provides plotting methods for line charts and histograms; its plotting interface uses Matplotlib by default. ([pandas.pydata.org](https://pandas.pydata.org/docs/user_guide/visualization.html))


### Investigate unusual values

An unusually large return may be a real markete event, a data issue, or a calculation spanning an unexpected time gap. Flag it for review rather than automatically deleting it.

This project uses an absolute-return threshold as a simple **inspection hueristic** not as a statistical test or a rule for removing data.

## Interview questions

1. What is the purpose of EDA ?
2. Why are price levels and returnns useful for different questions ?
3. What can a histogram show that a summary table might not ?
4. Why should an unusual return be investigated rather than automatically removed ?


## Recap

- Use summaries and visualizations together to inspect data.
- Plot prices and returns separately because they represent differnt quantities
- Treat unusual observation a sinvestigation prompts, not automatic errors.
- Check dates and data limitations before interpreting returns.