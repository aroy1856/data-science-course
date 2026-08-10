# GenAI Assignment 9 - NumPy Basics

First data analysis assignment — mostly just getting used to NumPy arrays, element-wise math, aggregations, and a bit of stats. Ends with a tiny weekly sales use case.

## How to run

Open `numpy.ipynb` and run the cells top to bottom.

Needs `numpy` installed (`uv sync` / whatever you use for this repo is fine).

## What's inside

**Task 1 - Creating arrays**  
Made a 1D range (1–10), a 3×3 reshape of 1–9, and an array from a plain list. Printed shape + dtype for each.

**Task 2 - Math operations**  
Two arrays `A` and `B` — did `+ - * / **` with operators, then the same stuff again with `np.add` / `np.subtract` / etc.

**Task 3 - Math formulas**  
On `[2, 4, 6, 8, 10]`: sqrt, exp, log, sum, and cumulative sum — all via NumPy functions.

**Task 4 - Aggregations**  
3×3 matrix: row-wise / column-wise sum (`axis`), plus min, max, and overall mean.

**Task 5 - Stats on marks**  
Mean, median, variance, std, min/max, and range for a small marks array.

**Task 6 - Percentiles & sorting**  
Sorted the same marks, got 25th / 50th / 75th percentiles, and counted how many scored above the average.

**Task 7 - Mini sales analysis**  
Weekly sales array: total, daily average, high/low, std, and which days were above average.

## Files

- `numpy.ipynb` — all the code
- `README.md` — this file
