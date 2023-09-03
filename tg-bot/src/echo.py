# -*- coding: utf-8 -*-
import os
import psutil

def echo(update, context):
    try:
        print(f"\n | Command: {update.callback_query['data']}\n | From: {update.callback_query.message.chat['username']}\n | Message_ID: {update.callback_query.message.message_id}\n | ID: {update.callback_query.message.chat_id}\n")
    except:
        try:
            print(f"\n | Text: {update.message.text}\n | From: {update.message.chat['username']}\n | ID: {update.message.chat_id}\n")
        except:
            print(f"\n | Text: {update.inline_query.query}\n | From: {update.inline_query.from_user['username']}\n | ID: {update.inline_query.from_user.id}\n")

    print(f"\n || CPU usage: {psutil.cpu_percent()} %\n || MEM usage: {int((psutil.Process(os.getpid()).memory_info()[0]/2 **30) * 1024)} MB\n")