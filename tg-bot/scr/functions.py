# -*- coding: utf-8 -*-
import keyboardbot as kb

from telegram import InlineKeyboardMarkup

from spec import checkban, openf

def start_handler(update, context):
    if checkban(update, context):
        return
    context.bot.send_message(chat_id=update.message.chat_id, text=openf("data", "start"),
                             reply_markup=InlineKeyboardMarkup(kb.start_key))

def back_handler(update, context):
    if checkban(update, context):
        return
    update.message.reply_text(openf("menu", "menu"),
                              reply_markup=InlineKeyboardMarkup(kb.start_key))

from spec import Echo_Checker

def echo_handler(update, context):
    if checkban(update, context):
        return
    Checker = Echo_Checker(update, context)
    if Checker.echo_check(update.message.text):
        update.message.reply_text(Checker.message,
                                  reply_markup=Checker.reply_markup)
        return

    with open("data/echo/hi.txt", "r", encoding="utf-8") as file:
        file = file.readlines(0)
    hi = True
    for i in file:
        if i.replace("\n", "").lower() in update.message.text.lower() and hi == True:
            update.message.reply_text(openf("data/echo", "echohi"),
                                      reply_markup=InlineKeyboardMarkup(kb.back))
            hi = False
    if hi == True:
        update.message.reply_text(openf("data/echo", "echo"),
                                  reply_markup=InlineKeyboardMarkup(kb.back))