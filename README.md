# Mortality-Rate-Prediction-using-ML

 COVID-19 Mortality Rate Prediction & Health Analysis
This project explores how post-COVID indicators affect mortality rates across countries. It combines Machine Learning, Data Cleaning, PCA, Correlation Analysis, and Power BI Dashboards to deliver insights using real-world health data.

🔍 Problem Statement
Predict mortality rate using post-COVID features (not life expectancy).

Reduce data complexity using PCA and uncover patterns.

Identify major risk factors using correlation and feature importance.

Create Power BI dashboards for interactive storytelling.


📁 DAM                     
├── Cleaned COVID Dataset.xlsx     # Raw dataset
├── Cleaned_COVID_Output.xlsx      # Cleaned dataset (output)
├── COVID Vaccinations-CSE Test.xlsx  # Original input sheet
├── Linear regression.py           # Linear Regression ML model
├── Random forest.py               # Random Forest ML model
├── PCA.py                         # PCA visualization
├── Correlation Matrix.py         # Correlation heatmap
├── DAM Dashboard.pbix            # Power BI Dashboards (2 tabs)
├── Actual vs Predicted (Linear Regression).jpg
├── Actual vs Predicted (Random Forest).jpg
└── README.md


 
Data Cleaning
DAM (Jupyter/VS Code):

Removed columns like iso_code, tests_units

Handled null values with threshold filtering

Replaced remaining missing values with column-wise mean

Life expectancy reflects mortality rates and serves as a measure of the overall health and longevity of a population.

Linear Regression
Linear regression.py:

Target: Predicted mortality rate

Evaluated using RMSE and R² Score

Visualized Actual vs Predicted (image included)

Random Forest Regressor
Random forest.py:

Trained on same features as linear regression

Performed better due to non-linear handling

Feature importance chart created

Actual vs Predicted visual included

PCA (Principal Component Analysis)
PCA.py:

Reduced high-dimensional data into 2 principal components

Visualized cluster patterns based on life expectancy

Correlation Matrix
Correlation Matrix.py:

Identified strong/weak relations among health variables

Helped eliminate multicollinearity

Power BI Dashboards
DAM Dashboard.pbix:

Dashboard 1: Health Risk Overview (Elder Vulnerability, Burden Score, etc.)

Dashboard 2: Social Health Indicators (DAX, population health)

Includes slicers for year & country, DAX-calculated KPIs


✅ Random Forest gave better predictions due to non-linearity in post-COVID health impact.

📸 Visuals Included

Actual vs Predicted (Linear Regression).jpg

Actual vs Predicted (Random Forest).jpg


⚙️ Tech Stack
Python: pandas, sklearn, seaborn, matplotlib

Power BI: Custom dashboards, DAX KPIs

Excel: Original and cleaned files

🚀 How to Run
Clone this repository

Run DAM → to generate Cleaned_COVID_Output.xlsx

Use Linear regression.py and Random forest.py to train and evaluate

Open DAM Dashboard.pbix in Power BI Desktop

