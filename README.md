Global Superstore Sales Analytics
This project analyzes global superstore sales data from 2011 to 2014 using Python, SQL, and Power BI to uncover business insights and identify growth opportunities.
Dataset Overview
Source: Global Superstore Dataset
Records: 51,290 transactions
Timeframe: January 2011 - December 2014
Customers: 4,873 unique customers
Products: 10,292 unique products
Key Metrics
Total Sales: $12,642,905.00
Total Profit: $1,467,457.29
Profit Margin: 11.61%
Average Order Value: $246.50
Peak Month: November 2014
Regional Performance
Central: $2,822,399 (22.3%)
South: $1,600,960 (12.7%)
North: $1,248,192 (9.9%)
Oceania: $1,100,207 (8.7%)
Southeast Asia: $884,438 (7.0%)
North Asia: $848,349 (6.7%)
Technology Stack
Python: pandas, numpy, matplotlib, seaborn, plotly
SQL: data querying and transformation
Power BI: interactive dashboards
Project Structure
sales-performance-analytics/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_analysis.ipynb
│   ├── 04_eda.ipynb
│   └── 05_visualization.ipynb
├── sql/
│   ├── queries/
│   ├── db_connect.py
│   ├── run_all_queries.py
│   └── upload_csv_to_sql.py
├── dashboards/
├── reports/
└── requirements.txt
Getting Started

Clone the repository
Install dependencies: pip install -r requirements.txt
Set up database connection in .env file
Run Jupyter notebooks in sequence
Execute SQL queries for specific insights
Open Power BI dashboards for interactive analysis

Analysis Components
Data exploration and cleaning
Statistical analysis and trend identification
Interactive visualizations
SQL analytics for business questions
Dashboard creation for decision support