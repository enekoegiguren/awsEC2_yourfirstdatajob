import streamlit as st


# ---- PAGE SETUP ------

## HOME PAGE

home_page = st.Page(
    page = 'pages/home.py',
    title = "Home",
    icon = ":material/home:"
)

skills_page = st.Page(
    page = 'pages/skills.py',
    title = "Skills",
    icon = ":material/home:"
)

# ---- NAVIGATION SETUP
pg = st.navigation(
    {
        "Home": [home_page],
        "Insights": [skills_page]
    }
)

pg.run()