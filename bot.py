from telegram.ext import Application
from config import TOKEN
from handlers.start import start_command
from handlers.hunt import hunt_command

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(start_command)
    app.add_handler(hunt_command)

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
