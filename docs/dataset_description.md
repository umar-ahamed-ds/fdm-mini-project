Missing Value Analysis

Observation:
All 19 attributes contain zero missing values.

Decision:
No missing value treatment was applied.

Reason:
Applying imputation would unnecessarily modify complete observations.

# Phase 3 — Duplicate Record Analysis

## Objective

Identify duplicate observations in the wildfire dataset and determine
whether they should be removed before model training.

## Analysis Performed

Duplicate records were investigated by comparing complete rows and
considering the spatio-temporal nature of the dataset. Records with
the same geographical location but different dates were treated as
valid observations because they represent different environmental
conditions.

## Findings

The dataset contains 13,920 exact duplicate records.
These records represent identical observations repeated multiple times.

## Decision

Exact duplicate rows will be removed during preprocessing because they
do not provide additional information and may introduce bias during
model training.

# Phase 4 — Target Variable Analysis

## Objective

Analyze the distribution of the target variable (`Wildfire`) to understand
the classification problem and identify whether class imbalance exists.

## Analysis Performed

The frequency distribution of the `Wildfire` target variable was analyzed
to compare the number of wildfire and non-wildfire observations.

## Findings

The dataset contains two classes:

- No wildfire: 9,007,860 observations (94.7%)
- Wildfire: 502,065 observations (5.3%)

The target variable is highly imbalanced, with wildfire events representing
a smaller proportion of the dataset.

## Decision

The original class distribution will be preserved during preprocessing
because it represents the real-world occurrence of wildfire events.

Class imbalance will be considered during model development using suitable
techniques such as class weighting or resampling if required.

# Phase 5 — Data Type Analysis

## Objective

Identify the data types of all attributes in the wildfire dataset and
categorize features into numerical, categorical, date/time, and target
variables.

## Analysis Performed

The data types of each column were examined to understand which
preprocessing techniques may be required before model training.

## Findings

The dataset contains:
- 17 numerical attributes
- 1 date/time attribute (`datetime`)
- 1 categorical target attribute (`Wildfire`)

The numerical attributes represent geographical, weather, fuel moisture,
and fire-related environmental measurements.

The `datetime` attribute is stored as a string and requires feature
engineering to extract meaningful temporal information.

The `Wildfire` target variable is categorical and requires encoding before
model training.

## Decision

Numerical features will be analyzed for distribution and scaling
requirements.

The `datetime` attribute will be transformed into useful time-based
features such as month or season.

The `Wildfire` target variable will be encoded into numerical values during
the preprocessing stage.

# Phase 06 — Statistical Summary Analysis

## Objective

Analyze the statistical characteristics of numerical features to understand
their distributions, ranges, and identify abnormal values that may require
preprocessing.

## Analysis Performed

Statistical summaries of numerical attributes were generated using
descriptive statistics including count, mean, standard deviation,
minimum, maximum, and quartile values.

## Findings

All numerical attributes contained values for all 9,509,925 observations.
However, multiple environmental features contained an unusual maximum value
of 32767.

Further investigation showed that 25,725 records contained the value 32767
across all environmental variables. This value represents unavailable
weather measurements rather than valid environmental observations.

## Decision

The value 32767 will be treated as a sentinel value representing missing
environmental data during preprocessing.

Records with unavailable environmental measurements will be removed because
they do not provide useful information for wildfire prediction and replacing
them with estimated values may introduce artificial weather patterns.

# Phase 07 — Outlier Analysis

## Objective

Identify extreme values in numerical features and determine whether they
represent invalid data points or meaningful environmental conditions.

## Analysis Performed

Feature distributions were examined using percentile analysis and IQR-based
outlier detection for important environmental variables such as temperature
and wind speed.

## Findings

The analysis identified extreme values in several environmental features.
However, these values were within realistic environmental ranges.

For example, maximum temperature values and wind speed values identified by
the IQR method represent possible extreme weather conditions rather than
data errors.

The previously identified value 32767 was treated separately as a sentinel
value representing unavailable measurements.

## Decision

No automatic outlier removal will be performed on valid environmental
extreme values because these conditions may contain important wildfire
patterns.

Only invalid sentinel values representing missing measurements will be
removed during preprocessing.

# Phase 08 — Feature Engineering Preparation

## Objective

Identify useful transformations for the datetime attribute and determine
which temporal features can improve wildfire prediction while avoiding
unnecessary features and data leakage.

## Analysis Performed

The datetime attribute was converted from string format into a datetime
datatype. The dataset time coverage and wildfire distribution across months
were analyzed to determine whether temporal patterns exist.

## Findings

The dataset covers observations from 2013-12-31 to 2025-04-13, providing
more than 11 years of temporal information.

Monthly wildfire distribution shows seasonal variation, with higher wildfire
observations occurring during mid-year months, particularly June to August.

This indicates that temporal information may contribute useful patterns for
wildfire prediction.

## Decision

The datetime attribute will be transformed during preprocessing to create
the following features:

- Year
- Month
- Day of year

These features can capture long-term and seasonal wildfire patterns.

Features such as day of week will not be included because they have limited
relevance to wildfire occurrence.

# Phase 09 — Feature Relationship Analysis

## Objective

Analyze relationships between features and identify useful predictors,
redundant variables, and potential feature selection requirements.

## Analysis Performed

Correlation analysis was performed between numerical features and the
wildfire target. Feature-to-feature correlation was also analyzed after
removing invalid records containing sentinel values.

## Findings

Initial correlation analysis was affected by sentinel values (32767),
which represented unavailable environmental measurements. After removing
these invalid records, realistic feature relationships were observed.

Strong relationships were identified among several environmental features.
For example, temperature variables showed strong positive correlation,
while fuel moisture variables showed strong relationships with fire
indices.

The `etr` and `pet` variables showed very high correlation, indicating
potential redundancy.

## Decision

Features will not be removed based only on correlation values because
many relationships represent meaningful environmental interactions.

Highly correlated features will be evaluated further during model
development and feature selection.

# Phase 10 — Data Leakage Analysis

## Objective

Identify potential data leakage risks and determine an appropriate data
splitting strategy for wildfire prediction.

## Analysis Performed

Dataset attributes were reviewed to identify features that could contain
future information or directly reveal the wildfire outcome. The temporal
distribution of observations was also analyzed to determine a suitable
training and testing approach.

## Findings

The dataset contains location, weather, fire index, and temporal features.
No attributes were identified that directly reveal wildfire outcomes after
the event.

The `Wildfire` and `Wildfire_encoded` attributes represent the target
variable and will not be used as input features.

The dataset contains observations from 2013 to 2025, making it a
time-dependent dataset. Random splitting may introduce temporal leakage by
allowing future information to appear in training data.

## Decision

A time-based train-test split will be used during model development.

Historical observations will be used for training, while later years will
be reserved for evaluation to simulate real-world wildfire prediction.