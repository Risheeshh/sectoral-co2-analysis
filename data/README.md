# Data Documentation

This directory documents the data sources used in the sectoral CO₂ emission analysis presented in the accompanying research manuscript. To respect licensing and redistribution policies, raw datasets are not included directly in this repository.

## Primary Data Source
- **Kaggle CO₂ Emissions Dataset**
  - Contains country-level, sector-wise CO₂ emission records with temporal coverage.
  - Fields include country, date, sector, and emission values.
  - Source: Kaggle (publicly available dataset)

## Reference Data Source
- **Our World in Data (OWID) – CO₂ Emissions**
  - Provides long-term global and country-level CO₂ emission statistics.
  - Used as a reference dataset for contextual analysis and trend comparison.

## Data Usage in This Study
The datasets are used exclusively for:
- Descriptive analysis of sector-wise emission trends
- Generation of analytical visualizations
- Supporting methodological discussion in the manuscript

No predictive modeling, forecasting, or model training is performed using these data.

## Preprocessing Notes
Minimal preprocessing steps are applied, including:
- Date standardization and extraction of annual values
- Aggregation of emissions by country, year, and sector
- Renaming of variables for clarity and consistency

These steps are implemented in the scripts provided in the `analysis/` directory.

## Licensing and Redistribution
Users must obtain the datasets directly from their original sources and comply with all applicable licensing and usage terms. This repository does not redistribute proprietary or restricted data.
