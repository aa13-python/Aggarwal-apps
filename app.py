import streamlit as st
import os

# 1. Page Configuration
# Uses a fallback emoji if the SVG file is missing to prevent page crashes
icon_path = "gemini_svg.svg"
page_icon = icon_path if os.path.exists(icon_path) else "⚛️"

rocket_svg = "rocket_svg.svg" if os.path.exists("rocket_svg.svg") else None

# NOTE: If your Streamlit version does not support SVGs for page_icon, 
# you may need to change 'icon_path' to point to a .png or .jpg file instead.
st.set_page_config(
    page_title="Clinical Application Portfolio",
    page_icon=page_icon, 
    layout="centered"
)

# 2. Simplified CSS for Clinical Theme
st.markdown("""
    <style>
    /* Streamlit Link Buttons */
    .stLinkButton > button {
        border-color: #FFD166 !important;
        color: #0B132B !important;
        font-weight: 600;
    }
    .stLinkButton > button:hover {
        border-color: #FFD166 !important;
        color: #FFD166 !important;
        background-color: #0B132B !important;
    }
    /* Typography */
    h1, h2, h3 { color: #0B132B; }
    </style>
""", unsafe_allow_html=True)

# 3. Header Section with Logo
col1, col2 = st.columns([1, 4])
with col1:
    # Safety check: Only load the image if the file actually exists
    if os.path.exists(icon_path):
        # NOTE: Streamlit's st.image sometimes struggles with raw SVG paths. 
        # If it fails, convert the SVG to PNG.
        st.image(icon_path, width=120) 
    else:
        st.error("⚠️ Image missing.")
        st.caption("Ensure 'gemini-svg.svg' is in the same folder as this script.")
        
with col2:
    st.title("Dr. A.A.'s Clinical Apps Portfolio")
    st.write("Centralized hub for theranostics and quantitative tools.")

st.divider()

# 4. Radionuclide Therapies Section
st.subheader("Nuclear Medicine")

st.markdown("### 💊 I-131 Thyroid Therapy Calculator")
st.link_button("Launch Thyroid Therapy App", "https://thyroid-therapy.streamlit.app")

st.write("---")

# 5. Future Additions
st.subheader("Additional tools coming soon...")

# Fixed inline ternary statement - converted to a standard if/else block
if rocket_svg:
    st.image(rocket_svg, width=50)
else:
    st.write("🚀 Coming Soon!")