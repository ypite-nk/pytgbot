# -*- coding: utf-8 -*-
file = open("tmp/info.log", "r+")
password = open("tmp/log.txt", "r").readlines(0)
def clear(update, context):
    file.truncate(0)
    context.bot.send_message(chat_id=update.message.chat_id, text="Logg clear")