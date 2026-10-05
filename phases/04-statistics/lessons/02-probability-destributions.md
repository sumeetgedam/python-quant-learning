# Lesson 2: Probability Distribution

## Learning objectives

- Explain what a probability distribution describes
- Use a histogram to inspect an empirical distribution
- Interpret quantiles
- Compare observed data with a normal distribution without assuming they match.

## Core concepts

A **probability distribution** describes the possible values of a variable and how probability is assigned to those values.

### Empirical distributions and  histograms

An **empirical distribution** is a summary of the values observed in a dataset. A histogram groups observations into intervals called bins and shows how many values fall into each line.

```python
import mtplotlib.pyplot as plt

plt.host(values, bins=40, density=True)
```

With `density=True`, the histogram is scaled as a density rather than raw counts. It helps compare its shape with a probability density curve.

The apparent shape of a histogram depends partly on the bins choices. Use it as a useful view of the data, not as proof that the data follows a particular throretical distribution.

### Quantiles

A **quantile** is a value below which a given fraction of observations falls. For example, the 5th percentileis a value at or below which approximatelty 5% of the observed values fall.

```python
import numpy as np

fifth_percentile = np.quantile(values, 0.05)
median = np.quantile(values, 0.50)
ninety_fifth_percentile = np.quantile(values, 0.95)
```

Quantiles can describe the center and tails observed data without assuming a normal distribution.

### The normal distribution as a reference

A normal distribution is a theoretical, symmetric, bell-shaped distribution described by its mean and standard deviation. We can overlay a normal curve with the same mean and standard deviation as observed returns to compare shapes.

A comparison is not evidence that returns truly follow a normal distribution. Historical returns may have asymmetry or more extreme observations than anormal curve suggests.

### Interpret our market data carefully

This project calculates returns between available observations. When dates are missing, a return interval may span more than one trading session. The histogram describes the returns in this particular dataset and does not establish the probability of future outcomes.

## Interview quesitons

1. What does a histogram ?
2. What does the 5th percentile mean ?
3. Why is an empirical distribution different from a theoretical distribution ?
4. Does overlayinga normal curve prove that data is normally distributed ?
5. Why should we be careful interpreting this project's returns as one-day returns ?


## Recap

- A distribution describes values and their probabilities or observed frequencies.
- Histograms show an empirical distribution; their appearance depends on binning
- Quantiles summarize positions in observed data.
- A normal curve can be a comparison, but should not be assumed to describe market returns.