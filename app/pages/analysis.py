import streamlit as st
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

# Fetch data from the database
def fetch_data():
    engine = connect_to_db()
    query = "SELECT * FROM ft_jobdata WHERE avg_salary < 200000"
    data = pd.read_sql(query, engine)
    engine.dispose()  # Properly close the connection
    return data

# Fetch data
data = fetch_data()

# ---- Analysis Page Content ----
st.title("Job Opportunities Analysis - Detailed")

# ---- Experience Analysis ----
st.write("### Experience by Job")
data['experience_rounded'] = data['experience'].round().astype(int)  # Round experience for cleaner visuals

if not data.empty:
    fig_exp_box = px.box(
        data,
        x='job_category',
        y='experience_rounded',
        points=False,  # Disable outlier points
        title="Experience Requirement by Job Category (Without Outliers)",
        labels={'experience_rounded': 'Years of Experience', 'job_category': 'Job Category'}
    )
    st.plotly_chart(fig_exp_box)
else:
    st.write("No data available for Experience Analysis.")

# ---- Salary Analysis by Job ----
st.write("### Salary by Job")
data['avg_salary_rounded'] = data['avg_salary'].round()  # Round average salary

if not data.empty:
    # Box plot for salary distribution by job category
    fig_salary_job_box = px.box(
        data,
        x='job_category',
        y='avg_salary_rounded',
        points=False,  # Disable outlier points
        title="Salary Distribution by Job Category (Without Outliers)",
        labels={'avg_salary_rounded': 'Average Salary (€)', 'job_category': 'Job Category'}
    )
    st.plotly_chart(fig_salary_job_box)
else:
    st.write("No data available for Salary Analysis by Job.")

# ---- Salary Analysis by Years of Experience ----
st.write("### Salary by Years of Experience")
if not data.empty:
    fig_salary_exp = px.box(
        data,
        x='experience_rounded',
        y='avg_salary_rounded',
        points=False,  # Disable outlier points
        title="Salary by Years of Experience (Without Outliers)",
        labels={'experience_rounded': 'Years of Experience', 'avg_salary_rounded': 'Average Salary (€)'}
    )
    st.plotly_chart(fig_salary_exp)
else:
    st.write("No data available for Salary Analysis by Experience.")

# ---- Scatter Plot for Rounded Data ----
st.write("### Salary by Job Category and Experience")
# Group by job category and experience level, and calculate average salary to smooth out the data
grouped_data = data.groupby(['job_category', 'experience_rounded']).agg(avg_salary=('avg_salary_rounded', 'mean')).reset_index()

if not grouped_data.empty:
    fig_salary_exp_scatter = px.scatter(
        grouped_data,
        x='experience_rounded',
        y='avg_salary',
        color='job_category',
        size='avg_salary',
        title="Average Salary by Experience and Job Category",
        labels={'experience_rounded': 'Years of Experience', 'avg_salary': 'Average Salary (€)', 'job_category': 'Job Category'},
        color_discrete_sequence=px.colors.qualitative.Plotly
    )
    st.plotly_chart(fig_salary_exp_scatter)
else:
    st.write("No data available for Salary Analysis by Job Category and Experience.")
