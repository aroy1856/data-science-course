# Assignment 16 - SVM, Trees, Ensembles, Validation

Telecom churn dataset (`telecom_churn.csv`). Covers SVM, decision trees, train/val/test splits, cross-validation, bagging vs boosting, and random forest. No deep learning — just sklearn stuff.

## How to run

1. Open `advanced-ml-algorithms.ipynb`
2. Run from the top
3. Keep `telecom_churn.csv` in this folder

Needs: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`

## What I did

**Part 1 — SVM & Decision Trees**
- Used telecom churn data, scaled numerical features only
- SVM with linear kernel (~85% acc) vs RBF kernel (~92% acc) — RBF did better on this data
- Decision tree with visualization, compared low vs high `max_depth` for over/underfitting (high depth had higher train acc but gap between train/test got bigger)

**Part 2 — Validation & Cross-Validation**
- Split train into train + validation (on top of existing test split)
- Tuned `max_depth` manually by looping values and checking validation accuracy — best was 5 (~91% val acc)
- Evaluated final model on test set
- Also ran 5-fold CV with GridSearchCV and compared CV score (~93%) vs single test accuracy (~91%)

**Part 3 — Ensembles**
- Wrote up bagging vs boosting concepts (Task 5.1)
- Trained `BaggingClassifier` and `AdaBoostClassifier` (both with decision tree base, 10 estimators, max_depth=3)
- AdaBoost beat bagging on test (~92% vs ~89%)
- Random Forest (~89%) was similar to bagging, both a bit below AdaBoost. Printed feature importances.

## Where I struggled

- `base_estimator` param got renamed to `estimator` in newer sklearn — had to fix that for Bagging/AdaBoost or it throws TypeError
- Task 3 vs Task 4 confused me at first — manual validation loop is different from GridSearchCV with `cv=5`
- Tree plot with all features was huge, had to limit depth to make it readable
- RBF SVM took longer to train than linear, worth keeping in mind on bigger datasets

## Files

- `advanced-ml-algorithms.ipynb` — notebook
- `telecom_churn.csv` — dataset
- `ecommerce_sales_analytics_5000.csv` — extra file in folder (didn't use for this one)
- `README.md` — this file
