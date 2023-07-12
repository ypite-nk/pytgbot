# -*- coding: utf-8 -*-
import keyboardbot as kb

from telegram import InlineKeyboardMarkup, ParseMode

from spec import checkban, openf, write_marks

def start_handler(update, context):
    if checkban(update, context):
        return
    context.bot.send_message(chat_id=update.message.chat_id, text=openf("descriptext", "start_description"),
                             reply_markup=InlineKeyboardMarkup(kb.start_key))

def help_handler(update, context):
    if checkban(update, context):
        return
    context.bot.send_message(chat_id=update.message.chat_id, text="По всем вопросам вы можете обратиться к @ypite_nk",
                             reply_markup=InlineKeyboardMarkup(kb.commands_out))

def faq_handler(update, context):
    if checkban(update, context):
        return
    update.message.reply_text(openf("info", "faq_handler"), reply_markup=InlineKeyboardMarkup(kb.FAQ))

def pack_handler(update, context):
    if checkban(update, context):
        return
    update.message.reply_text(openf("info", "pack"), reply_markup=InlineKeyboardMarkup(kb.commands_out), parse_mode=ParseMode.HTML)

def link_handler(update, context):
    if checkban(update, context):
        return
    update.message.reply_text(openf("links", "mylinks"),
                              reply_markup=InlineKeyboardMarkup(kb.link))

def learn_handler(update, context):
    if checkban(update, context):
        return
    update.message.reply_text(openf("learn", "description"), reply_markup=InlineKeyboardMarkup(kb.learns))

def support_handler(update, context):
    if checkban(update, context):
        return
    update.message.reply_photo('https://raw.githubusercontent.com/ypite-nk/Sticker/main/paytinkoff.webp', parse_mode=ParseMode.HTML)
    update.message.reply_text(openf("info", "support"), reply_markup=InlineKeyboardMarkup(kb.support), parse_mode=ParseMode.HTML)

def echo_handler(update, context):
    if checkban(update, context):
        return
    
    if write_marks(update, context):
        return

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
    if checkban(update, context):
        return
    update.message.reply_text(openf("descriptext", "menu"), reply_markup=InlineKeyboardMarkup(kb.start_key))

def fun_handler(update, context):
    if checkban(update, context):
        return
    update.message.reply_text(openf("descriptext", "fun"),
                              reply_markup=InlineKeyboardMarkup(kb.key))