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
# FIXED REPO PATH
# --------------------------------------------------
BASE_PATH = Path("data-analytics-portfolio")


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
# SKILLS SECTION
# --------------------------------------------------
st.header("Core Skills")

st.markdown("""
- Data cleaning, transformation, and analysis  
- Business intelligence and dashboard development  
- Exploratory data analysis and reporting  
""")


# --------------------------------------------------
# TECH STACK
# --------------------------------------------------
st.header("Tech Stack")

icons = {
    "Python": "icons/Python.svg",
    "Pandas": "icons/Pandas.svg",
    "DuckDB": "icons/DuckDB_logo.svg",
    "Plotly": "icons/Ploty.svg",
    "Streamlit": "icons/Streamlit.svg",
    "SQL Server": "icons/Microsoft SQL Server.svg",
    "PyCharm": "icons/PyCharm.svg",
    "VS Code": "icons/Visual Studio Code (VS Code).svg"
}

cols = st.columns(len(icons))

for col, (name, rel_path) in zip(cols, icons.items()):
    full_path = BASE_PATH / rel_path

    with col:
        if full_path.exists():
            st.image(str(full_path), width=65)
            st.caption(name)
        else:
            st.error(f"Missing file: {full_path}")


# --------------------------------------------------
# CONNECT WITH ME (UPDATED WITH ICONS)
# --------------------------------------------------
st.header("Connect With Me")

col1, col2 = st.columns(2)

# Medium
with col1:
    medium_path = BASE_PATH / "icons/medium.jpg"
    if medium_path.exists():
        st.markdown(
            f"""
            <a href="https://medium.com/@ntando.nkuna2099" target="_blank">
                <img src="data:image/jpg;base64,{open(medium_path, "rb").read().hex()}" 
                style="width:80px; display:block; margin:auto;" />
            </a>
            """,
            unsafe_allow_html=True
        )
        st.caption("Medium")
    else:
        st.error("Medium icon missing")

# GitHub
with col2:
    github_path = BASE_PATH / "icons/github.png"
    if github_path.exists():
        st.markdown(
            f"""
            <a href="https://github.com/Ntando-Nkuna" target="_blank">
                <img src="data:image/png;base64,{open(github_path, "rb").read().hex()}" 
                style="width:80px; display:block; margin:auto;" />
            </a>
            """,
            unsafe_allow_html=True
        )
        st.caption("GitHub")
    else:
        st.error("GitHub icon missing")


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
