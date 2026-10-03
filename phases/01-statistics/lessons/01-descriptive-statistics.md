# Lesson 1: Descriptive Statistics

## Learning objectives

- Describe a dataset using mean, median, and mode
- Understand variance as a measure of spread
- Distinguish population variance from sample variance

## Example dataset

Use the values : 
```text
2, 4, 4, 6
```

### Mean

The **mean** is the arithmetic average: add the values and divide by how many there are.

```text
(2 + 4 + 4 + 6) / 4 = 4
```

### Median

The **median** is the middle value after sorting the data.

Here there are two middle values, 4 and 4, so the median is their average: **4**

### Mode

The **mode** is the most frequently occurring value. Here, the mode **4**.

### Variance

**Variance** measures how spread out values are around the mean. First, subtract the mean from each value :

```text
Values     : 2 4 4 6
Mean       : 4 4 4 4
Difference :-2 0 0 2
```

Square the differences and average them to get the **population variance**:

```text
(4 + 0 + 0 + 4) / 4 = 2
```

For a **sample variance**, divide by one less than the number of observations:

```text
(4 + 0 + 0 + 4) / (4 - 1) = 8/3
```

Use population variance when describing the entire group of interest. Sample variance is commonly use when estimating variability in a larger population from a sample.

Variance is in squared units; standard deviation is its square root and is in original units.

## Interview questions

1. How do mean and median differ ?
2. When might the median better describe a dataset than the mean ?
3. What does variance measure ?
4. Why does the sample variance divide by one less than the sample size ?

## Exercise

For the dataset `1, 3, 3, 5, 8`, calculate:

1. Mean
2. Median
3. Mode
4. Population variance

## Recap

- Mean is the arithmetic average.
- Median is the middle value after sorting
- Mode is the most frequent value.
- Variance describes spread around the mean.