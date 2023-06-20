# -*- coding: utf-8 -*-
import telegram
import keyboard as kb

from telegram import InlineKeyboardMarkup

def start_handler(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="".join(open("../start_description.txt", "r", encoding="utf-8").readlines(0)),
                             reply_markup=InlineKeyboardMarkup(kb.start_key))

def info_handler(update, context):
    update.message.reply_text("".join(open("../info_handler.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.commands_out))

def help_handler(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="По всем вопросам вы можете обратиться к @ypite_nk",
                             reply_markup=InlineKeyboardMarkup(kb.commands_out))

def faq_handler(update, context):
    update.message.reply_text("Какой тип информации вас интересует?", reply_markup=InlineKeyboardMarkup(kb.FAQ))

def pack_handler(update, context):
    update.message.reply_text("".join(open("../pack.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.commands_out), parse_mode=telegram.ParseMode.HTML)

def link_handler(update, context):
    update.message.reply_text("".join(open("../links/Mylink.txt", "r", encoding="utf-8").readlines(0)),
                              reply_markup=InlineKeyboardMarkup(kb.button))

def learn_handler(update, context):
    update.message.reply_text("".join(open("../learn/description.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.learns))

def support_handler(update, context):
    update.message.reply_text("".join(open("../support.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.support))

def echo_handler(update, context):
    update.message.reply_text("Пожалуйста, воспользуйтесь интерфейсом или командами. Если у вас есть вопросы: /help")

def back_handler(update, context):
    update.message.reply_text("Меню", reply_markup=InlineKeyboardMarkup(kb.start_key))