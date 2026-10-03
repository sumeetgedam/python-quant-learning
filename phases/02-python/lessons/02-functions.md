# Lesson 2: Functions

## Learning objectives

- Define and call a function
- Pass information using parameters and arguments.
- Return a result from a function.

## Defining and calling a function

A **function** is a reusable block of code. Define one with `def`, followed by its name and parameters.

```python
def calculate_position_value(price, shares):
    return price * shares
    
value = calculate_position_value(50.0, 10)
print(value) # 500.0
```

Here, `price` and `shares` are **parameters**. The values `50.0` and `10` passed when calling the function are **arguments**.

## Return values

`return` sends a result back to the caller. A function without a `return` statement returns `None`.

```python
def print_position_value(price, shares):
    print(price * shares)
    
result = print_position_value(50.0, 10)
print(result)
```

Use `return` when the calling code needs to use the result in a calculation or store it.

## Default and keyword arguments

A parameter can have a default value  

```python
def calculate_position_value(price, shares = 1):
    return price * shares
    
print(calculate_position_value(50.0)) # 50.0
```

You can pass arguments by parameter name : 

```python
value = calculate_position_value(price = 50.0, shares = 10)
```

## A finance example : simple return

```python
def calculate_simple_return(previous_price, current_price):
    return (current_price - previous_price) / previous_price
    
daily_return = calculate_simple_return(100.0, 102.0)
print(daily_return) # 0.02
```

This calculates a return of `0.02`, or 2%. This example assumes `previous_price` is not zero.

## Interview questions

1. What is the difference between a parameter and an argument ?
2. What does a function return if it has no `return` statement ?
3. Why might you use a function instead of repeating the same code ?
4. What is a default argument ?

## Exercise

Write a function called `calculate_trade_value` that takes `price` and `quantity`, then returns their product.

Call it with a price of `25.0` and a quantity of `8`, and print the result.


## Recap

- Define functions with `def`
- Parameters receive values passed as arguments.
- `return` sends a result back to the caller.
- Default arguments make parameters optional when calling a function.