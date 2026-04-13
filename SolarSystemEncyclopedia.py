import streamlit as st

st.set_page_config(page_title="Cosmic Encyclopedia", layout="centered")

st.title("🛰️ IoTM: Cosmic Encyclopedia")
st.subheader("Welcome, Explorer Medhansh!")

st.markdown("""
### Instructions:
1. **Physical Poster:** Scan the QR code next to a planet on the A3 sheet.
2. **Digital App:** Use the sidebar on the left to select a planet manually.
3. **Calculators:** Each page will calculate your weight and travel time!
""")

st.info("👈 Select a planet from the sidebar to begin your journey.")
