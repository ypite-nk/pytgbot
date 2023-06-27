# -*- coding: utf-8 -*-
import telegram
import keyboardbot as kb

from telegram import InlineKeyboardMarkup
from openf import openf
from echo import echo

def start_handler(update, context):
    echo(update, context)
    context.bot.send_message(chat_id=update.message.chat_id, text=openf("descriptext", "start_description"),
                             reply_markup=InlineKeyboardMarkup(kb.start_key))

def info_handler(update, context):
    echo(update, context)
    update.message.reply_text(openf("info", "info_handler"), reply_markup=InlineKeyboardMarkup(kb.commands_out))

def help_handler(update, context):
    echo(update, context)
    context.bot.send_message(chat_id=update.message.chat_id, text="По всем вопросам вы можете обратиться к @ypite_nk",
                             reply_markup=InlineKeyboardMarkup(kb.commands_out))

def faq_handler(update, context):
    echo(update, context)
    update.message.reply_text(openf("info", "faq_handler"), reply_markup=InlineKeyboardMarkup(kb.FAQ))

def pack_handler(update, context):
    echo(update, context)
    update.message.reply_text(openf("info", "pack"), reply_markup=InlineKeyboardMarkup(kb.commands_out), parse_mode=telegram.ParseMode.HTML)

def link_handler(update, context):
    echo(update, context)
    update.message.reply_text(openf("links", "mylinks"),
                              reply_markup=InlineKeyboardMarkup(kb.link))

def learn_handler(update, context):
    echo(update, context)
    update.message.reply_text(openf("learn", "description"), reply_markup=InlineKeyboardMarkup(kb.learns))

def support_handler(update, context):
    echo(update, context)
    update.message.reply_text(openf("info", "support"), reply_markup=InlineKeyboardMarkup(kb.support))

def echo_handler(update, context):
    echo(update, context)
    with open("info/hi.txt", "r", encoding="utf-8") as file:
        file = file.readlines(0)
    hi = True
    if ";" in update.message.text:
        if update.message.text.split(";")[0] == "РЕЦЕНЗИЯ":
            if len(update.message.text.split(";")) == 5:
                marksget = update.message.text.split(";")
                context.bot.send_message(chat_id=-1001955905639, text="Type: " + marksget[0] + "\n" + 
                                                                        "Link: " + marksget[1] + "\n" + 
                                                                        "Text: " + marksget[2] + "\n" + 
                                                                        "A: " + marksget[3] + "\n" + 
                                                                        "P: " + marksget[4] + "\n")
                update.message.reply_text(openf("info/ypiter/marks", "markssucces"))
            else:
                update.message.reply_text(openf("info/ypiter/marks", "markserror"))
    else:
        for i in file:
            if i.replace("\n", "").lower() in update.message.text.lower():
                update.message.reply_text(openf("info", "echohi"))
                hi = False
        if hi == True:
            update.message.reply_text(openf("info", "echo"))

    hi = True

def back_handler(update, context):
    echo(update, context)
    update.message.reply_text(openf("descriptext", "menu"), reply_markup=InlineKeyboardMarkup(kb.start_key))