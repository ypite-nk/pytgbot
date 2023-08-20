# -*- coding: utf-8 -*-
import telegram
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater, CallbackQueryHandler, InlineQueryHandler, PrefixHandler

import logging
logging.basicConfig(filename="tmp/info.log", level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)

bot = telegram.Bot(token="6143246892:AAEQGuhkqKZ-6Hsn7cvvbUMwOW0rNOHHGSE")
updater = Updater(token="6143246892:AAEQGuhkqKZ-6Hsn7cvvbUMwOW0rNOHHGSE", use_context=True)
ud = updater.dispatcher

from case import echo_call
ud.add_handler(CallbackQueryHandler(echo_call))

import functions as func
ud.add_handler(CommandHandler('start', func.start_handler))
ud.add_handler(CommandHandler('menu', func.back_handler))
ud.add_handler(CommandHandler("back", func.back_handler))

import prefix
ud.add_handler(PrefixHandler('/', 'погода', prefix.prefix_weather))
ud.add_handler(PrefixHandler('/', 'update', prefix.update))
ud.add_handler(PrefixHandler('/', 'update_event', prefix.update_event))
ud.add_handler(PrefixHandler('/', 'update_week', prefix.update_week))

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

import logg
ud.add_handler(CommandHandler(logg.password[0], logg.clear))

while True:
    try:
        updater.start_polling()
        updater.idle()
    except ZeroDivisionError as err: logger.error(err)