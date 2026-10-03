# Lesson 8: File Processing

## Learning objectives

- Open and read files safely.
- Write results to a file.
- Read simple CSV data with Python's `csv` module.

## Reading a text file

Use `with open(...)` to open a file. The file is automatically closed when the `with` block ends.

```python
with open("prices.txt", "r", encoding="utf-8") as file:
    contents = file.read()
  
print(contents)
```

Common modes : 

- `"r"` : read
- `"w"` : write, replacing existing contents
- `"a"` : append to the end of a file

Use `encoding="utf-8"` for text files unless you have a reason to use another encoding.

## Reading line by line

For large files, process one line at a time rather loading the entire file into memory :

```python
with open("prices.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

`strip()` removes surrounding whitespace, including the line ending.

## Writing a text file

```python
daily_return = 0.025

with open("summary.txt", "w", encoding="utf-8") as file: 
    file.write(f"Daily return: {daily_return:.1%}\n")
```

Be careful with `"w"`: it replaces the file's existing contents. Use `"a"` to append instead.

## Reading CSV data

CSV files store tabular data as rows and columns. Python's built-in `csv` module can read them :

```python
import csv

with open("trades.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        symbol = row["symbol"]
        quantity = int(row["quantity"])
        print(symbol, quantity)
```

`DictReader` uses the CSV header row as dictionary keys. Values are read as strings, so convert them to numeric types when needed.

## Interview question

1. Why use `with open(...)` instead of opening a file without a context manager ?
2. What is the difference between `"w"` and `"a"` mode ?
3. Why might you process a large file one line at a time ?
4. Why do CSV values often need type conversion ?

## Exercise 

Create a file named `trades.csv` with this content :

```csv
symbol,price,quantity
AAPL,200.0,5
MSFT,400.0,2
```

Write a Python script that reads the file and print each symbol and its trade value (`price * quantity`).

## Recap

- Use `with open(...)` so files close automatically.
- Choose file mode carefully : `"w"` replaces; `"a"` appends.
- Process large text files line by line when practical.
- CSV values are read as strings; convert them before numeric calculations.