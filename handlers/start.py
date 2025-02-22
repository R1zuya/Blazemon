from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackContext
from pokemon_api import get_pokemon_data

async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Choose Starter", callback_data='choose_starter')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome to the Pokémon Telegram Bot!\nChoose your starter:", reply_markup=reply_markup)

start_command = CommandHandler("start", start)

