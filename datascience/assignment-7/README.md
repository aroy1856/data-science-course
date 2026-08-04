# Cardiac Diagnostics

Heart disease classification on `heart.csv`.

## How to run

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

Open `ass-7.ipynb` and run all cells. Keep `heart.csv` in this folder.

## What is in the notebook

- EDA (target balance, correlation, boxplots)
- one-hot encode categorical columns
- train/test split + 5-fold cv
- compare Logistic Regression, Decision Tree, Random Forest, KNN
- metrics, confusion matrix, ROC
- logistic regression coefficients as feature importance
- short writeup on what mattered for cardiac risk in this data
