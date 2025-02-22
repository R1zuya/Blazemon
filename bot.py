from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

TOKEN = "YOUR_BOT_TOKEN_HERE"

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Welcome to the Pokémon Bot!")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
