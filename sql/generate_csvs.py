# File: sql/generate_csvs.py

import pandas as pd
import os
from db_connect import get_engine

def generate_csvs():
    """Run SQL queries and save their results to CSV files."""

    engine = get_engine()

    query_files = [
        "01_sales_summary.sql",
        "02_top_customers.sql",
        "03_regional_analysis.sql",
        "04_category_analysis.sql",
        "05_monthly_trends.sql"
    ]

    output_dir = "../data/sql_results"
    os.makedirs(output_dir, exist_ok=True)

    for query_file in query_files:
        try:
            with open(f"queries/{query_file}", "r") as file:
                query = file.read()

            df = pd.read_sql(query, con=engine)

            output_file = os.path.join(output_dir, query_file.replace('.sql', '.csv'))
            df.to_csv(output_file, index=False)

        except Exception as e:
            print(f"Error saving CSV for {query_file}: {e}")

if __name__ == "__main__":
    generate_csvs()
