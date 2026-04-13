import streamlit as st
import base64
import os

# 1. Page Config
st.set_page_config(page_title="Mercury", page_icon="☄️", layout="wide")

def apply_custom_styles(image_file):
    path = os.path.join(os.getcwd(), image_file)
    with open(path, "rb") as f:
        encoded_string = base64.b64encode(f.read())
    
    st.markdown(
        f"""
        <style>
        /* Main App Background */
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string.decode()}");
            background-size: cover;
            background-attachment: fixed;
        }}
        .block-container {{ padding-top: 1rem !important; }}

        /* --- SIDEBAR FIX: DARK BACKGROUND & NEON TEXT --- */
        [data-testid="stSidebar"] {{
            background-color: #060b14 !important;
            border-right: 2px solid #00F2FF;
        }}
        
        [data-testid="stSidebarNavItems"] span, [data-testid="stSidebar"] p {{
            color: #00F2FF !important;
            font-weight: bold !important;
        }}

        /* --- FONT COLORS --- */
        label, .stMarkdown p {{ 
            color: #00F2FF !important; 
            font-weight: bold !important;
        }}

        h1, h2, h3 {{ 
            color: #00F2FF !important; 
            text-shadow: 2px 2px 8px #000000;
        }}

        /* Result Text inside boxes - Pure White */
        div[data-testid="stMarkdownContainer"] p {{
            color: #FFFFFF !important;
        }}
        
        .stAlert {{
            background-color: rgba(0, 242, 255, 0.15) !important;
            border: 1px solid #00F2FF !important;
        }}

        /* Planet Fact Box - Adjusted for closer spacing */
        .compact-box {{
            background-color: rgba(0, 0, 0, 0.7);
            border: 2px solid #00F2FF;
            padding: 12px;
            border-radius: 10px;
            color: #FFFFFF !important;
            font-size: 1rem;
            margin-left: -40px; /* Pulls the box closer to the image */
        }}

        /* Mobile adjustment: if screen is small, don't use negative margin */
        @media (max-width: 800px) {{
            .compact-box {{ margin-left: 0px; }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

try:
    apply_custom_styles('background.jpeg')
except:
    pass

st.title("🚀 Mercury: The Swift Planet")

# Adjusted ratios to bring columns closer [0.8, 2]
top_col1, top_col2 = st.columns([0.8, 2])

with top_col1:
    st.image("planets/mercury.jpg", width=160)

with top_col2:
    # The 'margin-left: -40px' in CSS handles the close proximity
    st.markdown('<div class="compact-box">Mercury is the smallest planet and closest to the Sun. It orbits the Sun in just 88 Earth days!</div>', unsafe_allow_html=True)

st.write("") 

calc_col1, calc_col2 = st
