# Assignment 15 - ML Algorithms & Metrics

Same ecommerce CSV as assignment 14. This one is more about actually training models (linear/logistic regression, naive bayes, KNN) and checking if they’re any good with different metrics. Also overfitting/underfitting stuff at the end.

## How to run

1. Open `ml-algorithms.ipynb`
2. Run from the top
3. Keep `ecommerce_sales_analytics_5000.csv` in this folder

Needs: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`

## What I did

**Part 1 — Linear Regression**
- Target = `revenue`, pipeline with preprocessing
- Train/test split, predict, actual vs predicted plot

**Part 2 — Regression metrics**
- MAE, MSE, RMSE on test predictions + short interpretation

**Part 3 — Classification**
- Made a classification target, logistic regression, naive bayes, KNN with different k values
- Compared logistic vs naive bayes accuracy

**Part 4 — Classification metrics**
- Accuracy, precision, recall, F1 via classification report + confusion matrix for all 3 models

**Part 5 — Model behavior**
- k=1 vs k=100 KNN to show overfit vs underfit (train vs test accuracy)
- Wrote bias/variance answers tied to what we saw in Task 7

## Where I struggled

- Dates had to be split into year/month/day — can’t pass raw datetime to sklearn
- Accidentally named variables `confusion_matrix` same as the function → weird TypeError until I renamed to `cm`
- k=1 vs k=100 naming was confusing at first (k=1 is actually the “overfit” one)

## Files

- `ml-algorithms.ipynb` — notebook
- `ecommerce_sales_analytics_5000.csv` — dataset
- `README.md` — this file
