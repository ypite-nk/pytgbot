# -*- coding: utf-8 -*-
from telegram import InlineQueryResultArticle, InputTextMessageContent
from spec import check_acces

@check_acces
def inline_query(update, context):
    if not update.inline_query.query: return
    
    from uuid import uuid4

    if "profile" in update.inline_query.query.lower() or "профиль" in update.inline_query.query.lower():
        from prefix import inline_profile

        uid = update.inline_query.from_user.id

        profile = inline_profile(update, context)
        if not profile: return

        result = [InlineQueryResultArticle(id=str(uuid4()),
                                           title=f"Профиль пользователя:{uid}",
                                           input_message_content=InputTextMessageContent(profile)
                                           )
                  ]

        update.inline_query.answer(result)

    elif "city" in update.inline_query.query.lower() or "город" in update.inline_query.query.lower():
        from prefix import inline_city

        uid = update.inline_query.from_user.id

        city = inline_city(update, context)
        if not city: return

        result = [InlineQueryResultArticle(id=str(uuid4()),
                                           title=f"Город пользователя:{uid}",
                                           input_message_content=InputTextMessageContent(city)
                                           )
                  ]

        update.inline_query.answer(result)
    
    elif "-" in update.inline_query.query and "w" not in update.inline_query.query:
        from telegram import InlineQueryResultPhoto

        linkslist = []
        command, value = update.inline_query.query.split("-")
        try:
            for i in open("links/mem_links.txt", "r", encoding="utf-8").readlines(0):
                if i not in linkslist: linkslist.append(i)
            int(value)
            
            if command == "memp":
                try: result = [InlineQueryResultPhoto(id=str(uuid4()),
                                                      photo_url=linkslist[int(value)].replace("\n", ""),
                                                      thumb_url=linkslist[int(value)].replace("\n", ""))
                               ]
                except IndexError: result = [InlineQueryResultPhoto(id=str(uuid4()),
                                                                    photo_url="https://raw.githubusercontent.com/ypite-nk/Sticker/main/zero.webp",
                                                                    thumb_url="https://raw.githubusercontent.com/ypite-nk/Sticker/main/zero.webp")
                                             ]
                update.inline_query.answer(result)

        except: return