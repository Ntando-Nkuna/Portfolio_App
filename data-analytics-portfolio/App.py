import streamlit as st
from pathlib import Path


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Ntando Nkuna | Data & Analytics Portfolio",
    layout="wide"
)


# --------------------------------------------------
# PROJECT ROOT (IMPORTANT FIX)
# --------------------------------------------------
BASE_PATH = Path(__file__).resolve().parent


# If your structure is:
# data-analysis-portfolio/
#    app.py
#    icons/
# then this works automatically


# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------
st.title("Ntando Nkuna")
st.subheader("Data Engineering & Analytics Specialist")

st.write(
    """
    I am a third-year ILS student focused on transforming raw data into structured insights
    using analytics, visualization, and data engineering techniques.
    """
)


# --------------------------------------------------
# TECH STACK
# --------------------------------------------------
st.header("Tech Stack")


icons = {
    "Python": "icons/python.svg",
    "Pandas": "icons/pandas.svg",
    "DuckDB": "icons/duckdb.svg",
    "Plotly": "icons/plotly.svg",
    "Streamlit": "icons/streamlit.svg",
    "SQL Server": "icons/microsoft_sql_server.svg",
    "PyCharm": "icons/pycharm.svg",
    "VS Code": "icons/vscode.svg"
}


cols = st.columns(len(icons))

for col, (name, rel_path) in zip(cols, icons.items()):
    full_path = BASE_PATH / rel_path

    with col:
        if full_path.exists():
            st.image(str(full_path), width=65)
            st.caption(name)
        else:
            st.error(f"Missing: {full_path}")
