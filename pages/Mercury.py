import streamlit as st
import base64
import os

# 1. Page Config
st.set_page_config(page_title="Exploring Mercury", page_icon="☄️")

# 2. Background Function (Adjusted for sub-folder)
def add_bg_from_local(image_file):
    # We look one level up (..) to find the background in the main folder
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

# Try to load background from the main directory
try:
    add_bg_from_local('background.jpeg')
except:
    st.write("Background not found")

# 3. Content
st.title("🚀 Mercury: The Swift Planet")

col1, col2 = st.columns([1, 1.5])

with col1:
    # Look into the 'planets' folder for the image
    st.image("planets/mercury.jpg", width=180)

with col2:
    st.info("Mercury is the smallest planet in our solar system and the closest to the Sun—is only slightly larger than Earth's Moon.")

# 4. Calculator
st.markdown("### ⚖️ Weight Calculator")
weight = st.number_input("Enter your Earth weight (kg):", value=50)
mercury_weight = round(weight * 0.38, 2)
st.success(f"On Mercury, you would weigh: **{mercury_weight} kg**")
