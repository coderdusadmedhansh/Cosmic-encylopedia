import streamlit as st
import base64
import os

# 1. Page Config
st.set_page_config(page_title="Exploring Mercury", page_icon="☄️")

# 2. Background & Sidebar Styling Function
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

        /* Sidebar Glassmorphism effect */
        [data-testid="stSidebar"] {{
            background-color: rgba(0, 0, 0, 0.7) !important;
            border-right: 1px solid #00F2FF;
        }}

        /* Sidebar Planet Names - High Visibility */
        [data-testid="stSidebarNavItems"] span {{
            color: #00F2FF !important;
            font-size: 1.2rem !important;
            font-weight: bold !important;
        }}

        /* Active/Selected Page Highlight */
        [data-testid="stSidebarNavItems"] a[aria-current="page"] span {{
            color: #FFFFFF !important;
            text-shadow: 0px 0px 10px #00F2FF;
        }}

        /* Main Content Colors */
        h1, h2, h3, p, label {{ 
            color: #00F2FF !important; 
            text-shadow: 2px 2px 4px #000000;
        }}

        /* Info Box Styling */
        .stInfo {{ 
            background-color: rgba(0, 242, 255, 0.1) !important; 
            border: 1px solid #00F2FF !important; 
            color: white !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Apply the styles
try:
    apply_custom_styles('background.jpeg')
except Exception:
    st.error("Background image not found in the main directory.")

# 3. Content Layout
st.title("🚀 Mercury: The Swift Planet")

col1, col2 = st.columns([1, 1.5])

with col1:
    # Look into the 'planets' folder for the image
    st.image("planets/mercury.jpg", width=200)

with col2:
    st.info("Mercury is the smallest planet in our solar system and the closest to the Sun. It orbits the Sun faster than any other planet!")

st.divider()

# 4. Calculators
c1, c2 = st.columns(2)

with c1:
    st.markdown("### ⚖️ Weight")
    u_weight = st.number_input("Earth Weight (kg):", min_value=1, value=50)
    res_w = round(u_weight * 0.38, 2)
    st.success(f"On Mercury: **{res_w} kg**")

with c2:
    st.markdown("### 🚀 Travel Time")
    mode = st.selectbox("Vehicle:", ["Rocket", "Light Speed"])
    dist_km = 91000000 # 91 Million km
    
    if mode == "Rocket":
        days = round(dist_km / (28000 * 24), 1)
        st.success(f"**{days} days**")
    else:
        seconds = round(dist_km / 300000, 2)
        st.success(f"**{seconds} sec**")

# Competition Footer
st.markdown("---")
st.caption("Developer: Medhansh Dusad | IoTM Cosmic Builders 2026")
