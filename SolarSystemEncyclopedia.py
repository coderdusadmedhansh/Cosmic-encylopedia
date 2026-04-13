import streamlit as st
import base64

# 1. Page Configuration
st.set_page_config(page_title="Cosmic Encyclopedia", page_icon="🚀", layout="centered")

# 2. Add Space Background and Neon Font Styling
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string.decode()}");
            background-size: cover;
            background-attachment: fixed;
        }}
        /* White text for general content */
        .main, p, span, label, .stMarkdown {{ 
            color: #FFFFFF !important; 
            font-weight: 500;
        }}
        /* Electric Blue for Headers */
        h1, h2, h3 {{ 
            color: #00F2FF !important; 
            text-shadow: 2px 2px 10px #000000;
        }}
        /* Transparent Glassmorphism for boxes */
        .stInfo, .stSuccess {{
            background-color: rgba(255, 255, 255, 0.15) !important;
            border: 1px solid rgba(0, 242, 255, 0.3) !important;
            color: white !important;
            border-radius: 15px;
        }}
        /* Styling the inputs */
        .stNumberInput input, .stSelectbox div {{
            background-color: rgba(0, 0, 0, 0.7) !important;
            color: #00F2FF !important;
        }}
        /* Reduce top padding to fit screen */
        .block-container {{
            padding-top: 2rem !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

try:
    add_bg_from_local('background.jpeg')
except:
    st.sidebar.warning("Background image not found.")

# 3. Planet Data
planets = {
    "Mercury": {"gravity": 0.38, "dist": 91, "fact": "Smallest planet and closest to the Sun!"},
    "Venus": {"gravity": 0.91, "dist": 41, "fact": "Hottest planet with a toxic atmosphere."},
    "Earth": {"gravity": 1.0, "dist": 0, "fact": "Our home! The only planet with life."},
    "Mars": {"gravity": 0.38, "dist": 78, "fact": "The Red Planet, home to iron dust."},
    "Jupiter": {"gravity": 2.34, "dist": 628, "fact": "A massive gas giant; the largest planet."},
    "Saturn": {"gravity": 1.06, "dist": 1275, "fact": "Famous for its spectacular icy rings."},
    "Uranus": {"gravity": 0.92, "dist": 2723, "fact": "An ice giant that rotates on its side."},
    "Neptune": {"gravity": 1.19, "dist": 4351, "fact": "The windiest planet in our solar system."}
}

st.title("👨‍🚀 Cosmic Encyclopedia")

# 4. QR Code Auto-Select Logic
query_params = st.query_params
planet_list = list(planets.keys())
default_index = 0
if "planet" in query_params:
    param_planet = query_params["planet"].title()
    if param_planet in planet_list:
        default_index = planet_list.index(param_planet)

selected_planet = st.sidebar.selectbox("Choose a Planet", planet_list, index=default_index)

# 5. Compact Layout (Fits on 1 Screen)
col_img, col_text = st.columns([1, 1.4])

with col_img:
    try:
        # Reduced to 140px for ultra-compact mobile view
        st.image(f"{selected_planet.lower()}.jpg", width=140)
    except:
        st.write("✨")

with col_text:
    st.subheader(f"Exploring {selected_planet}")
    st.info(planets[selected_planet]["fact"])

# 6. Interactive Calculators
st.divider()
c1, c2 = st.columns(2)

with c1:
    st.markdown("### ⚖️ Weight")
    u_weight = st.number_input("Earth (kg):", min_value=1, value=50, key="w_in")
    res_w = round(u_weight * planets[selected_planet]["gravity"], 2)
    st.success(f"**{res_w} kg**")

with c2:
    st.markdown("### 🚀 Travel")
    mode = st.selectbox("Vehicle:", ["Rocket", "Light Speed"], key="m_in")
    dist_km = planets[selected_planet]["dist"] * 1000000
    if selected_planet == "Earth":
        st.write("You are here!")
    elif mode == "Rocket":
        days = round(dist_km / (28000 * 24), 1)
        st.success(f"**{days} d**")
    else:
        seconds = round(dist_km / 300000, 2)
        st.success(f"**{seconds}s**")

# Footer with Name and Competition
st.markdown(
    f"""
    <div style='text-align: center; font-size: 0.8rem; margin-top: 20px;'>
        <b>Developer:</b> Medhansh Dusad <br>
        <b>Competition:</b> IoTM - March'26 - Cosmic Builders
    </div>
    """,
    unsafe_allow_html=True
)