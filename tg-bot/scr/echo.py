# -*- coding: utf-8 -*-
import os
import psutil
def echo(update, context): # ОТЛАДКА
    try:
        print(f"\n | Text: {update.callback_query['data']}\n | From: {update.callback_query.message.chat['username']}\n | Message_ID: {update.callback_query.message.message_id}\n | ID: {update.callback_query.message.chat['id']}\n")
    except TypeError:
        print(f"\n | Command: {update.message.text}\n | From: {update.message.chat['username']}\n | ID: {update.message.chat['id']}\n")

    print(f"\n || CPU usage: {psutil.cpu_percent()} %\n || MEM usage: {int((psutil.Process(os.getpid()).memory_info()[0]/2 **30) * 1024)} MB\n")