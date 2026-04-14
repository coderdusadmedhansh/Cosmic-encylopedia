import streamlit as st
import base64
import os

# 1. Page Config
st.set_page_config(page_title="Uranus", page_icon="💎", layout="wide")

def apply_custom_styles(image_file):
    path = os.path.join(os.getcwd(), image_file)
    with open(path, "rb") as f:
        encoded_string = base64.b64encode(f.read())
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string.decode()}");
            background-size: cover;
            background-attachment: fixed;
        }}
        .block-container {{ padding-top: 1rem !important; }}

        [data-testid="stSidebar"] {{
            background-color: #060b14 !important;
            border-right: 2px solid #00F2FF;
        }}
        
        [data-testid="stSidebarNavItems"] span, [data-testid="stSidebar"] p {{
            color: #00F2FF !important;
            font-weight: bold !important;
        }}

        label, .stMarkdown p {{ 
            color: #00F2FF !important; 
            font-weight: bold !important;
        }}

        h1, h2, h3 {{ 
            color: #00F2FF !important; 
            text-shadow: 2px 2px 8px #000000;
        }}

        div[data-testid="stMarkdownContainer"] p {{
            color: #FFFFFF !important;
        }}
        
        .stAlert {{
            background-color: rgba(0, 242, 255, 0.15) !important;
            border: 1px solid #00F2FF !important;
        """
        f"""
            border: 1px solid #00F2FF !important;
        }}

        .compact-box {{
            background-color: rgba(0, 0, 0, 0.7);
            border: 2px solid #00F2FF;
            padding: 12px;
            border-radius: 10px;
            color: #FFFFFF !important;
            font-size: 1rem;
            margin-left: -40px; 
        }}

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

st.title("🚀 Uranus: The Ice Giant")

# Top Layout
top_col1, top_col2 = st.columns([0.8, 2])

with top_col1:
    # Ensure uranus.jpg is in your planets folder
    if os.path.exists("planets/uranus.jpg"):
        st.image("planets/uranus.jpg", width=160)
    else:
        st.error("Missing uranus.jpg in planets folder")

with top_col2:
    st.markdown('<div class="compact-box">Uranus is the coldest planet in the solar system. It is tilted so far that it actually orbits the sun on its side! It also has 13 faint rings.</div>', unsafe_allow_html=True)

st.write("") 

# Bottom Layout
calc_col1, calc_col2 = st.columns(2)

with calc_col1:
    st.markdown("### ⚖️ Weight")
    u_weight = st.number_input("Earth (kg):", min_value=1, value=50, key="w7")
    # Uranus Gravity is 0.89
    res_w = round(u_weight * 0.89, 2)
    st.info(f"On Uranus: {res_w} kg")

with calc_col2:
    st.markdown("### 🚀 Travel")
    mode = st.selectbox("Vehicle:", ["Rocket", "Light Speed"], key="v7")
    # Average distance to Uranus is ~2.6 Billion km
    dist_km = 2600000000 
    
    if mode == "Rocket":
        val = round(dist_km / (28000 * 24), 1)
        st.info(f"Time: {val} Days")
    else:
        val = round(dist_km / 300000, 1)
        st.info(f"Time: {val} Sec")

st.markdown("<p style='text-align: center; font-size: 12px; color: #888888;'>Developer: Medhansh Dusad | Cosmic Builders 2026</p>", unsafe_allow_html=True)
