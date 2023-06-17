# -*- coding: utf-8 -*-
from token import COMMA
import telegram
import random
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater, CallbackQueryHandler, CallbackContext
from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, Update, ParseMode
import used_class

token = "5873796392:AAEE1i9cwQ5Y2T6Mk-TJkTHruANhCmPr_uU"
bot = telegram.Bot(token=token)
updater = Updater(token=token, use_context=True)

menudel = InlineKeyboardButton("Меню", callback_data="/backdel")
backdel = [[menudel]]

marks_openLIST = ["MARKS-", "A", "N"]

conflict = False

mem_m = ['', '', '', '', '']
LikeCount = 0
DisLikeCount = 0

ypiterFAQ = [[InlineKeyboardButton("Общее", callback_data='all'), InlineKeyboardButton("Рецензии", callback_data='marks')],
             [InlineKeyboardButton("14 лет", callback_data='14'), InlineKeyboardButton("15 лет", callback_data='15')],
             [InlineKeyboardButton("Назад", callback_data="faq"), menudel]]

FAQ = [[InlineKeyboardButton("О боте", callback_data="botinfo"), InlineKeyboardButton("О ypiter", callback_data="ypiinfo")],
       [InlineKeyboardButton("Команды", callback_data="commands"), menudel]]

rap = [[InlineKeyboardButton("50 Cent", callback_data="50 Cent"), InlineKeyboardButton("Lil Peep", callback_data="Lil Peep"),
        InlineKeyboardButton("Egor Creed", callback_data="Egor Creed"), InlineKeyboardButton("100 gecs", callback_data="100 gecs")],
       [InlineKeyboardButton("Назад", callback_data="/fun"), menudel]]

start_key = [[InlineKeyboardButton("FAQ", callback_data="faq"), InlineKeyboardButton("Инфо", callback_data="info"), InlineKeyboardButton("Команды", callback_data="commands")],
             [InlineKeyboardButton("Обратная связь", callback_data="helper")]]

marks = [[InlineKeyboardButton("1::A", callback_data="A-1"), InlineKeyboardButton("2::A", callback_data="A-2"), InlineKeyboardButton("3::A", callback_data="A-3")],
         [InlineKeyboardButton("Назад", callback_data="ypiinfo"), menudel]]

commands_out = [[InlineKeyboardButton("Команды", callback_data="commands"), menudel]]

def echo(update, context): # ОТЛАДКА
    print(update.callback_query['data'] + " from " + update.callback_query.message.chat['username'])
    print(context)

def start_handler(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="".join(open("start_description.txt", "r", encoding="utf-8").readlines(0)),
                             reply_markup=InlineKeyboardMarkup(start_key))

def info_handler(update, context):
    update.message.reply_text("".join(open("info_handler.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(commands_out))

def help_handler(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="По всем вопросам вы можете обратиться к @ypite_nk",
                             reply_markup=InlineKeyboardMarkup(commands_out))

def faq_handler(update, context):
    update.message.reply_text("Какой тип информации вас интересует?", reply_markup=InlineKeyboardMarkup(FAQ))

def fun_handler(update, context):
    key = [[InlineKeyboardButton("rap", callback_data="rap"), InlineKeyboardButton("mem", callback_data="mem"),
            InlineKeyboardButton("3", callback_data="3"), InlineKeyboardButton("4", callback_data="4")],
            [InlineKeyboardButton("Команды", callback_data="commands"), menudel]]
    update.message.reply_text("Смотри, есть 4 игры на выбор.\n/rap - стикер = репер\n/mem - рандомный мемас из базы\n",
                              reply_markup=InlineKeyboardMarkup(key))

def pack_handler(update, context):
    update.message.reply_text("".join(open("pack.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(commands_out), parse_mode=telegram.ParseMode.HTML)

def link_handler(update, context):
    button = [[InlineKeyboardButton(text="Вконтакте", url="https://vk.com/ypite"), InlineKeyboardButton(text="Группа Вк", url="https://vk.com/cloud_ypiter")],
              [InlineKeyboardButton(text="Youtube", url="https://www.youtube.com/channel/UCQunVaPHyI2MvS0rU56_MhA"), InlineKeyboardButton(text="TikTok", url="https://vm.tiktok.com/ZT81sSebh/")],
              [InlineKeyboardButton("Команды", callback_data="commands"), menudel]]
    update.message.reply_text("".join(open("Mylink.txt", "r", encoding="utf-8").readlines(0)),
                              reply_markup=InlineKeyboardMarkup(button))

def support_handler(update, context):
    support = [[InlineKeyboardButton(text="Поддержать", url="https://pay.freekassa.ru/?m=&oa=&o=&s=6813a8f3dde2603e317b5b405dd3c4c3&currency=RUB")],
               [InlineKeyboardButton("Команды", callback_data="commands"), menudel]]
    update.message.reply_text("".join(open("support.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(support))

def echo_handler(update, context):
    update.message.reply_text("Пожалуйста, воспользуйтесь интерфейсом или командами. Если у вас есть вопросы: /help")

def back_handler(update, context):
    options = ['FAQ', 'Инфо', 'Команды', 'Обратная связь']
    update.message.reply_text("Меню", reply_markup=InlineKeyboardMarkup(start_key))

def game2_handler(update, context):
    global mem_m
    global LikeCount, DisLikeCount
    global active_mem
    
    mem_n = []
    for i in range(len(open("mem_links.txt", "r", encoding="utf-8").readlines(0))):
        mem_n.append(used_class.Mem(i))
    
    active_mem = random.choice(mem_n)
    
    while active_mem.data()[0] == mem_m[0] or active_mem.data()[0] == mem_m[1] or active_mem.data()[0] == mem_m[2] or active_mem.data()[0] == mem_m[3] or active_mem.data()[0] == mem_m[4]:
        active_mem = random.choice(mem_n)

    LikeCount = active_mem.data()[2]
    DisLikeCount = active_mem.data()[3]
    update.callback_query.message.reply_photo(active_mem.data()[0],
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Мем", callback_data="mem"),
                 InlineKeyboardButton(str(LikeCount), callback_data="like-" + str(LikeCount)),
                 InlineKeyboardButton(str(DisLikeCount), callback_data="dislike-" + str(DisLikeCount))],
                [InlineKeyboardButton("Назад", callback_data="/fun"), menudel]]))
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
    global conflict
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
            update.callback_query.message.reply_text("".join(open(marks_openLIST[0] + value + "-" + action + ".txt", "r", encoding="utf-8").readlines(0)),
                                                     reply_markup=InlineKeyboardMarkup(marks))

        conflict = False
    else:
        echo(update, context) #ОТЛАДКА
        match update.callback_query['data']:
            case "/back":
                update.callback_query.message.reply_text('Меню', reply_markup=InlineKeyboardMarkup(start_key))

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
                                                                          reply_markup=InlineKeyboardMarkup(start_key)).message_id

            case "botinfo":
                new_message_id = update.callback_query.message.reply_text("".join(open("Bot.txt", "r", encoding="utf-8").readlines(0)),
                                                                          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Назад", callback_data="faq"), menudel]])).message_id
            case "ypiinfo":
                new_message_id = update.callback_query.message.reply_text("".join(open("Ypiter.txt", "r", encoding="utf-8").readlines(0)),
                                                                          reply_markup=InlineKeyboardMarkup(ypiterFAQ)).message_id

            case "all":
                 new_message_id = update.callback_query.message.reply_text("".join(open("YpiAll.txt", "r", encoding="utf-8").readlines(0)),
                                                         reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Назад", callback_data="ypiinfo"), menudel]])).message_id
            case "14":
                 new_message_id = update.callback_query.message.reply_text("".join(open("Ypi14.txt", "r", encoding="utf-8").readlines(0)),
                                                         reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Назад", callback_data="ypiinfo"), menudel]])).message_id
            case "15":
                 new_message_id = update.callback_query.message.reply_text("".join(open("Ypi15.txt", "r", encoding="utf-8").readlines(0)),
                                                         reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Назад", callback_data="ypiinfo"), menudel]])).message_id

            case "marks":
                new_message_id = update.callback_query.message.reply_text("Выберите номер рецензии:",
                                                                          reply_markup=InlineKeyboardMarkup(marks))
        
            case "rap":
                new_message_id = update.callback_query.message.reply_text(str(open("Game_Description1.txt", "r", encoding="utf-8").readlines(0)[0]),
                                                                          reply_markup=InlineKeyboardMarkup(rap)).message_id
            case "50 Cent":
                new_message_id = update.callback_query.message.reply_sticker(sticker_links['fifticent'][0],
                                                                             reply_markup=InlineKeyboardMarkup(rap)).message_id
            case "Lil Peep":
                new_message_id = update.callback_query.message.reply_sticker(sticker_links['lilpeep'][0],
                                                                             reply_markup=InlineKeyboardMarkup(rap)).message_id
            case "Egor Creed":
                new_message_id = update.callback_query.message.reply_sticker(sticker_links['egorcreed'][0],
                                                                             reply_markup=InlineKeyboardMarkup(rap)).message_id
            case "100 gecs":
                new_message_id = update.callback_query.message.reply_sticker(sticker_links['gecs'][0],
                                                                             reply_markup=InlineKeyboardMarkup(rap)).message_id 

            case "faq":
                new_message_id = update.callback_query.message.reply_text("Какой тип информации вас интересует?",
                                                                          reply_markup=InlineKeyboardMarkup(FAQ)).message_id
            case "info":
                new_message_id = update.callback_query.message.reply_text("".join(open("Info.txt", "r", encoding="utf-8").readlines(0)),
                                                                          reply_markup=InlineKeyboardMarkup(backdel)).message_id
            case "commands":
                new_message_id = update.callback_query.message.reply_text("".join(open("Commands.txt", "r", encoding="utf-8").readlines(0)),
                                                                          reply_markup=InlineKeyboardMarkup(backdel)).message_id
            case "helper":
                new_message_id = update.callback_query.message.reply_text("Если у вас есть вопросы, которые не решились в /FAQ, то напишите @ypite_nk",
                                                                          reply_markup=InlineKeyboardMarkup(backdel)).message_id
        if not conflict:
            context.chat_data['message_id'] = new_message_id
    conflict = False

updater.dispatcher.add_handler(CommandHandler('start', start_handler))
updater.dispatcher.add_handler(CommandHandler('info', info_handler))
updater.dispatcher.add_handler(CommandHandler('help', help_handler))
updater.dispatcher.add_handler(CommandHandler('FAQ', faq_handler))
updater.dispatcher.add_handler(CommandHandler('fun', fun_handler))
updater.dispatcher.add_handler(CommandHandler('pack', pack_handler))
updater.dispatcher.add_handler(CommandHandler('links', link_handler))
updater.dispatcher.add_handler(CommandHandler('support', support_handler))

updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo_handler))

updater.dispatcher.add_handler(CommandHandler('menu', back_handler))
updater.dispatcher.add_handler(CommandHandler("back", back_handler))

updater.dispatcher.add_handler(CommandHandler('mem', game2_handler))
#updater.dispatcher.add_handler(CommandHandler('game3', game3_handler))
#updater.dispatcher.add_handler(CommandHandler('game4', game4_handler))

updater.dispatcher.add_handler(CallbackQueryHandler(echo_button))

updater.start_polling()
updater.idle()