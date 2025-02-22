import requests
import json
from config import POKEMON_API_URL

def get_pokemon_data(pokemon_name):
    url = f"{POKEMON_API_URL}pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        pokemon_info = {
            "name": data["name"].capitalize(),
            "type": [t["type"]["name"] for t in data["types"]],
            "base_stats": {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]},
            "moves": [move["move"]["name"] for move in data["moves"][:4]],
            "catch_rate": 45,  # Set a default or fetch from another endpoint
        }
        return pokemon_info
    else:
        return None

