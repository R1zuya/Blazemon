import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

TOKEN = os.environ.get("7972422177:AAGTkCgvKuYLu16qdzB1LrnidxvKwB1n93E")  # Use environment variable for token
if not TOKEN:
    print("TELEGRAM_BOT_TOKEN environment variable not set. Please set it.")
    exit()
