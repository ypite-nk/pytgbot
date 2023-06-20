# -*- coding: utf-8 -*-
import telegram
import functions as func
from case import echo_button, fun_handler, game2_handler

from telegram.ext import CommandHandler, MessageHandler, Filters, Updater, CallbackQueryHandler, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
from uuid import uuid4
from html import escape

token = "6143246892:AAEQGuhkqKZ-6Hsn7cvvbUMwOW0rNOHHGSE"
bot = telegram.Bot(token=token)
updater = Updater(token=token, use_context=True)

def inline_query(update, context):
    query = update.inline_query.query

    if not query:
        return

    result = [
        InlineQueryResultArticle(id=str(uuid4()), title="Caps",
                                 input_message_content=InputTextMessageContent(query.upper())
                                 ),
        InlineQueryResultArticle(id=str(uuid4()), title="Bold",
                                 input_message_content=InputTextMessageContent(f"<b>{escape(query)}</b>", parse_mode=telegram.ParseMode.HTML)
                                 ),
        InlineQueryResultArticle(id=str(uuid4()), title="Italic",
                                 input_message_content=InputTextMessageContent(f"<i>{escape(query)}</i>", parse_mode=telegram.ParseMode.HTML)
                                 ),
        ]

    update.inline_query.answer(result)

updater.dispatcher.add_handler(CommandHandler('start', func.start_handler))
updater.dispatcher.add_handler(CommandHandler('info', func.info_handler))
updater.dispatcher.add_handler(CommandHandler('help', func.help_handler))
updater.dispatcher.add_handler(CommandHandler('FAQ', func.faq_handler))
updater.dispatcher.add_handler(CommandHandler('fun', fun_handler))
updater.dispatcher.add_handler(CommandHandler('pack', func.pack_handler))
updater.dispatcher.add_handler(CommandHandler('links', func.link_handler))
updater.dispatcher.add_handler(CommandHandler('learning', func.learn_handler))
updater.dispatcher.add_handler(CommandHandler('support', func.support_handler))

updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), func.echo_handler))

updater.dispatcher.add_handler(CommandHandler('menu', func.back_handler))
updater.dispatcher.add_handler(CommandHandler("back", func.back_handler))

updater.dispatcher.add_handler(CommandHandler('mem', game2_handler))
#updater.dispatcher.add_handler(CommandHandler('game3', game3_handler))
#updater.dispatcher.add_handler(CommandHandler('game4', game4_handler))

updater.dispatcher.add_handler(CallbackQueryHandler(echo_button))
updater.dispatcher.add_handler(InlineQueryHandler(inline_query))

updater.start_polling()
updater.idle()