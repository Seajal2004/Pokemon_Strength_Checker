import random
from services.poke_client import fetch_pokemon_data

# Type effectiveness chart (simplified for demo)
type_chart = {
    "fire": {"grass": 2.0, "water": 0.5, "fire": 0.5},
    "water": {"fire": 2.0, "grass": 0.5, "water": 0.5},
    "grass": {"water": 2.0, "fire": 0.5, "grass": 0.5},
    "electric": {"water": 2.0, "electric": 0.5, "grass": 0.5},
    "ground": {"electric": 2.0, "fire": 2.0},
    "normal": {},
}

# Status effect mechanics
status_effects = ["burn", "poison", "paralysis"]

def calculate_type_effectiveness(move_type, defender_types):
    multiplier = 1.0
    for d_type in defender_types:
        multiplier *= type_chart.get(move_type, {}).get(d_type, 1.0)
    return multiplier

def apply_status_effect(pokemon, status):
    pokemon["status"] = status
    pokemon["status_counter"] = 0

def process_status(pokemon, log):
    if pokemon.get("status") == "burn":
        burn_damage = int(pokemon["stats"]["hp"] * 0.1)
        pokemon["hp"] -= burn_damage
        log.append(f"{pokemon['name'].capitalize()} is hurt by burn for {burn_damage} damage.")
    elif pokemon.get("status") == "poison":
        poison_damage = int(pokemon["stats"]["hp"] * 0.08)
        pokemon["hp"] -= poison_damage
        log.append(f"{pokemon['name'].capitalize()} is hurt by poison for {poison_damage} damage.")
    elif pokemon.get("status") == "paralysis":
        if random.random() < 0.25:
            log.append(f"{pokemon['name'].capitalize()} is paralyzed and can't move!")
            return False
    return True

def calculate_damage(attacker, defender, move):
    power = move.get("power", 50)
    atk = attacker["stats"].get("attack", 50)
    defense = defender["stats"].get("defense", 50)
    base = (((2 * 50 / 5 + 2) * power * atk / defense) / 50) + 2
    effectiveness = calculate_type_effectiveness(move["type"], defender["types"])
    return int(base * effectiveness), effectiveness

def choose_move(pokemon):
    valid_moves = [m for m in pokemon["moves"] if m["power"]]
    return random.choice(valid_moves) if valid_moves else None

async def simulate_battle(p1_name, p2_name):
    p1 = await fetch_pokemon_data(p1_name)
    p2 = await fetch_pokemon_data(p2_name)

    if "error" in p1 or "error" in p2:
        return ["Invalid Pokémon data."], "No Winner"

    p1_obj = {"name": p1["name"], "stats": p1["stats"], "types": p1["types"], "moves": p1["moves"], "hp": p1["stats"]["hp"]}
    p2_obj = {"name": p2["name"], "stats": p2["stats"], "types": p2["types"], "moves": p2["moves"], "hp": p2["stats"]["hp"]}

    p1_obj["status"] = None
    p2_obj["status"] = None

    log = []

    # Determine initial turn order
    first, second = (p1_obj, p2_obj) if p1["stats"]["speed"] >= p2["stats"]["speed"] else (p2_obj, p1_obj)

    turn = 1
    while p1_obj["hp"] > 0 and p2_obj["hp"] > 0:
        log.append(f"\n🎯 Turn {turn}:")

        for attacker, defender in [(first, second), (second, first)]:
            if attacker["hp"] <= 0 or defender["hp"] <= 0:
                break

            can_move = process_status(attacker, log)
            if not can_move:
                continue

            move = choose_move(attacker)
            if not move:
                log.append(f"{attacker['name'].capitalize()} has no usable moves!")
                continue

            damage, effectiveness = calculate_damage(attacker, defender, move)
            defender["hp"] -= damage
            log.append(f"{attacker['name'].capitalize()} uses {move['name'].capitalize()} on {defender['name'].capitalize()} for {damage} damage!")
            if effectiveness > 1:
                log.append("It's super effective!")
            elif effectiveness < 1:
                log.append("It's not very effective...")

            # 30% chance to apply a random status effect
            if random.random() < 0.3 and not defender.get("status"):
                status = random.choice(status_effects)
                apply_status_effect(defender, status)
                log.append(f"{defender['name'].capitalize()} is now affected by {status.upper()}!")

            if defender["hp"] <= 0:
                log.append(f"💀 {defender['name'].capitalize()} fainted!")
                break

        turn += 1

    winner = p1_obj["name"] if p1_obj["hp"] > 0 else p2_obj["name"]
    return log, winner