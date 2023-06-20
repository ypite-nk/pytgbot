# -*- coding: utf-8 -*-

def case(update, context):
    match update.callback_query['data']:
            case "/back":
                update.callback_query.message.reply_text('Меню', reply_markup=InlineKeyboardMarkup(kb.start_key))

            case "/fun":
                fun_handler(update.callback_query, context)

            case "mem":
                game2_handler(update, context)

            case _:
                conflict = False

        if not conflict:
            change(update, context)
    
        match update.callback_query['data']:
            case "/backdel":
                new_message_id = update.callback_query.message.reply_text('Меню',
                                                                          reply_markup=InlineKeyboardMarkup(kb.start_key)).message_id
#   FAQ
            case "botinfo":
                new_message_id = update.callback_query.message.reply_text("".join(open("Bot.txt", "r", encoding="utf-8").readlines(0)),
                                                                          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Назад", callback_data="faq"), kb.menudel]])).message_id
            case "ypiinfo":
                new_message_id = update.callback_query.message.reply_text("".join(open("Ypiter.txt", "r", encoding="utf-8").readlines(0)),
                                                                          reply_markup=InlineKeyboardMarkup(kb.ypiterFAQ)).message_id
#   О YPITER
            case "all":
                 new_message_id = update.callback_query.message.reply_text("".join(open("YpiAll.txt", "r", encoding="utf-8").readlines(0)),
                                                         reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Назад", callback_data="ypiinfo"), kb.menudel]])).message_id
            case "14":
                 new_message_id = update.callback_query.message.reply_text("".join(open("Ypi14.txt", "r", encoding="utf-8").readlines(0)),
                                                         reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Назад", callback_data="ypiinfo"), kb.menudel]])).message_id
            case "15":
                 new_message_id = update.callback_query.message.reply_text("".join(open("Ypi15.txt", "r", encoding="utf-8").readlines(0)),
                                                         reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Назад", callback_data="ypiinfo"), kb.menudel]])).message_id
#   РЕЦЕНЗИИ
            case "marks":
                new_message_id = update.callback_query.message.reply_text("Выберите номер рецензии:",
                                                                          reply_markup=InlineKeyboardMarkup(kb.marks))
#   GAME:RAP
            case "rap":
                new_message_id = update.callback_query.message.reply_text(str(open("Game_Description1.txt", "r", encoding="utf-8").readlines(0)[0]),
                                                                          reply_markup=InlineKeyboardMarkup(kb.rap)).message_id
            case "50 Cent":
                new_message_id = update.callback_query.message.reply_sticker(sticker_links['fifticent'][0],
                                                                             reply_markup=InlineKeyboardMarkup(kb.rap)).message_id
            case "Lil Peep":
                new_message_id = update.callback_query.message.reply_sticker(sticker_links['lilpeep'][0],
                                                                             reply_markup=InlineKeyboardMarkup(kb.rap)).message_id
            case "Egor Creed":
                new_message_id = update.callback_query.message.reply_sticker(sticker_links['egorcreed'][0],
                                                                             reply_markup=InlineKeyboardMarkup(kb.rap)).message_id
            case "100 gecs":
                new_message_id = update.callback_query.message.reply_sticker(sticker_links['gecs'][0],
                                                                             reply_markup=InlineKeyboardMarkup(kb.rap)).message_id 
#   MENU
            case "faq":
                new_message_id = update.callback_query.message.reply_text("Какой тип информации вас интересует?",
                                                                          reply_markup=InlineKeyboardMarkup(kb.FAQ)).message_id
            case "info":
                new_message_id = update.callback_query.message.reply_text("".join(open("Info.txt", "r", encoding="utf-8").readlines(0)),
                                                                          reply_markup=InlineKeyboardMarkup(kb.backdel)).message_id
            case "commands":
                new_message_id = update.callback_query.message.reply_text("".join(open("links/Commands.txt", "r", encoding="utf-8").readlines(0)),
                                                                          reply_markup=InlineKeyboardMarkup(kb.backdel)).message_id
            case "helper":
                new_message_id = update.callback_query.message.reply_text("Если у вас есть вопросы, которые не решились в /FAQ, то напишите @ypite_nk",
                                                                          reply_markup=InlineKeyboardMarkup(kb.backdel)).message_id
#   LEARN
            case "learn":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/description.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.learns)).message_id

            case "learning":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/learning.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.learn)).message_id
#       GENRES
            case "books":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/booklist.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.booklist1)).message_id

            case "booklist2":
                new_message_id = update.callback_query.message.reply_text("Выберите жанр", reply_markup=InlineKeyboardMarkup(kb.booklist2)).message_id

            case "booklist3":
                new_message_id = update.callback_query.message.reply_text("Выберите жанр", reply_markup=InlineKeyboardMarkup(kb.booklist3)).message_id

            case "backbook1":
                new_message_id = update.callback_query.message.reply_text("Выберите жанр", reply_markup=InlineKeyboardMarkup(kb.booklist1)).message_id

            case "backbook2":
                new_message_id = update.callback_query.message.reply_text("Выберите жанр", reply_markup=InlineKeyboardMarkup(kb.booklist2)).message_id

            case "classic":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/classic.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "foreign":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/foreign.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "rus":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/rus.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "detective":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/detective.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "fantasy":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/fantasy.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "fantastik":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/fantastik.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "prose":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/prose.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "scary":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/scary.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "adv":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/adv.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "action":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/action.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "stories":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/stories.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "poem":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/poem.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "scince":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/scince.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "psycho":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/psycho.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "comics":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/comics.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "manga":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/manga.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "esotericism":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/esotericism.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "culture":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/culture.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "romans":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/romans.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "books":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/books.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "bookfaq":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/bookfaq.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "religion":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/religion.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "funny":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/funny.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "tale":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/tale.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "kids":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/kids.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "buisness":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/buisness.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "home":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/home.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id
#   IT-LEARN
            case "it":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/it.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(kb.it)).message_id
#       CODING
            case "coding":
                new_message_id = update.callback_query.message.reply_text("Выберите язык программирования...", reply_markup=InlineKeyboardMarkup(kb.coding)).message_id

            case "py":
                new_message_id = update.callback_query.message.reply_text("Программа обучения Python\n\nПользуясь этими материалами вам будет более понятно и просто учить ЯП - Python",
                                                                          reply_markup=InlineKeyboardMarkup(kb.python)).message_id

            case "+":
                new_message_id = update.callback_query.message.reply_text("Программа обучения C++\n\nПользуясь этими материалами вам будет более понятно и просто учить ЯП - C++",
                                                                          reply_markup=InlineKeyboardMarkup(kb.cpp)).message_id

            case "js":
                new_message_id = update.callback_query.message.reply_text("Программа обучения JavaScript\n\nПользуясь этими материалами вам будет более понятно и просто учить ЯП - JavaScript",
                                                                          reply_markup=InlineKeyboardMarkup(kb.js)).message_id
#       ADMIN
            case "admin":
                new_message_id = update.callback_query.message.reply_text("Выберите деятельность...", reply_markup=InlineKeyboardMarkup(kb.admin)).message_id
#       WEB
            case "web":
                new_message_id = update.callback_query.message.reply_text("Выберите способ разработки...", reply_markup=InlineKeyboardMarkup(kb.web)).message_id

            case "html_m":
                new_message_id = update.callback_query.message.reply_text("Программа обучения HTML и CSS", reply_markup=InlineKeyboardMarkup(kb.html_m)).message_id

            case "php":
                new_message_id = update.callback_query.message.reply_text("Программа обучения PHP", reply_markup=InlineKeyboardMarkup(kb.php)).message_id

            case "django":
                new_message_id = update.callback_query.message.reply_text("Программа обучения Django", reply_markup=InlineKeyboardMarkup(kb.django)).message_id

#       S_ADMIN
            case "s_admin":
                new_message_id = update.callback_query.message.reply_text("Обучение Сис. администрированию\n\nПользуясь этими материалами вам будет более понятно и просто учить СА", reply_markup=InlineKeyboardMarkup(kb.s_admin)).message_id
#       DATA_SCIENS
            case "data_sciens":
                new_message_id = update.callback_query.message.reply_text("Обучение Data Sciens\n\nПользуясь этими материалами вам будет более понятно и просто учить DS", reply_markup=InlineKeyboardMarkup(kb.data_sciens)).message_id

            case "sql":
                new_message_id = update.callback_query.message.reply_text("Обучение работе с SQL", reply_markup=InlineKeyboardMarkup(kb.sql)).message_id
#   3D-LEARN
            case "3d":
                new_message_id = update.callback_query.message.reply_text("Обучение 3D моделированию", reply_markup=InlineKeyboardMarkup(kb.modeling)).message_id