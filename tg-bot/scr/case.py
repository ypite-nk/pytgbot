# -*- coding: utf-8 -*-
import random
import used_class

import keyboardbot as kb

from echo import echo
from spec import checkban, openf

from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode

mem_m = ['', '', '', '', '']
video_mem = ['', '', '', '', '']
joke_mem = ['', '', '', '', '']
thought_mem = ['', '', '', '', '']
old_message_id = 0
likestat = False
dislikestat = False

def fun_handler(update, context):
    if checkban(update, context):
        return 0
    update.message.reply_text(openf("descriptext", "fun"),
                              reply_markup=InlineKeyboardMarkup(kb.key))

def game2_handler(update, context):
    if checkban(update, context):
        return 0
    global active_mem, LikeCount, DisLikeCount, mem_m, edit_message_id
    mem_n = []
    LikeCount, DisLikeCount = 0, 0
    active_mem = 0
    for i in range(len(open("links/mem_links.txt", "r", encoding="utf-8").readlines(0))):
        mem_n.append(used_class.Mem(i))
    active_mem = random.choice(mem_n)
    while active_mem.data()[0] in mem_m:
        active_mem = random.choice(mem_n)
    LikeCount = active_mem.data()[2]
    DisLikeCount = active_mem.data()[3]
    print(active_mem.data()[0])
    edit_message_id = update.callback_query.message.reply_photo(active_mem.data()[0], reply_markup=InlineKeyboardMarkup(kb.mem(LikeCount, DisLikeCount))).message_id
    mem_m[4] = mem_m[3]
    mem_m[3] = mem_m[2]
    mem_m[2] = mem_m[1]
    mem_m[1] = mem_m[0]
    mem_m[0] = active_mem.data()[0]

def vid_handler(update, context):
    if checkban(update, context):
        return 0

    global video_mem
    with open("links/vid.txt", "r", encoding="utf-8") as file:
        file = file.readlines()
    active_video = random.choice(file).replace("\n", "")
    while active_video in video_mem:
        active_video = random.choice(file).replace("\n", "")
    update.callback_query.message.reply_video(open(active_video, 'rb'), reply_markup=InlineKeyboardMarkup(kb.vid))
    video_mem[4] = video_mem[3]
    video_mem[3] = video_mem[2]
    video_mem[2] = video_mem[1]
    video_mem[1] = video_mem[0]
    video_mem[0] = active_video

def joke_handler(update, context):
    if checkban(update, context):
        return 0

    global joke_mem
    with open("data/joke.txt", "r", encoding="utf-8") as file:
        file = file.readlines()
    joke = random.choice(file).replace("\n", "")
    while joke in joke_mem:
        joke = random.choice(file).replace("\n", "")
    print(joke)
    update.callback_query.message.reply_text(joke, reply_markup=InlineKeyboardMarkup(kb.jokes), parse_mode=ParseMode.MARKDOWN_V2)
    joke_mem[4] = joke_mem[3]
    joke_mem[3] = joke_mem[2]
    joke_mem[2] = joke_mem[1]
    joke_mem[1] = joke_mem[0]
    joke_mem[0] = joke

def thought_handler(update, context):
    if checkban(update, context):
        return 0

    global thought_mem
    with open("data/thought.txt", "r", encoding="utf-8") as file:
        file = file.readlines()
    thought = random.choice(file).replace("\n", "")
    while thought in thought_mem:
        thought = random.choice(file).replace("\n", "")
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
    echo(update, context) #ОТЛАДКА
    if checkban(update, context):
        return 0
    global marks_namelist
    global conflict
    global old_message_id, likestat, dislikestat

    reply_text = update.callback_query.message.reply_text
    reply_sticker = update.callback_query.message.reply_sticker

    sticker_links = {'fifticent' : open("links/fifticent.txt").readlines(0), 'lilpeep' : open("links/lilpeep.txt").readlines(0),
                    'gecs' : open("links/100gecs.txt").readlines(0), 'egorcreed' : open("links/egorcreed.txt").readlines(0),
                    'dog' : open("links/dog.txt").readlines(0)
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

        if action == "A" or action == "П":
            reply_text(openf("info/ypiter/marks", "MARKS-" + value + "-" + action),
                                                     reply_markup=InlineKeyboardMarkup(kb.set_mark(marks_namelist)))
        
    else:
        conflict = False
        match update.callback_query['data']:
            case "/back":
                reply_text(openf('descriptext', 'Menu'), reply_markup=InlineKeyboardMarkup(kb.start_key))

            case "/fun":
                fun_handler(update.callback_query, context)

            case "photomem":
                game2_handler(update, context)

            case "videomem":
                vid_handler(update, context)

            case "jokes":
                joke_handler(update, context)

            case "thought":
                thought_handler(update, context)

            case _:
                conflict = False

        if not conflict:
            change(update, context)
    
        match update.callback_query['data']:
            case "/backdel":
                new_message_id = reply_text(openf('descriptext', 'Menu'), 
                                            reply_markup=InlineKeyboardMarkup(kb.start_key)).message_id
#   FAQ
            case "botinfo":
                new_message_id = reply_text(openf("info", "Bot"),
                                            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Назад", callback_data="faq"), kb.menudel]])).message_id
            case "ypiinfo":
                new_message_id = reply_text(openf("info/ypiter", "Ypiter"),
                                            reply_markup=InlineKeyboardMarkup(kb.ypiterFAQ)).message_id
#   О YPITER
            case "all":
                 new_message_id = reply_text(openf("info/ypiter", "YpiAll"),
                                             reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Назад", callback_data="ypiinfo"), kb.menudel]]),
                                             parse_mode=ParseMode.HTML).message_id
            case "ypimore":
                new_message_id = reply_text(openf("info/ypiter", "YpiAllMore"),
                                            reply_markup=InlineKeyboardMarkup(kb.ypimore))
            case "14":
                 new_message_id = reply_text(openf("info/ypiter", "Ypi14"),
                                             reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Назад", callback_data="ypiinfo"), kb.menudel]])).message_id
            case "15":
                 new_message_id = reply_text(openf("info/ypiter", "Ypi15"),
                                             reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Назад", callback_data="ypiinfo"), kb.menudel]])).message_id
#   РЕЦЕНЗИИ
            case "marks":
                with open("info/ypiter/marks/markslist.txt", "r", encoding="utf-8") as file:
                    marks = file.readlines()
                    marks_namelist = []
                    for i in range(int(marks[0].split(";")[0])+1):
                        if "-" in marks[0].split(";")[i]:
                            marks_namelist.append(marks[0].split(";")[i])
                
                new_message_id = reply_text(openf("info/ypiter/marks", "marks"),
                                            reply_markup=InlineKeyboardMarkup(kb.set_mark(marks_namelist))).message_id

            case "getmark":
                new_message_id = reply_text(openf("info/ypiter/marks", "marksget"),
                                            reply_markup=InlineKeyboardMarkup(kb.ypiterFAQ)).message_id
#   GAME:RAP
            case "rap":
                new_message_id = reply_text(openf('descriptext', "Game_Description1"),
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
            case "faq":
                new_message_id = reply_text(openf("descriptext", "faq"),
                                            reply_markup=InlineKeyboardMarkup(kb.FAQ)).message_id
            case "info":
                new_message_id = reply_text(openf('', "version"),
                                            reply_markup=InlineKeyboardMarkup(kb.backdel)).message_id
            case "commands":
                new_message_id = reply_text(openf('links', 'links'),
                                            reply_markup=InlineKeyboardMarkup(kb.backdel)).message_id
            case "helper":
                new_message_id = reply_text(openf("descriptext", "helper"),
                                            reply_markup=InlineKeyboardMarkup(kb.backdel)).message_id
            case "projects":
                new_message_id = reply_text(openf("info", "projects"),
                                            reply_markup=InlineKeyboardMarkup(kb.projects)).message_id
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
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb["classic"]),
                                            parse_mode=ParseMode.HTML).message_id

            case "foreign":
                new_message_id = reply_text(openf("learn/genres", "foreign"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb["foreign"]),
                                            parse_mode=ParseMode.HTML).message_id

            case "rus":
                new_message_id = reply_text(openf("learn/genres", "rus"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb["rus"]),
                                            parse_mode=ParseMode.HTML).message_id

            case "detective":
                new_message_id = reply_text(openf("learn/genres", "detective"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb["detective"]),
                                            parse_mode=ParseMode.HTML).message_id

            case "fantasy":
                new_message_id = reply_text(openf("learn/genres", "fantasy"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb["fantasy"]),
                                            parse_mode=ParseMode.HTML).message_id

            case "fantastik":
                new_message_id = reply_text(openf("learn/genres", "fantastik"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb["fantastik"]),
                                            parse_mode=ParseMode.HTML).message_id

            case "prose":
                new_message_id = reply_text(openf("learn/genres", "prose"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb["prose"]),
                                            parse_mode=ParseMode.HTML).message_id

            case "scary":
                new_message_id = reply_text(openf("learn/genres", "scary"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb["scary"]),
                                            parse_mode=ParseMode.HTML).message_id

            case "adv":
                new_message_id = reply_text(openf("learn/genres", "adv"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb["adv"]),
                                            parse_mode=ParseMode.HTML).message_id

            case "action":
                new_message_id = reply_text(openf("learn/genres", "action"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb["action"]),
                                            parse_mode=ParseMode.HTML).message_id

            case "stories":
                new_message_id = reply_text(openf("learn/genres", "stories"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb["stories"]),
                                            parse_mode=ParseMode.HTML).message_id

            case "poem":
                new_message_id = reply_text(openf("learn/genres", "poem"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb["poem"]),
                                            parse_mode=ParseMode.HTML).message_id

            case "scince":
                new_message_id = reply_text(openf("learn/genres", "scince"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb["scince"]),
                                            parse_mode=ParseMode.HTML).message_id

            case "psycho":
                new_message_id = reply_text(openf("learn/genres", "psycho"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb["psycho"]),
                                            parse_mode=ParseMode.HTML).message_id

            case "comics":
                new_message_id = reply_text(openf("learn/genres", "comics"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb["comics"]),
                                            parse_mode=ParseMode.HTML).message_id

            case "manga":
                new_message_id = reply_text(openf("learn/genres", "manga"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb["manga"]),
                                            parse_mode=ParseMode.HTML).message_id

            case "esotericism":
                new_message_id = reply_text(openf("learn/genres", "esotericism"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb["esotericism"]),
                                            parse_mode=ParseMode.HTML).message_id

            case "culture":
                new_message_id = reply_text(openf("learn/genres", "culture"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb["culture"]),
                                            parse_mode=ParseMode.HTML).message_id

            case "romans":
                new_message_id = reply_text(openf("learn/genres", "romans"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb["romans"]),
                                            parse_mode=ParseMode.HTML).message_id

            case "books":
                new_message_id = reply_text(openf("learn/genres", "books"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb["books"]),
                                            parse_mode=ParseMode.HTML).message_id

            case "bookfaq":
                new_message_id = reply_text(openf("learn/genres", "bookfaq"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb["bookfaq"]),
                                            parse_mode=ParseMode.HTML).message_id

            case "religion":
                new_message_id = reply_text(openf("learn/genres", "religion"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb["religion"]),
                                            parse_mode=ParseMode.HTML).message_id

            case "funny":
                new_message_id = reply_text(openf("learn/genres", "funny"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb["funny"]),
                                            parse_mode=ParseMode.HTML).message_id

            case "tale":
                new_message_id = reply_text(openf("learn/genres", "tale"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb["tale"]),
                                            parse_mode=ParseMode.HTML).message_id

            case "kids":
                new_message_id = reply_text(openf("learn/genres", "kids"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb["kids"]),
                                            parse_mode=ParseMode.HTML).message_id

            case "buisness":
                new_message_id = reply_text(openf("learn/genres", "buisness"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb["buisness"]),
                                            parse_mode=ParseMode.HTML).message_id

            case "home":
                new_message_id = reply_text(openf("learn/genres", "home"),
                                            reply_markup=InlineKeyboardMarkup(kb.genreskb["home"]),
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

        if not conflict:
            context.chat_data['message_id'] = new_message_id
    conflict = False

def echo_call(update, context):
    try:
        echo_button(update, context)
    except:
        update.callback_query.message.reply_text("Error", reply_markup=InlineKeyboardMarkup(kb.backdel))