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
# UPDATER NOT UD ; UD - updater.dispatcher FROM add_handler!!!
from case import echo_call, fun_handler
ud.add_handler(CallbackQueryHandler(echo_call))#                 base check-callback-query
import functions as func
ud.add_handler(CommandHandler('start', func.start_handler))#     command
ud.add_handler(CommandHandler('menu', func.back_handler))#       any command-line
ud.add_handler(CommandHandler("back", func.back_handler))#       any command-line
import prefix
ud.add_handler(PrefixHandler('/', 'рецензия', prefix.prefix_marks))#     any-func
ud.add_handler(PrefixHandler('/', 'погода', prefix.prefix_weather))#     any-func
ud.add_handler(PrefixHandler('/', 'город', prefix.city_create))#         create game
ud.add_handler(PrefixHandler('/', 'мойгород', prefix.mycity))#           info game
ud.add_handler(PrefixHandler('/', 'mycity', prefix.mycity))#             info game
ud.add_handler(PrefixHandler('/', 'change', prefix.change))#             control game
ud.add_handler(PrefixHandler('/', 'изменить', prefix.change))#           control game
ud.add_handler(PrefixHandler('/', 'update', prefix.update))#             update time-game
ud.add_handler(PrefixHandler('/', 'update_event', prefix.update_event))# update time-game
# filters for spam
ud.add_handler(MessageHandler(Filters.text & (~Filters.command), func.echo_handler))
ud.add_handler(MessageHandler(Filters.photo, func.echo_handler))
from inline import inline_query
ud.add_handler(InlineQueryHandler(inline_query))# inline-mode
import spec
ud.add_handler(PrefixHandler('/', 'ban', spec.admin))#     ADMIN COMMAND
ud.add_handler(PrefixHandler('/', 'unban', spec.admin))#   ADMIN COMMAND
ud.add_handler(PrefixHandler('/', 'addbeta', spec.admin))# ADMIN COMMAND
ud.add_handler(PrefixHandler('/', 'delbeta', spec.admin))# ADMIN COMMAND
import logg
ud.add_handler(CommandHandler(logg.password[0], logg.clear))

while True:
    try:
        updater.start_polling()
        updater.idle()
    except ZeroDivisionError as err:
        logger.error(err)
        continue