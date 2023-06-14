# -*- coding: utf-8 -*-
import telegram
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater
from telegram import ReplyKeyboardMarkup

token = "5873796392:AAEE1i9cwQ5Y2T6Mk-TJkTHruANhCmPr_uU"
bot = telegram.Bot(token=token)
updater = Updater(token=token, use_context=True)

Bot_txt = open("Bot.txt", "r", encoding="utf-8").readlines(0)
Command_txt = open("Commands.txt", "r", encoding="utf-8")
Info = open("Info.txt", "r", encoding="utf-8").readlines(0)

sticker_links = {'fifticent' : open("links/fifticent.txt").readlines(0), 'lilpeep' : open("links/lilpeep.txt").readlines(0),
         'gecs' : open("links/100gecs.txt").readlines(0), 'egorcreed' : open("links/egorcreed.txt").readlines(0)
         }

Ypiter_txt = open("Ypiter.txt", "r", encoding="utf-8").readlines(0)
Ypi_All = open("YpiAll.txt", "r", encoding="utf-8").readlines(0)
Ypi_14 = open("Ypi14.txt", "r", encoding="utf-8").readlines(0)
Ypi_15 = open("Ypi15.txt", "r", encoding="utf-8").readlines(0)

Game1_Description = open("Description1.txt", "r", encoding="utf-8").readlines(0)
#Game2_Description = open("", "r", encoding="utf-8").readlines(0)
#Game3_Description = open("", "r", encoding="utf-8").readlines(0)
#Game4_Description = open("", "r", encoding="utf-8").readlines(0)

Commands_txt = []
for i in range(4):
    Commands_txt.append(Command_txt.readlines(i))

Commands_txt = str(Commands_txt[0][0]) + "\n" + str(Commands_txt[0][1]) + "\n" + str(Commands_txt[0][2]) + "\n" + str(Commands_txt[0][3]) + "\n" + str(Commands_txt[0][4])

ypiterFAQ = ["Общее", "Info-14", "Info-15", "/back"]

def create_keyboard(options):
    keyboard = []
    for option in options:
        keyboard.append([option])
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def autoClose_keyboard(options):# FOR MORE INFO ANY NUMBERS
    keyboard = []
    for option in options:
        keyboard.append([option])
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)

def back_keyboard():
    keyboard = []
    options = ["/back"]
    for option in options:
        keyboard.append([option])
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def start_handler(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text='Тебя приветсвует текстовый помощник ypite, здесь собрана вся информация о моем создателе - Ypiter"e')
    context.bot.send_message(chat_id=update.message.chat_id, text='Воспользуйся командами или клавиатурой для взаимодействия со мной.\nЕсли есть вопросы, пиши: /menu')

def help_handler(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="По всем вопросам вы можете обратиться к @ypite_nk")

def faq_handler(update, context):
    update.message.reply_text("Какой тип информации вас интерисует?", reply_markup=create_keyboard(["О боте", "О ypiter", "/back"]))

def fun_handler(update, context):
    anw = update.message.reply_text
    anw("Смотри, есть 4 игры на выбор. Пиши /game1 или /game2 и т.д.", reply_markup=autoClose_keyboard(["/game1", "/game2", "/game3", "/game4", "/back"]))
    anw("Дополнительная ифнормация об играх: /funinfo")

def link_handler(update, context):
    pass

def funInfo_handler(update, context):
    pass

def echo_handler(update, context):
    print(update.message.text)
    if update.message.text == "FAQ":
        update.message.reply_text("Какой тип информации вас интересует?", reply_markup=create_keyboard(["О боте", "О ypiter", "/back"]))
    elif update.message.text == "О боте":
        update.message.reply_text(str(Bot_txt[0]))
    elif update.message.text == "О ypiter":
        update.message.reply_text(str(Ypiter_txt[0]), reply_markup=autoClose_keyboard(ypiterFAQ))
    
    elif update.message.text == "Общее":
        update.message.reply_text(str(Ypi_All[0]), reply_markup=autoClose_keyboard(ypiterFAQ))
    elif update.message.text == "Info-14":
        update.message.reply_text(str(Ypi_14[0]), reply_markup=autoClose_keyboard(ypiterFAQ))
    elif update.message.text == "Info-15":
        update.message.reply_text(str(Ypi_15[0]), reply_markup=autoClose_keyboard(ypiterFAQ))
    
    elif update.message.text == "Обратная связь":
        update.message.reply_text("Если у вас есть вопросы, которые не решились в /FAQ, то напишите @ypite_nk")

    elif update.message.text == "Инфо":
        update.message.reply_text(str(Info[0]))

    elif update.message.text == "Команды":
        update.message.reply_text(Commands_txt)

    elif update.message.text == "50 Cent":
        update.message.reply_sticker(sticker_links['fifticent'][0])

    elif update.message.text == "Lil Peep":
        update.message.reply_sticker(sticker_links['lilpeep'][0])

    elif update.message.text == "Egor Creed":
        update.message.reply_sticker(sticker_links['egorcreed'][0])

    elif update.message.text == "100 gecs":
        update.message.reply_sticker(sticker_links['gecs'][0])

def stick_handler(update, context):
    update.message.reply_sticker("https://raw.githubusercontent.com/ypite-nk/Sticker/main/5413715884726300309.webp")

def back_handler(update, context):
    options = ['FAQ', 'Обратная связь', 'Инфо', 'Команды']
    keyboard = create_keyboard(options)
    update.message.reply_text("Меню", reply_markup=keyboard)

def game1_handler(update, context):
    update.message.reply_text(str(Game1_Description[0]), reply_markup=create_keyboard(["50 Cent", "Lil Peep", "Egor Creed", "100 gecs", "/back"]))

def game2_handler(update, context):
    pass

def game3_handler(update, context):
    pass

def game4_handler(update, context):
    pass

updater.dispatcher.add_handler(CommandHandler('start', start_handler))
updater.dispatcher.add_handler(CommandHandler('help', help_handler))
updater.dispatcher.add_handler(CommandHandler('FAQ', faq_handler))
updater.dispatcher.add_handler(CommandHandler('fun', fun_handler))
updater.dispatcher.add_handler(CommandHandler('links', link_handler))
updater.dispatcher.add_handler(CommandHandler('funinfo', funInfo_handler))

updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo_handler))
updater.dispatcher.add_handler(MessageHandler(Filters.sticker, stick_handler))

updater.dispatcher.add_handler(CommandHandler('menu', back_handler))
updater.dispatcher.add_handler(CommandHandler("back", back_handler))

updater.dispatcher.add_handler(CommandHandler('game1', game1_handler))
updater.dispatcher.add_handler(CommandHandler('game2', game2_handler))
updater.dispatcher.add_handler(CommandHandler('game3', game3_handler))
updater.dispatcher.add_handler(CommandHandler('game4', game4_handler))

updater.start_polling()
updater.idle()