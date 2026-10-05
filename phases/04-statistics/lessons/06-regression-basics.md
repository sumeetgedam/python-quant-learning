# Lesson 6: Regression Basics

## Learning objetives

- Describe the purpose of simple linear regression.
- Interpret a regression slope and interpret
- Explain residual and R-squared.
- Recogize why a fitted relationship does not prove causation or predictability.

## Core concepts

**Simple linear regression** describes a straight-line relationship between one input variable, x, and an outcome variable, y:

```text
predicted y = intercept + slope * x
```

The least-squares method chooses the line that minimizes the sum f squared differences between observed and predicted y values.

### Slope and intercept

- The **slope** describes how much the model's predicted y changes for a one-unit increase in x
- The **intercept** is the model's predicted y when x is zero.

Interpret the slope in the units used by the data. In this project both inputs are fractional changes. For example, a change of `0.01` means 1%, not one percentage point in a displayed percent scale.

### Residuals and R-squared

A **residual** is an observed outcome minus its fitted value :

```text
residual = observed y - predicted y
```

Residuals are the parts of the observations not accounted for by the fitted line.

**R-squared** describes the fraction of the observed variation in y accounted for the fitted linear relationship in this sample. It does not measure causation, prove that a model is appropriate, or gyarantee performance on new data.

### Project example

We use : 

- x : VIX percentage change
- y : S&P 500 return

Both changes are calculated between shared available dates. Missing dates can make an interval longer than one tradeing session

This is a contemporaneous association : both changes cover the same interval. It is **not** a model predicting a future S&P 500 return from information available beforehand. A fitted line does not show that VIX changes cause market returns.

## Interview questions

1. What does the slope represent in a simple linear regression ?
2. What is a residual ?
3. What does R-squared summarize, and what does it not establish ?
4. Why isn't this example a future prediction model ?
5. Why should dates be aligned before fitting the model ?

## Recap

- Simple regression fits a line relating one input to one outcome.
- Interpret coeedicients int the variables' units.
- Residuals are observed outcomes minus fitted outcomes.
- R-squared describes fit in the observed sample; it does not prove causation or future predictive performance.
- Align time-series observations and check assumptions before interpreting regression results.