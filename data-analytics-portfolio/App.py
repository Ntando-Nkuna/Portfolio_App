import streamlit as st
import os


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Ntando Nkuna | Data & Analytics Portfolio",
    layout="wide"
)


# --------------------------------------------------
# BASE PATH (GitHub-safe)
# --------------------------------------------------
BASE_PATH = os.path.dirname(__file__)


# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------
st.title("Ntando Nkuna")
st.subheader("Data Engineering & Analytics Specialist")

st.write(
    """
    I am a third-year ILS student with a strong aptitude for working with data,
    focusing on transforming raw information into structured, insight-driven
    outputs through analytics, visualization, and efficient data processes.
    """
)


# --------------------------------------------------
# SKILLS SECTION
# --------------------------------------------------
st.header("Core Skills")

st.markdown("""
- Data cleaning, transformation, and analysis  
- Business intelligence and dashboard development  
- Exploratory data analysis and reporting  
""")


# --------------------------------------------------
# TECH STACK (FIXED & CLEAN)
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

for col, (name, path) in zip(cols, icons.items()):
    full_path = os.path.join(BASE_PATH, path)

    with col:
        if os.path.exists(full_path):
            st.image(full_path, width=65)
            st.caption(name)
        else:
            st.error(f"Missing file: {path}")


# --------------------------------------------------
# PROJECTS SECTION
# --------------------------------------------------
st.header("Highlighted Work")

st.markdown("""
- End-to-end analytics pipelines using Python and SQL  
- Interactive dashboards built with Power BI and Plotly  
- Data transformation and reporting using DuckDB  
""")


# --------------------------------------------------
# FEEDBACK FORM
# --------------------------------------------------
st.header("Leave Feedback")

with st.form("feedback_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Email (optional)")
    rating = st.slider("Rating", 1, 5, 4)
    comment = st.text_area("Comments")
    submitted = st.form_submit_button("Submit")

if submitted:
    st.success("Thank you for your feedback!")
