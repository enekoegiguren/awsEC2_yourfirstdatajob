import streamlit as st
import psycopg2
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Connect to the PostgreSQL database using SQLAlchemy
def connect_to_db():
    engine = create_engine(f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('POSTGRE_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}")
    return engine

# Fetch data from the database using SQLAlchemy connection
def fetch_data():
    engine = connect_to_db()
    query = "SELECT * FROM ft_jobdata"
    data = pd.read_sql(query, engine)
    engine.dispose()  # Properly close the connection
    return data

# Format salary as € in thousands (k)
def format_salary(value):
    return f"{value / 1000:.0f}k €"

# Fetch data
data = fetch_data()

# Sidebar for Page Navigation
st.sidebar.title("Navigation")
st.sidebar.markdown("[Main](./)")
st.sidebar.markdown("[Analysis](./pages/analysis.py)")

# ---- Main Page Content ----
st.title("Job Opportunities Analysis - Main")

# ---- Filter Section ----
st.write("### Filter Options")
col1, col2, col3 = st.columns(3)

with col1:
    job_categories = data['job_category'].unique().tolist()
    selected_category = st.selectbox("Select Job Category", options=["All"] + job_categories)

with col2:
    data['extracted_date'] = pd.to_datetime(data['extracted_date'])
    data['year'] = data['extracted_date'].dt.year
    years = data['year'].unique().tolist()
    selected_year = st.selectbox("Select Year", options=["All"] + years)

with col3:
    data['month'] = data['extracted_date'].dt.month
    months = data['month'].unique().tolist()
    selected_month = st.selectbox("Select Month", options=["All"] + months)

filtered_data = data.copy()
if selected_category != "All":
    filtered_data = filtered_data[filtered_data['job_category'] == selected_category]
if selected_year != "All":
    filtered_data = filtered_data[filtered_data['year'] == selected_year]
if selected_month != "All":
    filtered_data = filtered_data[filtered_data['month'] == selected_month]

# ---- KPIs Calculation ----
average_experience = filtered_data['experience'].mean() if not filtered_data['experience'].isnull().all() else 0
min_salary = filtered_data['avg_salary'].min() if not filtered_data['avg_salary'].isnull().all() else 0
max_salary = filtered_data['avg_salary'].max() if not filtered_data['avg_salary'].isnull().all() else 0
average_salary = filtered_data['avg_salary'].mean() if not filtered_data['avg_salary'].isnull().all() else 0

# ---- KPI Section ----
st.write("### Key Performance Indicators (KPIs)")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Average Experience (Years)", f"{average_experience:.0f}", " ")

with col2:
    st.metric("Minimum Salary (€)", format_salary(min_salary))

with col3:
    st.metric("Maximum Salary (€)", format_salary(max_salary))

with col4:
    st.metric("Average Salary (€)", format_salary(average_salary))

# ---- Most Demanded Job Categories Section ----
st.write("### Most Demanded Job Categories")
if not filtered_data.empty:
    most_demanded_jobs = filtered_data['job_category'].value_counts().head(10)
    st.bar_chart(most_demanded_jobs)
else:
    st.write("No data available for the selected filters.")

# ---- Map with Circle Markers ----
st.write("### Job Locations Map")
if not filtered_data.empty:
    job_counts = filtered_data.groupby(['latitude', 'longitude']).size().reset_index(name='job_count')
    fig = px.scatter_mapbox(
        job_counts,
        lat="latitude",
        lon="longitude",
        size="job_count",
        color_continuous_scale=px.colors.cyclical.IceFire,
        size_max=15,
        zoom=5,
        mapbox_style="carto-positron",
        title="Job Density in France"
    )
    st.plotly_chart(fig)
else:
    st.write("No data available to display on the map.")