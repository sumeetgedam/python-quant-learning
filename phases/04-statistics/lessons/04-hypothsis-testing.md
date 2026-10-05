# Lesson 4: Hypothesis Testing

## Learning objectives

- State null and alternative hypotheses.
- Explain a p-value and significance level
- Use a one-sample t-test as an educatinoal example
- Avoid overstating what a test result means.

## Core concepts

A **hypothesis test** evaluates how compatible observed data are with a specified null hypothesis, under the test's assumptions.

### Null and Alternative Hypotheses

For this example, let u represent the population mean return : 

- Null hypothesis: H0: u = 0
- Two-sided alternatice H1 : u != 0

The alternative is two-sided because we are asking whether the mean differs from zero in either direction.

### Test statistic and p-value

A one-sample t-test compares a sample mean with a hypothesized mean. Its calculation uses the sample mean, sample variability, and sample size. SciPy's `ttest_1samp` performs this test and returns a test statistic and p-value. It assumes independent observations. [SciPy documention](https://docs.scipy.org/dco/scipy/reference/generated/scipy.stats.ttest_1samp.html)

A **p-value** is the probability, assuming the null hypothesis and test model are true, of obtaining a test statistic at least as extreme as the observed one. It is **not** the probability that the null hypothesis is true.

### Signigicance level and decision.

Choose a significance level, a(alpha), before looking at the result. For example, a  = 0.06.

- If p-value < a, reject the null hypothesis under the test procedure
- Otherwise, fail to reject the null hypothesis.

"Fail to reject" does not prove that the null hypothesis is true Statistical significance also does not tell us whether an effect is large or practically important.

### Important limitation for this project

The standard one-sample t-test assumes independent obseravtions. Market returns are ordered in time, and may have dependence or changing volatility. Additionally, our returns are between available observations; missing dates can make interval longer than one trading session.

Therefore, this script id for learning how to formulate and run a test. Do not treat its result as dependable finding about expected market returns.

## Interview questions

1. What are the null and alternative hypotheses in this example ?
2. What does a p-value mean ?
3. What does "fail to reject the null" mean ?
4. Why doesn't statistical significance necessarily imply practical importance ?
5. Why is the independence assumpotion a concern for market time series ?

## Recap

- State bypotheses and choose a before interpreting results.
- A p-value is conditional on the null hypothesis and test assumptions.
- A small p-value is not the probability that the null is true.
- A test decision does not establish that an effect is important or predictive.
- Check whether a test's assumptions make sense for the data.