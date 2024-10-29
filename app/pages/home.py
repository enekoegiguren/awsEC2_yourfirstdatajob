import streamlit as st
import psycopg2
import pandas as pd
import folium
from streamlit_folium import st_folium
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Connect to the PostgreSQL database
def connect_to_db():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("POSTGRE_PASS"),
        database=os.getenv("DB_NAME")
    )
    return conn

# Fetch data from the database
def fetch_data():
    conn = connect_to_db()
    query = "SELECT * FROM ft_jobdata"
    data = pd.read_sql(query, conn)
    conn.close()
    return data

# Fetch data
data = fetch_data()

# ---- KPIs Calculation ----
avg_experience = data['experience'].mean()
min_salary = data['avg_salary'].min()
max_salary = data['avg_salary'].max()
avg_salary = data['avg_salary'].mean()

st.title("Job Opportunities Analysis")

# ---- KPI Section ----
st.write("### Key Performance Indicators (KPIs)")

# Calculate KPIs
average_experience = data['experience'].mean() if not data['experience'].isnull().all() else 0
min_salary = data['avg_salary'].min() if not data['avg_salary'].isnull().all() else 0
max_salary = data['avg_salary'].max() if not data['avg_salary'].isnull().all() else 0
average_salary = data['avg_salary'].mean() if not data['avg_salary'].isnull().all() else 0

# Display KPIs with st.metric
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Average Experience (Years)", f"{average_experience:.2f}", " ")

with col2:
    st.metric("Minimum Salary (€)", f"{min_salary:.2f}", " ")

with col3:
    st.metric("Maximum Salary (€)", f"{max_salary:.2f}", " ")

with col4:
    st.metric("Average Salary (€)", f"{average_salary:.2f}", " ")

# ---- Circle Map Section ----
st.write("### Job Locations Map")
# Group by latitude and longitude to count jobs
job_counts = data.groupby(['latitude', 'longitude']).size().reset_index(name='job_count')

# Create a folium map centered around France
map_center = [46.6034, 1.8883]  # Approximate center of France
job_map = folium.Map(location=map_center, zoom_start=6)

# Add circle markers for each location
for idx, row in job_counts.iterrows():
    folium.CircleMarker(
        location=(row['latitude'], row['longitude']),
        radius=row['job_count'] * 2,  # Adjust the multiplier for circle size
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity=0.6,
        popup=f"Jobs: {row['job_count']}"
    ).add_to(job_map)

# Display the map in Streamlit
st_folium(job_map, width=700)