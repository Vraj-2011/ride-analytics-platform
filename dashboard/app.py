import streamlit as st
import pandas as pd
import os
import time
import subprocess
from sqlalchemy import create_engine

# Get DB URL (Docker or local)
db_url = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgress@db:5432/rides_db"
)

engine = create_engine(db_url)

st.title("🚖 Ride Analytics Platform")

# 🔄 Refresh Data Button
if st.button("🔄 Refresh Data"):
    try:
        subprocess.run(["python", "scripts/load_data.py"])
        st.success("Data refreshed successfully!")
    except Exception as e:
        st.error(f"Error refreshing data: {e}")

# 🔄 Safe DB connection (retry)
df = None

for i in range(5):
    try:
        df = pd.read_sql("SELECT * FROM rides", engine)
        break
    except Exception:
        st.warning("Waiting for database...")
        time.sleep(3)

if df is None:
    st.error("Database not available. Please try again later.")
    st.stop()

# Convert timestamp
if "timestamp" in df.columns:
    df["timestamp"] = pd.to_datetime(df["timestamp"])

# Sidebar filters
st.sidebar.header("Filters")

city = st.sidebar.multiselect(
    "Select City",
    df["city"].unique(),
    default=df["city"].unique()
)

filtered_df = df[df["city"].isin(city)]

# 📅 Date filter
date = st.sidebar.date_input("Select Date (optional)")

if date:
    filtered_df = filtered_df[
        filtered_df["timestamp"].dt.date == date
    ]

# KPIs
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"${filtered_df['fare'].sum():,.2f}")
col2.metric("Total Rides", len(filtered_df))
col3.metric("Avg Fare", f"${filtered_df['fare'].mean():.2f}")

# Charts
st.subheader("💰 Revenue by City")
st.bar_chart(filtered_df.groupby("city")["fare"].sum())

st.subheader("⏰ Rides by Hour")
st.line_chart(filtered_df.groupby("hour")["ride_id"].count())

st.subheader("🚗 Efficiency (Fare per KM)")
st.bar_chart(filtered_df.groupby("city")["fare_per_km"].mean())

# Insights
top_city = filtered_df.groupby("city")["fare"].sum().idxmax()
peak_hour = filtered_df.groupby("hour")["ride_id"].count().idxmax()

st.success(f"🏆 Top City: {top_city}")
st.info(f"🔥 Peak Hour: {peak_hour}:00")

# Footer
st.markdown("---")
st.caption("🚀 Built with Python, PostgreSQL & Docker")