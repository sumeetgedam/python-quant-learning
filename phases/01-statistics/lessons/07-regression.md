# Lesson 7: Regression

## Learning objectives

- Explain what regression models
- Identify the response and predictor variables.
- Interpret a simple linear regression equation

## Core concepts

**Regression** models the relationship between an outcome and one or more input variables. It can help describe relationships or make predictions, but a fitted relationship alone does not prove causation.

### Simple linear regression

Simple linear regression uses one predictor :

```text
y = B0 + B1x + e
```

- `y`  : outcome ( response variable )
- `x`  : predictor ( input variable )
- `B0` : intercept; the model's predicted `y` when `x = 0`
- `B1` : slope; the predicted change in `y` for one unit increase in `x`
- `e`  : the part of `y` not explained by the model

In practice, the model estimates the coefficients from data.

### Example

Suppose a fitted model predicts a stock's return using a market index's return  :

```text
predicted stock return = 0.2% + 1.1 x market return
```

The slope says that, according to this fitted model, a one-percentage-point increase in market return is associated with a predicted 1.1 percentage-point increase int the stock's return. It does not guarantee that outcome or establish causation.

### Multiple regression

Multiple regression uses more than one predictor : 
```text
y = B0 + B1x1 + B2x2 +....+e
```

It can model several factors at once. Results still depend on the data, model assumptions, and which predictors are included.


## Interview questions

1. What do the intercept and slope represent in simple linear regression ?
2. What is the difference between a predictor and an outcome ?
3. Does regression prove that a predictor causes an outcome ?
4. What changes when you use multiple regression ?

## Exercise

A model is : 
```text
predicted sales = 10 + 3 x advertising spend
```

1. What is the predicted sales value when advertising spend is 0 ?
2. How does the prediction change when spend increases by 1 unit ?
3. Does this model prove that advertising causes sales to increase ?

## Recap 

- Regression models the relationship between an outcome and predictor variables.
- The slope describes the model's predicted change in the outcome as a predictor changes.
- Regression can describe or predict; it does not by itself prove causation.