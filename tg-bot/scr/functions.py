# -*- coding: utf-8 -*-
import telegram
import random
import used_class
import keyboardbot as kb

from telegram import InlineKeyboardMarkup

from spec import checkban
from openf import openf
from echo import echo

def start_handler(update, context):
    echo(update, context)
    if checkban(update, context):
        return 0
    context.bot.send_message(chat_id=update.message.chat_id, text=openf("descriptext", "start_description"),
                             reply_markup=InlineKeyboardMarkup(kb.start_key))

def help_handler(update, context):
    echo(update, context)
    if checkban(update, context):
        return 0
    context.bot.send_message(chat_id=update.message.chat_id, text="По всем вопросам вы можете обратиться к @ypite_nk",
                             reply_markup=InlineKeyboardMarkup(kb.commands_out))

def faq_handler(update, context):
    echo(update, context)
    if checkban(update, context):
        return 0
    update.message.reply_text(openf("info", "faq_handler"), reply_markup=InlineKeyboardMarkup(kb.FAQ))

def pack_handler(update, context):
    echo(update, context)
    if checkban(update, context):
        return 0
    update.message.reply_text(openf("info", "pack"), reply_markup=InlineKeyboardMarkup(kb.commands_out), parse_mode=telegram.ParseMode.HTML)

def link_handler(update, context):
    echo(update, context)
    if checkban(update, context):
        return 0
    update.message.reply_text(openf("links", "mylinks"),
                              reply_markup=InlineKeyboardMarkup(kb.link))

def learn_handler(update, context):
    echo(update, context)
    if checkban(update, context):
        return 0
    update.message.reply_text(openf("learn", "description"), reply_markup=InlineKeyboardMarkup(kb.learns))

def support_handler(update, context):
    echo(update, context)
    if checkban(update, context):
        return 0
    update.message.reply_text(openf("info", "support"), reply_markup=InlineKeyboardMarkup(kb.support))

def echo_handler(update, context):
    echo(update, context)
    if checkban(update, context):
        return 0
    with open("info/hi.txt", "r", encoding="utf-8") as file:
        file = file.readlines(0)
    hi = True
    for i in file:
        if i.replace("\n", "").lower() in update.message.text.lower():
            update.message.reply_text(openf("info", "echohi"), reply_markup=InlineKeyboardMarkup(kb.backdel))
            hi = False
    if hi == True:
        update.message.reply_text(openf("info", "echo"), reply_markup=InlineKeyboardMarkup(kb.backdel))

    hi = True

def back_handler(update, context):
    echo(update, context)
    if checkban(update, context):
        return 0
    update.message.reply_text(openf("descriptext", "menu"), reply_markup=InlineKeyboardMarkup(kb.start_key))

def fun_handler(update, context):
    echo(update, context)
    if checkban(update, context):
        return 0
    update.message.reply_text(openf("descriptext", "fun"),
                              reply_markup=InlineKeyboardMarkup(kb.key))

def prefix_marks(update, context):
    echo(update, context)
    if checkban(update, context):
        return 0
    marks_id_memory = []
    with open("info/ypiter/marks/memory.txt", "r", encoding="utf-8") as file:
        file = file.readlines()
        for i in file:
            marks_id_memory.append(i.replace("\n", ""))
    if update.message.chat['username'] in marks_id_memory:
        update.message.reply_text("Вы уже отправляли рецензию!")
    else:
        if "\n" in update.message.text and len(update.message.text.split("\n")) == 5:
            with open("info/ypiter/marks/memory.txt", "w", encoding="utf-8") as file:
                marks_id_memory.append(update.message.chat['username'])
                for i in range(len(marks_id_memory)):
                    if i != len(marks_id_memory):
                        file.write(marks_id_memory[i] + "\n")
                    else:
                        file.write(marks_id_memory[i])
            marksget = update.message.text.split("\n")
            context.bot.send_message(chat_id=-1001955905639, text="Type: " + marksget[0] + "\n" + 
                                                                        "Link: " + marksget[1] + "\n" + 
                                                                        "Text: " + marksget[2] + "\n" + 
                                                                        "A: " + marksget[3] + "\n" + 
                                                                        "P: " + marksget[4] + "\n")
            update.message.reply_text(openf("info/ypiter/marks", "markssucces"), reply_markup=InlineKeyboardMarkup(kb.backdel))
        else:
            update.message.reply_text(openf("info/ypiter/marks", "markserror"), reply_markup=InlineKeyboardMarkup(kb.backdel))