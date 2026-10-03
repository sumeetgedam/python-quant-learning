# Lesson 2: Probability

## Learning objectives

- Define probability, sample space, and event.
- Calculate simple probabilities.
- Distinguish independent events from mutually exclusive events.

## Core concepts

**Probability** measures how likely an event is. IT ranges from 0 (impossible) to 1 (certain).

When outcomes are equally likely:

```text
Probability of an event = 
    number of favorable outcomes / number of possible outcomes
```

### Sample space and event

The **sample space** is the set of all possible outcomes. An **event** is an outcome or group of outcomes we care about.

For a fair six-sided die, the sample space is `{1, 2, 3, 4, 5, 6}`. The event "roll an even number" is `{2, 4, 6}`, so its probability is `3/6 = 1/2`.

### Complement

The **complement** of an event is that the event does not happen.

```text
P(not A)  = 1 - P(A)
```

If the probability of rain is `0.3`, the probability of no rain is `0.7`.

### Independent events

Two events are **independent** when knowing that one occurred does not change the probability of the other.

For independent events :

```text
P(A and B) = P(A) x P(B)
```

For example, for two fair coin tosses, the probability of getting heads both times is `1/2 x 1/2 = 1/4`.

### Mutually exclusive events

Two events are **mutually exclusive** if they cannot happen at the same time.

For mutually exclusive events:

```text
P(A or B) = P(A) + P(B)
```

On one die roll, getting a 2 and getting a 5 are mutually exclusive.

### Conditional probability

**Conditional probability** is the probability of event A given that event B has occurred :

```text
P(A given B) =  P(A and B) / P(B)
```

It helps describe how new information changes a probability

## Interview questions

1. What is the difference between an event and a sample space ?
2. What does it mean for two events to be independent ?
3. Can two mutually exclusive events both occur ?
4. What does conditional probability represent ?

## Exercise

A fair six-sided die is rolled once.

1. What is the probability of rolling a number greater than 4?
2. What is the probability of not rolling a 1 ?
3. Are "roll an even number" and "rill a 3" mutually exclusive ?

## Recap

- Probability ranges from 0 to 1.
- The complement probability is `1 - P(A)`
- Independent events do not affect each other's probabilities.
- Mutually exclusive events cannot happen at the same time.
- Conditional probability incorporates information that an event has occurred.