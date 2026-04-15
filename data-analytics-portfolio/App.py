import streamlit as st
import base64
import os


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Ntando Nkuna | Data & Analytics Portfolio",
    layout="wide"
)


# --------------------------------------------------
# BASE PATH (GitHub repo root)
# --------------------------------------------------
BASE_PATH = os.path.dirname(__file__)  # safer for Streamlit deployment


# --------------------------------------------------
# Helpers
# --------------------------------------------------
@st.cache_data
def get_file_as_base64(file_path: str):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None


# --------------------------------------------------
# Background Styling
# --------------------------------------------------
background_path = os.path.join(BASE_PATH, "background", "banner.svg")
backgr = get_file_as_base64(background_path)

if backgr:
    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/svg+xml;base64,{backgr}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}

        .fade-in {{
            animation: fadeIn 1s ease-in-out;
            line-height: 1.6;
        }}

        .tech-stack {{
            display: flex;
            justify-content: center;
            gap: 40px;
            margin-top: 30px;
            flex-wrap: wrap;
        }}

        .tech-item {{
            text-align: center;
        }}

        .tech-item img {{
            width: 60px;
            height: 60px;
            margin-bottom: 8px;
        }}

        .tech-item span {{
            font-size: 14px;
            font-weight: 500;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(15px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# --------------------------------------------------
# Hero Section
# --------------------------------------------------
st.markdown(
    """
    <div class="fade-in">
        <h1>Ntando Nkuna</h1>
        <h3>Data Engineering & Analytics Specialist</h3>
        <p>
            I am a third-year ILS student with a strong aptitude for working with data,
            focusing on transforming raw information into structured, insight-driven
            outputs through analytics, visualization, and efficient data processes.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Skills Section
# --------------------------------------------------
st.markdown(
    """
    <div class="fade-in">
        <h2>Core Skills</h2>

        <h4>Data & Analytics</h4>
        <ul>
            <li>Data cleaning, transformation, and analysis</li>
            <li>Business intelligence and dashboard development</li>
            <li>Exploratory data analysis and reporting</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Tech Stack Icons Section
# --------------------------------------------------
icons = {
    "Python": os.path.join(BASE_PATH, "icons", "python.svg"),
    "Pandas": os.path.join(BASE_PATH, "icons", "pandas.svg"),
    "DuckDB": os.path.join(BASE_PATH, "icons", "DuckDB_logo.svg"),
    "Plotly": os.path.join(BASE_PATH, "icons", "plotly.svg"),
    "Streamlit": os.path.join(BASE_PATH, "icons", "streamlit.svg"),
    "SQL Server": os.path.join(BASE_PATH, "icons", "sqlserver.svg")
}

icon_html = ""

for name, path in icons.items():
    svg = get_file_as_base64(path)
    if svg:
        icon_html += f"""
        <div class="tech-item">
            <img src="data:image/svg+xml;base64,{svg}" />
            <span>{name}</span>
        </div>
        """

st.markdown(
    f"""
    <div class="fade-in">
        <h2>Tech Stack</h2>
        <div class="tech-stack">
            {icon_html}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Projects Section
# --------------------------------------------------
st.markdown(
    """
    <div class="fade-in">
        <h2>Highlighted Work</h2>
        <ul>
            <li>End-to-end analytics pipelines using Python and SQL</li>
            <li>Interactive dashboards built with Power BI and Plotly</li>
            <li>Data transformation and reporting using DuckDB</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Feedback Form (UI Only)
# --------------------------------------------------
st.markdown(
    """
    <div class="fade-in">
        <h2>Leave Feedback</h2>
        <p>I’d love to hear your thoughts on my portfolio.</p>
    </div>
    """,
    unsafe_allow_html=True
)

with st.form("feedback_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Email (optional)")
    rating = st.slider("Rating", 1, 5, 4)
    comment = st.text_area("Comments")
    submitted = st.form_submit_button("Submit")

if submitted:
    st.success("Thank you for your feedback!")
