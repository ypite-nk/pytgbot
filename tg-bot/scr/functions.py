# -*- coding: utf-8 -*-
import keyboardbot as kb
from telegram import InlineKeyboardMarkup
from spec import check_acces, openfile

@check_acces
def start_handler(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text=openfile("data", "start"),
                             reply_markup=InlineKeyboardMarkup(kb.start_key))
    from login import User
    User(str(update.message.chat_id)).authorize()

@check_acces
def back_handler(update, context):
    update.message.reply_text(openfile("menu", "menu"),
                              reply_markup=InlineKeyboardMarkup(kb.start_key))

from spec import Echo_Checker

@check_acces
def echo_handler(update, context):
    Checker = Echo_Checker(update, context)
    if Checker.echo_check():
        update.message.reply_text(Checker.message,
                                  reply_markup=Checker.reply_markup)
        return

    with open("data/echo/hi.txt", "r", encoding="utf-8") as file: file = file.readlines(0)
    hi = True
    for i in file:
        if i.replace("\n", "").lower() in update.message.text.lower() and hi == True:
            update.message.reply_text(openfile("data/echo", "echohi"),
                                      reply_markup=InlineKeyboardMarkup(kb.back))
            hi = False
    if hi == True: update.message.reply_text(openfile("data/echo", "echo"),
                                             reply_markup=InlineKeyboardMarkup(kb.back))