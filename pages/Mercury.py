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
        /* --- MAIN APP BACKGROUND --- */
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string.decode()}");
            background-size: cover;
            background-attachment: fixed;
        }}
        .block-container {{ padding-top: 1rem !important; }}

        /* --- SIDEBAR FIX: DARK BACKGROUND & NEON TEXT --- */
        [data-testid="stSidebar"] {{
            background-color: #060b14 !important; /* Deep space dark blue/black */
            border-right: 2px solid #00F2FF;
        }}
        
        /* Forces all text in the sidebar to be Neon Blue */
        [data-testid="stSidebarNavItems"] span, [data-testid="stSidebar"] p, [data-testid="stSidebar"] h1 {{
            color: #00F2FF !important;
            font-weight: bold !important;
            font-size: 1.1rem !important;
        }}

        /* Change color of the "Home" link if it appears */
        [data-testid="stSidebarNavItems"] a {{
            color: #00F2FF !important;
        }}

        /* --- CONTENT COLORS --- */
        label, .stMarkdown p {{ 
            color: #00F2FF !important; 
            font-weight: bold !important;
        }}

        h1, h2, h3 {{ 
            color: #00F2FF !important; 
            text-shadow: 2px 2px 8px #000000;
        }}

        /* Result Text inside boxes - Pure White for readability */
        div[data-testid="stMarkdownContainer"] p {{
            color: #FFFFFF !important;
        }}
        
        .stAlert {{
            background-color: rgba(0, 242, 255, 0.2) !important;
            border: 1px solid #00F2FF !important;
        }}

        .compact-box {{
            background-color: rgba(0, 0, 0, 0.7);
            border: 2px solid #00F2FF;
            padding: 15px;
            border-radius: 10px;
            color: #FFFFFF !important;
            font-size: 1.1rem;
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

top_col1, top_col2 = st.columns([1, 2])
with top_col1:
    st.image("planets/mercury.jpg", width=160)
with top_col2:
    st.markdown('<div class="compact-box">Mercury is the smallest planet and closest to the Sun. It orbits the Sun in just 88 Earth days!</div>', unsafe_allow_html=True)

st.write("") 

calc_col1, calc_col2 = st.columns(2)
with calc_col1:
    st.markdown("### ⚖️ Weight")
    u_weight = st.number_input("Earth (kg):", min_value=1, value=50, key="w1")
    res_w = round(u_weight * 0.38, 2)
    st.info(f"On Mercury: {res_w} kg")

with calc_col2:
    st.markdown("### 🚀 Travel")
    mode = st.selectbox("Vehicle:", ["Rocket", "Light Speed"], key="v1")
    dist_km = 91000000
    if mode == "Rocket":
        val = round(dist_km / (28000 * 24), 1)
        st.info(f"Time: {val} Days")
    else:
        val = round(dist_km / 300000, 1)
        st.info(f"Time: {val} Sec")

st.markdown("<p style='text-align: center; font-size: 12px; color: #888888;'>Developer: Medhansh Dusad | Cosmic Builders 2026</p>", unsafe_allow_html=True)
