﻿# -*- coding: utf-8 -*-
import telegram
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater, CallbackQueryHandler, InlineQueryHandler, PrefixHandler

import logging
logging.basicConfig(filename="tmp/info.log", level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)

with open("token.txt", "r", encoding="utf-8") as token: token = token.readlines(0)[0]

bot = telegram.Bot(token=token)
updater = Updater(token=token, use_context=True)
ud = updater.dispatcher

from case import Callback_checker
ud.add_handler(CallbackQueryHandler(Callback_checker))

import functions as func
ud.add_handler(CommandHandler('start', func.start_handler))
ud.add_handler(CommandHandler('menu', func.back_handler))
ud.add_handler(CommandHandler("back", func.back_handler))

import prefix
#ud.add_handler(PrefixHandler('/', 'погода', prefix.prefix_weather))
ud.add_handler(PrefixHandler('/', 'update', prefix.update))
ud.add_handler(PrefixHandler('/', 'update_event', prefix.update_event))
ud.add_handler(PrefixHandler('/', 'update_week', prefix.update_week))
#from login import get_graph
#ud.add_handler(PrefixHandler('/', 'graph', get_graph))

ud.add_handler(MessageHandler(Filters.text & (~Filters.command), func.echo_handler))
ud.add_handler(MessageHandler(Filters.photo, func.echo_handler))

from inline import inline_query
ud.add_handler(InlineQueryHandler(inline_query))

import spec
ud.add_handler(PrefixHandler('/', 'ban', spec.admin))
ud.add_handler(PrefixHandler('/', 'unban', spec.admin))
ud.add_handler(PrefixHandler('/', 'addbeta', spec.admin))
ud.add_handler(PrefixHandler('/', 'delbeta', spec.admin))
ud.add_handler(PrefixHandler('/', 'message', spec.admin))
ud.add_handler(PrefixHandler('/', 'givevip', spec.admin))
ud.add_handler(PrefixHandler('/', 'delvip', spec.admin))
ud.add_handler(PrefixHandler('/', 'wordly', spec.admin))
ud.add_handler(PrefixHandler('/', 'give_money', spec.admin))
ud.add_handler(PrefixHandler('/', 'del_money', spec.admin))

import logg
ud.add_handler(CommandHandler(logg.password[0], logg.clear))

while True:
    try:
        updater.start_polling()
        updater.idle()
    except ZeroDivisionError as err: logger.error(err)