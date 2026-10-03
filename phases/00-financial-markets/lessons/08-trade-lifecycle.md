# Lesson 8: Trade Lifecycle

## Learning objectives

- Describe the main steps in a trade
- Distinguish execution, clearing, and settlement.
- Understand why trade records need reliable identifiers and timestamps.

## Core concepts

A **trade lifecycle** is the process from submitting an order through completing the exchange of securities and money.

### 1. Order submission

A trader or system sends an order with instructions such as the instrument, side, quantity, and order type.

### 2. Validation and routing

The broker or trading system checks the order and routes it to a venue or another destination. The order may be rejected if it fails a required check.

### 3. Execution

The order matches with another order, creating a trade. An order can be fully filled, partially filled, or left unfilled.

### 4. Confirmation

Trade details are recorded and communicated, including the instrument, price, quantity, and execution time.

### 5. Clearing

The trade details are processed so the parties' obligations can be determined, such as who owes securities and who owes money.

### 6. Settlement

The securities and money are exchanged according to the market's settlement process and schedule.

## Example

An investor submits an order to buy 100 shares. It fills for 60 shares, leaving 40 unfilled. The completed 60-share trade is recorded, processed through clearing, and later settled. The remaining 40 shares are still part of the order unless it is canceled or otherwise completed.

## Why this matters for data analysis

A submitted order is not necessarily a trade, and an executed trade is not necessarily settled yet. Keep their record distinct. Identifier and timestamps help connect events and avoid counting an order, executing, or settlement more than once.


## Interview questions

1. What is the difference between an order and an execution ?
2. What does a partial fill mean ?
3. How do clearing and settlement differ ?
4. Why should order, execution, and settlement records not be treated as interchangeable ?

## Exercise

A buy order is submitted for 100 shares. IT fills for 70 shares, and the remaining 30 shares are canceled.

1. How many shares were executed ?
2. How may shares were canceled ?
3. Has the trade necessarily settled at the moment it is executed ?

## Recap

- The lifecycle runs from order submission through settlement.
- An order may be rejected, unfilled, partially filled, or fully filled.
- Execution create a trade; clearing processes obligations; settlement completes the exchange.
- Track lifecycle events separately in market-data analysis.