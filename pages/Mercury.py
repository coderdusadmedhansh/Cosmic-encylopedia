import streamlit as st
import base64
import os

# 1. Page Config - Set to wide to use screen better
st.set_page_config(page_title="Mercury", page_icon="☄️", layout="wide")

def apply_custom_styles(image_file):
    path = os.path.join(os.getcwd(), image_file)
    with open(path, "rb") as f:
        encoded_string = base64.b64encode(f.read())
    
    st.markdown(
        f"""
        <style>
        /* Force background and remove top padding */
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string.decode()}");
            background-size: cover;
            background-attachment: fixed;
        }}
        .block-container {{
            padding-top: 1rem !important;
            padding-bottom: 0rem !important;
        }}
        
        /* Make sidebar links visible */
        [data-testid="stSidebarNavItems"] span {{
            color: #00F2FF !important;
            font-weight: bold !important;
        }}

        /* Neon Text Styles */
        h1, h2, h3, p, label {{ 
            color: #00F2FF !important; 
            margin-bottom: 5px !important;
        }}

        /* Compact Container Boxes */
        .compact-box {{
            background-color: rgba(0, 0, 0, 0.6);
            border: 1px solid #00F2FF;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 10px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

try:
    apply_custom_styles('background.jpeg')
except:
    pass

# 3. Main Header (Compact)
st.title("🚀 Mercury: The Swift Planet")

# 4. Top Row: Image and Fact
top_col1, top_col2 = st.columns([1, 2])

with top_col1:
    # Reduced image size to save vertical space
    st.image("planets/mercury.jpg", width=160)

with top_col2:
    st.markdown('<div class="compact-box">Mercury is the smallest planet and closest to the Sun. It orbits the Sun in just 88 Earth days!</div>', unsafe_allow_html=True)

st.write("") # Tiny spacer

# 5. Bottom Row: Calculators side-by-side
calc_col1, calc_col2 = st.columns(2)

with calc_col1:
    st.markdown("### ⚖️ Weight")
    u_weight = st.number_input("Earth (kg):", min_value=1, value=50, key="w1")
    res_w = round(u_weight * 0.38, 2)
    st.info(f"On Mercury: **{res_w} kg**")

with calc_col2:
    st.markdown("### 🚀 Travel")
    mode = st.selectbox("Vehicle:", ["Rocket", "Light Speed"], key="v1")
    dist_km = 91000000
    if mode == "Rocket":
        val = round(dist_km / (28000 * 24), 1)
        st.info(f"Time: **{val} Days**")
    else:
        val = round(dist_km / 300000, 1)
        st.info(f"Time: **{val} Sec**")

# Minimalist Footer
st.markdown("<p style='text-align: center; font-size: 12px; color: grey;'>Developer: Medhansh Dusad | Cosmic Builders 2026</p>", unsafe_allow_html=True)
