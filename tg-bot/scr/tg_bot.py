﻿# -*- coding: utf-8 -*-
import telegram
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater, CallbackQueryHandler, InlineQueryHandler, PrefixHandler

import logging
logging.basicConfig(filename="tmp/info.log", level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)

token = "6143246892:AAEQGuhkqKZ-6Hsn7cvvbUMwOW0rNOHHGSE"
bot = telegram.Bot(token=token)
updater = Updater(token=token, use_context=True)

import spec
from case import echo_button, fun_handler
from inline import inline_query
import functions as func

updater.dispatcher.add_handler(CallbackQueryHandler(echo_button))

updater.dispatcher.add_handler(InlineQueryHandler(inline_query))

updater.dispatcher.add_handler(CommandHandler('start', func.start_handler))
updater.dispatcher.add_handler(CommandHandler('help', func.help_handler))
updater.dispatcher.add_handler(CommandHandler('FAQ', func.faq_handler))
updater.dispatcher.add_handler(CommandHandler('fun', fun_handler))
updater.dispatcher.add_handler(CommandHandler('pack', func.pack_handler))
updater.dispatcher.add_handler(CommandHandler('links', func.link_handler))
updater.dispatcher.add_handler(CommandHandler('learning', func.learn_handler))
updater.dispatcher.add_handler(CommandHandler('support', func.support_handler))

updater.dispatcher.add_handler(CommandHandler('menu', func.back_handler))
updater.dispatcher.add_handler(CommandHandler("back", func.back_handler))

updater.dispatcher.add_handler(PrefixHandler('!', 'рецензия', func.prefix_marks))

updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), func.echo_handler))

updater.dispatcher.add_handler(PrefixHandler('/', 'ban', spec.ban))
updater.dispatcher.add_handler(PrefixHandler('/', 'unban', spec.unban))

updater.dispatcher.add_handler(CommandHandler('banlist', spec.banlist))

import logg

updater.dispatcher.add_handler(CommandHandler(logg.password[0], logg.clear))

while True:
    try:
        updater.start_polling()
        updater.idle()
    except ZeroDivisionError as err:
        logger.error(err)
        continue