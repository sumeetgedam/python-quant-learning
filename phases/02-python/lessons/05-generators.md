# Lesson 5: Generators

## Learning objectives

- Explain what a generator is.
- Use `yield` to produce values one at a time.
- Understand why generators can be useful for large datasets.

## Care concept

A **generator** produces values one at a time instead of building and returning an entire collection at once.

A function containing `yield` is a **generator function**. Calling it returns a generator object. Each time Python requests the next value, the function runs until its next `yield`, then pauses while keeping its state.

```python
def generate_prices():
    yield 100.0
    yield 101.5
    yield 99.8
    
prices = generate_prices()

print(next(prices)) # 100.0
print(next(prices)) # 101.5
```

A `for` loop requests values until the generator is exhausted : 

```Python
for price in generate_prices():
    print(price)
```

## A finance example

A generator can process prices one at a time : 
    
```Python
def calculate_returns(prices):
    previous_price = None
    
    for price in prices:
        if previous_price is not None:
            yield (price - previous_price) / previous_price
            
        previous_price = price
        
prices = [100.0, 102.0, 101.0]

for daily_return in calculate_returns(prices):
    print(daily_return)
```

The function yields each return as it is calculated rather than first building a separate list of all returns.

## Why use generators ?

Generators can be useful when processing large files or data steams because they produce values on demand. They can reduce the memory needed compared with creating a full list.

A generator is consumed  as its values are requested; once exhausted, it does not automatically start over.

## Interview question

1. What does `yield` do ?
2. What does a generator function return when called ?
3. How can generators help when processing large datasets ?
4. Can an exhausted generator to reused from the beginning ?

## Exercise

Write a generator function called `generate_trade_values` that takes a list of prices and yields each price multiplied by 10 shares.

Call it with `[10.0, 12.0, 15.0]` and print each yielded value using a `for` loop.

## Recap

- A function with `yield` produces a generator.
- Generator produce values on demand and pause between them.
- They can help process large inputs without storing all results at once.
- An exhausted generator does not restart automatically.