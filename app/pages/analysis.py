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

# Fetch data
data = fetch_data()

# ---- Analysis Page Content ----
st.title("Job Opportunities Analysis - Detailed")

# ---- Experience Analysis ----
st.write("### Experience by Job")
data['experience_rounded'] = data['experience'].round()
if not data.empty:
    fig_exp_box = px.box(
        data,
        x='job_category',
        y='experience_rounded',
        points="all",
        title="Experience Requirement by Job Category",
        labels={'experience_rounded': 'Years of Experience', 'job_category': 'Job Category'}
    )
    st.plotly_chart(fig_exp_box)
else:
    st.write("No data available for Experience Analysis.")

# ---- Salary Analysis by Job ----
st.write("### Salary by Job")
if not data.empty:
    fig_salary_job = px.box(
        data,
        x='job_category',
        y='avg_salary',
        points="all",
        title="Salary Distribution by Job Category",
        labels={'avg_salary': 'Average Salary (€)', 'job_category': 'Job Category'}
    )
    st.plotly_chart(fig_salary_job)
else:
    st.write("No data available for Salary Analysis by Job.")

# ---- Salary Analysis by Years of Experience ----
st.write("### Salary by Years of Experience")
if not data.empty:
    fig_salary_exp = px.box(
        data,
        x='experience_rounded',
        y='avg_salary',
        points="all",
        title="Salary by Years of Experience",
        labels={'experience_rounded': 'Years of Experience', 'avg_salary': 'Average Salary (€)'}
    )
    st.plotly_chart(fig_salary_exp)
else:
    st.write("No data available for Salary Analysis by Experience.")