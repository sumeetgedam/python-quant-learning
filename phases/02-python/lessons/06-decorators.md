# Lesson 6: Decorators

## Learning objectives

- Explain what a decorator does.
- Recognize the `@decorator` syntax.
- Write a simple decorator that adds behavior to a function.

## Core concept

A **decorator** is function that takes another function and returns a function with added or modified behavior.

```python
def announce(func):
    def wrapper():
        print("Starting calculation")
        result = func()
        print("Calculation complete")
        return result
    return wrapper
```

Apply it using `@announce`

```python
@announce
def calculate():
    return 2 + 3
    
print(calculate())
```

This is equivalent to  :

```python
def calculate():
    return 2 + 3
    
calculate = announce(calculate)
```

When `calculate()` is called, the wrapper runs, calls the original function, and returns its result.

## Passing arguments

A general-purpose wrapper can accept any positional and keyword arguments : 

```python
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name}")
        return func(*args, **kwargs)
    
    return wrapper
```

`*args` collects positional arguments; `**kwargs` collects keyword arguments.

In production code, `functools.wraps` is commonly use so the decorated function retains useful metadata such as its original name.

## Why use decorators ?

Decorators are useful for behavior that applies to many functions, such as logging, timing, or access checks without repeating that behavior inside each function.

## Interview questions

1. What dies a decorator receive and return ?
2. What does the `@decorator` syntax do ?
3. Why might a wrapper use `*args` and `**kwargs` ?
4. What is `functools.wraps` used for ?

## Exervice

Write a decorator called `announce` that: 

1. Prints `"Starting"` before calling a function.
2. Calls the function and stores its result.
3. Prints `"Finished"` afterward.
4. Return the result.

Apply it to a function that returns a trade value, then call that function.

## Recap

- A decorator wraps a function to add behavior.
- `@decorator` is shorthand for reassigning the function to the decorator's results.
- `*args` and`**kwargs` let a wrapper pass through different arguments.