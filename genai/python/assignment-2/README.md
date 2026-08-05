# GenAI Assignment 2 - Control Statements

This notebook is me working through if/elif/else, for loops, while loops, and break/continue — basically using a small order/discount example to practice the usual control flow stuff.

## How to run

Just open `control_statement.ipynb` and run the cells.

## What's inside

**Task 1 - Discount Rules (if / elif / else)**  
Took an order amount from the user, checked it was a number, then applied discount tiers (15% / 10% / 7% / 0%). Also added the optional 5% tax after discount and printed the final total.

**Task 2 - Process Multiple Orders (for loop)**  
Ran the same discount logic over a fixed list of orders and printed a small summary for each one. Also tracked total revenue after discounts and how many orders actually got a discount.

**Task 3 - User Menu (while loop + break/continue)**  
Simple menu loop: add an order, show discounted totals, or quit with `q`. Used `continue` for bad input and `break` to exit.

**Task 4 - Loop Control with Conditions (break & continue)**  
Went through a daily sales list. Skipped zeros with `continue`, stopped on `-1` (corrupted data) with `break`, and kept a running total for the valid days.

## Files

- `control_statement.ipynb` — all the code
- `README.md` — this file
