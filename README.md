Sales Performance Dashboard (Global Superstore Analytics)
Overview
This project analyzes global superstore sales data from 2011 to 2014 using Python, SQL, and Power BI to uncover business insights and identify growth opportunities.
The dataset included:

51,290 transactions
4,873 unique customers
10,292 unique products
4 years of sales data across multiple regions

Tools & Methods
Tools: Python, SQL, Power BI
Techniques: Data cleaning, statistical analysis, trend identification, interactive visualization
Business Results

Total sales of $12,642,905.00 with 11.61% profit margin
Central region leads with $2,822,399 (22.3% of total sales)
Peak sales month identified as November 2014
Average order value of $246.50 across all transactions

Technical Implementation

Data Processing:
Cleaned and standardized 51,290 transaction records using Python (Pandas)
SQL queries for regional aggregations and performance analysis
Handled missing values and data type inconsistencies

Analysis Approach:
Regional sales comparison across Central, South, North Asia, and other markets
Time-series analysis to identify seasonal patterns and peak periods
Customer segmentation based on purchase frequency and value
Product category profitability assessment

Visualization:
Interactive Power BI dashboard with drill-down capabilities
Regional performance breakdown with comparative metrics
Monthly and seasonal trend charts
KPI cards tracking revenue, margin, and order volume

How I Did It
Step 1: Data Preparation
Used Python and SQL to clean and organize the raw sales data. Processed transactions, customer information, and product details across multiple regions.
Step 2: Analysis
Performed comprehensive analysis including:

Regional performance comparison
Monthly and seasonal trend analysis
Customer segmentation by purchase behavior
Product category profitability assessment

Step 3: Insights & Dashboards
Built interactive dashboards in Power BI and created visualizations using Python. Explored sales patterns, regional differences, and customer purchasing trends.
Key Insights

Central region generates highest revenue at $2,822,399 (22.3%)
November 2014 represents peak sales performance
South region follows with $1,600,960 (12.7%) in sales
North Asia shows potential for growth at $848,349 (6.7%)
Average order value indicates healthy transaction size
Seasonal patterns reveal opportunities for targeted campaigns

Project Structure

data/ (raw and processed sales data)
notebooks/ (Python analysis and exploration)
sql/ (database queries and transformations)
dashboards/ (Power BI visualizations)
reports/ (findings and recommendations)

Getting Started

Clone the repository
Install dependencies: pip install -r requirements.txt
Set up database connection in .env file
Run Jupyter notebooks in sequence
Execute SQL queries for specific insights
Open Power BI dashboards for interactive analysis
