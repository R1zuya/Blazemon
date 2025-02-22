import random
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from pokemon_api import get_pokemon_data

async def hunt(update: Update, context: CallbackContext):
    wild_pokemon_name = random.choice(["bulbasaur", "charmander", "squirtle"])
    wild_pokemon = get_pokemon_data(wild_pokemon_name)

    if wild_pokemon:
        message = f"A wild {wild_pokemon['name']} appeared!\nType: {', '.join(wild_pokemon['type'])}"
        await update.message.reply_text(message)
    else:
        await update.message.reply_text("No Pokémon found!")

hunt_command = CommandHandler("hunt", hunt)

