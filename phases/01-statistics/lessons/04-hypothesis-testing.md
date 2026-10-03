# Lesson 4: Hypothesis Testing

## Learning objectives

- Explain the null ad alternative hypothesis
- Interpret a p-value and significance level.
- Distinguish Type I and Type II errors.

## Core concepts

**Hypothesis testing** uses sample data to assess a claim about a population.

### Set up the hypothesis

- **Null hypothesis (H0):** the baseline claim, often "no effect" or "no difference".
- **Alternative hypothesis (H1):** the effect of difference being investigated.

Example : To investigate whether a strategy's average return differs from zero:

```text
H0 : average return = 0
H1 : average return != 0
```

### Significance level

The **significance level**, written as a(alpha), is a threshold chosen before testing. A common example is `a = 0.05`

### p-value and decision

The **p-value** is the probability, assuming the null hypotheses is true, of observing results at least as extreme as the ones obtained.

- If `p-value <= a`, reject H0
- If `p-value > a`, fail to reject H0.

A p-value is **not** the probability that H0 is true. Failing to reject H0 also does not prove it is true.

### Possible errors

- **Type I error:** rejecting a true null hypothesis, a false positive
- **Type II error:** failing to reject a false null hypothesis, a false negative.

## Example

Suppose a test gives p-value of `0.03`, and the chosen significance level is `0.05`.
Since `0.03 <= 0.05`, reject the null hypothesis under this test.

This does not prove the alternative hypothesis is true; it means the result meets the chosen threshold for evidence against H0.

## Interview questions

1. What do the null and alternative hypothesis represent ?
2. What does a p-value tell you ?
3. Does a p-value of 0.03 mean there is a 3% chance that the null hypothesis is true ?
4. What are Type I and Type II errors ?

## Exercise

A test uses `a = 0.05` and produces a p-value of `0.08`.

1. Should you reject or fail to reject H0 ?
2. Does this prove H0, is true ?
3. What would a Type I error mean in this test ?

## Recap

- A test evaluates sample evidence against a null hypothesis.
- Compare the p-value with the preselected significance level.
- A p-value is not the probability that the null by hypothesis is true.
- Type I and Type II errors are different kinds of incorrect conclusions.