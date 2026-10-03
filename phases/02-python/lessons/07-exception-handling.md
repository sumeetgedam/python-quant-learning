# Lesson 7: Exception Handling

## Learning objectives

- Explain what an exception is.
- Handle expected errors with `try` and `except`.
- Use `else`, `finally`, and `raise`.

## Core concept

An **exception** signals that something went wrong while a progress was running. Without handling it, the program may stop.

```python
price = float("not-a-price") # Raises ValueError
```

Use `try` and `except` to handle an error : 

```python
price_text = "not-a-price"

try:
    price = float(price_text)
except ValueError:
    print("Price must be numeric")
```

Catch the **specific excetion** you expect. A bare `except: ` can hide unwanted errors and make bugs harder to find.

## `else` and `finally`

- `else` runs if the `try` block raised no exception.
- `finally` runs whether or not an exception occured,

```python
try:
   price = float("25.50")
except ValueError:
    print("Invalid price")
else:   
    print(f"Parsed price: {price}")
finally: 
    print("Parsing attempt completed")   
```

## Raising an exception

Use `raise` when you code detects an invalid input : 

```python
def calculate_return(previous_price, current_price):
    if previous_price <= 0:
        raise ValueError("previous_price mus tbe greater than zero")
        
    return (current_price - previous_price) / previous_price
```

## Interview questions

1. What is an exception ?
2. What is the purpose of `try` and `except` ?
3. When does the `else` block run ?
4. Why should you catch specific exceptions ?
5. What does `raise` do ?


## Exercise

Write a function that converts a price string to a `float`

- Return the converted value if it is vaid .
- Catch `ValueError` and print `"Invalid price"` if it is not.

Try it with `"12.5"` and `"unknown"`

## Recap

- Exceptions report runtime errors
- Use `try` and `except` to handle expected failures.
- Catch specific exceptions rather than hiding errors with a bare `except`.
- Use `raise` to report invalid input from your own code.