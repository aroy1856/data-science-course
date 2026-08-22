# Assignment 13 - Data Gathering, Cleaning & EDA

This assignment is about loading data from different sources, cleaning it, and doing basic EDA on the sales CSV.

I did a lot of it myself, but some parts I got stuck on and needed help figuring out (noted below). Goal for me was to actually understand the steps, not just get cells to run.

## How to run

1. Open `eda.ipynb`
2. Run from the top
3. Keep `sales_data.csv` in this folder

For TMDB (Task 4): put `TMDB_API_KEY` in a `.env` file. If the API times out, the notebook can use a saved JSON instead.

Packages used: `pandas`, `matplotlib`, `seaborn`, `requests`, `python-dotenv`, `scikit-learn`

## What I did

**Part 1 — loading data**

- CSV: loaded sales data, checked shape / columns / head / describe / info
- JSON: made a small `data.json` and read it with pandas
- SQLite: created `sample.db` + `employees` table, inserted rows, read with SQL
- API: fetched TMDB popular movies, picked a few columns, saved `tmdb_movies.csv`

**Part 2 — cleaning**

- Checked missing values, dtypes, num vs categorical columns
- Cleaning steps: fill missing (practice), drop duplicates, snake_case names, fix date type
- Encoding: label encode some columns, one-hot others, then split `X` / `y` (`sales_amount` as target)

**Part 3 — EDA**

- Univariate: hist + KDE, count plots, boxplots
- Bivariate: scatter, heatmap, bar/box plots
- Wrote insights at the end (including stuff I was unsure about)

## Where I struggled

- JSON: single object broke `read_json` until I put records in a list
- Encoding: still a bit fuzzy on when to use label encoding vs one-hot
- SQLite: had a “database is locked” issue when re-running cells without closing the connection

## Files

- `eda.ipynb` — notebook
- `sales_data.csv` — main dataset
- `data.json` — small JSON for Task 2
- `sample.db` — SQLite for Task 3
- `tmdb_movies.csv` — movies from API
- `README.md` — this file
