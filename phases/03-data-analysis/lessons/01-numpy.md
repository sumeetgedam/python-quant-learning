# Lesson 1 : Numpy

## Learning objectives

- Create and inspect a NumPy array
- Perform calculations across an array without writing a loop
- Calculate simple dialy changes fomr the market-price data

## What is NumPy ?

NumPy is a Python library for working with numerical data.Its core structure is an `ndarray`, an array that can hold and efficiently process numerical values. ([numpy.org](https://numpy.org/doc/stable/user/quickstart.html))

```python
import numpy as np

prices = np.array([100.0, 102.0, 101.0])

print(prices.mean())
print(prices.max())
```

## Vectorized calculations

A vectorized operation applies a calculation across an array :

```python
prices = np.array([100.0, 102.0, 101.0])

price_changes = prices[1:]  - prices[:-1]
print(price_changes) # [2, -1]
```

`prices[1:]` contains every value except the first; `prices[:-1]` contains every value except the last. Subtracting these gives the change between consecutive prices.

Simple returns are calculated as : 

```text
(current_price - previous_price) / previous_orice
```

In NumPy : 

```python
daily_returns = (prices[1:] - prices[:-1]) / prices[:-1]
```

This produces one fewer return than the number of prices, because each return needs a previous price.

## Interview questions

1. What is a NumPy `ndarray` ?
2. What does it mean to perform a vectorized calculation ?
3. Why are there fewer daily returns than daily prices ?
4. Does this index's daily price change include dividends ?


## Recap

- NumPy arrays store and process numerical values.
- Vectorized operations apply calculations across arrays.
- Consecutive prices can be used to calculate simple returns.
- Check what a financial dataset represent before interpreting its results.