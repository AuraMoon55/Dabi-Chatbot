from Chatbot import dispatcher, updater, SUPPORT_CHAT, ALIVE_PIC 


def chumt():
    if SUPPORT_CHAT is not None and isinstance(SUPPORT_CHAT, str):
        try:
            dispatcher.bot.send_photo(f"@{SUPPORT_CHAT}", f"{ALIVE_PIC}",  caption="Im alive to chat master")
            updater.start_polling(timeout=15, read_latency=4)
            updater.idle()
