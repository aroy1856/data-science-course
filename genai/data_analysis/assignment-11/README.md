# GenAI Assignment 11 - Matplotlib

Playing around with matplotlib on a real-ish sales CSV (~1000 rows). Line, scatter, bars, stacked bars, histogram, pie — nothing too crazy, just getting comfortable with plots.

## How to run

Open `matplotlib.ipynb` and run cells from the top. Keep `sales_data.csv` in the same folder.

Needs `matplotlib`, `pandas`, and `numpy`.

## What's inside

**Data**  
Loaded `sales_data.csv`, then pulled `Month` / `Year` out of `Sale_Date` so grouping by month is easier.

**Task 1 - Line plot**  
Average `Sales_Amount` by month with markers, title, labels. X-ticks rotated so month names don’t overlap.

**Task 2 - Scatter**  
`Quantity_Sold` vs `Sales_Amount` — just to see if more units roughly means more money.

**Task 3 - Bar plots**  
Vertical bars for total sales by product category, then a horizontal `barh` for sales by region.

**Task 4 - Multiple bars**  
Side-by-side monthly totals for each sales rep (David, Eve, Bob, Alice, Charlie). Used offsets + a smaller bar width so months don’t glue together.

**Task 5 - Stacked bar**  
Quantity sold by month, stacked by region.

**Task 6 - Histogram**  
Distribution of `Sales_Amount` with 10 bins.

**Task 7 - Pie chart**  
Category share of total sales with `%` labels.

## Files

- `matplotlib.ipynb` — all the plots
- `sales_data.csv` — the dataset
- `README.md` — this file
