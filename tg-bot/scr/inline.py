# -*- coding: utf-8 -*-
from telegram import InlineQueryResultPhoto
from uuid import uuid4

linkslist = []
result = []

def inline_query(update, context):
    global linkslist, result
    query = update.inline_query.query

    if not query:
        return

    for i in open("links/mem_links.txt", "r", encoding="utf-8").readlines(0):
        if i not in linkslist:
            linkslist.append(i)
    if "-" in query:
        command, value = query.split("-")
        try:
            int(value)
            print(linkslist[value])
            if command == "memp":
                try:
                    result = [InlineQueryResultPhoto(id=str(uuid4()), photo_url=linkslist[int(value)].replace("\n", ""), thumb_url=linkslist[int(value)].replace("\n", ""))]
                except IndexError:
                    result = [InlineQueryResultPhoto(id=str(uuid4()), photo_url="https://raw.githubusercontent.com/ypite-nk/Sticker/main/zero.webp",
                                                                        thumb_url="https://raw.githubusercontent.com/ypite-nk/Sticker/main/zero.webp")]
            update.inline_query.answer(result)
        except ValueError:
            return