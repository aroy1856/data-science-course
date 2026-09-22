# Final Report — Food Delivery Time Prediction

**Assignment:** Machine Learning Assignment 1  
**Notebook:** `Food_Delivery_Time_Prediction.ipynb`  
**Dataset:** `Food_Delivery_Time_Prediction.csv`

---

## 1. Objective

The goal of this project is to predict food delivery times using order, location, weather, traffic, and rider-related features. Two modelling approaches were used:

1. **Linear Regression** — predict continuous `Delivery_Time` (minutes)
2. **Logistic Regression** — classify deliveries as **Fast** or **Delayed**

The work covers data preprocessing, exploratory data analysis (EDA), feature engineering, model training/evaluation, and operational recommendations.

---

## 2. Dataset Description

| Item | Detail |
|------|--------|
| Rows | 200 orders |
| Columns | 15 original features |
| Target | `Delivery_Time` (minutes) |
| Missing values | None |

### Original columns

| Column | Type | Description |
|--------|------|-------------|
| `Order_ID` | ID | Unique order identifier (dropped for modelling) |
| `Customer_Location` | string `(lat, lon)` | Customer coordinates |
| `Restaurant_Location` | string `(lat, lon)` | Restaurant coordinates |
| `Distance` | numeric | Provided distance between restaurant and customer |
| `Weather_Conditions` | categorical | Rainy, Sunny, Snowy, Cloudy |
| `Traffic_Conditions` | categorical | Low, Medium, High |
| `Delivery_Person_Experience` | numeric | Rider experience (1–10) |
| `Order_Priority` | categorical | Low, Medium, High |
| `Order_Time` | categorical | Morning, Afternoon, Evening, Night |
| `Vehicle_Type` | categorical | Bike, Bicycle, Car |
| `Restaurant_Rating` | numeric | Restaurant rating |
| `Customer_Rating` | numeric | Customer rating |
| `Delivery_Time` | numeric | Target — delivery duration (minutes) |
| `Order_Cost` | numeric | Order value |
| `Tip_Amount` | numeric | Tip given |

### Key descriptive statistics (`Delivery_Time`)

| Stat | Value |
|------|-------|
| Mean | ~70.5 min |
| Median | ~72.8 min |
| Std | ~29.8 min |
| Min / Max | 15.2 / 119.7 min |

Average distance is about **11.5 km**. Weather, traffic, priority, time-of-day, and vehicle type are fairly balanced across categories.

---

## 3. Preprocessing Steps

### 3.1 Missing values & basic cleanup

- Checked nulls with `isna().sum()` — **no missing values**, so no imputation was required.
- Dropped `Order_ID` (not useful for prediction).

### 3.2 Location parsing

`Customer_Location` and `Restaurant_Location` were stored as strings like `(17.03, 79.74)`. These were split into numeric columns:

- `Customer_Location_lat`, `Customer_Location_lon`
- `Restaurant_Location_lat`, `Restaurant_Location_lon`

Original string location columns were then dropped.

### 3.3 Encoding categorical variables

Categorical features (`Weather_Conditions`, `Traffic_Conditions`, `Order_Priority`, `Order_Time`, `Vehicle_Type`) were one-hot encoded:

- Pipeline path: `OneHotEncoder` via `ColumnTransformer`
- Modelling path: `pd.get_dummies(..., drop_first=True)` to avoid dummy-variable trap

### 3.4 Scaling numeric features

Continuous predictors (e.g. `Distance`, `Order_Cost`, ratings, experience) were standardized with `StandardScaler` before fitting Linear / Logistic Regression so feature scales do not dominate the fit.

### 3.5 Outlier handling

Boxplots were used for `Distance`, `Delivery_Time`, `Order_Cost`, and `Tip_Amount`. An IQR rule (±1.5 × IQR) was applied to `Delivery_Time` and `Distance`. In this dataset, no rows were removed (values stayed within fences).

---

## 4. Exploratory Data Analysis (EDA)

### 4.1 Descriptive statistics

Computed mean, median, mode, and variance for numeric columns to understand central tendency and spread.

### 4.2 Correlation analysis

A correlation heatmap was plotted for numeric features against `Delivery_Time`.

**Finding:** Correlations with `Delivery_Time` are **weak** (absolute values mostly under ~0.1). Even `Distance` does not show a strong linear relationship with delivery time in this sample. That limits how well simple linear models can perform.

### 4.3 Visual EDA

- Scatter: Distance vs Delivery Time  
- Boxplots: Traffic / Weather vs Delivery Time  
- Pair plot: Distance, Delivery Time, Order Cost, Experience  

These plots support the same conclusion: relationships look noisy rather than strongly structured.

---

## 5. Feature Engineering

### 5.1 Haversine distance

Even though a `Distance` column already exists, distance was recomputed from lat/lon using the Haversine formula (great-circle distance in km) as `Haversine_Distance`.

**Note:** Haversine values in this file are often much larger than the provided `Distance` column, which suggests the given Distance is likely a **route/operational distance** (or generated separately), not raw geodesic distance. For modelling, the provided `Distance` feature was kept as the main distance signal; Haversine was used as an engineering check.

### 5.2 Rush Hour

Created binary feature `Rush_Hour`:

- `1` if `Order_Time` is **Morning** or **Evening**
- `0` otherwise (Afternoon / Night)

Counts were roughly balanced (~96 rush vs ~104 non-rush).

---

## 6. Predictive Modelling

Train/test split: **80% train / 20% test**, `random_state=42`.

Features used (after encoding): Distance, experience, ratings, order cost, tip, rush hour, and one-hot weather/traffic/priority/time/vehicle columns. Raw lat/lon and Haversine were excluded from the final feature matrix to reduce redundancy/noise.

### 6.1 Linear Regression (continuous `Delivery_Time`)

| Metric | Value (approx.) |
|--------|------------------|
| MSE | ~1021.9 |
| RMSE | ~32.0 min |
| MAE | ~27.2 min |
| R² | ~-0.11 |

**Interpretation:** Negative R² means the model performs worse than predicting the mean delivery time on the test set. This matches the weak feature–target correlations found in EDA. The model pipeline is correct; the dataset itself does not contain a strong linear signal for ETA prediction.

### 6.2 Logistic Regression (Fast vs Delayed)

Binary target was created using the median delivery time (~72.8 min):

- **Fast** = Delivery_Time ≤ median  
- **Delayed** = Delivery_Time > median  

(100 Fast / 100 Delayed overall — balanced classes.)

| Metric | Value (approx.) |
|--------|------------------|
| Accuracy | ~0.43 |
| Precision / Recall / F1 | ~0.39–0.47 (see classification report in notebook) |
| ROC AUC | ~0.36 |

Confusion matrix and ROC curve are plotted in the notebook.

**Interpretation:** Accuracy near chance and AUC below 0.5 again indicate that available predictors do not cleanly separate Fast vs Delayed in this sample. The classification workflow (thresholding, metrics, CM, ROC) was still completed as required.

---

## 7. Model Comparison

| Aspect | Linear Regression | Logistic Regression |
|--------|-------------------|---------------------|
| Goal | Estimate delivery minutes | Flag Fast vs Delayed |
| Output | Continuous prediction | Class + probability |
| Key metrics | MSE, MAE, R² | Accuracy, Precision, Recall, F1, CM, ROC |
| Observed performance | Weak (R² &lt; 0) | Weak (~chance accuracy) |
| Practical use (if data were stronger) | Customer ETA | Ops risk flag / staffing alert |

**Conclusion:** Both models address different business questions. On *this* dataset, neither is reliable for production decisions because features are weakly related to delivery time. With better real-world telemetry (actual road time, prep delay, live traffic), the same pipeline would be more informative.

---

## 8. Actionable Insights & Recommendations

Even with weak predictive power here, the intended operational actions from this kind of analysis are:

1. **Route optimization**  
   Prioritize shorter / less congested paths when Distance and Traffic are high; integrate live traffic APIs in a real system.

2. **Staffing by time of day**  
   Increase rider coverage during Rush Hour (Morning & Evening) when order volume and congestion typically rise.

3. **Vehicle allocation**  
   Prefer Bike/Car over Bicycle in Rainy/Snowy weather or High traffic zones to reduce delay risk.

4. **Rider training & assignment**  
   Pair low-experience riders with easier routes; use experience as a soft constraint in assignment logic.

5. **Customer communication**  
   If a delay classifier improves on richer data, use it to warn customers early and reduce complaint volume.

6. **Data quality next steps**  
   Collect prep time, live traffic index, weather severity, and actual GPS path length. The current Distance vs Haversine mismatch should be investigated before trusting distance features.

---

## 9. Deliverables Checklist

| Deliverable | Status |
|-------------|--------|
| Jupyter notebook with preprocessing, training, evaluation | Done — `Food_Delivery_Time_Prediction.ipynb` |
| Visualizations (scatter, pair, heatmap, CM, ROC) | Done (in notebook) |
| Final report (dataset, preprocessing, comparison, recommendations) | Done — this document |

---

## 10. Limitations & Future Work

- Sample size is small (n = 200).
- Feature–target relationships appear weak / possibly synthetic-noise-like.
- Only Linear and Logistic Regression were required; tree-based or regularized models might be tried later, but they will not fix a fundamentally weak signal.
- Better labels (true delay causes) and richer features are the highest-impact next steps.

---

*Report corresponding to the analysis in `Food_Delivery_Time_Prediction.ipynb`.*
