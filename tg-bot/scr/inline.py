# -*- coding: utf-8 -*-
from telegram import InlineQueryResultPhoto, InlineQueryResultArticle, InputTextMessageContent
from spec import check_acces

linkslist = []
result = []

@check_acces
def inline_query(update, context):
    if not update.inline_query.query: return

    global linkslist, result
    
    from uuid import uuid4
    
    if "-" in update.inline_query.query and "w" not in update.inline_query.query:
        
        command, value = update.inline_query.query.split("-")
        try:
            for i in open("links/mem_links.txt", "r", encoding="utf-8").readlines(0):
                if i not in linkslist: linkslist.append(i)
            int(value)
            
            if command == "memp":
                try: result = [InlineQueryResultPhoto(id=str(uuid4()), photo_url=linkslist[int(value)].replace("\n", ""), thumb_url=linkslist[int(value)].replace("\n", ""))]
                except IndexError: result = [InlineQueryResultPhoto(id=str(uuid4()), photo_url="https://raw.githubusercontent.com/ypite-nk/Sticker/main/zero.webp", thumb_url="https://raw.githubusercontent.com/ypite-nk/Sticker/main/zero.webp")]
            update.inline_query.answer(result)

        except ValueError: return

    if "w" in update.inline_query.query.lower() and " " in update.inline_query.query:

        value1, value2 = update.inline_query.query.lower().split(" ")
        
        from prefix import prefix_weather
        
        if value2 == 'w':

            if value1 is None: return
            else:

                result = prefix_weather(None, None, value1)

                if result is not None:
                    list_val = []

                    for i in value1: list_val.append(i)
                    list_val[0] = list_val[0].upper()

                    value1 = ""

                    for i in list_val: value1 += i
                    result = [InlineQueryResultArticle(id=str(uuid4()), title=value1 + " погода",
                                                       input_message_content=InputTextMessageContent("Город: " + value1 + 
                                                                         "\nТемпература: " + str(result[0]) +
                                                                         "\nНебо: " + str(result[1]) +
                                                                         "\nВетер: " + str(result[2]) + " м/с"))]
                    update.inline_query.answer(result)

                else: return