# -*- coding: utf-8 -*-
import telegram
import random
import used_class
import keyboardbot as kb

from telegram import InlineKeyboardMarkup
from openf import openf
from echo import echo

def start_handler(update, context):
    echo(update, context)
    context.bot.send_message(chat_id=update.message.chat_id, text=openf("descriptext", "start_description"),
                             reply_markup=InlineKeyboardMarkup(kb.start_key))

def info_handler(update, context):
    echo(update, context)
    update.message.reply_text(openf("info", "info_handler"), reply_markup=InlineKeyboardMarkup(kb.commands_out))

def help_handler(update, context):
    echo(update, context)
    context.bot.send_message(chat_id=update.message.chat_id, text="По всем вопросам вы можете обратиться к @ypite_nk",
                             reply_markup=InlineKeyboardMarkup(kb.commands_out))

def faq_handler(update, context):
    echo(update, context)
    update.message.reply_text(openf("info", "faq_handler"), reply_markup=InlineKeyboardMarkup(kb.FAQ))

def pack_handler(update, context):
    echo(update, context)
    update.message.reply_text(openf("info", "pack"), reply_markup=InlineKeyboardMarkup(kb.commands_out), parse_mode=telegram.ParseMode.HTML)

def link_handler(update, context):
    echo(update, context)
    update.message.reply_text(openf("links", "mylinks"),
                              reply_markup=InlineKeyboardMarkup(kb.link))

def learn_handler(update, context):
    echo(update, context)
    update.message.reply_text(openf("learn", "description"), reply_markup=InlineKeyboardMarkup(kb.learns))

def support_handler(update, context):
    echo(update, context)
    update.message.reply_text(openf("info", "support"), reply_markup=InlineKeyboardMarkup(kb.support))

def echo_handler(update, context):
    echo(update, context)
    with open("info/hi.txt", "r", encoding="utf-8") as file:
        file = file.readlines(0)
    hi = True
    if ";" in update.message.text:
        if update.message.text.split(";")[0].lower() == "рецензия":
            if len(update.message.text.split(";")) == 5:
                marksget = update.message.text.split(";")
                context.bot.send_message(chat_id=-1001955905639, text="Type: " + marksget[0] + "\n" + 
                                                                        "Link: " + marksget[1] + "\n" + 
                                                                        "Text: " + marksget[2] + "\n" + 
                                                                        "A: " + marksget[3] + "\n" + 
                                                                        "P: " + marksget[4] + "\n")
                update.message.reply_text(openf("info/ypiter/marks", "markssucces"), reply_markup=InlineKeyboardMarkup(kb.backdel))
            else:
                update.message.reply_text(openf("info/ypiter/marks", "markserror"), reply_markup=InlineKeyboardMarkup(kb.backdel))
    else:
        for i in file:
            if i.replace("\n", "").lower() in update.message.text.lower():
                update.message.reply_text(openf("info", "echohi"), reply_markup=InlineKeyboardMarkup(kb.backdel))
                hi = False
        if hi == True:
            update.message.reply_text(openf("info", "echo"), reply_markup=InlineKeyboardMarkup(kb.backdel))

    hi = True

def back_handler(update, context):
    echo(update, context)
    update.message.reply_text(openf("descriptext", "menu"), reply_markup=InlineKeyboardMarkup(kb.start_key))

def fun_handler(update, context):
    update.message.reply_text(openf("descriptext", "fun"),
                              reply_markup=InlineKeyboardMarkup(kb.key))

def game2_handler(update, context):
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

    update.callback_query.message.reply_photo(active_mem.data()[0],
            reply_markup=InlineKeyboardMarkup(kb.mem(LikeCount, DisLikeCount)))

    mem_m[4] = mem_m[3]
    mem_m[3] = mem_m[2]
    mem_m[2] = mem_m[1]
    mem_m[1] = mem_m[0]
    mem_m[0] = active_mem.data()[0]

def vid_handler(update, context):
    video = []
    video_mem = ['', '', '', '', '']
    with open("links/vid.txt", "r", encoding="utf-8") as file:
        file = file.readlines()
        for i in file:
            video.append(i)
    active_video = random.choice(video).replace("\n", "")
    while active_video in video_mem:
        active_video = random.choice(video).replace("\n", "")
    update.message.reply_video(open(active_video, 'rb'))
    video_mem[4] = video_mem[3]
    video_mem[3] = video_mem[2]
    video_mem[2] = video_mem[1]
    video_mem[1] = video_mem[0]
    video_mem[0] = active_video