import os 
import logging
import sys
import time

import telegram.ext as tg
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

APP_ID = int(os.environ.get('API_ID', None))

API_HASH = os.environ.get("API_HASH", None)

SUPPORT_CHAT = os.environ.get("SUPPORT", "Villainevil_support")

ALIVE_PIC = os.environ.get("ALIVE_PIC", None)

updater = tg.Updater(
    TOKEN,
    workers=min(32, os.cpu_count() + 4),
    request_kwargs={"read_timeout": 10, "connect_timeout": 10},
)
dispatcher = updater.dispatcher

pbot = Client("Chatty", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)

pbot.start()

app = pbot.get_me()
BOT_ID = app.id
BOT_USERNAME = app.username
