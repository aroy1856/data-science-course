# Assignment 14 - Feature Engineering & ML Pipeline

Working with an ecommerce sales CSV (~5000 rows). Main focus was making new features, encoding categoricals, scaling numbers, and putting it all into a sklearn pipeline with LinearRegression.

Some steps I figured out myself, a few I needed help with (notes below).

## How to run

1. Open `ml-pipeline.ipynb`
2. Run cells from the top
3. Keep `ecommerce_sales_analytics_5000.csv` in this folder

Needs: `pandas`, `numpy`, `scikit-learn`

## What I did

**Part 1 — features**
- Made a couple new columns from existing ones (like price-related / revenue stuff)
- Date/text step: extracted parts from date if available (or noted if skipped)

**Part 2 — encoding**
- Found categorical columns
- Tried `pd.get_dummies` first (just to see how it works)
- Then used `ColumnTransformer` + `OneHotEncoder` (this is the cleaner way)

**Part 3 — scaling**
- `StandardScaler` on numerical cols (mean ~0, std ~1)
- `MinMaxScaler` too (values between 0 and 1) and compared both

**Part 4 — pipeline**
- Built num pipeline (scaling) + cat pipeline (one-hot), combined with ColumnTransformer
- Full pipeline: preprocess → LinearRegression
- Train/test split, fit, predict, checked MSE and R²
- Wrote short answers for why pipelines help

## Where I struggled

- `get_dummies` gave True/False instead of 0/1 — fixed with `dtype=int`
- After `ColumnTransformer.fit_transform`, I lost column names until I used `get_feature_names_out()`
- Setting up the full Pipeline was a bit confusing at first (what goes in num vs cat, and not leaking scaling onto test data)

## Files

- `ml-pipeline.ipynb` — notebook
- `ecommerce_sales_analytics_5000.csv` — dataset
- `README.md` — this file
