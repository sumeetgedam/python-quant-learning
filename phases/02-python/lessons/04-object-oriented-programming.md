# Lesson 4: Object-Oriented Programming

## Learning objectives

- Explain the relationship between a class and an object.
- Define attributes and methods.
- Use `__init__` and `self` in a simple class

## Classes and objects

A **class** describes a kind of object: the data it holds and the actions it can perform.

An **object** is a particular instance of that class.

For example, a `Position` class can describe a position's symbol, price, and share count. Each actual position is a separate object.

## Attributes and methods

- **Attributes** store data on an object
- **Methods** are functions defined inside a class that work with that object.

```python
class Position:
    def __init__(self, symbol, price, shares):
        self.symbol = symbol
        self.price  = price
        self.shares = shares
        
    def market_value(self):
        return self.price * self.shares
        
position = Position("AAPL", 225.50, 10)

print(position.symbol) # AAPL
print(position.market_value()) # 2255.0
```

`__init__` runs when a new object is created and sets its initial attributes.

`self` refers to the particular object the method is working with. Python supplies it when you call the method, so you do not pass it explicitly.

## Why use a class ?

A class use keep related data and behavior together. Instead of separately passing a symbol, price, and share count to many functions, a `Position` object groups them and provides a method to calculate its market value.

## Interview questions

1. What is the difference between a class and an object ?
2. Wht are attributes and method ?
3. What does `self` refer to ?
4. What is `__init__` used for ?


## Exercise

Create a `Trade` class with : 

- Attribute: `symbol`, `price` and `quantity`
- A method called `trade_value` that returns `price * quantity`

Create one `Trade` object and print its symbol and trade value

## Recap

- A class defines a type of object;  an object is an instance of that class.
- Attributes hold object data; methods define object behavior.
- `__init__` initializes a new object's attributes.
- `self` refers to the current object.