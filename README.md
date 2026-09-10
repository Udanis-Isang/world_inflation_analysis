# World Inflation Analysis

## Project Overview

This project explores annual inflation rates across countries, with a focus on how inflation differs by:

- Income level
- Geographic region
- Country

The analysis combines data preprocessing with exploratory data analysis (EDA) and visualizations using **Pandas, Matplotlib, Seaborn, Plotly, and country_converter**.

> **Scope note:** The conclusions in this README are based strictly on the analysis and outputs contained in `World_Inflation.ipynb`.

---

## Objectives

The project aims to:

1. Inspect and clean the dataset.
2. Assess missing data and retain useful variables.
3. Standardize country identifiers for geographic visualization.
4. Examine the distribution of annual inflation rates.
5. Compare inflation across World Bank-style income groups.
6. Compare inflation across geographic regions.
7. Visualize inflation geographically.
8. Identify countries with the highest recorded inflation rates.

---

## Dataset

The notebook loads:

`inflation_cost_of_living_dataset.csv`

The original dataset contains:

- **217 rows**
- **20 columns**

The dataset includes country information, geographic information, income classification, inflation data, and several cost-of-living variables.

### Key variables used

| Variable | Description |
|---|---|
| `country` | Country name |
| `region` | Geographic region |
| `income_level` | Country income classification |
| `capital_city` | Capital city |
| `latitude` / `longitude` | Geographic coordinates |
| `country_code_y` | Country code associated with inflation records |
| `inflation_year` | Year of the inflation observation |
| `inflation_annual_pct` | Annual inflation rate (%) |
| `IS03_country` | ISO-3 country code created for mapping |

---

## Data Preprocessing

### Missing-value assessment

The notebook identified substantial missingness in several variables.

The most important observations were:

- `country_code_x`: **100% missing**
- `inflation_year`: **17.5% missing**
- `inflation_annual_pct`: **17.5% missing**
- Cost-of-living variables generally had **more than 79% missing values**
- Some transportation and utility variables had more than **87% missing values**

The notebook therefore removed columns with more than **50% missing values**.

This reduced the working dataset from:

**20 columns → 9 original columns**

An additional `IS03_country` column was then created, producing a **10-column analysis dataset**.

### Country-code standardization

The `country_converter` package was used to convert country names into ISO-3 codes for geographic visualization.

Two country names were not automatically recognized:

- Channel Islands
- Naoero

These were reported by the converter during preprocessing.

The resulting map data also contained one `not found` country-code value, so country-code coverage should be checked before using the map for a formal publication.

### Inflation-year distribution

Among the available inflation records:

| Inflation year | Records |
|---:|---:|
| 2024 | 174 |
| 2023 | 2 |
| 2022 | 3 |

This inflation analysis is overwhelmingly a **2024 cross-sectional analysis**.

---

# Exploratory Data Analysis

## 1. Inflation Distribution

The notebook examined the distribution of `inflation_annual_pct` using:

- Histogram
- Box plot

These visualizations were used to inspect the overall spread and identify potential extreme values.

The country-level inflation values are highly uneven, with some countries recording exceptionally high inflation rates.

---

## 2. Countries by Region

The dataset contains seven geographic regions:

- Europe & Central Asia
- Sub-Saharan Africa
- Latin America & Caribbean
- East Asia & Pacific
- Middle East, North Africa, Afghanistan & Pakistan
- South Asia
- North America

The largest regional groups in the dataset are:

| Region | Countries |
|---|---:|
| Europe & Central Asia | 58 |
| Sub-Saharan Africa | 48 |
| Latin America & Caribbean | 42 |
| East Asia & Pacific | 37 |
| Middle East, North Africa, Afghanistan & Pakistan | 23 |
| South Asia | 6 |
| North America | 3 |

Because the number of countries differs substantially between regions, regional comparisons should focus on **average inflation rates**, rather than simply comparing the number of countries.

---

## 3. Inflation by Income Level

Average annual inflation increases substantially as the income classification decreases.

| Income level | Mean annual inflation (%) |
|---|---:|
| High income | 2.42 |
| Upper middle income | 8.78 |
| Lower middle income | 12.35 |
| Low income | 20.68 |

### Key finding

There is a clear descriptive relationship in this dataset between income classification and inflation:

**Lower-income groups recorded considerably higher average inflation rates than higher-income groups.**

The average inflation rate for low-income countries was approximately **8.5 times** the average for high-income countries.

This is a descriptive finding and should not be interpreted as proof that income level causes inflation.

---

## 4. Regional Inflation

Average annual inflation by region was:

| Region | Mean annual inflation (%) |
|---|---:|
| North America | 2.67 |
| East Asia & Pacific | 3.13 |
| South Asia | 3.97 |
| Europe & Central Asia | 4.43 |
| Middle East, North Africa, Afghanistan & Pakistan | 9.53 |
| Latin America & Caribbean | 11.21 |
| Sub-Saharan Africa | 15.54 |

### Key finding

**Sub-Saharan Africa recorded the highest average inflation rate among the regions in the dataset, at approximately 15.54%.**

North America recorded the lowest regional average at approximately **2.67%**.

The difference between these two regional averages is roughly **12.87 percentage points**.

The regional pattern broadly mirrors the income-level comparison: regions containing a larger concentration of lower-income countries tend to have higher average inflation in this dataset.

---

## 5. Income Level by Region

The notebook also examines how countries in each income category are distributed across regions.

### Low-income countries

The majority of low-income countries in the dataset are located in **Sub-Saharan Africa**, with:

- 21 in Sub-Saharan Africa
- 3 in Middle East, North Africa, Afghanistan & Pakistan
- 1 in East Asia & Pacific

### Lower-middle-income countries

Lower-middle-income countries are particularly concentrated in:

- Sub-Saharan Africa: 20
- East Asia & Pacific: 8
- Middle East, North Africa, Afghanistan & Pakistan: 7
- Latin America & Caribbean: 5
- South Asia: 4
- Europe & Central Asia: 3

### Upper-middle-income countries

The largest concentrations are:

- Latin America & Caribbean: 18
- Europe & Central Asia: 15
- East Asia & Pacific: 13

### High-income countries

The largest concentration is in:

- Europe & Central Asia: 40
- Latin America & Caribbean: 19
- East Asia & Pacific: 15

The notebook also identifies **Seychelles** as the only high-income country classified within Sub-Saharan Africa in this dataset.

Seychelles had an annual inflation rate of approximately **0.31%** in 2024.

---

# Highest-Inflation Countries

The notebook identified the following ten countries as having the highest recorded annual inflation rates:

| Rank | Country | Annual inflation (%) |
|---:|---|---:|
| 1 | Argentina | 219.88 |
| 2 | Sudan | 138.81 |
| 3 | Zimbabwe | 104.71 |
| 4 | South Sudan | 91.44 |
| 5 | Turkiye | 58.51 |
| 6 | West Bank and Gaza | 53.67 |
| 7 | Lebanon | 45.24 |
| 8 | Nigeria | 33.24 |
| 9 | Iran, Islamic Rep. | 32.46 |
| 10 | Malawi | 32.18 |

### Key finding

Argentina had the highest recorded inflation rate in the dataset at approximately **219.88%**, substantially above Sudan at approximately **138.81%**.

The top ten are dominated by countries experiencing very high inflation, with the top four all exceeding **90%**.

---

# Geographic Visualization

A Plotly choropleth map was created to visualize inflation by country.

The map uses the generated ISO-3 country codes and `inflation_annual_pct` as the color variable.

This provides a useful geographic view of where inflation was comparatively high or low.

### Mapping limitation

The notebook's country-code conversion reported unmatched country names, and the resulting map contained a `not found` location. The mapping should therefore be validated before treating the visualization as a fully authoritative global map.

---

# Main Findings

The analysis produces five major findings:

### 1. Inflation differs strongly by income group

Average inflation rises from approximately **2.42% for high-income countries** to **20.68% for low-income countries**.

### 2. Sub-Saharan Africa has the highest regional average

Sub-Saharan Africa recorded an average inflation rate of approximately **15.54%**, the highest among the seven regions analyzed.

### 3. North America has the lowest regional average

North America recorded approximately **2.67%**, the lowest regional average in the dataset.

### 4. Inflation is highly concentrated among a small number of countries

Argentina, Sudan, Zimbabwe, and South Sudan recorded inflation rates above **90%**, illustrating the strong influence of extreme country-level observations on the overall distribution.

### 5. The dataset is primarily a 2024 snapshot

Of the 179 available inflation observations:

- 174 are from 2024
- 2 are from 2023
- 3 are from 2022

Therefore, the project is best described as a **cross-sectional analysis of recent inflation**, not a historical inflation trend analysis.

---

# Important Limitations

Several limitations should be considered when interpreting the findings.

## Missing inflation observations

Inflation data are available for **179 of 217 countries**, meaning approximately **17.5%** of rows do not have an inflation value.

Group averages therefore use only countries with available inflation observations.

## Unequal regional sample sizes

The number of countries differs considerably across regions. For example, North America contains only three countries in the dataset, while Europe & Central Asia contains 58.

Consequently, a regional average based on three observations should be interpreted more cautiously than one based on dozens of observations.

## Mostly single-year data

The dataset does not contain enough observations across multiple years to support meaningful inflation trend analysis.

## Descriptive rather than causal analysis

The observed relationship between income level and inflation does **not** establish causation.

Other factors may influence inflation, including monetary policy, exchange rates, fiscal conditions, commodity prices, political instability, supply shocks, and other macroeconomic variables.

## Cost-of-living variables were removed

Most cost-of-living variables contained more than 50% missing values and were removed during preprocessing.

Consequently, the final analysis does not investigate the relationship between inflation and cost-of-living indicators.

## Country-code validation

The ISO-3 conversion generated unmatched country-name warnings. The mapping should be validated before using the geographic visualization in a publication or decision-making context.

---

# Tools and Technologies

- **Python**
- **Pandas** — data manipulation and aggregation
- **NumPy** — numerical operations
- **Matplotlib** — static visualization
- **Seaborn** — statistical visualization
- **Plotly Express** — interactive visualization
- **country_converter** — country-code standardization
- **Jupyter Notebook / VS Code** — analysis environment

---

# Visualizations

The notebook contains visualizations including:

- Annual inflation distribution histogram
- Annual inflation box plot
- Distribution of countries by region
- Average inflation by income level
- Regional distribution by income level
- Average inflation by region
- World inflation choropleth map
- Top 30 countries by inflation
- Top 10 countries by inflation


# Conclusion

The analysis shows substantial differences in inflation across both income groups and geographic regions.

High-income countries recorded the lowest average inflation, while low-income countries recorded the highest. Among geographic regions, Sub-Saharan Africa had the highest average inflation, while North America had the lowest.

At the country level, inflation was heavily concentrated among a small number of countries, with Argentina recording the highest value in the dataset at approximately 219.88%.

Overall, the project provides a useful descriptive snapshot of global inflation, particularly for **2024**, but further statistical testing and multi-year data would be needed to establish stronger relationships, assess uncertainty, and investigate inflation trends over time.
