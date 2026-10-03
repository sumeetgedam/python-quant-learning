# Lesson 8: Time Series

## Learning objectives

- Explain what makes data a time series
- Recognize trend, seasonality, and noise.
- Understand why time order matters in analysis.

## Core concepts 

A **time series** is a sequence of observations recorded over time, such as daily stock prices or monthly sales. Observations may be regularly spaced or sometimes irregularly spaced.

### Common patterns

- **Trend:** a longer-term upward or downward movement
- **Seasonality:** a recurring pattern at a known interval, such as higher sales each december.
- **Noise:** variation that is not explained by the patterns being studied.

A time series can contain more than one of these patterns.

### Why time order matters

Time series observations may be related to earlier observations. Shuffling the data can hide this relationship and lead to misleading analysis.

When evaluating a forecasting model, use earlier observations to predict later ones.
Randomly splitting time ordered data can accidentally let information from the future influence the model.

### Prices and returns

In finance, analysts often examine returns as well as prices. A simple return between two consecutive prices is : 

```text
return  = (current price - previous price) / previous price
```

Prices and returns answer different questions: prices show the level; returns show the relative change between observations.

## Example :

Monthly sales rise gradually over several years, with an additional increase every December. the gradual rise is a tread; the recurring December increase is seasonanlity.

## Interview question

1. What is a time series ?
2. How does seasonality differ from trend ?
3. Why is a random train-test split often unsuitable for forecasting ?
4. How do prices differ from returns ?

## Exercise 

A company's monthly sales generally rise each year, and sales are consistently higher every December.

1. Identify the trend
2. Identify the seasonal pattern
3. Why should you preserve the months' order when testing a forecasting model ?

## Recap

- A time series is data recorded over time
- Trend and seasonality are different patterns; noise may also be present.
- Preserve time order when analyzing or evaluating forecasts.
- Prices show levels; returns show relative changes.