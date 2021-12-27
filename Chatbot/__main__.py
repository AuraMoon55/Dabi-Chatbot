import requests as r

from telegram.ext import (
    ConversationHandler,
    CallbackQueryHandler,
)
import os, sys
import json
import html
from telegram.ext.dispatcher import run_async
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from pyrogram import Client
from Chatbot import dispatcher, updater, pbot, BOT_USERNAME, ALIVE_PIC, SUPPORT_CHAT
import asyncio
from pyrogram import fitlers
from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram.error import BadRequest, RetryAfter, Unauthorized
from telegram.ext import CommandHandler, run_async, CallbackContext, MessageHandler, Filters
from telegram.utils.helpers import mention_html, mention_markdown, escape_markdown
from time import sleep
from telegram import ParseMode


START_MSG = """
Hey there {}, I am {} 
I am a chatbot you can either add me to group for chatting. 
or you can chat here.\n For more information click on About button.\n
For updates join my updates channel and for bot support join my support chat \n
The links are given below."""

ABT_MSG = """
Hey there {}, this bot was made by \n
• [PSYCHOPOMP](https://t.me/Horni_Senpaii) \n \n
This bot uses kuki api to process your text and give a perfect reply. \n
• [Kuki Api](https://www.kuki.ai/research) \n
• [Pyrogram](https://docs.pyrogram.org) \n  \n
Repository Link \n
• Not added yet 
"""

Home_btn = InlineKeyboardMarkup([[InlineKeyboardButton(text="About", callback_data="abt")],
                                 [InlineKeyboardButton(text="Support Group", url="https://t.me/Villainevil_support"),
                                  InlineKeyboardButton(text="Updates Channel", url="https://t.me/dabi_updates")],
                                 [InlineKeyboardButton(text="Close", callback_data="abt_close")]
                                ])


Abt_btn = InlineKeyboardMarkup([[InlineKeyboardButton(text="Back", callback_data="abt_back"),
                                 InlineKeyboardButton(text="Close", callback_data="abt_close")]
                               ])


@pbot.on_callback_query(filters.regex("abt"))
async def faqs(update, context):
    update.effectivemessage.edit(text=ABT_MSG.format(update.effective_user.first_name), reply_markup= Abt_btn, parse_mode=ParseMode.MARKDOWN)

@pbot.on_callback_query(filters.regex("abt_close"))
async def abt_close(update, context):
    update.effective_message.delete()

@pbot.on_callback_query(filters.regex("abt_back"))
async def abt_back(update, context):
    query.message.edit(text=START_MSG.format(context.bot.id, update.effective_user.first_name), reply_markup= Home_btn, parse_mode=ParseMode.MARKDOWN)

@pbot.on_message(filters.command(["start", f"start@{BOT_USERNAME}"]) & filters.private)
async def start(update: Update, context: CallbackContext):
            msg = update.effective_message
            umer_name = update.effective_user.first_name
            bot = context.bot
            msg.reply_text(START_MESSAGE.format(umer_name), 
                              reply_markup=Home_btn,
                              parse_mode=ParseMode.MARKDOWN)

@pbot.on_message(filters.command(["start", f"start@{BOT_USERNAME}"]) & filters.group )
async def grp_start(message: Message, context: CallbackContext):
             bot = context.bot
             msg.reply_text("Thanks for adding me to this group. Feel free to chat.")

@pbot.on_message(filters.text & filters.incoming & filters.private & filters.group)
def chatbot(update: Update, context: CallbackContext):
    message = update.effective_message
    chat_id = update.effective_chat.id
    bot = context.bot
    if message.text and not message.document:
        Message = message.text
        bot.send_chat_action(chat_id, action="typing")
        Chab = r.get('https://kukiapi.up.railway.app/Kuki/chatbot?message='+Message)
        Chet = json.loads(Chab.text)
        chet = Chet['reply']
        sleep(0.3)
        message.reply_text(chet, timeout=60)

def main():

    if SUPPORT_CHAT is not None and isinstance(SUPPORT_CHAT, str):
        try:
            dispatcher.bot.send_photo(f"@{SUPPORT_CHAT}, f"{ALIVE_PIC}", caption="I'm alive to chat! master")
            updater.start_polling(timeout=15, read_latency=4)
            updater.idle()

if __name__ = "__main__":
   main()
