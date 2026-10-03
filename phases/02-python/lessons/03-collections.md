# Lesson 3: Collections

## Learning objectives

- Recognize Python's common collection types.
- Choose a collection for given task.
- Add, access, and update collection items.

## Lists

A **list** stores an ordered, changeable sequence. Lists can contain duplicate values.

```python
prices = [100.0, 101.5, 99.8]

prices.append(102.0)
print(prices[0]) # 100.0
```

List indexes start at `0`. Use `len()` to get the number of items.

## Tuples

A **tuple** stores an ordered sequence that cannot be changed after creation

```python
trade = ("AAPL", 10, 225.50)

symbol = trade[0]
```

Tuples are useful for grouping values that should stay together and not be reassigned.

## Dictionaries

A **dictionaries** stores key-value pairs. Keys are unique; values can be repeated.

```python
position = {
    "symbol" : "AAPL",
    "shares" : 10,
    "price"  : 225.50,
    }
print(position["symbol"]) # AAPL
position["shares"] = 12
```

Use `.get()` when a key might be missing :

```python
sector = position.get("sector", "unknown")
```

## Sets

A **set** stores unique values. It is useful for removing duplicates or checking membership.

```python
symbols = {"AAPL", "MSFT", "AAPL"}
print(len(symbols)) # 2
```

A set does not support accessing items by position.

## Choosing a collection

| Collection | Ordered?            | Changeable? | Allows duplicates? | Typical use              |
|------------|---------------------|-------------|--------------------|--------------------------|
| List       | Yes                 | Yes         | Yes                | Sequence of prices       |
| Tuple      | Yes                 | No          | Yes                | Fixed group of values    |
| Dictionary | Insertion order     | Yes         | Keys: no           | Record with named fields |
| Set        | No positional order | Yes         | No                 | Unique symbols           | 

## Iterating over a collection

Use a `for` loop to process items : 

```python
prices = [100.0, 101.5, 99.8]

for price in prices : 
    print(price)
```

For dictionary keys and values :

```python
for key, value in position.items():
    print(key, value)
```

## Interview questions

1. When would you use a list instead of a tuple ?
2. How do you retrieve a value from a dictionary ?
3. What happens when a set contains duplicate values ?
4. Which collection would you use to map a stock symbol to its prices ?

## Exercise

Create :

1. A list containing three daily prices
2. A tuple containing a trade's symbol and quantity.
3. A dictionary containing a symbol and its price.
4. A set from a list that contains duplicate stock symbols.

Print one item from each collection.

## Recap

- Use lists for ordered sequence that may change.
- Use tuples for ordered sequence that should not change.
- Use dictionaries to look up values by key.
- Use sets to store unique values.