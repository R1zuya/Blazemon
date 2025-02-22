import random
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from utils.helpers import calculate_damage

async def battle(update: Update, context: CallbackContext):
    user_pokemon = "Charmander"
    wild_pokemon = "Squirtle"
    damage = calculate_damage(user_pokemon, wild_pokemon)
    await update.message.reply_text(f"{user_pokemon} attacked {wild_pokemon} and dealt {damage} damage!")

battle_command = CommandHandler("battle", battle)
