# Lesson 7: Regression Diagnostics

## Learning objectives

- Explain what regression residuals are.
- Use diagnostic plots to look for problems a fitted line may hide.
- Recognize pattern that may indicate model limitations.
- Understand why time-series residual require special attention.

## Core concepts

A **residual** is the observed outcome minus the model's fitted value : 

```text
residual = observed value - fitted value
```

Residual are the parts of the outcome not captured by the model. Looking at them can reveal patterns that a summary such as R-squared does not.


### Residuals versus fitted values

Plot residuals against fitted values :

- A roughly patternless cloud around zero is consistent with a simple linear-model assumption.
- Curved pattern may indicate that a straight line misses a non-linear relationship
- A fan shape, where spread grows or shrinks, may indicate changing residual variance.
- Insolated points may warrnt investigation.

These patterns are clues, not automatic proof that a model is invalid.

### Q-Q plot

A quantile-quantile (Q-Q) plot compares residual quantiles with quantils of a reference normal distribution. Strong deviations from the reference line, especially in the tails, suggest residuals may not be normally distributed.

Normal residuals are relevant to some classical inference procedures; They are not required just to calculate a leat-squares line.

### Residuals over time

For time-series data, plot residuala in date order. Clusters, runs, or changing spread can signal that residuals are not behaving like independent, constant-variance noise.

A lad-1 residual correlation is a simple descriptive check for adjacent residual moving together. It is not a complete test for time dependence.

### Project limitations

This project regresses S&P 500 returns on VIX changes measured over the same available date intervals. It is a contemporaneous relationship, not a prediction of future returns. Missing date may also cause intervals to span more than one trading session.

Diagnostics can reveal potential issues, but they do not fix them or prove causation, Any next modeling step should preserve time order and be evaluated on data not used to fit the model.

## Interview question

1. How is a residual calculated ?
2. What pattern in a residual-versus-fitted plot might suggest nonlinearity ?
3. What does a Q-Q plot help you inspect ?
4. Why is plotting residuals in time order useful for time-series data ?
5. Does a good looking diagnostic plot prove that a model is correct ?

## Recap

- Residual show what a fitted model did not explain.
- Diagnostic plots can reveal nonlinearity, changing spread, unusual point, or time patterns.
- Treat diagnostics as investifation tools rather that automatic verdicts
- Preserve time order when evaluation time-series models
