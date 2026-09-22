# Assignment 1 - Food Delivery Time Prediction

Predict food delivery time from distance, weather, traffic, vehicle type, and related features. Covers preprocessing, EDA, feature engineering, then **Linear Regression** (time) and **Logistic Regression** (Fast vs Delayed).

## How to run

1. Open `Food_Delivery_Time_Prediction.ipynb`
2. Run all cells from the top
3. Keep `Food_Delivery_Time_Prediction.csv` in this folder

Packages used: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`

## What I did

**Phase 1 — data + EDA**

- Loaded CSV, checked missing values (none in this set)
- Parsed lat/lon out of `Customer_Location` / `Restaurant_Location` strings
- Encoded categoricals (one-hot / `get_dummies`) and standardized numeric cols
- Descriptive stats (mean / median / mode / variance), correlation heatmap
- Scatter / box / pair plots; IQR outlier check on Distance & Delivery_Time

**Feature engineering**

- Haversine distance from lat/lon (Distance column already exists, still computed it)
- `Rush_Hour` from Order_Time (Morning / Evening = 1)

**Phase 2 — models**

- Linear Regression → predict continuous `Delivery_Time` (80/20 split)
  - Metrics: MSE, RMSE, MAE, R²
- Logistic Regression → Fast vs Delayed (median Delivery_Time as cutoff)
  - Metrics: accuracy, precision, recall, F1, confusion matrix

**Phase 3 — comparison + report**

- Confusion matrix + ROC curve for logistic model
- Full write-up in `Final_Report.md` (dataset, preprocessing, model comparison, recommendations)

## Notes

- Correlations with `Delivery_Time` are weak in this dataset, so model scores are not great — still ran the full pipeline as required.
- Full task list is in `Food_Delivery_Time_Prediction_tasks.md`
- Detailed final report: `Final_Report.md`

## Files

- `Food_Delivery_Time_Prediction.ipynb` — main notebook
- `Food_Delivery_Time_Prediction.csv` — dataset
- `Food_Delivery_Time_Prediction_tasks.md` — assignment brief
- `Final_Report.md` — standalone final report
- `README.md` — this file
