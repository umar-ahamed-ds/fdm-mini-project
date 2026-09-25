# Stage 4 — Data Preprocessing and Feature Engineering

## Wildfire Risk Prediction System

---

# 1. Overview

Data preprocessing is an essential step in machine learning because raw
datasets often contain duplicate records, invalid values, inconsistent
formats, and variables that cannot be directly used by machine learning
algorithms.

The objective of this stage was to transform the raw wildfire dataset into a
clean, structured, and machine-learning-ready dataset while preventing data
leakage.

The preprocessing pipeline followed the workflow:

```
Raw Dataset
      |
      ↓
Duplicate Removal
      |
      ↓
Sentinel Value Handling
      |
      ↓
Missing Value Analysis
      |
      ↓
Date Feature Engineering
      |
      ↓
Target Encoding
      |
      ↓
Feature Selection
      |
      ↓
Time-Based Train/Test Split
      |
      ↓
Scaling Decision
      |
      ↓
Processed Dataset
```

---

# Pipeline Node 01 — Remove Duplicate Records

## Concept

Duplicate records are identical observations that appear multiple times in a
dataset.

Keeping duplicates can negatively affect machine learning because repeated
records receive higher importance during training and may introduce bias.

Only complete duplicate rows were considered duplicates.

Rows with the same location but different dates were preserved because they
represent different temporal observations.

---

## Observation from EDA

Duplicate analysis was performed using:

```python
df.duplicated().sum()
```

The dataset contained:

```
13,920 duplicate records
```

The duplicate check was performed across all attributes rather than only
selected columns.

---

## Preprocessing Activity

Exact duplicate rows were removed using:

```python
df_processed = df_processed.drop_duplicates()
```

---

## Result

Before:

```
9,509,925 rows
```

After:

```
9,496,005 rows
```

Removed:

```
13,920 rows
```

---

# Pipeline Node 02 — Handle Sentinel Values

## Concept

Sentinel values are special values used to represent missing or unavailable
data.

Instead of storing missing measurements as NaN, some datasets use placeholder
values such as:

```
32767
```

Machine learning algorithms interpret these values as real numbers, which can
create incorrect patterns.

---

## Observation from EDA

Initial missing value analysis showed:

```
NaN values = 0
```

However, statistical analysis identified impossible values.

Example:

```
Maximum temperature = 32767
```

Further investigation showed that weather variables contained:

```
32767
```

in:

```
pr
rmax
rmin
sph
srad
tmmn
tmmx
vs
bi
fm100
fm1000
erc
etr
pet
vpd
```

A total of:

```
25,725 records
```

contained these invalid values.

---

## Decision

The affected records were removed.

Reason:

- Weather information was completely unavailable.
- Imputation could create artificial weather conditions.
- Only a small percentage of the dataset was affected.

---

## Preprocessing Activity

Rows containing sentinel values were removed:

```python
df_processed = df_processed[
    ~(df_processed == 32767).any(axis=1)
]
```

---

## Result

Before:

```
9,496,005 rows
```

After:

```
9,470,280 rows
```

Removed:

```
25,725 rows
```

---

# Pipeline Node 03 — Missing Value Handling

## Concept

Missing values represent unavailable information.

Common approaches include:

- removing incomplete records
- mean/median imputation
- forward/backward filling

The appropriate method depends on the meaning and amount of missing data.

---

## Observation from EDA

Initial analysis:

```python
df.isnull().sum()
```

showed:

```
No NaN values
```

The dataset represented missing weather information using the sentinel value
32767 instead.

After sentinel handling, missing values were checked again.

---

## Decision

No imputation was performed.

Reason:

- No actual missing values remained.
- Sentinel records were already removed.
- Artificial weather estimation was avoided.

---

## Preprocessing Activity

Verification:

```python
df_processed.isnull().sum()
```

Result:

```
All columns = 0
```

---

# Pipeline Node 04 — Date Feature Engineering

## Concept

Machine learning models cannot directly understand raw date strings.

The datetime attribute was transformed into numerical features that represent
seasonal and yearly patterns.

---

## Observation from EDA

The dataset covered:

```
2013-12-31 → 2025-04-13
```

The long time range indicated that temporal patterns may influence wildfire
occurrence.

Monthly analysis also showed seasonal differences in wildfire occurrence.

---

## Decision

The datetime column was transformed into:

| Feature | Purpose |
|---|---|
| year | Capture yearly variation |
| month | Capture seasonal patterns |
| day_of_year | Capture detailed seasonal position |

---

## Preprocessing Activity

Datetime conversion:

```python
df_processed["datetime"] = pd.to_datetime(
    df_processed["datetime"]
)
```

Feature extraction:

```python
df_processed["year"] = df_processed["datetime"].dt.year

df_processed["month"] = df_processed["datetime"].dt.month

df_processed["day_of_year"] = df_processed["datetime"].dt.dayofyear
```

Original datetime column removed:

```python
df_processed.drop(
    columns=["datetime"]
)
```

---

# Pipeline Node 05 — Target Encoding

## Concept

Machine learning algorithms require numerical target labels.

The wildfire target was converted from categorical values into binary values.

---

## Observation from EDA

Target distribution:

```
No wildfire  : 9,007,860
Wildfire     : 502,065
```

The problem was identified as binary classification.

---

## Decision

Mapping applied:

```
No  → 0

Yes → 1
```

---

## Preprocessing Activity

```python
df_processed["Wildfire"] = df_processed["Wildfire"].map(
{
    "No":0,
    "Yes":1
}
)
```

---

# Pipeline Node 06 — Feature Selection

## Concept

Feature selection identifies which variables should be provided to the model.

The objective is to keep meaningful predictors and avoid including the target
variable as an input.

---

## Observation from EDA

Correlation analysis showed relationships between environmental variables.

Examples:

```
tmmn ↔ tmmx

fm100 ↔ erc
```

However, these relationships represent natural environmental behaviour.

Features were not removed only because of correlation.

---

## Decision

Input features:

```
latitude
longitude
weather variables
fire indices
year
month
day_of_year
```

Target:

```
Wildfire
```

---

## Preprocessing Activity

Feature and target separation:

```python
X = df_processed.drop(
    columns=["Wildfire"]
)

y = df_processed["Wildfire"]
```

Final:

```
20 input features
1 target variable
```

---

# Pipeline Node 07 — Time-Based Train/Test Split

## Concept

Train-test splitting separates data used for learning and evaluation.

For time-dependent problems, random splitting can introduce future information
into training data.

---

## Observation from EDA

Dataset time range:

```
2013 → 2025
```

Wildfire prediction is a forecasting problem, therefore future observations
must not influence historical training.

---

## Decision

A chronological split was used.

Training:

```
2013/2014 → 2022
```

Testing:

```
2023 → 2025
```

---

## Preprocessing Activity

```python
train_mask = X["year"] <= 2022

test_mask = X["year"] >= 2023
```

Created:

```
X_train
X_test
y_train
y_test
```

---

# Pipeline Node 08 — Feature Scaling Decision

## Concept

Feature scaling transforms numerical variables into similar ranges.

Common techniques:

- Standardization
- Min-Max normalization

---

## Observation from EDA

Features had different ranges.

Examples:

```
latitude:
25 - 49

srad:
0 - 440

vpd:
0 - 8
```

---

## Decision

Scaling was not applied.

Reason:

The planned models are tree-based models such as:

- Random Forest
- XGBoost

Tree models are not sensitive to feature magnitude.

Scaling will only be applied if distance-based or gradient-based models are
tested later.

---

# Pipeline Node 09 — Save Processed Dataset

## Concept

The processed dataset is saved separately from the raw dataset to ensure:

- reproducibility
- easier model development
- preservation of original data

---

## Decision

Final processed dataset location:

```
data/processed/wildfire_processed.csv
```

---

## Final Dataset

The processed dataset contains:

- cleaned observations
- engineered date features
- encoded target variable
- selected input features

It is ready for machine learning model development.

---

# Final Preprocessing Summary

| Requirement | Status |
|---|---|
| Duplicate handling | Completed |
| Sentinel value handling | Completed |
| Missing value handling | Completed |
| Feature engineering | Completed |
| Target encoding | Completed |
| Feature selection | Completed |
| Leakage prevention | Completed |
| Train/test separation | Completed |
| Scaling decision | Justified |

---

# Conclusion

The raw wildfire dataset was successfully transformed into a clean and
machine-learning-ready dataset. Each preprocessing decision was supported by
EDA findings and designed to improve data quality while preventing information
leakage.