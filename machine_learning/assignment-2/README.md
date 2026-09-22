# Assignment 2 - Global Pollution Analysis and Energy Recovery

Analyze pollution indicators and model **energy recovery** (Linear Regression) plus **pollution severity** Low/Medium/High (Logistic Regression).

## How to run

1. Open `Global_Pollution_Analysis.ipynb`
2. Run all cells from the top
3. Keep `Global_Pollution_Analysis.csv` in this folder

Packages used: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`

## What I did

**Phase 1 — data + EDA**

- Loaded CSV, checked missing values (none)
- Renamed long column names for easier coding
- Label-encoded Country; kept Year numeric; scaled Air/Water/Soil indices
- Descriptive stats, correlation heatmap
- Line / bar / box plots for yearly trends and country CO₂

**Feature engineering**

- Yearly averages for energy recovered and air pollution
- Kept `Energy_Per_Capita`; added waste-per-capita features
- `Pollution_Score` = mean of Air + Water + Soil

**Phase 2 — models**

- Linear Regression → predict `Energy_Recovered` (GWh)  
  Metrics: MSE, RMSE, MAE, R²
- Logistic Regression → Low / Medium / High pollution (tertiles of Pollution_Score)  
  Metrics: accuracy, precision, recall, F1, confusion matrix

**Phase 3 — comparison + report**

- Confusion matrix + model comparison prints
- Country-level rough list for recovery-gap insights
- Full write-up in `Final_Report.md`

## Notes

- Energy recovery is weakly correlated with pollution features here → linear R² is poor
- Logistic accuracy is high because severity labels come from the same pollution indices
- Task brief: `Global Pollution Analysis and Energy Recovery.md`

## Files

- `Global_Pollution_Analysis.ipynb` — main notebook
- `Global_Pollution_Analysis.csv` — dataset
- `Global Pollution Analysis and Energy Recovery.md` — assignment brief
- `Final_Report.md` — standalone final report
- `README.md` — this file
