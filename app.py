import streamlit as st
from components.background import set_background
from components import data_explorer, battle_simulator

# Set background
set_background("image.jpeg")

# Sidebar Navigation (fully custom now)
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Choose a Section", ["🧬 Data Explorer", "⚔️ Battle Simulator"])

if page == "🧬 Data Explorer":
    data_explorer.show()
elif page == "⚔️ Battle Simulator":
    battle_simulator.show()