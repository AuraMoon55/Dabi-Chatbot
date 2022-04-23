import os 
import logging
import sys
import time

from pyrogram import Client, errors

StartTime = time.time()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("log.txt"),
        logging.StreamHandler(),
    ],
    level=logging.INFO,
)

ENV = bool(os.environ.get("ENV", False))

TOKEN = os.environ.get("TOKEN", "")

API_ID = int(os.environ.get('API_ID', None))

API_HASH = os.environ.get("API_HASH", None)

SUPPORT_CHAT = os.environ.get("SUPPORT", "Villainevil_support")

ALIVE_PIC = os.environ.get("ALIVE_PIC", None)


pbot = Client("Chatty", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)

pbot.start()

app = pbot.get_me()
BOT_ID = app.id
BOT_USERNAME = app.username
