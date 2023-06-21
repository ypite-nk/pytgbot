# -*- coding: utf-8 -*-
import telegram
import functions as func
from case import echo_button, fun_handler, game2_handler
from inline import inline_query

from telegram.ext import CommandHandler, MessageHandler, Filters, Updater, CallbackQueryHandler, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
# BOT INIT
token = "6143246892:AAEQGuhkqKZ-6Hsn7cvvbUMwOW0rNOHHGSE"
bot = telegram.Bot(token=token)
updater = Updater(token=token, use_context=True)
# COMMANDS
updater.dispatcher.add_handler(CommandHandler('start', func.start_handler))
updater.dispatcher.add_handler(CommandHandler('info', func.info_handler))
updater.dispatcher.add_handler(CommandHandler('help', func.help_handler))
updater.dispatcher.add_handler(CommandHandler('FAQ', func.faq_handler))
updater.dispatcher.add_handler(CommandHandler('fun', fun_handler))
updater.dispatcher.add_handler(CommandHandler('pack', func.pack_handler))
updater.dispatcher.add_handler(CommandHandler('links', func.link_handler))
updater.dispatcher.add_handler(CommandHandler('learning', func.learn_handler))
updater.dispatcher.add_handler(CommandHandler('support', func.support_handler))
# ECHO TEXT
updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), func.echo_handler))
# BASE COMMAND
updater.dispatcher.add_handler(CommandHandler('menu', func.back_handler))
updater.dispatcher.add_handler(CommandHandler("back", func.back_handler))
# GAME
updater.dispatcher.add_handler(CommandHandler('mem', game2_handler))
#updater.dispatcher.add_handler(CommandHandler('game3', game3_handler))
#updater.dispatcher.add_handler(CommandHandler('game4', game4_handler))
# CALLBACK FROM KEYBOARD
updater.dispatcher.add_handler(CallbackQueryHandler(echo_button))
# INLINE @mode
updater.dispatcher.add_handler(InlineQueryHandler(inline_query))
# POLLING AND IDLE
updater.start_polling()
updater.idle()