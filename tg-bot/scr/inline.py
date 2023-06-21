# -*- coding: utf-8 -*-
import telegram

from telegram import InlineQueryResultArticle, InputTextMessageContent
from uuid import uuid4
from html import escape

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