import requests as r
import os, sys
import json
import html
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client
from Chatbot import pbot, BOT_USERNAME, ALIVE_PIC, SUPPORT_CHAT
import asyncio
from pyrogram import filters


START_MSG = """
Hey there {}, I am {} 
I am a chatbot you can either add me to group for chatting. 
or you can chat here.
For more information click on About button.

For updates join my updates channel and for bot support join my support chat
The links are given below."""

ABT_MSG = """
Hey there {}, this bot was made by
• [PSYCHOPOMP](https://t.me/Horni_Senpaii)

This bot uses kuki api to process your text and give a perfect reply.
• [Kuki Api](https://www.kuki.ai/research)

• [Pyrogram](https://docs.pyrogram.org)

Repository Link
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
async def faqs(_, query):
    await query.message.edit(text=ABT_MSG.format(query.from_user.first_name), reply_markup= Abt_btn)

@pbot.on_callback_query(filters.regex("abt_close"))
async def abt_close(_, query):
    await query.message.delete()

@pbot.on_callback_query(filters.regex("abt_back"))
async def abt_back(bot, query):
    await query.message.edit(text=START_MSG.format(bot.id, query.from_user.first_name), reply_markup= Home_btn)

@pbot.on_message(filters.command(["start", f"start@{BOT_USERNAME}"]) & filters.private)
async def start(bot, message):
            msg = message
            umer_name = msg.from_user.first_name
            await msg.reply_text(START_MESSAGE.format(umer_name), 
                              reply_markup=Home_btn)

@pbot.on_message(filters.command(["start", f"start@{BOT_USERNAME}"]) & filters.group )
async def grp_start(bot, messages):
             await msg.reply_text("Thanks for adding me to this group. Feel free to chat.")

@pbot.on_message(filters.text & filters.incoming)
async def chatbot(bot, message):
    chat_id = message.chat.id
    await bot.send_chat_action(chat_id, action="typing")
    Chab = r.get('https://kukiapi.up.railway.app/Kuki/chatbot?message='+Message)
    Chet = json.loads(Chab.text)
    chet = Chet['reply']
    sleep(0.3)
    await message.reply_text(chet, timeout=60)

if __name__ == "__main__":
      pbot.send_photo(f"@{SUPPORT_CHAT}", f"{ALIVE_PIC}",  caption="Im alive to chat master")
      idle()
