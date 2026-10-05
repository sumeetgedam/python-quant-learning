# Lesson 3: Sampling and Estimation

## Learning objectives

- Distinguish a sample statistic from population parameter.
- Estimate a mean and its standard error.
- Describe a bootstrap confidence interval.
- Recognize assumptions and limitations when sampling time-series data.

## Core concepts

A **population parameter** describes a full population, such as the mean of all returns in a period of interest. A **sample statistic** is calculated from observed data and used to estimate a parameter.

The sample mean is one estimate : 

```text
sample mean = sum of observed values / number of observations
```

It describes the returns in the data we loaded; it is not a forecast of future returns. 

### Standard error

The **standard error** describes how much an estimate, such as the sample mean, might vary across repeated sampels under a statistical model.

For a sample mean, a common estimate is :

```text
standard error = sample standard deviation / square root of sample size
```

This formula assumes observations are independent and identically distributed. That assumption may not fit financial time series well.

### Bootstrap estimation

The **bootstrap** approximates sampling variation by repeatedly drawing samples with replacement from the observed data and recalculating a statistic.

For a bootstrap confidence interval for the mean :

1. Resample the observed returns with replacement.
2. Calculate the mean of each resample.
3. Use percentiles of those resampled means as interval endpoints.

A 95% bootstrap interval is often formed from the 2.5th and 97.5th percentiles of bootstrap means. It is an estimate under the resampling method and its assumptions, not a guarantee about future values.

### Time-series caution

Resampling individual return independently ignores their chronological order may not preserve time dependence or changing volatility. This lesson uses that simple bootstrap to demonstrate the idea, not to make a reliable investment inference. Time-series methods such as block bootstrap approaches can preserve some local dependence, but require additional choices.

Our returns are between available observations. If dates are missing, an interval may span more than one trading session.

## Interview question

1. What is the difference between a population parameter and a sample statistic ?
2. What does the standard error describe ?
3. How does bootstrap resampling work ?
4. Why can independently resampling time-series returns be misleading ?
5. Does a confidence interval guarantee that future returns will fall inside it ?

## Recap

- A sample statistic estimates a population parameter.
- Standard error desecribes uncertainty in an estimate under assumptions
- Bootstrap resampling approximates variation by repeatedly resampling data
- Simple independent resampling may not preserve time-series dependence.