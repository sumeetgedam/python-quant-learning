# Lesson 4: Market Data

## Learning objectives

- Distinguish trade data from quote data
- Understand OHLCV bars
- Recognize why timestamps and data quality matter.

## Core concepts

**Market data** describes trading activity and available prices for a financial instrument.

### Trades

A trade record describes an executed transaction. It commonly includes : 

- Price
- Quantity
- Timestamp
- Instrument identifier

### Quotes

A Quote shows prices and quantities currently offered by buyers and sellers.

- **Bid:** best displayed buying price.
- **Ask:** best displayed selling price.

A quote is not itself a completed trade.

### OHLCV bars

Market data is often grouped into time intervals, such as one minute or one day.

- **Open:** first recorded trade price in the interval.
- **High:** highest recorded trade price.
- **Low:** lowest recorded trade price.
- **Close:** last recorded trade price.
- **Volume:** total quantity traded during the interval.

These are commonly called **OHLCV** data.

### Data details to check

Before analyzing market data, check:

- **Timestamp and time zone:** Which interval does a record belong to ?
- **Instrument identifier:** Does it refer to the correct security ?
- **Frequency:** Is the data tick-by-tick, minute-level, or daily ?
- **Completeness:** Are records missing or duplicated ?
- **Price adjustments:** Have events such as stock splits been reflected ?

## Example

A one-minute bar for a stock might show :

```text
Open  : $50.00
High  : $50.12
Low   : $49.95
Close : $50.08
Volume: 8,500 shares
```

This summarizes trading during that minute; it does not show every individual trade or quote.

## Interview questions

1. What is the difference between a trade and a quote ?
2. What does OHLCV stand for ?
3. Why can timestamps and time zones matter when analyzing market data ?
4. Does a one-minute bar contain every trade that occurred during that minute ?

## Exercise

A daily bar has an open of $20, a high of $22, a low of $19, and a close of $21.

1. What does the high tell you ?
2. Does the bar tell you the order in which the high and low occurred ?
3. What additional information does volume provide ?

## Recap

- Trades describes completed transaction; quotes show available buying and selling prices.
- OHLCV bars summarize prices and volume over an interval.
- Always check timestamps, instrument identifiers, completeness, and adjustments.