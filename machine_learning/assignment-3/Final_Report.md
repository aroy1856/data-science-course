# Final Report — Food Delivery Time Prediction (Naive Bayes, KNN, Decision Tree)

**Assignment:** Machine Learning Assignment 3  
**Notebook:** `Food_Delivery_Time_Prediction.ipynb`  
**Dataset:** `Food_Delivery_Time_Prediction.csv`  
**Brief:** `Naive Bayes, (KNN), Decision Tree,- Food Delivery Time Prediction.md`

---

## 1. Objective

Predict whether a delivery will be **Fast** or **Delayed** (binary classification) using customer/restaurant location, weather, traffic, vehicle type, and related features.

Three classifiers were trained and compared:

1. **Gaussian Naive Bayes**
2. **K-Nearest Neighbors (KNN)**
3. **Decision Tree**

---

## 2. Dataset Description

| Item | Detail |
|------|--------|
| Rows | 200 orders |
| Original columns | 15 |
| Target (engineered) | `Delayed` (1 = delayed, 0 = fast) |
| Missing values | None |

Main features include `Distance`, `Weather_Conditions`, `Traffic_Conditions`, `Delivery_Person_Experience`, `Order_Priority`, `Order_Time`, `Vehicle_Type`, ratings, `Order_Cost`, `Tip_Amount`, and lat/lon parsed from location strings.

`Delivery_Time` (minutes) has mean ≈ 70.5 and median ≈ 72.8. The binary label uses the **median** as cutoff: above median → Delayed, otherwise Fast (balanced 100/100 overall).

---

## 3. Preprocessing & Feature Engineering

1. **Missing values:** checked; none present (median fill kept as practice only).
2. **Locations:** parsed `Customer_Location` / `Restaurant_Location` into lat/lon floats.
3. **Encoding / scaling:** categorical cols one-hot encoded; numeric cols standardized inside sklearn `Pipeline` + `ColumnTransformer`.
4. **Haversine distance:** computed from lat/lon (Distance column also exists).
5. **Rush_Hour:** Morning/Evening = 1, else 0.
6. **Label:** `Delayed` from median `Delivery_Time`.
7. **Train/test split:** 80/20, `random_state=42`.

Dropped from model features: raw `Delivery_Time` (leakage), lat/lon (replaced by Distance / Haversine usage in EDA; lat/lon dropped from `X`), and `Haversine_Distance` in the classifier matrix to avoid redundancy with `Distance`.

---

## 4. Models

All three share the same preprocessing pipeline, then a classifier:

| Model | Sklearn class | Notes |
|-------|---------------|--------|
| Naive Bayes | `GaussianNB` | Assumes feature independence / Gaussian continuous features |
| KNN | `KNeighborsClassifier` | Default `n_neighbors=5` |
| Decision Tree | `DecisionTreeClassifier` | Default depth (can overfit on small data) |

---

## 5. Evaluation Results (test set, approx.)

| Model | Accuracy | Precision | Recall | F1-score |
|-------|----------|-----------|--------|----------|
| KNN | ~0.50 | ~0.52 | ~0.52 | ~0.52 |
| Naive Bayes | ~0.43 | ~0.46 | ~0.52 | ~0.49 |
| Decision Tree | ~0.45 | ~0.48 | ~0.48 | ~0.48 |

Confusion matrices and ROC-style plots for each model are in the notebook (Phase 3).

**Interpretation:** Scores are near chance. Correlations between features and `Delivery_Time` / delay labels are weak in this dataset, so all three struggle. Among them, **KNN** edged the others slightly on this split.

---

## 6. Model Comparison — Strengths & Weaknesses

| Model | Strengths | Weaknesses |
|-------|-----------|------------|
| **Naive Bayes** | Fast, simple, works with small data | Independence assumption often wrong; weakest accuracy here |
| **KNN** | No heavy training, flexible decision boundary | Sensitive to scaling/K; slow on large data; best of three here but still ~50% |
| **Decision Tree** | Easy to interpret (rules) | Overfits easily; unstable on noisy labels |

**Recommendation for this task**

- If the priority is **slightly better predictive score on this sample:** prefer **KNN** (after tuning `k` with CV in a follow-up).
- If the priority is **interpretability for ops** (why an order looks delayed): prefer a **pruned Decision Tree** (`max_depth`, `min_samples_split`).
- **Naive Bayes** is a useful baseline but was weakest here.

Given weak signal in the CSV, improving features / data quality matters more than swapping classifiers.

---

## 7. Actionable Insights

1. Treat delay risk as a **screening signal**, not a hard promise — models are not reliable enough yet on this data.
2. Ops levers that still make sense from domain knowledge: route optimization in high traffic, more staff in rush hours, faster vehicles in bad weather, training for low-experience riders.
3. Next modelling steps: tune KNN `k` and tree depth with cross-validation; try class-balanced metrics; collect stronger features (prep time, live traffic).

---

## 8. Deliverables Checklist

| Deliverable | Status |
|-------------|--------|
| Notebook with preprocessing + NB / KNN / DT | Done |
| Visualizations (EDA, CM, ROC) | Done (in notebook) |
| Final report | Done — this document |

---

*Report corresponding to `Food_Delivery_Time_Prediction.ipynb` (Assignment 3).*
