import streamlit as st
import base64

# Function to keep the same space background
def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        encoded_string = base64.b64encode(f.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string.decode()}");
            background-size: cover;
        }}
        h1, h2, h3, p, span {{ color: #00F2FF !important; }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Since the file is inside the 'pages' folder, we use '../' to find the background
try:
    add_bg_from_local('background.jpeg')
except:
    pass

st.title("🚀 Exploring Mercury")

# Planet Data
gravity = 0.38
fact = "Smallest planet and closest to the Sun!"

col1, col2 = st.columns([1, 1.4])
with col1:
    # Use '../' to look outside the pages folder for the image
    st.image("mercury.jpg", width=150)

with col2:
    st.info(fact)

# Simple Weight Calculator
weight = st.number_input("Earth Weight (kg):", value=50)
st.success(f"Weight on Mercury: {round(weight * gravity, 2)} kg")
