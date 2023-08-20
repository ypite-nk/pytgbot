# -*- coding: utf-8 -*-
import keyboardbot as kb
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode

mem_m = ['', '', '', '', '']
old_message_id = 0

likestat, dislikestat = False, False

def fun_handler(update, context): update.callback_query.message.reply_text(openfile("menu/more/fun", "fun"),
                                                                           reply_markup=InlineKeyboardMarkup(kb.key))

def photo_handler(update, context):
    global mem_m, active_mem, LikeCount, DisLikeCount
    global edit_message_id
    
    import random
    from used_class import MemPhoto
    
    mem_n = []
    LikeCount, DisLikeCount = 0, 0
    active_mem = 0
    
    for i in range(len(
                   open("menu/more/fun/photo/links.txt", "r", encoding="utf-8").readlines(0))):
        mem_n.append(MemPhoto(i))

    active_mem = random.choice(mem_n)
    while active_mem.data()[0] in mem_m: active_mem = random.choice(mem_n)
    
    LikeCount = active_mem.data()[2]
    DisLikeCount = active_mem.data()[3]
    
    edit_message_id = update.callback_query.message.reply_photo(active_mem.data()[0],
                                                                reply_markup=InlineKeyboardMarkup(kb.mem(LikeCount,
                                                                                                         DisLikeCount)
                                                                                                  )).message_id
    
    mem_m[4], mem_m[3], mem_m[2], mem_m[1] = mem_m[3], mem_m[2], mem_m[1], mem_m[0]
    mem_m[0] = active_mem.data()[0]

def change(update, context):
    global message_id
    message_id = update.callback_query.message.message_id
    chat_id = update.callback_query.message.chat_id
    try:
        context.bot.delete_message(chat_id, message_id)
        return True
    except: return None

from spec import check_acces, openfile, global_raiting, buy
from spec import bank_test, bank_test_back
from spec import Create, Status_changer
from prefix import mycity, myprofile, mybank
from login import cost_rubles, cost_youshk

def echo_button(update, context):
    global old_message_id, likestat, dislikestat

    reply_text = update.callback_query.message.reply_text
    reply_sticker = update.callback_query.message.reply_sticker

    sticker_links = {
        'fifticent' : open("menu/more/fun/rap/fifticent.txt").readlines(0),
        'lilpeep' : open("menu/more/fun/rap/lilpeep.txt").readlines(0),
        'gecs' : open("menu/more/fun/rap/100gecs.txt").readlines(0),
        'egorcreed' : open("menu/more/fun/rap/egorcreed.txt").readlines(0),
        'dog' : open("menu/more/fun/rap/dog.txt").readlines(0)
        }
    conflict = True
    if "-" in update.callback_query['data']:

        action, value = update.callback_query.data.split("-")
        
        if "m_" in action:
            prefix, action = action.split("_")

            if action == "like":
                if str(edit_message_id) != str(old_message_id) and dislikestat is not True:
                    active_mem.change_raiting(int(value) + 1, int(DisLikeCount))

                    old_message_id, likestat = edit_message_id, True

                elif str(edit_message_id) == str(old_message_id) and dislikestat is not True:
                    active_mem.change_raiting(int(value) - 1, int(DisLikeCount))
                
                    old_message_id, likestat = "", False
            
            elif action == "dislike":
                if str(edit_message_id) != str(old_message_id) and likestat is not True:
                    active_mem.change_raiting(int(LikeCount), int(value) + 1)

                    old_message_id, dislikestat = edit_message_id, True

                elif str(edit_message_id) == str(old_message_id) and likestat is not True:
                    active_mem.change_raiting(int(LikeCount), int(value) - 1)
                
                    old_message_id, dislikestat = "", False

        context.bot.edit_message_reply_markup(chat_id=update.callback_query.message.chat_id,
                                                  message_id=edit_message_id,
                                                  reply_markup=InlineKeyboardMarkup(
                                                      kb.mem(
                                                          active_mem.data()[2],
                                                          active_mem.data()[3]
                                                          )
                                                      )
                                                  )
            
    else:
        if "!changer" in update.callback_query['data']:
            callback = update.callback_query['data'].split("_")[1]

            changer = Status_changer(update, context)
            changer.change(callback)
            
            reply_text(changer.message,
                       reply_markup=changer.keyboard)
            
            return

        match update.callback_query['data']:
            case "discard":
                Status_changer(update, context).clear_status()
                reply_text("Изменения отменены", reply_markup=InlineKeyboardMarkup(kb.back))

            case "fun": fun_handler(update, context)
            case "photomem": photo_handler(update, context)

            case "discard_test":
                bank_test_back(update, context)
                reply_text("Тест отменен",
                           reply_markup=InlineKeyboardMarkup(kb.bankstart))

            case _: conflict = False

        if "#" in update.callback_query['data']:
            match update.callback_query['data']:
                case "1#1":
                    reply_text("Неверный ответ!",
                               reply_markup=InlineKeyboardMarkup(kb.back))
                    bank_test_back(update, context)
                case "1#2":
                    reply_text("Верный ответ!")
                    bank_test(update, context, 2)
                case "2#1":
                    reply_text("Неверный ответ!",
                               reply_markup=InlineKeyboardMarkup(kb.back))
                    bank_test_back(update, context)
                case "2#2":
                    reply_text("Неверный ответ!",
                               reply_markup=InlineKeyboardMarkup(kb.back))
                    bank_test_back(update, context)
                case "2#3":
                    reply_text("Неверный ответ!",
                               reply_markup=InlineKeyboardMarkup(kb.back))
                    bank_test_back(update, context)
                case "2#4":
                    reply_text("Верный ответ!")
                    bank_test(update, context, 3)
                case "3#1":
                    reply_text("Неверный ответ!",
                               reply_markup=InlineKeyboardMarkup(kb.back))
                    bank_test_back(update, context)
                case "3#2":
                    reply_text("Неверный ответ!",
                               reply_markup=InlineKeyboardMarkup(kb.back))
                    bank_test_back(update, context)
                case "3#3":
                    reply_text("Неверный ответ!",
                               reply_markup=InlineKeyboardMarkup(kb.back))
                    bank_test_back(update, context)
                case "3#4":
                    reply_text("Верный ответ!")
                    bank_test(update, context, 4)
            return
            
        if "shop=" in update.callback_query['data']:
            text = update.callback_query['data'].split("=")[1]
            
            reply_text(f"Выберите способ покупки {text}",
                       reply_markup=InlineKeyboardMarkup(kb.shops(text)))
            return
            
        if "buy=" in update.callback_query['data']:
            command, typ, text = update.callback_query['data'].split("=")
            
            if typ == "R": 
                costs = cost_rubles()
                reply_text(f"Чтобы купить {text}, оплатите стоимость товара по ссылке ниже, подписав сообщение текстом b/{text} и выбрав 'Бот' в качестве цели, и отправьте скриншот оплаты и текст b/{text} @r_ypite\n\nК сожалению, более удобные способы оплаты пока что не доступны",
                           reply_markup=InlineKeyboardMarkup(kb.buy_R(text, costs[text])))
                    
            elif typ == "Y":
                costs = cost_youshk()
                
                reply_text(f"Стоимость {text}: {costs[text]}",
                           reply_markup=InlineKeyboardMarkup(kb.buy_Y(text, costs[text])))
            return

        if "shopbuy:" in update.callback_query['data']:
            command, text, cost = update.callback_query['data'].split(":")
            shopbuy = buy(text, int(cost), str(update.callback_query.message.chat_id))
            
            if shopbuy:
                reply_text(f"Вы успешно приобрели {text}",
                           reply_markup=InlineKeyboardMarkup(kb.shop))
            elif shopbuy is None:
                reply_text(f"У вас не зарегестрирован банк!\nДля его регестрации пройдите в Меню -> Банк",
                           reply_markup=InlineKeyboardMarkup(kb.backmenu))
            else:
                reply_text(f"Вам нехватило Юшек для приобретения {text} или у вас уже есть этот товар!",
                           reply_markup=InlineKeyboardMarkup(kb.shop))
            return
            
        if not conflict:
            if change(update, context) is None:
                return

        match update.callback_query['data']:
# BACK TO MENU
            case "/back":
                new_message_id = reply_text(openfile('menu', 'menu'), 
                                            reply_markup=InlineKeyboardMarkup(kb.start_key)).message_id
#   FAQ
            case "botinfo":
                new_message_id = reply_text(openfile("menu/faq", "bot"),
                                            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("<<<", callback_data="faq"), kb.backmenu]])).message_id
#   О YPITER
            case "all":
                 new_message_id = reply_text(openfile("menu/faq/ypiter", "all"),
                                             reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("<<<", callback_data="ypiinfo"), kb.backmenu]]),
                                             parse_mode=ParseMode.HTML).message_id

#   GAME:RAP
            case "rap":
                new_message_id = reply_text(openfile('menu/more/fun/rap', "Game_Description1"),
                                            reply_markup=InlineKeyboardMarkup(kb.rap)).message_id
            case "50 Cent":
                new_message_id = reply_sticker(sticker_links['fifticent'][0],
                                               reply_markup=InlineKeyboardMarkup(kb.rap)).message_id
            case "Lil Peep":
                new_message_id = reply_sticker(sticker_links['lilpeep'][0],
                                               reply_markup=InlineKeyboardMarkup(kb.rap)).message_id
            case "Egor Creed":
                new_message_id = reply_sticker(sticker_links['egorcreed'][0],
                                               reply_markup=InlineKeyboardMarkup(kb.rap)).message_id
            case "100 gecs":
                new_message_id = reply_sticker(sticker_links['gecs'][0],
                                               reply_markup=InlineKeyboardMarkup(kb.rap)).message_id 
            case "dog":
                new_message_id = reply_sticker(sticker_links['dog'][0],
                                                reply_markup=InlineKeyboardMarkup(kb.rap)).message_id
#   MENU
            case "profile":
                new_message_id = myprofile(update, context)
            case "bank":
                new_message_id = bank_test(update, context)
            case "info":
                new_message_id = reply_text(openfile('menu', "info"),
                                            reply_markup=InlineKeyboardMarkup(kb.back)).message_id
            case "helper":
                new_message_id = reply_text(openfile("menu", "callback"),
                                            reply_markup=InlineKeyboardMarkup(kb.back)).message_id
            case "projects":
                new_message_id = reply_text(openfile("menu", "projects"),
                                            reply_markup=InlineKeyboardMarkup(kb.projects)).message_id
            case "mycity":
                new_message_id = mycity(update, context)
            case "cityBack":
                new_message_id = mycity(update, context)
            case "more":
                new_message_id = reply_text(openfile("menu", "menu"),
                                            reply_markup=InlineKeyboardMarkup(kb.more)).message_id
            case "social":
                new_message_id = reply_text(openfile("menu/more", "social"),
                                            reply_markup=InlineKeyboardMarkup(kb.link)).message_id
            case "packs":
                new_message_id = reply_text(openfile("menu/more", "pack"),
                                            reply_markup=InlineKeyboardMarkup(kb.commands_out),
                                            parse_mode=ParseMode.HTML).message_id
            case "donate":
                new_message_id = reply_text(openfile("menu/more", "donate"),
                                            reply_markup=InlineKeyboardMarkup(kb.support),
                                            parse_mode=ParseMode.HTML).message_id
            case "bots":
                new_message_id = reply_text(openfile("menu/more/bots", "bots"),
                                            reply_markup=InlineKeyboardMarkup(kb.bots),
                                            parse_mode=ParseMode.HTML).message_id
#   LEARN
            case "learn":
                new_message_id = reply_text("К сожалению, данный раздел пока не доступен",#openfile("learn", "description"),
                                            reply_markup=InlineKeyboardMarkup(kb.back)).message_id#kb.learns

            case "learning":
                new_message_id = reply_text("К сожалению, данный раздел пока не доступен",#openfile("learn", "learning")
                                            reply_markup=InlineKeyboardMarkup(kb.back)).message_id#kb.learn
#       GENRES
            case "books":
                new_message_id = reply_text(openfile("learn", "booklist"),
                                            reply_markup=InlineKeyboardMarkup(kb.booklist1)).message_id

            case "booklist2":
                new_message_id = reply_text(openfile("learn", "booklist"),
                                            reply_markup=InlineKeyboardMarkup(kb.booklist2)).message_id

            case "booklist3":
                new_message_id = reply_text(openfile("learn", "booklist"),
                                            reply_markup=InlineKeyboardMarkup(kb.booklist3)).message_id

            case "backbook1":
                new_message_id = reply_text(openfile("learn", "booklist"),
                                            reply_markup=InlineKeyboardMarkup(kb.booklist1)).message_id

            case "backbook2":
                new_message_id = reply_text(openfile("learn", "booklist"),
                                            reply_markup=InlineKeyboardMarkup(kb.booklist2)).message_id

            case "classic":
                new_message_id = reply_text(openfile("learn/genres", "classic"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "foreign":
                new_message_id = reply_text(openfile("learn/genres", "foreign"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "rus":
                new_message_id = reply_text(openfile("learn/genres", "rus"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "detective":
                new_message_id = reply_text(openfile("learn/genres", "detective"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "fantasy":
                new_message_id = reply_text(openfile("learn/genres", "fantasy"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "fantastik":
                new_message_id = reply_text(openfile("learn/genres", "fantastik"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "prose":
                new_message_id = reply_text(openfile("learn/genres", "prose"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "scary":
                new_message_id = reply_text(openfile("learn/genres", "scary"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "adv":
                new_message_id = reply_text(openfile("learn/genres", "adv"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "action":
                new_message_id = reply_text(openfile("learn/genres", "action"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "stories":
                new_message_id = reply_text(openfile("learn/genres", "stories"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "poem":
                new_message_id = reply_text(openfile("learn/genres", "poem"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "scince":
                new_message_id = reply_text(openfile("learn/genres", "scince"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "psycho":
                new_message_id = reply_text(openfile("learn/genres", "psycho"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "comics":
                new_message_id = reply_text(openfile("learn/genres", "comics"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "manga":
                new_message_id = reply_text(openfile("learn/genres", "manga"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "esotericism":
                new_message_id = reply_text(openfile("learn/genres", "esotericism"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "culture":
                new_message_id = reply_text(openfile("learn/genres", "culture"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "romans":
                new_message_id = reply_text(openfile("learn/genres", "romans"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "books":
                new_message_id = reply_text(openfile("learn/genres", "books"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "bookfaq":
                new_message_id = reply_text(openfile("learn/genres", "bookfaq"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "religion":
                new_message_id = reply_text(openfile("learn/genres", "religion"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "funny":
                new_message_id = reply_text(openfile("learn/genres", "funny"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "tale":
                new_message_id = reply_text(openfile("learn/genres", "tale"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "kids":
                new_message_id = reply_text(openfile("learn/genres", "kids"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "buisness":
                new_message_id = reply_text(openfile("learn/genres", "buisness"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "home":
                new_message_id = reply_text(openfile("learn/genres", "home"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
#   IT-LEARN
            case "it":
                new_message_id = reply_text(openfile("learn", "it"),
                                            reply_markup=InlineKeyboardMarkup(kb.it)).message_id
#       CODING
            case "coding":
                new_message_id = reply_text(openfile("learn/descriptext", "coding"),
                                            reply_markup=InlineKeyboardMarkup(kb.coding)).message_id

            case "py":
                new_message_id = reply_text(openfile("learn/descriptext", "py"),
                                            reply_markup=InlineKeyboardMarkup(kb.python)).message_id

            case "+":
                new_message_id = reply_text(openfile("learn/descriptext", "+"),
                                            reply_markup=InlineKeyboardMarkup(kb.cpp)).message_id

            case "js":
                new_message_id = reply_text(openfile("learn/descriptext", "js"),
                                            reply_markup=InlineKeyboardMarkup(kb.js)).message_id
#       ADMIN
            case "admin":
                new_message_id = reply_text(openfile("learn/descriptext", "admin"),
                                            reply_markup=InlineKeyboardMarkup(kb.admin)).message_id
#       WEB
            case "web":
                new_message_id = reply_text(openfile("learn/descriptext", "web"),
                                            reply_markup=InlineKeyboardMarkup(kb.web)).message_id

            case "html_m":
                new_message_id = reply_text(openfile("learn/descriptext", "html"),
                                            reply_markup=InlineKeyboardMarkup(kb.html_m)).message_id

            case "php":
                new_message_id = reply_text(openfile("learn/descriptext", "php"),
                                            reply_markup=InlineKeyboardMarkup(kb.php)).message_id

            case "django":
                new_message_id = reply_text(openfile("learn/descriptext", "django"),
                                            reply_markup=InlineKeyboardMarkup(kb.django)).message_id
#       S_ADMIN
            case "s_admin":
                new_message_id = reply_text(openfile("learn/descriptext", "sys"),
                                            reply_markup=InlineKeyboardMarkup(kb.s_admin)).message_id
#       DATA_SCIENS
            case "data_sciens":
                new_message_id = reply_text(openfile("learn/descriptext", "ds"),
                                            reply_markup=InlineKeyboardMarkup(kb.data_sciens)).message_id

            case "sql":
                new_message_id = reply_text(openfile("learn/descriptext", "sql"),
                                            reply_markup=InlineKeyboardMarkup(kb.sql)).message_id
#   3D-LEARN
            case "3d":
                new_message_id = reply_text(openfile("learn/descriptext", "3d"),
                                            reply_markup=InlineKeyboardMarkup(kb.modeling)).message_id
#   CITY_GAME
#       CREATE
            case "create":
                new_message_id = reply_text(openfile("data/city/descrip", "create"),
                                            reply_markup=InlineKeyboardMarkup(kb.city_createtypes)).message_id
#       CREATE-HOUSE
            case "house":
                new_message_id = reply_text(openfile("data/city/descrip", "create_house"),
                                            reply_markup=InlineKeyboardMarkup(kb.city_create_house)).message_id
            case "house1":
                new_message_id = reply_text(openfile("data/city/descrip/create", "create")).message_id
                Create(update, context).house1()
            case "house2":
                new_message_id = reply_text(openfile("data/city/descrip/create", "create")).message_id
                Create(update, context).house2()
            case "house3":
                new_message_id = reply_text(openfile("data/city/descrip/create", "create")).message_id
                Create(update, context).house3()
#       CREATE-COMMERCICAL
            case "commercical":
                new_message_id = reply_text(openfile("data/city/descrip", "create_commercical"),
                                            reply_markup=InlineKeyboardMarkup(kb.city_create_commercical)).message_id
            case "comm1":
                new_message_id = reply_text(openfile("data/city/descrip/create", "create")).message_id
                Create(update, context).comm1()
            case "comm2":
                new_message_id = reply_text(openfile("data/city/descrip/create", "create")).message_id
                Create(update, context).comm2()
            case "comm3":
                new_message_id = reply_text(openfile("data/city/descrip/create", "create")).message_id
                Create(update, context).comm3()
#       CREATE-INDUSTRY
            case "industry":
                new_message_id = reply_text(openfile("data/city/descrip", "create_industry"),
                                            reply_markup=InlineKeyboardMarkup(kb.city_create_industry)).message_id
            case "ind1":
                new_message_id = reply_text(openfile("data/city/descrip/create", "create_ind_1"),
                                            reply_markup=InlineKeyboardMarkup(kb.city_create_ind1)).message_id
            case "1indenergy":
                new_message_id = reply_text(openfile("data/city/descrip/create", "create")).message_id
                Create(update, context).ind1_1()
            case "2indenergy":
                new_message_id = reply_text(openfile("data/city/descrip/create", "create")).message_id
                Create(update, context).ind1_2()
            case "3indenergy":
                new_message_id = reply_text(openfile("data/city/descrip/create", "create")).message_id
                Create(update, context).ind1_3()
            case "ind2":
                new_message_id = reply_text(openfile("data/city/descrip/create", "create_ind_2"),
                                            reply_markup=InlineKeyboardMarkup(kb.city_create_ind2)).message_id
            case "1indwater":
                new_message_id = reply_text(openfile("data/city/descrip/create", "create")).message_id
                Create(update, context).ind2_1()
            case "2indwater":
                new_message_id = reply_text(openfile("data/city/descrip/create", "create")).message_id
                Create(update, context).ind2_2()
            case "3indwater":
                new_message_id = reply_text(openfile("data/city/descrip/create", "create")).message_id
                Create(update, context).ind2_3()
            case "ind3":
                new_message_id = reply_text(openfile("data/city/descrip/create", "create_ind_3"),
                                            reply_markup=InlineKeyboardMarkup(kb.city_create_ind3)).message_id
            case "1indmat":
                new_message_id = reply_text(openfile("data/city/descrip/create", "create")).message_id
                Create(update, context).ind3_1()
            case "2indmat":
                new_message_id = reply_text(openfile("data/city/descrip/create", "create")).message_id
                Create(update, context).ind3_2()
            case "3indmat":
                new_message_id = reply_text(openfile("data/city/descrip/create", "create")).message_id
                Create(update, context).ind3_3()
# PROFILE
            case "profile_change":
                new_message_id = reply_text(openfile("menu/profile", "change"),
                                            reply_markup=InlineKeyboardMarkup(kb.profile_change)).message_id
            case "city_change":
                new_message_id = reply_text(openfile("data/city/descrip", "change"),
                                            reply_markup=InlineKeyboardMarkup(kb.city_change)).message_id
# LEARNING LANGUAGE
            case "lang":
                new_message_id = reply_text(openfile("learn", "language"),
                                            reply_markup=InlineKeyboardMarkup(kb.lang)).message_id
            case "learn_eng":
                new_message_id = reply_text(openfile("learn/language", "english"),
                                            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Изучать", url="https://dzen.ru/ypiter")], [kb.backmenu2]]),
                                            parse_mode=ParseMode.HTML).message_id
            case "learn_pol":
                new_message_id = reply_text(openfile("learn/language", "polski"),
                                            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Изучать", url="https://dzen.ru/ypiter")], [kb.backmenu2]]),
                                            parse_mode=ParseMode.HTML).message_id
            case "learn_dts":
                new_message_id = reply_text(openfile("learn/language", "deutsch"),
                                            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Изучать", url="https://dzen.ru/ypiter")], [kb.backmenu2]]),
                                            parse_mode=ParseMode.HTML).message_id
            case "raiting":
                new_message_id = global_raiting(update, context)

            case "quests":
                new_message_id = reply_text(openfile("menu/more/fun/quests", "quests"),
                                            reply_markup=InlineKeyboardMarkup(kb.quests),
                                            parse_mode=ParseMode.HTML).message_id
            case "buyvip":
                new_message_id = reply_text(openfile("menu/profile", "buyvip"),
                                            reply_markup=InlineKeyboardMarkup(kb.profile_back),
                                            parse_mode=ParseMode.HTML).message_id
            case "shop":
                new_message_id = reply_text(openfile("menu/shop", "shop"),
                                            reply_markup=InlineKeyboardMarkup(kb.shop),
                                            parse_mode=ParseMode.HTML).message_id
            case "mybank":
                new_message_id = mybank(update, context)
            case "projlist":
                new_message_id = reply_text("None",
                                            reply_markup=InlineKeyboardMarkup(kb.back)).message_id
            case "profmore":
                new_message_id = reply_text("None",
                                            reply_markup=InlineKeyboardMarkup(kb.back)).message_id
            case "quest1":
                new_message_id = reply_text("None",
                                            reply_markup=InlineKeyboardMarkup(kb.back)).message_id
            case "quest2":
                new_message_id = reply_text("None",
                                            reply_markup=InlineKeyboardMarkup(kb.back)).message_id
            case "start_test_19":
                new_message_id = bank_test(update, context, 1)

        if not conflict: context.chat_data['message_id'] = new_message_id
    conflict = False

@check_acces
def echo_call(update, context):
    echo_button(update, context)
    #update.callback_query.message.reply_text("Error",
     #                                                reply_markup=InlineKeyboardMarkup(kb.back))