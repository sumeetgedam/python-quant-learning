# Lesson 1: Python Basics

## Learning objectives

- Assign values to variables
- Recognize common Python data types.
- Perform basic calculations and convert types.

## Variable and data types

A **variable** is a name that refer to a value. Python determines the value's type when you assign it.

```python
symbol         = "AAPL"
price          = 225.50
shares         = 10
is_market_open = True
```

Common built-in types : 

| Type    | Example  | Use             |
|---------|----------|-----------------|
| `int`   | `10`     | Whole numbers   |
| `float` | `225.50` | Decimal numbers |
| `str`   | `"AAPL"` | Text            |
| `bool`  | `True`   | True or False   |


Use `type()` to inspect a value :
```python
print(type(price)) # <class 'float'>
```

## Basic calculations

```python
position_value = price * shares
print(position_value) # 2255.0
```

Python supports addition (`+`), subtraction (`-`), multiplication (`*`), and division(`/`). Division with `/` returns a float.

## Converting types

Data read from files or other sources may arrive as text. Convert it before using it in calculations :

```python
price_text = "225.50"
price = float(price_text)

shares_text  = "10"
shares = int(shares_text)

position_value = price * shares
```

A conversion can fail if the text is not valid for that type. For example,
`int("Hello") raises a `ValueError`.

## Naming variables

Use a clear names, usually lowercase with underscores :

```python
daily_return = 0.012
```

Names are case-sensitive : `price` and `Price` are different variables.

## Interview questions

1. What is a variable ?
2. What is the difference between `int` and `float` ?
3. What type does `float("12.5")` produce ?
4. What can happen if you convert non-numeric text to an integer ?

## Exercise

Write Python code that : 

1. Assign a stock symbol, price, and share count to variables
2. Calculation and prints the position value.
3. Converts `"12.5"` to a float and prints its type.

## Recap

- Variables refer to values.
- Common types include `int`, `float`, `str`, and `bool`.
- Convert text to numeric types before calculating with it.