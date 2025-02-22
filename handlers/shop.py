async def my_inventory(update: Update, context: CallbackContext):
    await update.message.reply_text("You have 10 Poké Balls and $500.")

async def shop(update: Update, context: CallbackContext):
    await update.message.reply_text("Poké Mart is open! Buy Poké Balls!")

inventory_command = CommandHandler("inventory", my_inventory)
shop_command = CommandHandler("shop", shop)

