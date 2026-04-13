import streamlit as st
import base64
import os

# 1. Page Config
st.set_page_config(page_title="Exploring Mercury", page_icon="☄️")

# 2. Background Function
def add_bg_from_local(image_file):
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
        h1, h2, h3, p, span, label {{ color: #00F2FF !important; }}
        .stInfo {{ background-color: rgba(255, 255, 255, 0.1); border: 1px solid #00F2FF; }}
        </style>
        """,
        unsafe_allow_html=True
    )

try:
    add_bg_from_local('background.jpeg')
except:
    pass

# 3. Content
st.title("🚀 Mercury: The Swift Planet")

col1, col2 = st.columns([1, 1.5])

with col1:
    # Ensuring path is correct for the 'planets' folder
    st.image("planets/mercury.jpg", width=180)

with col2:
    st.info("Mercury is the smallest planet in our solar system and the closest to the Sun.")

st.divider()

# 4. CALCULATORS SECTION
c1, c2 = st.columns(2)

with c1:
    st.markdown("### ⚖️ Weight")
    u_weight = st.number_input("Earth (kg):", min_value=1, value=50)
    # Mercury Gravity is 0.38
    res_w = round(u_weight * 0.38, 2)
    st.success(f"**{res_w} kg**")

with c2:
    st.markdown("### 🚀 Travel Time")
    mode = st.selectbox("Vehicle:", ["Rocket", "Light Speed"])
    # Distance to Mercury is ~91 Million km
    dist_km = 91 * 1000000
    
    if mode == "Rocket":
        # Rocket speed ~28,000 km/h
        days = round(dist_km / (28000 * 24), 1)
        st.success(f"**{days} days**")
    else:
        # Light speed ~300,000 km/s
        seconds = round(dist_km / 300000, 2)
        st.success(f"**{seconds} seconds**")
