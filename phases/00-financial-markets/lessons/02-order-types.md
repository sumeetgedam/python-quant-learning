# Lesson 2: Order Types

## Learning objectives

- Explain the difference between market and limit orders
- Describe how stop and stop-limit orders work
- Understand the trade-off between execution certainty and price control

## Core concepts

An **order** is an instruction to buy or sell a financial instrument

### Market order

A market order asks to buy or sell as soon as possible at the best available prices

- **Advantage:** Usually more likey to execute quickly
- **Trade-off:** The final execution price is not guaranteed; it can differ from the price you last saw.

### Limit order

A limit order sets the worst price you are willing to accept.

- A buy limit sets the maximum purchase price.
- A sell limit sets the minimum sale price.
- **Advantage:** You control the execution price.
- **Trade-off:** The order may not execute.


### Stop order

A stop order becomes a market order when its stop price is reached.

- It provides a limit on the execution price.
- The order may not execute if the market moves past that limit.

## Example

Suppose a stock is trading near $50.

- A **buy limit at $49** means: buy only at $49 or lower.
- A **buy stop at $52** means: when the stop is triggered, submit a market buy order
- A **buy stop-limit** with a stop at $52 and limit at $53 means: when triggered, submit a limit buy at $53 or lower.

Examples are simplified. Order behavior can depend on the broker, venue, and order instructions.

## Interview questions

1. What is the main difference between a market order and a limit order?
2. Does a limit order guarantee execution?
3. After a stop order is triggered, is its execution price guaranteed?
4. How does a stop-limit order differ from a stop order?


## Exercise

A stock is trading at $100. Describe what could happen with each order:

1. A market buy order
2. A buy limit order at $98
3. A buy stop order at $105

## Recap 
- Market order prioritize execution; their price is not guaranteed.
- Limit orders control the acceptable price; execution is not guaranteed.
- A stop order typically becomes a market order when triggered.
- A stop-limit order becomes a limit order when triggered.
