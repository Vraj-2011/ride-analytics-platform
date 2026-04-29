import pandas as pd

# Load raw data
df = pd.read_csv("data/rides.csv")

# Convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Feature engineering
df["hour"] = df["timestamp"].dt.hour
df["day"] = df["timestamp"].dt.day_name()

# Business metric
df["fare_per_km"] = df["fare"] / df["distance_km"]

# Save processed data
df.to_csv("data/processed_rides.csv", index=False)

print("✅ Data processed")