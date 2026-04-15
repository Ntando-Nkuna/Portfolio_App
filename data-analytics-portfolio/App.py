import streamlit as st
from pathlib import Path
import base64


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
# BACKGROUND IMAGE (FIXED - PRODUCTION SAFE)
# --------------------------------------------------
background_path = BASE_PATH / "background" / "banner.jpg"  # recommended format


def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


if background_path.exists():
    bg_base64 = get_base64(background_path)

    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/jpg;base64,{bg_base64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.warning(f"Background image not found: {background_path}")


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
# CONNECT WITH ME
# --------------------------------------------------
st.header("Connect With Me")

col1, col2 = st.columns(2)

with col1:
    st.link_button(
        label="📘 Medium Profile",
        url="https://medium.com/@ntando.nkuna2099"
    )

with col2:
    st.link_button(
        label="💻 GitHub Profile",
        url="https://github.com/Ntando-Nkuna"
    )


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
