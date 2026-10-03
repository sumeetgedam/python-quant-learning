# Lesson 3: Distributions

## Learning objectives

- Explain what a probability distribution describes
- Recognize normal, binomial, and Poisson distributions.
- Match a simple problem to a suitable distribution.

## Core concept

A **Probability distribution** describes the possible values of a variable and how likely those values.

Distributions may be **discrete** (countable values, such as 0, 1, 2, ...) or **continuous** (values across a range, such as a measurement).

## Normal distribution

The **normal distribution** is continuous and bell-shaped. It is described by its mean, which sets its center, and standard deviation, which describes its spread.

**Example:** Measurement errors are sometimes modeled as approximately normal. Don't assume financial returns follow a normal distribution without checking the data.

## Binomial distribution

The **binomial distribution** models the number of successes in a fixed number of independent trials, when each trial has the same probability of success.

**Example:** If a fair coin is flipped 10 times, the number of heads is binomial with 10 trials and success probability 0.5.

## Poisson distribution

The **Poisson distribution** models the count of events in a fixed interval when events occur at a stable average rate under suitable assumptions.

**Example:** It could model the number of incoming requests in a minute if the arrival rate is reasonably stable.

## Quick comparison

| Distribution | Type       | Models                                    |
|--------------|------------|-------------------------------------------|
| Normal       | Continuous | Measurements or values around a mean      |
| Binomial     | Discrete   | Successes across a fixed number of trials | 
| Poisson      | Discrete   | Event counts in a fixed interval          |

## Interview questions

1. What does a probability distribution describe ?
2. What kind of variable does a binomial distribution model ?
3. How does a Poisson distribution differ from a binomial distribution ?
4. Why shouldn't we assume market returns are normally distributed without checking ?

## Exercise

Choose the most suitable distribution-normal, binomial, or Poisson, for each scenario :

1. Number of heads in 20 coin flips
2. Number of customer calls arriving in one minute
3. Height in a large group of adults

## Recap

- A distribution describes possible values and their probabilities.
- Normal distribution model continuous values; binomial and Poisson distribution model counts.
- Choose a distribution based on how the data is generated, and check whether its assumptions make sense.