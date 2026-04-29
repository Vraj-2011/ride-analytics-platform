import pandas as pd
import os
from sqlalchemy import create_engine

# Get DB URL from environment (Docker) or fallback to local
db_url = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgress@db:5432/rides_db"
)

engine = create_engine(db_url)

# Load processed data
df = pd.read_csv("data/processed_rides.csv")

# Load into PostgreSQL
df.to_sql("rides", engine, if_exists="replace", index=False)

print("✅ Data loaded into PostgreSQL")