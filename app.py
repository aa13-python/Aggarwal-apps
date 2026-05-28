import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="My Program Portfolio",
    page_icon="📁",
    layout="centered"
)

# 2. Header Section
st.title("Program Portfolio")
st.write("Welcome to my central application hub. Select a program below to launch it.")

st.divider()

# 3. Application Links Section
st.subheader("Clinical Tools & Calculators")

# App 1: Thyroid Therapy
st.markdown("### ☢️ Thyroid Therapy Calculator")
st.write("An automated tool for I-131 dose calculations and therapy management.")
st.link_button("Launch Thyroid Therapy App", "https://thyroid-therapy.streamlit.app")

st.write("---")

# Placeholder for your next program
st.markdown("### 🚀 [Future Program Name]")
st.write("Description of your next Python or Streamlit project.")
# Keep the button disabled until you have a real URL
st.link_button("Coming Soon", "https://github.com", disabled=True) 

# You can copy and paste the block above to keep adding new programs to your list.
