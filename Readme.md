# ⚔ PokéSim
# 🧬 Pokémon Battle Simulator & Data Explorer

An interactive Streamlit-based app for simulating Pokémon battles and exploring detailed Pokémon stats. Combines type effectiveness, turn-based logic, and status conditions like Burn, Poison, and Paralysis. Built for educational and entertainment purposes.

---

## 🚀 Features

- Simulate battles between two Pokémon with:
  - Type effectiveness (e.g. Fire vs Grass)
  - Damage calculations based on stats and move power
  - Turn order decided by Speed
  - Status effects (Paralysis, Burn, Poison)
- Pokémon Data Explorer:
  - View base stats, types, and abilities of any Pokémon
- Smooth user interface with background image and theme
- All in one-page Streamlit app — no login required

---

## 🛠 Tech Stack

| Layer        | Tech Used            |
|--------------|----------------------|
| Frontend     | Streamlit (Python)   |
| Backend      | Streamlit            |
| Data Source  | PokéAPI |
| Status Engine| Custom logic (Python classes) |
| UI Styling   | HTML + base64 for background image |

---



## ⚙ How to Run This Project

> 🧩 Prerequisite: Python 3.8+ installed on your system

### 1. Unzip the folder
Extract pokemon-simulator.zip anywhere on your machine.

2. Set up a Python environment (optional but recommended)

```bash
python -m venv venv
## Activate:
source venv/bin/activate        # On macOS / Linux
venv\Scripts\activate.bat       # On Windows
```


3. Install dependencies

```bash
pip install -r requirements.txt
```


4. Run the App

```bash
streamlit run app.py
```

🧪 How It Works
```bash
	1.	Select “Battle Simulator” or “Data Explorer” from the sidebar.
	2.	Enter Pokémon names (e.g. charizard, blastoise).
	3.	Battle Simulator:
	•	Computes damage using attack, defense, and type multiplier
	•	Simulates turn-by-turn battle with speed priority
	•	Includes status effects that affect outcome
	4.	Data Explorer:
	•	Shows Pokémon stats in table format
	•	Fetches data from internal logic or PokéAPI
	5.	All output is shown live in the main panel.
```

⸻
