# Lesson 6: Covariance

## Learning objectives

- Explain what covariance measures.
- Interpret positive, negative, and near-zero covariance.
- Distinguish covariance from correlation.

## Core concepts

**Covariance** describes how two variables vary together.

- **Positive covariance:** the variables tend to be above or below their means together.
- **Negative covariance:** when one tend to be above its mean, the other tends to be below its mean.
- **Near-zero covariance:** there is little *linear co-movement* in the data.

For observations `x` and `y`, population covariance is:

```text
Cov(X, Y) = average of [(x - mean of X) x (y - mean of Y)]
```

Sample covariance uses `n - 1` rather than `n` in the denominator.

### Covariance versus correlation

Covariance depends on the variables' units and scale. For example, measuring a value in dollars rather than cents changes the covariance.

Correlation is a standardized for of covariance : 

```text
Correlation(X, Y) = Cov(X, Y) / (standard deviation of X x standard deviation of Y)
```

Correlation has no units and ranges from `-1` to `+1`; covariance has units and not fixed range.

## Example

If two stocks' returns often move above their averages at the same time, their covariance is positive. This describes their co-movement over the data period; it does not show that one stock causes the other to move.

## Interview questions

1. What does positive covariance suggest ?
2. Why is covariance harder to interpret across datasets that correlation ?
3. How are covariance and correlation related ?
4. Does positive covariance establish causation ?

## Exercise 

Suppose the covariance between two variables is negative.

1. What does that suggest abut their linear co-movement ?
2. Does it tell you the strength of the relationship on a fixed `-1` to `+1` scale ?
3. Which measure covariance or correlation is standardized ?

## Recap

- Covariance describes how two variables vary together
- Its sign indicates the direction of linear co-movement.
- Its magnitude depends on units and scale.
- Correlation standardizes covariance, making it easier to compare.