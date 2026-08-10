# GenAI Assignment 10 - Pandas Basics

First proper Pandas notebook — Series math, DataFrames, filtering, groupby, a few built-in plots, and a tiny sales analysis at the end.

## How to run

Open `pandas.ipynb` and run the cells top to bottom.

Needs `pandas` (and whatever comes with it for the simple `.plot()` charts).

## What's inside

**Task 1 - Series basics**  
Made a marks Series from a list, printed values / index / dtype, and accessed the first element plus the last two.

**Task 2 - Series math**  
Element-wise stuff on the same Series: +5 grace marks, -2, `* 1.05`, and `/ 2`.

**Task 3 - Series helpers**  
Max / min / sum / mean, then a lambda for pass/fail (>= 70) and a count of who passed.

**Task 4 - Create a DataFrame**  
Students dict → DataFrame (`Name`, `Marks`, `Subject`). Peeked with `head` / `tail`, plus shape and column names.

**Task 5 - DataFrame functions**  
`.info()`, `.describe()`, `.head()`, `.tail()`, then sorted by marks descending and reset the index.

**Task 6 - Filtering**  
Marks > 75, Math students, above-average scorers, and failures (marks < 70).

**Task 7 - Grouping**  
`groupby` on Subject for average marks, student count, and max marks per subject.

**Task 8 - Simple plots**  
Bar / line / histogram of marks using Pandas' built-in `.plot()` only — no fancy matplotlib tweaking.

**Task 9 - Mini sales analysis**  
Weekday revenue DataFrame: total, daily average, best day, days above average, and a revenue-vs-day plot.

## Files

- `pandas.ipynb` — all the code
- `README.md` — this file
