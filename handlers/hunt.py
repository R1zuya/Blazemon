import random
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackContext
from pokemon_api import get_pokemon_data

POKEMON_SPECIES_URL = "https://pokeapi.co/api/v2/pokemon-species/"

# Function to check if a Pokémon is evolved
def is_evolved(pokemon_name):
    response = requests.get(f"{POKEMON_SPECIES_URL}{pokemon_name.lower()}/")
    if response.status_code == 200:
        data = response.json()
        return data["evolves_from_species"] is not None  # If it has a pre-evolution, it's evolved
    return False  # If API fails, assume it's unevolved

async def hunt(update: Update, context: CallbackContext):
    # Get a random Pokémon ID (from 1 to 151 for Gen 1, modify if needed)
    pokemon_id = random.randint(1, 151)
    
    # Fetch Pokémon data from API
    pokemon_data = get_pokemon_data(str(pokemon_id))
    if not pokemon_data:
        await update.message.reply_text("No Pokémon found!")
        return

    # Check if Pokémon is evolved
    evolved = is_evolved(pokemon_data["name"])
    
    # Set level range based on evolution stage
    level = random.randint(25, 55) if evolved else random.randint(1, 25)

    # Format response message
    message = f"A wild **{pokemon_data['name']}** appeared! 🌿🔥⚡\n"
    message += f"Type: {', '.join(pokemon_data['type'])}\n"
    message += f"Level: {level}\n"

    # Inline button for battle
    keyboard = [[InlineKeyboardButton("⚔️ Battle", callback_data=f"battle_{pokemon_data['name']}_{level}")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the message with the battle button
    await update.message.reply_text(message, reply_markup=reply_markup, parse_mode="Markdown")

hunt_command = CommandHandler("hunt", hunt)
