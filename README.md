# ISRO Satellite and Mission Data Analysis

## Project Overview
This project analyzes ISRO's satellite and mission data up to August 2022. It covers data loading, preprocessing, exploratory data analysis, mission success metrics, time series visualizations, and reporting. The goal is to derive insights on mission trends, success rates, and satellite launches with clean, modular code.

## Data Sources
- `ISRO missions - till AUGUST 2022.csv`: Mission-level data including dates, launch vehicles, and mission types.
- `satellites.csv`: Details of satellites including launch date, mass, and country.

## Project Structure
- `data/`: Raw dataset CSV files.
- `notebooks/`: Jupyter notebooks for each analysis phase from loading to reporting.
- `src/`: Python modules for reusable data loading, preprocessing, visualization, and reporting functions.
- `notebooks/outputs/`: Generated figures and reports.

## How to Run
1. Clone the repository.
2. Install dependencies:  
   `pip install -r requirements.txt`
3. Run the notebooks sequentially from:  
   `01_data_loading_and_preprocessing.ipynb` ➔  
   `02_eda_and_basic_visualizations.ipynb` ➔  
   `03_mission_analysis_and_success_metrics.ipynb` ➔  
   `04_time_series_and_advanced_visualizations.ipynb` ➔  
   `05_reporting_and_exporting.ipynb`

## Key Features
- Robust data cleaning and feature engineering to handle real-world dataset inconsistencies.
- Modular notebooks for a clear analysis pipeline.
- Visualizations covering trends, distributions, and mission success breakdowns.
- Exportable reports and figures for easy sharing.

## Future Work
- Integrate predictive modeling for mission outcomes.
- Add interactive dashboard for live data exploration.
- Expand datasets with cost and technical specs.

## Contact & Contributions
Author: Sai Tejeswar  
Email: [sanjeevisaitejeswarreddy@gmail.com]
