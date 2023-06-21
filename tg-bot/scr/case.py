﻿# -*- coding: utf-8 -*-
import random
import used_class

import keyboardbot as kb

from echo import echo
from openf import openf
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

active_mem = 0
LikeCount = 0
DisLikeCount = 0

def fun_handler(update, context):
    update.message.reply_text(openf("descriptext", "fun"),
                              reply_markup=InlineKeyboardMarkup(kb.key))

def game2_handler(update, context, typesend):
    global active_mem, LikeCount, DisLikeCount
    mem_m = ['', '', '', '', '']
    mem_n = []
    LikeCount, DisLikeCount = 0, 0
    active_mem = 0
    for i in range(len(open("links/mem_links.txt", "r", encoding="utf-8").readlines(0))):
        mem_n.append(used_class.Mem(i))
    
    active_mem = random.choice(mem_n)
    
    while active_mem.data()[0] == mem_m[0] or active_mem.data()[0] == mem_m[1] or active_mem.data()[0] == mem_m[2] or active_mem.data()[0] == mem_m[3] or active_mem.data()[0] == mem_m[4]:
        active_mem = random.choice(mem_n)

    LikeCount = active_mem.data()[2]
    DisLikeCount = active_mem.data()[3]
    if typesend:
        update.callback_query.message.reply_photo(active_mem.data()[0],
            reply_markup=InlineKeyboardMarkup(kb.mem(LikeCount, DisLikeCount)))
    else:
        while active_mem.data()[0] == mem_m[0] or active_mem.data()[0] == mem_m[1] or active_mem.data()[0] == mem_m[2] or active_mem.data()[0] == mem_m[3] or active_mem.data()[0] == mem_m[4]:
            active_mem = random.choice(mem_n)
        return active_mem.data()[0]
    mem_m[4] = mem_m[3]
    mem_m[3] = mem_m[2]
    mem_m[2] = mem_m[1]
    mem_m[1] = mem_m[0]
    mem_m[0] = active_mem.data()[0]

def change(update, context):
    global message_id
    message_id = update.callback_query.message.message_id
    chat_id = update.callback_query.message.chat_id
    context.bot.delete_message(chat_id, message_id)

def echo_button(update, context):
    sticker_links = {'fifticent' : open("links/fifticent.txt").readlines(0), 'lilpeep' : open("links/lilpeep.txt").readlines(0),
                    'gecs' : open("links/100gecs.txt").readlines(0), 'egorcreed' : open("links/egorcreed.txt").readlines(0)
                    }
    conflict = True
    if "-" in update.callback_query['data']:
        action, value = update.callback_query.data.split("-")
        if action == "like":
            active_mem.change_raiting(int(value) + 1, int(DisLikeCount))
        elif action == "dislike":
            active_mem.change_raiting(int(LikeCount), int(value) + 1)

        if action == "A":
            update.callback_query.message.reply_text(openf("info/ypiter/marks", "MARKS-" + value + "-" + action),
                                                     reply_markup=InlineKeyboardMarkup(kb.marks))

        conflict = False
    else:
        match update.callback_query['data']:
            case "/back":
                update.callback_query.message.reply_text(openf('descriptext', 'Menu'), reply_markup=InlineKeyboardMarkup(kb.start_key))

            case "/fun":
                fun_handler(update.callback_query, context)

            case "mem":
                game2_handler(update, context, 1)

            case _:
                conflict = False

        if not conflict:
            change(update, context)
    
        match update.callback_query['data']:
            case "/backdel":
                new_message_id = update.callback_query.message.reply_text(openf('descriptext', 'Menu'),
                                                        reply_markup=InlineKeyboardMarkup(kb.start_key)).message_id
#   FAQ
            case "botinfo":
                new_message_id = update.callback_query.message.reply_text(openf("info", "Bot"),
                                                        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Назад", callback_data="faq"), kb.menudel]])).message_id
            case "ypiinfo":
                new_message_id = update.callback_query.message.reply_text(openf("info/ypiter", "Ypiter"),
                                                        reply_markup=InlineKeyboardMarkup(kb.ypiterFAQ)).message_id
#   О YPITER
            case "all":
                 new_message_id = update.callback_query.message.reply_text(openf("info/ypiter", "YpiAll"),
                                                        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Назад", callback_data="ypiinfo"), kb.menudel]])).message_id
            case "14":
                 new_message_id = update.callback_query.message.reply_text(openf("info/ypiter", "Ypi14"),
                                                        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Назад", callback_data="ypiinfo"), kb.menudel]])).message_id
            case "15":
                 new_message_id = update.callback_query.message.reply_text(openf("info/ypiter", "Ypi15"),
                                                        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Назад", callback_data="ypiinfo"), kb.menudel]])).message_id
#   РЕЦЕНЗИИ
            case "marks":
                new_message_id = update.callback_query.message.reply_text(openf("info/ypiter/marks", "marks"),
                                                                          reply_markup=InlineKeyboardMarkup(kb.marks))
#   GAME:RAP
            case "rap":
                new_message_id = update.callback_query.message.reply_text(openf('descriptext', "Game_Description1"),
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
                new_message_id = update.callback_query.message.reply_text(openf("descriptext", "faq"),
                                                                          reply_markup=InlineKeyboardMarkup(kb.FAQ)).message_id
            case "info":
                new_message_id = update.callback_query.message.reply_text(openf('', "version"),
                                                                          reply_markup=InlineKeyboardMarkup(kb.backdel)).message_id
            case "commands":
                new_message_id = update.callback_query.message.reply_text(openf('links', 'links'),
                                                                          reply_markup=InlineKeyboardMarkup(kb.backdel)).message_id
            case "helper":
                new_message_id = update.callback_query.message.reply_text(openf("descriptext", "helper"),
                                                                          reply_markup=InlineKeyboardMarkup(kb.backdel)).message_id
#   LEARN
            case "learn":
                new_message_id = update.callback_query.message.reply_text(openf("learn", "description"), reply_markup=InlineKeyboardMarkup(kb.learns)).message_id

            case "learning":
                new_message_id = update.callback_query.message.reply_text(openf("learn", "learning"), reply_markup=InlineKeyboardMarkup(kb.learn)).message_id
#       GENRES
            case "books":
                new_message_id = update.callback_query.message.reply_text(openf("learn", "booklist"), reply_markup=InlineKeyboardMarkup(kb.booklist1)).message_id

            case "booklist2":
                new_message_id = update.callback_query.message.reply_text(openf("learn", "booklist"), reply_markup=InlineKeyboardMarkup(kb.booklist2)).message_id

            case "booklist3":
                new_message_id = update.callback_query.message.reply_text(openf("learn", "booklist"), reply_markup=InlineKeyboardMarkup(kb.booklist3)).message_id

            case "backbook1":
                new_message_id = update.callback_query.message.reply_text(openf("learn", "booklist"), reply_markup=InlineKeyboardMarkup(kb.booklist1)).message_id

            case "backbook2":
                new_message_id = update.callback_query.message.reply_text(openf("learn", "booklist"), reply_markup=InlineKeyboardMarkup(kb.booklist2)).message_id

            case "classic":
                new_message_id = update.callback_query.message.reply_text(openf("learn/genres", "classic"), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "foreign":
                new_message_id = update.callback_query.message.reply_text(openf("learn/genres", "foreign"), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "rus":
                new_message_id = update.callback_query.message.reply_text(openf("learn/genres", "rus"), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "detective":
                new_message_id = update.callback_query.message.reply_text(openf("learn/genres", "detective"), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "fantasy":
                new_message_id = update.callback_query.message.reply_text(openf("learn/genres", "fantasy"), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "fantastik":
                new_message_id = update.callback_query.message.reply_text(openf("learn/genres", "fantastik"), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "prose":
                new_message_id = update.callback_query.message.reply_text(openf("learn/genres", "prose"), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "scary":
                new_message_id = update.callback_query.message.reply_text(openf("learn/genres", "scary"), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "adv":
                new_message_id = update.callback_query.message.reply_text(openf("learn/genres", "adv"), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "action":
                new_message_id = update.callback_query.message.reply_text(openf("learn/genres", "action"), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "stories":
                new_message_id = update.callback_query.message.reply_text(openf("learn/genres", "stories"), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "poem":
                new_message_id = update.callback_query.message.reply_text(openf("learn/genres", "poem"), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "scince":
                new_message_id = update.callback_query.message.reply_text(openf("learn/genres", "scince"), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "psycho":
                new_message_id = update.callback_query.message.reply_text(openf("learn/genres", "psycho"), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "comics":
                new_message_id = update.callback_query.message.reply_text(openf("learn/genres", "comics"), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "manga":
                new_message_id = update.callback_query.message.reply_text(openf("learn/genres", "manga"), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "esotericism":
                new_message_id = update.callback_query.message.reply_text(openf("learn/genres", "esotericism"), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "culture":
                new_message_id = update.callback_query.message.reply_text(openf("learn/genres", "culture"), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "romans":
                new_message_id = update.callback_query.message.reply_text(openf("learn/genres", "romans"), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "books":
                new_message_id = update.callback_query.message.reply_text(openf("learn/genres", "books"), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "bookfaq":
                new_message_id = update.callback_query.message.reply_text(openf("learn/genres", "bookfaq"), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "religion":
                new_message_id = update.callback_query.message.reply_text(openf("learn/genres", "religion"), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "funny":
                new_message_id = update.callback_query.message.reply_text(openf("learn/genres", "funny"), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "tale":
                new_message_id = update.callback_query.message.reply_text(openf("learn/genres", "tale"), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "kids":
                new_message_id = update.callback_query.message.reply_text(openf("learn/genres", "kids"), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "buisness":
                new_message_id = update.callback_query.message.reply_text(openf("learn/genres", "buisness"), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id

            case "home":
                new_message_id = update.callback_query.message.reply_text(openf("learn/genres", "home"), reply_markup=InlineKeyboardMarkup(kb.booklist)).message_id
#   IT-LEARN
            case "it":
                new_message_id = update.callback_query.message.reply_text(openf("learn", "it"), reply_markup=InlineKeyboardMarkup(kb.it)).message_id
#       CODING
            case "coding":
                new_message_id = update.callback_query.message.reply_text(openf("learn/descriptext", "coding"), reply_markup=InlineKeyboardMarkup(kb.coding)).message_id

            case "py":
                new_message_id = update.callback_query.message.reply_text(openf("learn/descriptext", "py"),
                                                                          reply_markup=InlineKeyboardMarkup(kb.python)).message_id

            case "+":
                new_message_id = update.callback_query.message.reply_text(openf("learn/descriptext", "+"),
                                                                          reply_markup=InlineKeyboardMarkup(kb.cpp)).message_id

            case "js":
                new_message_id = update.callback_query.message.reply_text(openf("learn/descriptext", "js"),
                                                                          reply_markup=InlineKeyboardMarkup(kb.js)).message_id
#       ADMIN
            case "admin":
                new_message_id = update.callback_query.message.reply_text(openf("learn/descriptext", "admin"), reply_markup=InlineKeyboardMarkup(kb.admin)).message_id
#       WEB
            case "web":
                new_message_id = update.callback_query.message.reply_text(openf("learn/descriptext", "web"), reply_markup=InlineKeyboardMarkup(kb.web)).message_id

            case "html_m":
                new_message_id = update.callback_query.message.reply_text(openf("learn/descriptext", "html"), reply_markup=InlineKeyboardMarkup(kb.html_m)).message_id

            case "php":
                new_message_id = update.callback_query.message.reply_text(openf("learn/descriptext", "php"), reply_markup=InlineKeyboardMarkup(kb.php)).message_id

            case "django":
                new_message_id = update.callback_query.message.reply_text(openf("learn/descriptext", "django"), reply_markup=InlineKeyboardMarkup(kb.django)).message_id

#       S_ADMIN
            case "s_admin":
                new_message_id = update.callback_query.message.reply_text(openf("learn/descriptext", "sys"), reply_markup=InlineKeyboardMarkup(kb.s_admin)).message_id
#       DATA_SCIENS
            case "data_sciens":
                new_message_id = update.callback_query.message.reply_text(openf("learn/descriptext", "ds"), reply_markup=InlineKeyboardMarkup(kb.data_sciens)).message_id

            case "sql":
                new_message_id = update.callback_query.message.reply_text(openf("learn/descriptext", "sql"), reply_markup=InlineKeyboardMarkup(kb.sql)).message_id
#   3D-LEARN
            case "3d":
                new_message_id = update.callback_query.message.reply_text(openf("learn/descriptext", "3d"), reply_markup=InlineKeyboardMarkup(kb.modeling)).message_id

        if not conflict:
            context.chat_data['message_id'] = new_message_id
    conflict = False
    echo(update, context) #ОТЛАДКА