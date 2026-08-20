# GenAI Assignment 12 - Seaborn

Same sales CSV as assignment 11, but this time using seaborn for prettier plots — relational, distribution, categorical, regression, and a few figure-level ones at the end.

## How to run

Open `seaborn.ipynb` and run cells from the top. Keep `sales_data.csv` in the same folder.

Needs `seaborn`, `matplotlib`, and `pandas`.

## What's inside

**Data**  
Loaded `sales_data.csv` and converted `Sale_Date` to datetime.

**Task 1 - Relational plot**  
`relplot` with `Unit_Price` vs `Discount`, colored by `Product_Category`. Did it as line and scatter.

**Task 2 - Line, scatter & facet**  
`lineplot` and `scatterplot` for discount vs sales, then split by category using `col='Product_Category'`.

**Task 3 - Distribution**  
Histogram, KDE, rug plot on `Discount`, then hist + KDE together.

**Task 4 - Bivariate distribution**  
2D hist and KDE for `Discount` vs `Quantity_Sold`.

**Task 5 - Matrix plots**  
`pairplot` on the full dataframe and a correlation heatmap for numeric columns.

**Task 6 - Categorical**  
Bar, box, violin, and count plots using `Product_Category` with sales/discount.

**Task 7 - Regression**  
`regplot` for unit price vs quantity, then `lmplot` with hue by category.

**Task 8 - Multi-plots**  
Manual `FacetGrid` with scatter by category, then a small dashboard with `relplot`, `catplot`, and `displot`.

## Files

- `seaborn.ipynb` — all the plots
- `sales_data.csv` — the dataset
- `README.md` — this file
