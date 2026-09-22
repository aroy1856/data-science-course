# Final Report — Global Pollution Analysis and Energy Recovery

**Assignment:** Machine Learning Assignment 2  
**Notebook:** `Global_Pollution_Analysis.ipynb`  
**Dataset:** `Global_Pollution_Analysis.csv`

---

## 1. Objective

Analyze global pollution indicators and model:

1. **Linear Regression** — predict **Energy Recovered (GWh)** from pollution / waste / economy features  
2. **Logistic Regression** — classify rows into **Low / Medium / High** pollution severity  

Also explore trends over years and across countries, and suggest where waste-to-energy or pollution controls could help.

---

## 2. Dataset Description

| Item | Detail |
|------|--------|
| Rows | 200 country–year records |
| Columns | 13 |
| Years covered | 2000–2019 |
| Unique countries | 175 |
| Missing values | None |

### Columns (renamed in notebook for easier use)

| Original name | Working name | Role |
|---------------|--------------|------|
| Country | Country | Categorical (label-encoded) |
| Year | Year | Time feature |
| Air_Pollution_Index | Air_Pollution_Index | Pollution feature |
| Water_Pollution_Index | Water_Pollution_Index | Pollution feature |
| Soil_Pollution_Index | Soil_Pollution_Index | Pollution feature |
| Industrial_Waste (in tons) | Industrial_Waste | Waste feature |
| Energy_Recovered (in GWh) | Energy_Recovered | **Regression target** |
| CO2_Emissions (in MT) | CO2_Emissions | Emissions feature |
| Renewable_Energy (%) | Renewable_Energy | Energy mix feature |
| Plastic_Waste_Produced (in tons) | Plastic_Waste | Waste feature |
| Energy_Consumption_Per_Capita (in MWh) | Energy_Per_Capita | Per-capita energy |
| Population (in millions) | Population | Scale feature |
| GDP_Per_Capita (in USD) | GDP_Per_Capita | Economy feature |

### Key descriptive stats (approx.)

| Feature | Mean | Median | Notes |
|---------|------|--------|-------|
| Air_Pollution_Index | ~181 | ~183 | Wide spread (≈50–298) |
| CO2_Emissions (MT) | ~25 | ~25 | |
| Industrial_Waste (tons) | ~52.9k | ~55.3k | |
| Energy_Recovered (GWh) | ~260 | ~273 | Regression target |
| Energy_Per_Capita (MWh) | ~9.4 | ~9.2 | Already in dataset |

---

## 3. Preprocessing

### 3.1 Missing values

- Checked with `isna().sum()` → **0 missing**  
- Kept a median `fillna` loop as practice (no-op on this file)

### 3.2 Column cleanup

- Renamed long unit suffixes to short names (`Industrial_Waste`, `Energy_Recovered`, etc.)

### 3.3 Encoding

- **Country:** `LabelEncoder` (175 countries; one-hot would explode on n=200)  
- **Year:** kept numeric for trends; also stored `Year_Encoded`

### 3.4 Scaling

- Pollution indices (Air / Water / Soil) standardized with `StandardScaler` (`Air_Scaled`, etc.)  
- Model matrices also scaled before Linear / Logistic Regression

---

## 4. Exploratory Data Analysis

### 4.1 Descriptive statistics

Computed mean / median / variance for CO₂, industrial waste, pollution indices, and energy recovered.

### 4.2 Correlation with Energy_Recovered

Heatmap of numeric features showed **weak linear relationships** with `Energy_Recovered`. Strongest among weak signals:

| Feature | Corr with Energy_Recovered (approx.) |
|---------|--------------------------------------|
| Industrial_Waste | ~-0.16 |
| Year | ~0.09 |
| Soil_Pollution_Index | ~0.06 |
| Air_Pollution_Index | ~0.00 |
| CO2_Emissions | ~0.02 |

So pollution level alone does **not** strongly predict energy recovery in this sample.

### 4.3 Visualizations

- **Line plots:** yearly average Air Pollution and Energy Recovered (2000–2019)  
- **Bar chart:** top countries by average CO₂  
- **Box plots:** Air / Water / Soil indices and Energy Recovered distribution  

---

## 5. Feature Engineering

1. **Yearly trends**  
   - `Year_Avg_Energy_Recovered`  
   - `Year_Avg_Air_Pollution`  

2. **Per-capita style features**  
   - Dataset already includes `Energy_Per_Capita`  
   - Added `Industrial_Waste_Per_Capita` and `Plastic_Waste_Per_Capita` (waste ÷ population in people)

3. **Pollution_Score**  
   - Simple average of Air + Water + Soil indices  
   - Used for severity labels (Low / Medium / High via tertiles)

---

## 6. Predictive Modelling

Split: **80% train / 20% test**, `random_state=42`.

### 6.1 Linear Regression — Energy Recovered (GWh)

**Features used (examples):** Air / Water / Soil indices, Industrial_Waste, CO₂, Plastic_Waste, Renewable_Energy, Energy_Per_Capita, Population, GDP_Per_Capita, Year, Country_Encoded, Pollution_Score, yearly air trend, waste per capita.

| Metric | Approx. value |
|--------|----------------|
| MSE | ~29,240 |
| RMSE | ~171 GWh |
| MAE | ~150 GWh |
| R² | ~-0.21 |

**Interpretation:** Negative R² means the model underperforms a mean baseline on the test set. This matches the weak correlations in EDA — energy recovery is not well explained by a linear combo of these pollution features here. Pipeline and metrics are still completed as required.

### 6.2 Logistic Regression — Pollution severity (Low / Medium / High)

**Label:** tertiles of `Pollution_Score`  
**Features:** Air / Water / Soil indices, CO₂, industrial & plastic waste, renewables, energy per capita, GDP, Year, Country_Encoded  

| Metric | Approx. value |
|--------|----------------|
| Accuracy | ~0.98 |
| Precision / Recall / F1 | ~0.93–1.00 by class |
| Confusion matrix | Nearly diagonal (see notebook) |

**Interpretation:** Accuracy is high because severity labels are derived from the same pollution indices used as inputs (especially Air/Water/Soil). That is expected for this labelling choice — the classifier mainly recovers the tertile structure. It is still a valid demonstration of multinomial logistic classification, metrics, and confusion-matrix reporting.

---

## 7. Model Comparison

| Aspect | Linear Regression | Logistic Regression |
|--------|-------------------|---------------------|
| Goal | Predict Energy_Recovered (GWh) | Tag Low / Medium / High pollution |
| Output | Continuous | Class label |
| Metrics | R², MSE, MAE | Accuracy, Precision, Recall, F1, CM |
| Observed performance | Weak (R² &lt; 0) | Strong (~97–98% acc) |
| Practical use | ETA-style energy recovery estimate (needs better features/data) | Severity flagging / screening |

**Takeaway:** The two models answer different questions. On this dataset, severity classification works well by construction; energy-recovery regression does not — more process-level data (plant capacity, waste composition, recovery technology) would be needed for a useful energy model.

---

## 8. Actionable Insights & Recommendations

### 8.1 Countries that may benefit from better energy recovery

Rough ranking of **higher pollution / relatively lower energy recovery** (from notebook summary) included places such as:

- Christmas Island, Bolivia, Colombia, Tajikistan, Zimbabwe  
- Kyrgyz Republic, Saint Lucia, Saint Helena, Djibouti, Pakistan  

These are candidates to study for **waste-to-energy** and industrial waste capture (not absolute policy conclusions — sample is small and many countries appear only once).

### 8.2 Lower pollution / stronger renewable examples

Examples with lower average `Pollution_Score` and relatively higher renewables included Cape Verde, Cyprus, Kiribati, Portugal, etc. Useful as peer benchmarks for renewable share vs pollution profile.

### 8.3 Recommendations

1. **Waste-to-energy investment** where industrial/plastic waste is high but `Energy_Recovered` is low  
2. **Raise renewable share** in high-CO₂, low-recovery settings  
3. **Joint monitoring** of Air + Water + Soil (`Pollution_Score`) for severity alerts  
4. **Per-capita framing** (energy & waste per person) for fairer cross-country comparison  
5. **Data quality:** collect plant-level recovery rates, waste composition, and policy indicators — current features barely explain Energy_Recovered linearly  

---

## 9. Deliverables Checklist

| Deliverable | Status |
|-------------|--------|
| Jupyter notebook (full analysis) | Done — `Global_Pollution_Analysis.ipynb` |
| Visualizations (heatmap, line/bar/box, scatter, CM) | Done (in notebook) |
| Final report | Done — this document |

---

## 10. Limitations

- Only 200 rows; most countries appear rarely → country effects are noisy  
- Weak link between pollution features and Energy_Recovered  
- Logistic labels built from pollution indices → optimistic classification accuracy  
- Linear & logistic models only (as required); richer models won’t fix missing process features  

---

*Report corresponding to `Global_Pollution_Analysis.ipynb`.*
