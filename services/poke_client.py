import httpx

API_BASE = "https://pokeapi.co/api/v2"

async def fetch_pokemon_data(name):
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{API_BASE}/pokemon/{name}")
            if resp.status_code != 200:
                return {"error": f"Pokémon '{name}' not found."}

            pokemon_data = resp.json()
            stats = {s["stat"]["name"]: s["base_stat"] for s in pokemon_data["stats"]}
            types = [t["type"]["name"] for t in pokemon_data["types"]]
            abilities = [a["ability"]["name"] for a in pokemon_data["abilities"]]

            # Moves
            moves = []
            for move in pokemon_data["moves"][:10]:
                move_resp = await client.get(move["move"]["url"])
                move_data = move_resp.json()
                moves.append({
                    "name": move["move"]["name"],
                    "power": move_data.get("power"),
                    "accuracy": move_data.get("accuracy"),
                    "type": move_data["type"]["name"]
                })

            # Evolution
            species_resp = await client.get(pokemon_data["species"]["url"])
            evo_chain_url = species_resp.json()["evolution_chain"]["url"]
            evo_resp = await client.get(evo_chain_url)
            chain = evo_resp.json()["chain"]
            evolution = chain["evolves_to"][0]["species"]["name"] if chain["evolves_to"] else "None"

            return {
                "name": pokemon_data["name"],
                "types": types,
                "abilities": abilities,
                "stats": stats,
                "moves": moves,
                "evolution": evolution
            }
    except Exception as e:
        return {"error": str(e)}