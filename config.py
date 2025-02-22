import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Correct way to fetch the token
POKEMON_API_URL = "https://pokeapi.co/api/v2/"

if not TOKEN:
    print("Error: TELEGRAM_BOT_TOKEN is not set correctly!")
    exit()
