import pandas as pd
from db_connect import get_engine


# Load the CSV
df = pd.read_csv('../data/processed/cleaned_data.csv')

# Create connection
engine = get_engine()

# Upload to SQL
df.to_sql("cleaned_superstore", con=engine, if_exists="replace", index=False)

print("successfully uploaded")

