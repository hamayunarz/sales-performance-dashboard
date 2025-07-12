# File: sql/run_all_queries.py
# Basic script to run all your queries and print results

import pandas as pd
from db_connect import get_engine

def run_all_queries():
    """Run all SQL queries and display results"""
    
    engine = get_engine()
    
    query_files = [
        "01_sales_summary.sql",
        "02_top_customers.sql", 
        "03_regional_analysis.sql",
        "04_category_analysis.sql",
        "05_monthly_trends.sql"
    ]

    print("Running all queries...")
    print("-" * 40)

    for query_file in query_files:
        try:
            with open(f"queries/{query_file}", "r") as file:
                query = file.read()

            df = pd.read_sql(query, con=engine)

            print(f"\n✓ {query_file} — {len(df)} rows returned:")
            print(df.head())  # Print first few rows for preview

        except Exception as e:
            print(f"✗ Error with {query_file}: {str(e)}")

    print("\nDone!")

if __name__ == "__main__":
    run_all_queries()