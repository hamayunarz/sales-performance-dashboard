# sales-performance-dashboard
This project offers an in-depth analysis of global superstore sales data from 2014 to 2017. Using Python, SQL, and Power BI, the aim is to uncover valuable business insights, highlight growth opportunities, and improve profitability.

🎯 Objectives

Analyze four years of global sales data to identify trends and patterns
Pinpoint the most profitable regions, product categories, and customer segments
Create interactive dashboards to support data-driven decisions
Recommend strategies to drive growth and reduce losses
📊 Dataset

Source: Global Superstore Dataset (via Kaggle)
Size: 51,000+ records across 24 columns
Timeframe: 2014–2017
Scope: Global sales data by region, customer segment, and product category
🛠️ Tech Stack

Python: Data cleaning, exploration, and analysis using pandas, numpy, matplotlib, seaborn, plotly
SQL: Data querying and transformation
Power BI: Interactive dashboards and visual analytics
sales-performance-analytics/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_analysis.ipynb
|   |-- 04_eda.ipynb
│   └── 05_visualization.ipynb
├── sql/
│   ├── queries/
│   │   ├── 01_sales_summary.sql     
│   │   ├── 02_top_customers.sql      
│   │   ├── 03_regional_analysis.sql  
│   │   ├── 04_category_analysis.sql  
│   │   ├── 05_monthly_trends.sql    
│   │   └── fix_column_types.sql
│   ├── db_connect.py
│   ├── run_all_queries.py           
│   └── upload_csv_to_sql.py
├── .env
├── dashboards/
├── reports/
└── requirements.txt


