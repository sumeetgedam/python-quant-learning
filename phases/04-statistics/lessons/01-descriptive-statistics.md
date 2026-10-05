# Lesson 1: Descriptive statistics

## Learning objectives

- Summarize a dataset using mean, median, and standard deviation.
- Distinguish variance from standard deviation
- Understand why outlier can affect the mean.
- Interpret summary statistics in the context of market data.

## Core concepts

Descriptive statistics summarize a dataset. They help answer questions like 
"What is a typical observation ?"
and
"How spread out are the values ?"

### Mean and Median

The **mean** is the arithmetic average : 

```text
mean = sum of values / number of values
```

The **median is the middle value after sorting the observations. For an even number of observations, it is the average of the two middle values.

The mean can be strongly affected by unusually large or small observations. 
The median is less sensistive to those extremes, so comparing them can help describes akew or outliers.

### Variance and standard deviation

**Variance** summarizes squared differece from the mean.
**Standard deviation** is square root of variance, expressed in the same untis as the observations.

When calculating these from data, distinguish : 

- **Population standard deviation**: treats the observed values as the entire population.
- **Sample standard deviation**: estimates variability in a larger population from a sample.

NumPy's `std()` defaults to population standard deviation (`ddof=0`). Use `ddof=1` for the sample version

### Apply these to returns carefully 

A return such as `0.01` represents a 1% change. The standard deviation of returns describes their dispersion in fractional-return units.

Our dataset's return are between available observations. If dates are missing, an interval may cover more than one trading session. These summaries also describe the historical data we loaded; they do not predict future reutrns.

## Interview questions

1. How do the mean and median differ ?
2. Why is the median less affected by an extreme observation ?
3. What is the difference between population and sample standard deviation ?
4. What units does the standard deviation of fractional returns use ?
5. Why should you inspect observation dates when interpreting return ?

## Recap 

- The mean and median describe central tendency in different ways
- Standard deviation describes spread in the same unit as the observations.
- NumPy uses `ddof=0` by default; `ddof=1` calculates sample standard deviation
- Historical summries describes observed data; they are not forecasts.