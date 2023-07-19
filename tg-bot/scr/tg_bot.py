# -*- coding: utf-8 -*-
import telegram
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater, CallbackQueryHandler, InlineQueryHandler, PrefixHandler

import logging
logging.basicConfig(filename="tmp/info.log", level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)

token = "6143246892:AAEQGuhkqKZ-6Hsn7cvvbUMwOW0rNOHHGSE"
#token = "5658241360:AAFMBbtWmi-TrvNV2OnrylSEs8ijqVySoRw" Запасной токен
bot = telegram.Bot(token=token)
updater = Updater(token=token, use_context=True)

import spec
import prefix
import functions as func

from case import echo_call, fun_handler
from inline import inline_query

updater.dispatcher.add_handler(CallbackQueryHandler(echo_call))# base check-callback-query

updater.dispatcher.add_handler(CommandHandler('start', func.start_handler))#     command
updater.dispatcher.add_handler(CommandHandler('help', func.help_handler))#       command
updater.dispatcher.add_handler(CommandHandler('FAQ', func.faq_handler))#         command
updater.dispatcher.add_handler(CommandHandler('fun', fun_handler))#              command
updater.dispatcher.add_handler(CommandHandler('pack', func.pack_handler))#       command
updater.dispatcher.add_handler(CommandHandler('links', func.link_handler))#      command
updater.dispatcher.add_handler(CommandHandler('learning', func.learn_handler))#  command
updater.dispatcher.add_handler(CommandHandler('support', func.support_handler))# command

updater.dispatcher.add_handler(CommandHandler('menu', func.back_handler))#       any command-line
updater.dispatcher.add_handler(CommandHandler("back", func.back_handler))#       any command-line

updater.dispatcher.add_handler(PrefixHandler('/', 'рецензия', prefix.prefix_marks))# any-func
updater.dispatcher.add_handler(PrefixHandler('/', 'погода', prefix.prefix_weather))# any-func

updater.dispatcher.add_handler(PrefixHandler('/', 'город', prefix.city_create))# create game
updater.dispatcher.add_handler(PrefixHandler('/', 'мойгород', prefix.mycity))#   info game
updater.dispatcher.add_handler(PrefixHandler('/', 'mycity', prefix.mycity))#     info game
updater.dispatcher.add_handler(PrefixHandler('/', 'change', prefix.change))#     control game
updater.dispatcher.add_handler(PrefixHandler('/', 'изменить', prefix.change))#   control game
updater.dispatcher.add_handler(PrefixHandler('/', 'update', prefix.update))#     update time-game

updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), func.echo_handler))# filters for spam
updater.dispatcher.add_handler(MessageHandler(Filters.photo, func.echo_handler))#                     filters for spam

updater.dispatcher.add_handler(InlineQueryHandler(inline_query))# inline-mode

updater.dispatcher.add_handler(PrefixHandler('/', 'ban', spec.ban))#          ADMIN COMMAND
updater.dispatcher.add_handler(PrefixHandler('/', 'unban', spec.unban))#      ADMIN COMMAND
updater.dispatcher.add_handler(PrefixHandler('/', 'betaadd', spec.add_beta))# ADMIN COMMAND
updater.dispatcher.add_handler(PrefixHandler('/', 'betadel', spec.del_beta))# ADMIN COMMAND

import logg

updater.dispatcher.add_handler(CommandHandler(logg.password[0], logg.clear))

while True:
    try:
        updater.start_polling()
        updater.idle()
    except ZeroDivisionError as err:
        logger.error(err)
        continue