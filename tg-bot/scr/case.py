# -*- coding: utf-8 -*-
import random
import used_class
import keyboardbot as kb

from spec import checkban, openf
from spec import Create, Status_changer
from prefix import mycity, myprofile
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode

mem_m = ['', '', '', '', '']
video_mem = ['', '', '', '', '']
joke_mem = ['', '', '', '', '']
thought_mem = ['', '', '', '', '']
old_message_id = 0
likestat = False
dislikestat = False

def fun_handler(update, context):
    if checkban(update, context): return
    update.callback_query.message.reply_text(openf("menu/more/fun", "fun"), reply_markup=InlineKeyboardMarkup(kb.key))

def photo_handler(update, context):
    if checkban(update, context): return
    
    global active_mem, LikeCount, DisLikeCount, mem_m, edit_message_id

    mem_n = []
    LikeCount, DisLikeCount = 0, 0
    active_mem = 0
    
    for i in range(len(open("menu/more/fun/photo/links.txt", "r", encoding="utf-8").readlines(0))): mem_n.append(used_class.Mem(i))
    active_mem = random.choice(mem_n)
    
    while active_mem.data()[0] in mem_m: active_mem = random.choice(mem_n)
    
    LikeCount = active_mem.data()[2]
    DisLikeCount = active_mem.data()[3]
    
    edit_message_id = update.callback_query.message.reply_photo(active_mem.data()[0], reply_markup=InlineKeyboardMarkup(kb.mem(LikeCount, DisLikeCount))).message_id
    
    mem_m[4] = mem_m[3]
    mem_m[3] = mem_m[2]
    mem_m[2] = mem_m[1]
    mem_m[1] = mem_m[0]
    mem_m[0] = active_mem.data()[0]

def vid_handler(update, context):
    if checkban(update, context): return
    
    global video_mem
    
    with open("menu/more/fun/vid/vid.txt", "r", encoding="utf-8") as file: file = file.readlines()

    active_video = random.choice(file).replace("\n", "")
    while active_video in video_mem: active_video = random.choice(file).replace("\n", "")

    update.callback_query.message.reply_video(open(active_video, 'rb'), reply_markup=InlineKeyboardMarkup(kb.vid))

    video_mem[4] = video_mem[3]
    video_mem[3] = video_mem[2]
    video_mem[2] = video_mem[1]
    video_mem[1] = video_mem[0]
    video_mem[0] = active_video

def joke_handler(update, context):
    if checkban(update, context): return
    
    global joke_mem
    
    with open("menu/more/fun/joke/joke.txt", "r", encoding="utf-8") as file: file = file.readlines()

    joke = random.choice(file).replace("\n", "")
    while joke in joke_mem: joke = random.choice(file).replace("\n", "")
    
    update.callback_query.message.reply_text(joke, reply_markup=InlineKeyboardMarkup(kb.jokes), parse_mode=ParseMode.MARKDOWN_V2)
    
    joke_mem[4] = joke_mem[3]
    joke_mem[3] = joke_mem[2]
    joke_mem[2] = joke_mem[1]
    joke_mem[1] = joke_mem[0]
    joke_mem[0] = joke

def thought_handler(update, context):
    if checkban(update, context): return

    global thought_mem

    with open("menu/more/fun/thought/thought.txt", "r", encoding="utf-8") as file: file = file.readlines()
    
    thought = random.choice(file).replace("\n", "")
    while thought in thought_mem: thought = random.choice(file).replace("\n", "")

    update.callback_query.message.reply_text(thought, reply_markup=InlineKeyboardMarkup(kb.thought), parse_mode=ParseMode.MARKDOWN_V2)

    thought_mem[4] = thought_mem[3]
    thought_mem[3] = thought_mem[2]
    thought_mem[2] = thought_mem[1]
    thought_mem[1] = thought_mem[0]
    thought_mem[0] = thought

def change(update, context):
    global message_id
    message_id = update.callback_query.message.message_id
    chat_id = update.callback_query.message.chat_id
    context.bot.delete_message(chat_id, message_id)

def echo_button(update, context):
    if checkban(update, context): return

    global marks_namelist
    global old_message_id, likestat, dislikestat

    reply_text = update.callback_query.message.reply_text
    reply_sticker = update.callback_query.message.reply_sticker

    sticker_links = {'fifticent' : open("menu/more/fun/rap/fifticent.txt").readlines(0), 'lilpeep' : open("menu/more/fun/rap/lilpeep.txt").readlines(0),
                    'gecs' : open("menu/more/fun/rap/100gecs.txt").readlines(0), 'egorcreed' : open("menu/more/fun/rap/egorcreed.txt").readlines(0),
                    'dog' : open("menu/more/fun/rap/dog.txt").readlines(0)
                    }
    conflict = True
    if "-" in update.callback_query['data']:
        action, value = update.callback_query.data.split("-")
        if action == "like":
            if str(edit_message_id) != str(old_message_id) and dislikestat is not True:
                active_mem.change_raiting(int(value) + 1, int(DisLikeCount))
                context.bot.edit_message_reply_markup(chat_id=update.callback_query.message.chat_id, message_id=edit_message_id,
                                                  reply_markup=InlineKeyboardMarkup(kb.mem(active_mem.data()[2], active_mem.data()[3]))
                                                  )
                old_message_id = edit_message_id
                likestat = True
            elif str(edit_message_id) == str(old_message_id) and dislikestat is not True:
                active_mem.change_raiting(int(value) - 1, int(DisLikeCount))
                context.bot.edit_message_reply_markup(chat_id=update.callback_query.message.chat_id, message_id=edit_message_id,
                                                  reply_markup=InlineKeyboardMarkup(kb.mem(active_mem.data()[2], active_mem.data()[3]))
                                                  )
                old_message_id = ""
                likestat = False
            
        elif action == "dislike":
            if str(edit_message_id) != str(old_message_id) and likestat is not True:
                active_mem.change_raiting(int(LikeCount), int(value) + 1)
                context.bot.edit_message_reply_markup(chat_id=update.callback_query.message.chat_id, message_id=edit_message_id,
                                                  reply_markup=InlineKeyboardMarkup(kb.mem(active_mem.data()[2], active_mem.data()[3]))
                                                  )
                old_message_id = edit_message_id
                dislikestat = True
            elif str(edit_message_id) == str(old_message_id) and likestat is not True:
                active_mem.change_raiting(int(LikeCount), int(value) - 1)
                context.bot.edit_message_reply_markup(chat_id=update.callback_query.message.chat_id, message_id=edit_message_id,
                                                  reply_markup=InlineKeyboardMarkup(kb.mem(active_mem.data()[2], active_mem.data()[3]))
                                                  )
                old_message_id = ""
                dislikestat = False

        if action == "А" or action == "П":
            reply_text(openf("menu/faq/ypiter/marks/marks", "MARKS-" + value + "-" + action),
                                                     reply_markup=InlineKeyboardMarkup(kb.set_mark(marks_namelist)))

    else:
        if "!changer" in update.callback_query['data']:
            callback = update.callback_query['data'].split("_")[1]
            changer = Status_changer(update, context)
            changer.change(callback)
            reply_text(changer.message, changer.keyboard)
            return

        match update.callback_query['data']:
            case "discard":
                Status_changer(update, context).clear_status()
                reply_text("Изменения отменены", reply_markup=InlineKeyboardMarkup(kb.profile_change))

            case "fun":
                fun_handler(update, context)
            case "photomem":
                photo_handler(update, context)
            case "videomem":
                vid_handler(update, context)
            case "jokes":
                joke_handler(update, context)
            case "thought":
                thought_handler(update, context)
            case _: conflict = False

        if not conflict: change(update, context)

        match update.callback_query['data']:
# BACK TO MENU
            case "/back":
                new_message_id = reply_text(openf('menu', 'menu'), 
                                            reply_markup=InlineKeyboardMarkup(kb.start_key)).message_id
#   FAQ
            case "botinfo":
                new_message_id = reply_text(openf("menu/faq", "bot"),
                                            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("<<<", callback_data="faq"), kb.backmenu]])).message_id
            case "ypiinfo":
                new_message_id = reply_text(openf("menu/faq/ypiter", "faq"),
                                            reply_markup=InlineKeyboardMarkup(kb.ypiterFAQ)).message_id
#   О YPITER
            case "all":
                 new_message_id = reply_text(openf("menu/faq/ypiter", "all"),
                                             reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("<<<", callback_data="ypiinfo"), kb.backmenu]]),
                                             parse_mode=ParseMode.HTML).message_id
            case "ypimore":
                new_message_id = reply_text(openf("menu/faq/ypiter", "more"),
                                            reply_markup=InlineKeyboardMarkup(kb.back))
#   РЕЦЕНЗИИ
            case "marks":
                new_message_id = reply_text("Этот раздел пока недоступен, вернитесь позже",
                                            reply_markup=InlineKeyboardMarkup(kb.back)).message_id
                return
                with open("menu/faq/ypiter/marks/markslist.txt", "r", encoding="utf-8") as file:
                    marks = file.readlines()
                    marks_namelist = []
                    for i in range(int(marks[0].split(";")[0])+1):
                        if "-" in marks[0].split(";")[i]: marks_namelist.append(marks[0].split(";")[i])
                
                new_message_id = reply_text(openf("menu/faq/ypiter/marks", "marks"),
                                            reply_markup=InlineKeyboardMarkup(kb.set_mark(marks_namelist))).message_id

            case "getmark":
                new_message_id = reply_text(openf("menu/faq/ypiter/marks", "marksget"),
                                            reply_markup=InlineKeyboardMarkup(kb.ypiterFAQ)).message_id
#   GAME:RAP
            case "rap":
                new_message_id = reply_text(openf('menu/more/fun/rap', "Game_Description1"),
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
            case "faq":
                new_message_id = reply_text(openf("menu/faq", "faq"),
                                            reply_markup=InlineKeyboardMarkup(kb.FAQ)).message_id
            case "info":
                new_message_id = reply_text(openf('menu', "info"),
                                            reply_markup=InlineKeyboardMarkup(kb.back)).message_id
            case "helper":
                new_message_id = reply_text(openf("menu", "callback"),
                                            reply_markup=InlineKeyboardMarkup(kb.back)).message_id
            case "projects":
                new_message_id = reply_text(openf("menu", "projects"),
                                            reply_markup=InlineKeyboardMarkup(kb.projects)).message_id
            case "mycity":
                new_message_id = mycity(update, context)
            case "cityBack":
                new_message_id = mycity(update, context)
            case "more":
                new_message_id = reply_text(openf("menu", "menu"),
                                            reply_markup=InlineKeyboardMarkup(kb.more)).message_id
            case "social":
                new_message_id = reply_text(openf("menu/more", "social"),
                                            reply_markup=InlineKeyboardMarkup(kb.link)).message_id
            case "packs":
                new_message_id = reply_text(openf("menu/more", "pack"),
                                            reply_markup=InlineKeyboardMarkup(kb.commands_out),
                                            parse_mode=ParseMode.HTML).message_id
            case "donate":
                new_message_id = reply_text(openf("menu/more", "donate"),
                                            reply_markup=InlineKeyboardMarkup(kb.support),
                                            parse_mode=ParseMode.HTML).message_id
#   LEARN
            case "learn":
                new_message_id = reply_text(openf("learn", "description"),
                                            reply_markup=InlineKeyboardMarkup(kb.learns)).message_id

            case "learning":
                new_message_id = reply_text(openf("learn", "learning"),
                                            reply_markup=InlineKeyboardMarkup(kb.learn)).message_id
#       GENRES
            case "books":
                new_message_id = reply_text(openf("learn", "booklist"),
                                            reply_markup=InlineKeyboardMarkup(kb.booklist1)).message_id

            case "booklist2":
                new_message_id = reply_text(openf("learn", "booklist"),
                                            reply_markup=InlineKeyboardMarkup(kb.booklist2)).message_id

            case "booklist3":
                new_message_id = reply_text(openf("learn", "booklist"),
                                            reply_markup=InlineKeyboardMarkup(kb.booklist3)).message_id

            case "backbook1":
                new_message_id = reply_text(openf("learn", "booklist"),
                                            reply_markup=InlineKeyboardMarkup(kb.booklist1)).message_id

            case "backbook2":
                new_message_id = reply_text(openf("learn", "booklist"),
                                            reply_markup=InlineKeyboardMarkup(kb.booklist2)).message_id

            case "classic":
                new_message_id = reply_text(openf("learn/genres", "classic"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "foreign":
                new_message_id = reply_text(openf("learn/genres", "foreign"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "rus":
                new_message_id = reply_text(openf("learn/genres", "rus"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "detective":
                new_message_id = reply_text(openf("learn/genres", "detective"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "fantasy":
                new_message_id = reply_text(openf("learn/genres", "fantasy"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "fantastik":
                new_message_id = reply_text(openf("learn/genres", "fantastik"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "prose":
                new_message_id = reply_text(openf("learn/genres", "prose"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "scary":
                new_message_id = reply_text(openf("learn/genres", "scary"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "adv":
                new_message_id = reply_text(openf("learn/genres", "adv"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "action":
                new_message_id = reply_text(openf("learn/genres", "action"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "stories":
                new_message_id = reply_text(openf("learn/genres", "stories"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "poem":
                new_message_id = reply_text(openf("learn/genres", "poem"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "scince":
                new_message_id = reply_text(openf("learn/genres", "scince"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "psycho":
                new_message_id = reply_text(openf("learn/genres", "psycho"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "comics":
                new_message_id = reply_text(openf("learn/genres", "comics"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "manga":
                new_message_id = reply_text(openf("learn/genres", "manga"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "esotericism":
                new_message_id = reply_text(openf("learn/genres", "esotericism"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "culture":
                new_message_id = reply_text(openf("learn/genres", "culture"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "romans":
                new_message_id = reply_text(openf("learn/genres", "romans"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "books":
                new_message_id = reply_text(openf("learn/genres", "books"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "bookfaq":
                new_message_id = reply_text(openf("learn/genres", "bookfaq"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "religion":
                new_message_id = reply_text(openf("learn/genres", "religion"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "funny":
                new_message_id = reply_text(openf("learn/genres", "funny"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "tale":
                new_message_id = reply_text(openf("learn/genres", "tale"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "kids":
                new_message_id = reply_text(openf("learn/genres", "kids"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "buisness":
                new_message_id = reply_text(openf("learn/genres", "buisness"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
            case "home":
                new_message_id = reply_text(openf("learn/genres", "home"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb),
                                            parse_mode=ParseMode.HTML).message_id
#   IT-LEARN
            case "it":
                new_message_id = reply_text(openf("learn", "it"),
                                            reply_markup=InlineKeyboardMarkup(kb.it)).message_id
#       CODING
            case "coding":
                new_message_id = reply_text(openf("learn/descriptext", "coding"),
                                            reply_markup=InlineKeyboardMarkup(kb.coding)).message_id

            case "py":
                new_message_id = reply_text(openf("learn/descriptext", "py"),
                                            reply_markup=InlineKeyboardMarkup(kb.python)).message_id

            case "+":
                new_message_id = reply_text(openf("learn/descriptext", "+"),
                                            reply_markup=InlineKeyboardMarkup(kb.cpp)).message_id

            case "js":
                new_message_id = reply_text(openf("learn/descriptext", "js"),
                                            reply_markup=InlineKeyboardMarkup(kb.js)).message_id
#       ADMIN
            case "admin":
                new_message_id = reply_text(openf("learn/descriptext", "admin"),
                                            reply_markup=InlineKeyboardMarkup(kb.admin)).message_id
#       WEB
            case "web":
                new_message_id = reply_text(openf("learn/descriptext", "web"),
                                            reply_markup=InlineKeyboardMarkup(kb.web)).message_id

            case "html_m":
                new_message_id = reply_text(openf("learn/descriptext", "html"),
                                            reply_markup=InlineKeyboardMarkup(kb.html_m)).message_id

            case "php":
                new_message_id = reply_text(openf("learn/descriptext", "php"),
                                            reply_markup=InlineKeyboardMarkup(kb.php)).message_id

            case "django":
                new_message_id = reply_text(openf("learn/descriptext", "django"),
                                            reply_markup=InlineKeyboardMarkup(kb.django)).message_id
#       S_ADMIN
            case "s_admin":
                new_message_id = reply_text(openf("learn/descriptext", "sys"),
                                            reply_markup=InlineKeyboardMarkup(kb.s_admin)).message_id
#       DATA_SCIENS
            case "data_sciens":
                new_message_id = reply_text(openf("learn/descriptext", "ds"),
                                            reply_markup=InlineKeyboardMarkup(kb.data_sciens)).message_id

            case "sql":
                new_message_id = reply_text(openf("learn/descriptext", "sql"),
                                            reply_markup=InlineKeyboardMarkup(kb.sql)).message_id
#   3D-LEARN
            case "3d":
                new_message_id = reply_text(openf("learn/descriptext", "3d"),
                                            reply_markup=InlineKeyboardMarkup(kb.modeling)).message_id
#   CITY_GAME
#       CREATE
            case "create":
                new_message_id = reply_text(openf("data/city/descrip", "create"),
                                            reply_markup=InlineKeyboardMarkup(kb.city_createtypes)).message_id
#       CREATE-HOUSE
            case "house":
                new_message_id = reply_text(openf("data/city/descrip", "create_house"),
                                            reply_markup=InlineKeyboardMarkup(kb.city_create_house)).message_id
            case "house1":
                new_message_id = reply_text(openf("data/city/descrip/create", "create")).message_id
                Create(update, context).house1()
            case "house2":
                new_message_id = reply_text(openf("data/city/descrip/create", "create")).message_id
                Create(update, context).house2()
            case "house3":
                new_message_id = reply_text(openf("data/city/descrip/create", "create")).message_id
                Create(update, context).house3()
#       CREATE-COMMERCICAL
            case "commercical":
                new_message_id = reply_text(openf("data/city/descrip", "create_commercical"),
                                            reply_markup=InlineKeyboardMarkup(kb.city_create_commercical)).message_id
            case "comm1":
                new_message_id = reply_text(openf("data/city/descrip/create", "create")).message_id
                Create(update, context).comm1()
            case "comm2":
                new_message_id = reply_text(openf("data/city/descrip/create", "create")).message_id
                Create(update, context).comm2()
            case "comm3":
                new_message_id = reply_text(openf("data/city/descrip/create", "create")).message_id
                Create(update, context).comm3()
#       CREATE-INDUSTRY
            case "industry":
                new_message_id = reply_text(openf("data/city/descrip", "create_industry"),
                                            reply_markup=InlineKeyboardMarkup(kb.city_create_industry)).message_id
            case "ind1":
                new_message_id = reply_text(openf("data/city/descrip/create", "create_ind_1"),
                                            reply_markup=InlineKeyboardMarkup(kb.city_create_ind1)).message_id
            case "1indenergy":
                new_message_id = reply_text(openf("data/city/descrip/create", "create")).message_id
                Create(update, context).ind1_1()
            case "2indenergy":
                new_message_id = reply_text(openf("data/city/descrip/create", "create")).message_id
                Create(update, context).ind1_2()
            case "3indenergy":
                new_message_id = reply_text(openf("data/city/descrip/create", "create")).message_id
                Create(update, context).ind1_3()
            case "ind2":
                new_message_id = reply_text(openf("data/city/descrip/create", "create_ind_2"),
                                            reply_markup=InlineKeyboardMarkup(kb.city_create_ind2)).message_id
            case "1indwater":
                new_message_id = reply_text(openf("data/city/descrip/create", "create")).message_id
                Create(update, context).ind2_1()
            case "2indwater":
                new_message_id = reply_text(openf("data/city/descrip/create", "create")).message_id
                Create(update, context).ind2_2()
            case "3indwater":
                new_message_id = reply_text(openf("data/city/descrip/create", "create")).message_id
                Create(update, context).ind2_3()
            case "ind3":
                new_message_id = reply_text(openf("data/city/descrip/create", "create_ind_3"),
                                            reply_markup=InlineKeyboardMarkup(kb.city_create_ind3)).message_id
            case "1indmat":
                new_message_id = reply_text(openf("data/city/descrip/create", "create")).message_id
                Create(update, context).ind3_1()
            case "2indmat":
                new_message_id = reply_text(openf("data/city/descrip/create", "create")).message_id
                Create(update, context).ind3_2()
            case "3indmat":
                new_message_id = reply_text(openf("data/city/descrip/create", "create")).message_id
                Create(update, context).ind3_3()
# PROFILE
            case "profile_change":
                new_message_id = reply_text(openf("menu/profile", "change"),
                                            reply_markup=InlineKeyboardMarkup(kb.profile_change)).message_id
            case "city_change":
                new_message_id = reply_text(openf("data/city/descrip", "change"),
                                            reply_markup=InlineKeyboardMarkup(kb.city_change)).message_id
# LEARNING LANGUAGE
            case "lang":
                new_message_id = reply_text(openf("learn", "language"),
                                            reply_markup=InlineKeyboardMarkup(kb.lang)).message_id
            case "learn_eng":
                new_message_id = reply_text(openf("learn/language/English"),
                                            reply_markup=InlineKeyboardMarkup(InlineKeyboardButton(text="Изучать", url="https://dzen.ru/ypite")),
                                            parse_mode=ParseMode.HTML).message_id
            case "learn_pol":
                new_message_id = reply_text(openf("learn/language/Polski"),
                                            reply_markup=InlineKeyboardMarkup(InlineKeyboardButton(text="Изучать", url="https://dzen.ru/ypite")),
                                            parse_mode=ParseMode.HTML).message_id
            case "learn_dts":
                new_message_id = reply_text(openf("learn/language/Deutsch"),
                                            reply_markup=InlineKeyboardMarkup(InlineKeyboardButton(text="Изучать", url="https://dzen.ru/a/ZMopgZwfFQI9ROVm")),
                                            parse_mode=ParseMode.HTML).message_id

        if not conflict: context.chat_data['message_id'] = new_message_id
    conflict = False

def echo_call(update, context):
    try: echo_button(update, context)
    except: update.callback_query.message.reply_text("Error", reply_markup=InlineKeyboardMarkup(kb.back))