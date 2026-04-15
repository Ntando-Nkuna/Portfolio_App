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
# BASE PATH
# --------------------------------------------------
BASE_PATH = Path("data-analytics-portfolio")


# --------------------------------------------------
# BACKGROUND IMAGE
# --------------------------------------------------
background_path = BASE_PATH / "background" / "banner.jpg"


def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


if background_path.exists():
    bg_base64 = get_base64(background_path)

    st.markdown(
        f"""
        <style>

        /* GLOBAL BACKGROUND */
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/jpg;base64,{bg_base64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}

        /* GLOBAL TEXT = WHITE */
        html, body, [class*="css"] {{
            color: white !important;
        }}

        h1, h2, h3, h4, h5, h6, p, span, li, label {{
            color: white !important;
        }}

        /* DARK OVERLAY */
        .stApp {{
            background-color: rgba(0, 0, 0, 0.40);
        }}

        /* --------------------------------------------------
           CONNECT SECTION (BLACK TEXT OVERRIDE)
        -------------------------------------------------- */
        .connect-section, .connect-section * {{
            color: black !important;
        }}

        /* --------------------------------------------------
           FEEDBACK FORM (BLACK TEXT OVERRIDE)
        -------------------------------------------------- */
        div[data-testid="stForm"] * {{
            color: black !important;
        }}

        input, textarea {{
            color: black !important;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.warning(f"Background not found: {background_path}")


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
# CONNECT WITH ME (ICON LINKS)
# --------------------------------------------------
st.header("Connect With Me")

col1, col2 = st.columns(2)

medium_path = BASE_PATH / "icons/medium.jpg"
github_path = BASE_PATH / "icons/github.png"


# Medium Icon Link
with col1:
    if medium_path.exists():
        st.markdown(
            f"""
            <a href="https://medium.com/@ntando.nkuna2099" target="_blank">
                <img src="data:image/jpg;base64,{base64.b64encode(open(medium_path, "rb").read()).decode()}"
                width="90" style="display:block;margin:auto;" />
            </a>
            <p style="text-align:center;">Medium</p>
            """,
            unsafe_allow_html=True
        )
    else:
        st.error("Medium icon not found")


# GitHub Icon Link
with col2:
    if github_path.exists():
        st.markdown(
            f"""
            <a href="https://github.com/Ntando-Nkuna" target="_blank">
                <img src="data:image/png;base64,{base64.b64encode(open(github_path, "rb").read()).decode()}"
                width="90" style="display:block;margin:auto;" />
            </a>
            <p style="text-align:center;">GitHub</p>
            """,
            unsafe_allow_html=True
        )
    else:
        st.error("GitHub icon not found")

# --------------------------------------------------
# FEEDBACK FORM (BLACK TEXT)
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
