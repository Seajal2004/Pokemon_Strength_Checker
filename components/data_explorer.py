import streamlit as st
import asyncio
from services.poke_client import fetch_pokemon_data

def show():
    st.title("🧬 Pokémon Data Explorer")
    pokemon_name = st.text_input("Enter Pokémon name (e.g., pikachu, bulbasaur):")

    # Button to trigger data processing
    if st.button("Start"):
        if not pokemon_name:
            st.warning("Please enter a Pokémon name first.")
            return

        with st.spinner("Fetching data..."):
            data = asyncio.run(fetch_pokemon_data(pokemon_name.lower()))

        if not data or "error" in data:
            st.error(data.get("error", "Pokémon not found"))
            return

        st.header(data['name'].capitalize())
        st.subheader("📊 Base Stats")
        st.json(data["stats"])

        st.subheader("🧬 Types")
        st.write(", ".join(data["types"]))

        st.subheader("💡 Abilities")
        st.write(", ".join(data["abilities"]))

        st.subheader("⚔️ Sample Moves")
        for move in data["moves"]:
            st.markdown(f"**{move['name'].capitalize()}**")
            st.write(f"- Power: {move['power']}")
            st.write(f"- Accuracy: {move['accuracy']}")
            st.write(f"- Type: {move['type']}")
            st.markdown("---")

        st.subheader("🔁 Evolution")
        st.write(f"Evolves into: {data['evolution']}")