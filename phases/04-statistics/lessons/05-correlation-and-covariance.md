# Lesson 5: Correlation and Covariance

## LEarning objectives

- Explain covariance and correlation
- Interpret the sign and magnitude of correlation
- Align two time series before comparing time
- Understand why correlation does not establish causation.

## Core concepts

**Covariance** describes whether two cariables tend to move together : 

- Positice covariance: they tend to be above or below their mean together
- Negative covariance: when one is above its mean, the other tends to be below.
- Covariance near zero: little linear co-movement in the data.

Covariance depends on the unit of the variables, so its magnitude can be hard to interpret directly.

**Correlation** is a standardized version of covariance. Pearson correlation ranges from -1 to +1 :

- Near +1 : Strong prositive linear association.
- Near -1 : Strong negative linear association.
- Near 0: little linear assocation.

A correlation near zero does not rule out a non-linear relationship.

## Aligning time series

Before comparing two time series, match observations by date. In this project, we first keep dates present in both datasets, then calculate changes on those shared dates. This makes each pair of changes refer to the same interval between common observations.

Because a date may be missing in either source, an interval can cover more than one trading session. The script reports the date range and observation count

## Correlation is not causation

Correlation describes an association in the observed data. It does not establish that one variable causes changes in the other, nor does it guarantee the same relationship will hold in nother period.

## Interview questions

1. How does correlation differ from covariance ?
2. What does a correlation of -0.8 suggest ?
3. Why should two time series be aligned by date before comparison ?
4. Does correlation show that one variable causes the other ?
5. Can a correlation near zero rule out every type of relationship ?

## Recap

- Covariance and correlation describe co-movement.
- Correlation standardizes the relationship to a range from -1 to +1.
- Align dates before comparing changes in time series
- Association along does not demotrate causation.