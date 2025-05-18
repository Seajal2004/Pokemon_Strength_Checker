import streamlit as st
import asyncio
from services.poke_client import fetch_pokemon_data
from logic.battle_simulator import simulate_battle

def show():
    st.title("⚔️ Pokémon Battle Simulator")
    col1, col2 = st.columns(2)
    with col1:
        pkmn1 = st.text_input("Enter first Pokémon:", key="pkmn1")
    with col2:
        pkmn2 = st.text_input("Enter second Pokémon:", key="pkmn2")

    if st.button("Start Battle"):
        if not pkmn1 or not pkmn2:
            st.warning("Please enter both Pokémon names.")
            return

        with st.spinner("Validating Pokémon..."):
            data1 = asyncio.run(fetch_pokemon_data(pkmn1.lower()))
            data2 = asyncio.run(fetch_pokemon_data(pkmn2.lower()))

        if not data1 or "error" in data1:
            st.error(f"❌ Pokémon '{pkmn1}' not found.")
        elif not data2 or "error" in data2:
            st.error(f"❌ Pokémon '{pkmn2}' not found.")
        else:
            with st.spinner("Simulating battle..."):
                log, winner = asyncio.run(simulate_battle(pkmn1.lower(), pkmn2.lower()))
            st.subheader("📜 Battle Log")
            for line in log:
                st.write(f"• {line}")
            st.success(f"🏆 Winner: **{winner.capitalize()}**")