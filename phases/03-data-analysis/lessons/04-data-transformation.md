# Lesson 4: Data Transformation

## Learning objectives

- Explain why data is transformed for analysis.
- Calculate simple and log returns from prices.
- Rebase a price series to a common starting values.
- Understand how missing observations affect return intervals.

## Core concepts

A **data transformation** changes the representation of data to make it more useful for a particular analysis. It should not obscure what the original data means.

### Simple returns

For two consecutive available prices : 

```text
simple return = (current price / previous price) - 1
```

A result of `0.02` represents a 2% chang between those observations.

### Log returns

For positive prices  :

```text
log return = log(current price / previous price)
```

Log returns are sometimes use in quantitative analysis. They are not exactly the same as simple returns, although they are close for small price changes.

### Rebased prices

A rebased series expresses every price relative to the first observation : 

```text
rebased value = price / first price x 100
```

The first value is 100. This make it easier to compar erelative performance fro a common starting point.

### Missing observations and intervals

If a missing price is dropped, the next calculated return spans from the previous available observation to the next one. It may cover more than one trading session. Do not fill missing prices automatically or label every calculated return as a one-day return without checking the data.


## Interview questions

1. How is a simple return calculated from two prices ?
2. How does a log return differ from a simple return ?
3. Why might someone rebase a price series ?
4. What happens to a return interval when an intervening price is missing ?

## Recap

- Transformation create representations suited to an analysis.
- Returns describe price changes; rebasing expresses prices relative to a start
- Check missing observations before interpreting return intervals.