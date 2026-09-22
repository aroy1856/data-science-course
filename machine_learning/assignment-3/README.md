# Assignment 3 - Food Delivery Time Prediction (NB / KNN / Decision Tree)

Binary classification: predict **Fast** vs **Delayed** delivery using **Gaussian Naive Bayes**, **KNN**, and **Decision Tree**.

## How to run

1. Open `Food_Delivery_Time_Prediction.ipynb`
2. Run all cells from the top
3. Keep `Food_Delivery_Time_Prediction.csv` in this folder

Packages used: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`

## What I did

**Phase 1 — preprocessing + EDA**

- Loaded CSV, checked missing values (none)
- Parsed lat/lon; encoded cats + scaled nums in a sklearn pipeline
- EDA: stats, correlation heatmap, scatter/box/pair plots, IQR outliers
- Feature eng: Haversine distance, `Rush_Hour`, binary `Delayed` from median `Delivery_Time`

**Phase 2 — classifiers**

- GaussianNB, KNeighborsClassifier, DecisionTreeClassifier
- Shared `ColumnTransformer` + `Pipeline` (columns taken from `Xc_train` only)
- Metrics: accuracy, precision, recall, F1, confusion matrix (+ ROC plots)

**Phase 3 — comparison + report**

- Side-by-side metric printout and CM/ROC for each model
- Full write-up in `Final_Report.md`

## Notes

- Feature–delay signal is weak → accuracies hover around ~0.43–0.50
- KNN was slightly best on this split; Decision Tree is more interpretable
- Task brief: `Naive Bayes, (KNN), Decision Tree,- Food Delivery Time Prediction.md`

## Files

- `Food_Delivery_Time_Prediction.ipynb` — main notebook
- `Food_Delivery_Time_Prediction.csv` — dataset
- `Naive Bayes, (KNN), Decision Tree,- Food Delivery Time Prediction.md` — assignment brief
- `Final_Report.md` — standalone final report
- `README.md` — this file
