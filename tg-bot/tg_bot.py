# -*- coding: utf-8 -*-
import telegram
import random
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater, CallbackQueryHandler, CallbackContext
from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, Update

token = "5873796392:AAEE1i9cwQ5Y2T6Mk-TJkTHruANhCmPr_uU"
bot = telegram.Bot(token=token)
updater = Updater(token=token, use_context=True)

menu = InlineKeyboardButton("Меню", callback_data="/back")
menudel = InlineKeyboardButton("Меню", callback_data="/backdel")

conflict = False

mem_m = ['', '', '', '', '']

ypiterFAQ = [[InlineKeyboardButton("Общее", callback_data='all'), InlineKeyboardButton("14 лет", callback_data='14'), InlineKeyboardButton("15 лет", callback_data='15')],
             [menudel]]

FAQ = [[InlineKeyboardButton("О боте", callback_data="botinfo"), InlineKeyboardButton("О ypiter", callback_data="ypiinfo")],
       [menudel]]

back = [[menu]]
backdel = [[menudel]]

rap = [[InlineKeyboardButton("50 Cent", callback_data="50 Cent"), InlineKeyboardButton("Lil Peep", callback_data="Lil Peep"),
        InlineKeyboardButton("Egor Creed", callback_data="Egor Creed"), InlineKeyboardButton("100 gecs", callback_data="100 gecs")],
       [menu]]

start_key = [[InlineKeyboardButton("FAQ", callback_data="faq"), InlineKeyboardButton("Инфо", callback_data="info"), InlineKeyboardButton("Команды", callback_data="commands")],
             [InlineKeyboardButton("Обратная связь", callback_data="helper")]]

def start_handler(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text='Тебя приветсвует текстовый помощник ypite, здесь собрана вся информация о моем создателе - Ypiter"e\nВоспользуйся командами или клавиатурой для взаимодействия со мной',
                             reply_markup=InlineKeyboardMarkup(start_key))

def help_handler(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="По всем вопросам вы можете обратиться к @ypite_nk", reply_markup=InlineKeyboardMarkup(backdel))

def faq_handler(update, context):
    update.message.reply_text("Какой тип информации вас интересует?", reply_markup=InlineKeyboardMarkup(FAQ))

def fun_handler(update, context):
    answer = update.message.reply_text
    key = [
            [
             InlineKeyboardButton("rap", callback_data="rap"), InlineKeyboardButton("mem", callback_data="mem"),
             InlineKeyboardButton("3", callback_data="3"), InlineKeyboardButton("4", callback_data="4")
            ],
            [menu]
           ]
    answer("Смотри, есть 4 игры на выбор.\n/rap - стикер = репер\n/mem - рандомный мемас из базы\n", reply_markup=InlineKeyboardMarkup(key))

def link_handler(update, context):
    answer = update.message.reply_text
    button = [
                [InlineKeyboardButton(text="Вконтакте", url="https://vk.com/ypite")],
                [InlineKeyboardButton(text="Youtube", url="https://www.youtube.com/channel/UCQunVaPHyI2MvS0rU56_MhA")],
                [InlineKeyboardButton(text="TikTok", url="https://vm.tiktok.com/ZT81sSebh/")],
                [InlineKeyboardButton(text="Группа Вк", url="https://vk.com/cloud_ypiter")],
                [menu]
             ]
    answer("\n".join(open("Mylink.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(button))

def echo_handler(update, context):
    message = update.message.text
    update.message.reply_text("Пожалуйста, воспользуйтесь интерфейсом или командами. Если у вас есть вопросы: /help")

def back_handler(update, context):
    options = ['FAQ', 'Инфо', 'Команды', 'Обратная связь']
    update.message.reply_text("Меню", reply_markup=InlineKeyboardMarkup(start_key))

def game2_handler(update, context):
    global mem_m
    mem_links = open("mem_links.txt", "r", encoding="utf-8").readlines(0)
    mem_n = str(random.choice(mem_links))
    while mem_n == mem_m[0] or mem_n == mem_m[1] or mem_n == mem_m[2] or mem_n == mem_m[3] or mem_n == mem_m[4]:
        mem_n = str(random.choice(mem_links))
    update.callback_query.message.reply_photo(mem_n, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Мем", callback_data="mem"), menu]]))
    mem_m[4] = mem_m[3]
    mem_m[3] = mem_m[2]
    mem_m[2] = mem_m[1]
    mem_m[1] = mem_m[0]
    mem_m[0] = mem_n

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
    match update.callback_query['data']:
        case "/back":
            update.callback_query.message.reply_text('Меню', reply_markup=InlineKeyboardMarkup(start_key))

        case "all":
            update.callback_query.message.reply_text("\n".join(open("YpiAll.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(ypiterFAQ))
        case "14":
            update.callback_query.message.reply_text("\n".join(open("Ypi14.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(ypiterFAQ))
        case "15":
            update.callback_query.message.reply_text("\n".join(open("Ypi15.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(ypiterFAQ))

        case "mem":
            game2_handler(update, context)

        case _:
            conflict = False

    if not conflict:
        change(update, context)
    
    match update.callback_query['data']:
        case "/backdel":
            new_message_id = update.callback_query.message.reply_text('Меню', reply_markup=InlineKeyboardMarkup(start_key)).message_id

        case "botinfo":
            new_message_id = update.callback_query.message.reply_text("\n".join(open("Bot.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(back)).message_id
        case "ypiinfo":
            new_message_id = update.callback_query.message.reply_text("\n".join(open("Ypiter.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(ypiterFAQ)).message_id
        
        case "rap":
            new_message_id = update.callback_query.message.reply_text(str(open("Description1.txt", "r", encoding="utf-8").readlines(0)[0]), reply_markup=InlineKeyboardMarkup(rap)).message_id
        case "50 Cent":
            new_message_id = update.callback_query.message.reply_sticker(sticker_links['fifticent'][0]).message_id
        case "Lil Peep":
            new_message_id = update.callback_query.message.reply_sticker(sticker_links['lilpeep'][0]).message_id
        case "Egor Creed":
            new_message_id = update.callback_query.message.reply_sticker(sticker_links['egorcreed'][0]).message_id
        case "100 gecs":
            new_message_id = update.callback_query.message.reply_sticker(sticker_links['gecs'][0]).message_id

        case "faq":
            new_message_id = update.callback_query.message.reply_text("Какой тип информации вас интересует?", reply_markup=InlineKeyboardMarkup(FAQ)).message_id
        case "info":
            new_message_id = update.callback_query.message.reply_text("\n".join(open("Info.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(backdel)).message_id
        case "commands":
            new_message_id = update.callback_query.message.reply_text("\n".join(open("Commands.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(backdel)).message_id
        case "helper":
            new_message_id = update.callback_query.message.reply_text("Если у вас есть вопросы, которые не решились в /FAQ, то напишите @ypite_nk", reply_markup=InlineKeyboardMarkup(backdel)).message_id
    if not conflict:
        context.chat_data['message_id'] = new_message_id

    conflict = False

updater.dispatcher.add_handler(CommandHandler('start', start_handler))
updater.dispatcher.add_handler(CommandHandler('help', help_handler))
updater.dispatcher.add_handler(CommandHandler('FAQ', faq_handler))
updater.dispatcher.add_handler(CommandHandler('fun', fun_handler))
updater.dispatcher.add_handler(CommandHandler('links', link_handler))

updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo_handler))

updater.dispatcher.add_handler(CommandHandler('menu', back_handler))
updater.dispatcher.add_handler(CommandHandler("back", back_handler))

updater.dispatcher.add_handler(CommandHandler('mem', game2_handler))
#updater.dispatcher.add_handler(CommandHandler('game3', game3_handler))
#updater.dispatcher.add_handler(CommandHandler('game4', game4_handler))

updater.dispatcher.add_handler(CallbackQueryHandler(echo_button))

updater.start_polling()
updater.idle()