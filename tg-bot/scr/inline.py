# -*- coding: utf-8 -*-
from telegram import InlineQueryResultPhoto, InlineQueryResultArticle, InputTextMessageContent
from googletrans import Translator as TR
TR = TR()

from uuid import uuid4
from prefix import prefix_weather

linkslist = []
result = []

def inline_query(update, context):
    global linkslist, result
    query = update.inline_query.query

    if not query:
        return

    if "-" in query and "w" not in query:
        command, value = query.split("-")
        try:
            for i in open("links/mem_links.txt", "r", encoding="utf-8").readlines(0):
                if i not in linkslist:
                    linkslist.append(i)
            int(value)
            #print(linkslist[value])
            if command == "memp":
                try:
                    result = [InlineQueryResultPhoto(id=str(uuid4()), photo_url=linkslist[int(value)].replace("\n", ""), thumb_url=linkslist[int(value)].replace("\n", ""))]
                except IndexError:
                    result = [InlineQueryResultPhoto(id=str(uuid4()), photo_url="https://raw.githubusercontent.com/ypite-nk/Sticker/main/zero.webp",
                                                                        thumb_url="https://raw.githubusercontent.com/ypite-nk/Sticker/main/zero.webp")]
            update.inline_query.answer(result)
        except ValueError:
            return

    if "w" in query.lower() and " " in query:
        value1, value2 = query.lower().split(" ")
        if value2 == 'w':
            if value1 is None:
                return
            else:
                result = prefix_weather(None, None, value1)
                if result is not None:
                    list_val = []
                    value1 = TR.translate(value1, dest="ru").text
                    for i in value1:
                        list_val.append(i)
                    list_val[0] = list_val[0].upper()
                    print(list_val[0].upper())
                    value1 = ""
                    for i in list_val:
                        value1 += i
                    print(list_val)
                    result = [InlineQueryResultArticle(id=str(uuid4()), title=value1 + " погода",
                                                   input_message_content=InputTextMessageContent("Город: " + value1 + 
                                                                         "\nПогода: " + str(result[0]) +
                                                                         "\nТемпература: " + str(result[1])))]
                    update.inline_query.answer(result)
                else:
                    return