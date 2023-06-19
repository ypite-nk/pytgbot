# -*- coding: utf-8 -*-
import telegram
import random

from telegram.ext import CommandHandler, MessageHandler, Filters, Updater, CallbackQueryHandler, CallbackContext, InlineQueryHandler, ContextTypes
from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, Update, InlineQueryResultArticle, InputTextMessageContent
from uuid import uuid4
from html import escape

import used_class

token = "6143246892:AAEQGuhkqKZ-6Hsn7cvvbUMwOW0rNOHHGSE"
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
       [InlineKeyboardButton("...назад", callback_data="/fun"), menudel]]

start_key = [[InlineKeyboardButton("FAQ", callback_data="faq"), InlineKeyboardButton("Инфо", callback_data="info"), InlineKeyboardButton("Команды", callback_data="commands")],
             [InlineKeyboardButton("Обратная связь", callback_data="helper")]]

marks = [[InlineKeyboardButton("1::A", callback_data="A-1"), InlineKeyboardButton("2::A", callback_data="A-2"), InlineKeyboardButton("3::A", callback_data="A-3")],
         [InlineKeyboardButton("...назад", callback_data="ypiinfo"), menudel]]

commands_out = [[InlineKeyboardButton("Команды", callback_data="commands"), menudel]]

learns = [[InlineKeyboardButton("Образование", callback_data="learning"), InlineKeyboardButton("Книги", callback_data="books")],
             [menudel]]

learn = [[InlineKeyboardButton("IT", callback_data="it"), InlineKeyboardButton("3D", callback_data="3d")],
         [InlineKeyboardButton("...назад", callback_data="learn"), menudel]]

booklist = [[InlineKeyboardButton("...назад", callback_data="backbook1"), menudel]]

booklist1 = [[InlineKeyboardButton("Классика", callback_data="classic"), InlineKeyboardButton("Зарубежные", callback_data="foreign"), InlineKeyboardButton("Русская", callback_data="rus")],
        [InlineKeyboardButton("Детективы", callback_data="detective"), InlineKeyboardButton("Фэнтези", callback_data="fantasy"), InlineKeyboardButton("Фантастика", callback_data="fantastik")],
        [InlineKeyboardButton("Проза", callback_data="prose"), InlineKeyboardButton("Ужасы", callback_data="scary"), InlineKeyboardButton("Приключения", callback_data="adv")],
        [InlineKeyboardButton("...назад", callback_data="learn"), InlineKeyboardButton("Далее...", callback_data="booklist2")]]

booklist2 = [[InlineKeyboardButton("Боевики", callback_data="action"), InlineKeyboardButton("Повести", callback_data="stories"), InlineKeyboardButton("Поэзия", callback_data="poem")],
        [InlineKeyboardButton("Научпоп", callback_data="science"), InlineKeyboardButton("Психология", callback_data="psycho"), InlineKeyboardButton("Комиксы", callback_data="comics")],
        [InlineKeyboardButton("Манга", callback_data="manga"), InlineKeyboardButton("Эзотерика", callback_data="esotericism"), InlineKeyboardButton("Культура", callback_data="culture")],
        [InlineKeyboardButton("...назад", callback_data="backbook1"), InlineKeyboardButton("Далее...", callback_data="booklist3")]]

booklist3 = [[InlineKeyboardButton("Романы", callback_data="romans"), InlineKeyboardButton("Словари", callback_data="books"), InlineKeyboardButton("Справочники", callback_data="bookfaq")],
        [InlineKeyboardButton("Религия", callback_data="religion"), InlineKeyboardButton("Юмор", callback_data="funny"), InlineKeyboardButton("Рассказы", callback_data="tale")],
        [InlineKeyboardButton("Для детей", callback_data="kids"), InlineKeyboardButton("Бизнес", callback_data="buisness"), InlineKeyboardButton("Дом", callback_data="home")],
        [InlineKeyboardButton("...назад", callback_data="backbook2"), menudel]]

it = [[InlineKeyboardButton("Программирование", callback_data="coding")], [InlineKeyboardButton("Веб-разработка", callback_data="web")],
      [InlineKeyboardButton("Сис. Администрирование", callback_data="admin"), InlineKeyboardButton("Базы данных", callback_data="sql")],
      [InlineKeyboardButton("...назад", callback_data="learning"), menudel]]

coding = [[InlineKeyboardButton("Python", callback_data="py"), InlineKeyboardButton("C++", callback_data="+"), InlineKeyboardButton("JavaScript", callback_data="js")],
          [InlineKeyboardButton("...назад", callback_data="it"), menudel]]

python = [[InlineKeyboardButton(text="Материалы", url="https://www.python.org/")],
          [InlineKeyboardButton("...назад", callback_data="coding"), menudel]]

cpp = [[InlineKeyboardButton(text="Материалы", url="https://learn.microsoft.com/ru-ru/cpp/cpp/cpp-language-reference?view=msvc-170")],
          [InlineKeyboardButton("...назад", callback_data="coding"), menudel]]

js = [[InlineKeyboardButton(text="Материалы", url="https://learn.javascript.ru/")],
          [InlineKeyboardButton("...назад", callback_data="coding"), menudel]]

web = [[InlineKeyboardButton("HTML&CSS", callback_data="html_m"), InlineKeyboardButton("PHP", callback_data="php"), InlineKeyboardButton("django", callback_data="django")],
       [InlineKeyboardButton("...назад", callback_data="it"), menudel]]

html_m = [[InlineKeyboardButton(text="Материалы", url="https://developer.mozilla.org/ru/docs/Learn/Getting_started_with_the_web/HTML_basics")],
          [InlineKeyboardButton("...назад", callback_data="web"), menudel]]

php = [[InlineKeyboardButton(text="Материалы", url="https://developer.mozilla.org/ru/docs/Learn/Getting_started_with_the_web/HTML_basics")],
          [InlineKeyboardButton("...назад", callback_data="web"), menudel]]

django = [[InlineKeyboardButton(text="Материалы", url="https://developer.mozilla.org/ru/docs/Learn/Getting_started_with_the_web/HTML_basics")],
          [InlineKeyboardButton("...назад", callback_data="web"), menudel]]

admin = [[InlineKeyboardButton("Системный администратор", callback_data="s_admin"), InlineKeyboardButton("Data Sciens", callback_data="data_sciens")],
          [InlineKeyboardButton("...назад", callback_data="it"), menudel]]

s_admin = [[InlineKeyboardButton(text="Материалы", url="https://habr.com/ru/companies/ruvds/articles/486204/")],
           [InlineKeyboardButton("...назад", callback_data="admin"), menudel]]

data_sciens = [[InlineKeyboardButton(text="Материалы", url="https://habr.com/ru/articles/668428/")],
          [InlineKeyboardButton("...назад", callback_data="admin"), menudel]]

sql = [[InlineKeyboardButton(text="Материалы", url="https://habr.com/ru/articles/564390/")],
       [InlineKeyboardButton("...назад", callback_data="it"), menudel]]

modeling = [[InlineKeyboardButton(text="Материалы", url="https://habr.com/ru/companies/otus/articles/675410/")],
            [InlineKeyboardButton("...назад", callback_data="learning"), menudel]]

def echo(update, context): # ОТЛАДКА
    info = {'userdata' : "Text:{" + update.callback_query['data'] + "}, " + "from:{" + update.callback_query.message.chat['username'] + '}',
            'bot_data' : "Message ID: " + str(update.callback_query.message.message_id)}
    print(info)

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
    update.message.reply_text("".join(open("links/Mylink.txt", "r", encoding="utf-8").readlines(0)),
                              reply_markup=InlineKeyboardMarkup(button))

def learn_handler(update, context):
    update.message.reply_text("".join(open("learn/description.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(learns))

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
    for i in range(len(open("links/mem_links.txt", "r", encoding="utf-8").readlines(0))):
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
#   FAQ
            case "botinfo":
                new_message_id = update.callback_query.message.reply_text("".join(open("Bot.txt", "r", encoding="utf-8").readlines(0)),
                                                                          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Назад", callback_data="faq"), menudel]])).message_id
            case "ypiinfo":
                new_message_id = update.callback_query.message.reply_text("".join(open("Ypiter.txt", "r", encoding="utf-8").readlines(0)),
                                                                          reply_markup=InlineKeyboardMarkup(ypiterFAQ)).message_id
#   О YPITER
            case "all":
                 new_message_id = update.callback_query.message.reply_text("".join(open("YpiAll.txt", "r", encoding="utf-8").readlines(0)),
                                                         reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Назад", callback_data="ypiinfo"), menudel]])).message_id
            case "14":
                 new_message_id = update.callback_query.message.reply_text("".join(open("Ypi14.txt", "r", encoding="utf-8").readlines(0)),
                                                         reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Назад", callback_data="ypiinfo"), menudel]])).message_id
            case "15":
                 new_message_id = update.callback_query.message.reply_text("".join(open("Ypi15.txt", "r", encoding="utf-8").readlines(0)),
                                                         reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Назад", callback_data="ypiinfo"), menudel]])).message_id
#   РЕЦЕНЗИИ
            case "marks":
                new_message_id = update.callback_query.message.reply_text("Выберите номер рецензии:",
                                                                          reply_markup=InlineKeyboardMarkup(marks))
#   GAME:RAP
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
#   MENU
            case "faq":
                new_message_id = update.callback_query.message.reply_text("Какой тип информации вас интересует?",
                                                                          reply_markup=InlineKeyboardMarkup(FAQ)).message_id
            case "info":
                new_message_id = update.callback_query.message.reply_text("".join(open("Info.txt", "r", encoding="utf-8").readlines(0)),
                                                                          reply_markup=InlineKeyboardMarkup(backdel)).message_id
            case "commands":
                new_message_id = update.callback_query.message.reply_text("".join(open("links/Commands.txt", "r", encoding="utf-8").readlines(0)),
                                                                          reply_markup=InlineKeyboardMarkup(backdel)).message_id
            case "helper":
                new_message_id = update.callback_query.message.reply_text("Если у вас есть вопросы, которые не решились в /FAQ, то напишите @ypite_nk",
                                                                          reply_markup=InlineKeyboardMarkup(backdel)).message_id
#   LEARN
            case "learn":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/description.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(learns)).message_id

            case "learning":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/learning.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(learn)).message_id
#       GENRES
            case "books":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/booklist.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(booklist1)).message_id

            case "booklist2":
                new_message_id = update.callback_query.message.reply_text("Выберите жанр", reply_markup=InlineKeyboardMarkup(booklist2)).message_id

            case "booklist3":
                new_message_id = update.callback_query.message.reply_text("Выберите жанр", reply_markup=InlineKeyboardMarkup(booklist3)).message_id

            case "backbook1":
                new_message_id = update.callback_query.message.reply_text("Выберите жанр", reply_markup=InlineKeyboardMarkup(booklist1)).message_id

            case "backbook2":
                new_message_id = update.callback_query.message.reply_text("Выберите жанр", reply_markup=InlineKeyboardMarkup(booklist2)).message_id

            case "classic":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/classic.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(booklist)).message_id

            case "foreign":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/foreign.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(booklist)).message_id

            case "rus":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/rus.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(booklist)).message_id

            case "detective":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/detective.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(booklist)).message_id

            case "fantasy":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/fantasy.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(booklist)).message_id

            case "fantastik":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/fantastik.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(booklist)).message_id

            case "prose":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/prose.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(booklist)).message_id

            case "scary":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/scary.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(booklist)).message_id

            case "adv":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/adv.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(booklist)).message_id

            case "action":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/action.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(booklist)).message_id

            case "stories":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/stories.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(booklist)).message_id

            case "poem":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/poem.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(booklist)).message_id

            case "scince":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/scince.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(booklist)).message_id

            case "psycho":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/psycho.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(booklist)).message_id

            case "comics":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/comics.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(booklist)).message_id

            case "manga":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/manga.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(booklist)).message_id

            case "esotericism":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/esotericism.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(booklist)).message_id

            case "culture":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/culture.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(booklist)).message_id

            case "romans":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/romans.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(booklist)).message_id

            case "books":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/books.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(booklist)).message_id

            case "bookfaq":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/bookfaq.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(booklist)).message_id

            case "religion":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/religion.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(booklist)).message_id

            case "funny":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/funny.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(booklist)).message_id

            case "tale":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/tale.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(booklist)).message_id

            case "kids":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/kids.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(booklist)).message_id

            case "buisness":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/buisness.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(booklist)).message_id

            case "home":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/genres/home.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(booklist)).message_id
#   IT-LEARN
            case "it":
                new_message_id = update.callback_query.message.reply_text("".join(open("learn/it.txt", "r", encoding="utf-8").readlines(0)), reply_markup=InlineKeyboardMarkup(it)).message_id
#       CODING
            case "coding":
                new_message_id = update.callback_query.message.reply_text("Выберите язык программирования...", reply_markup=InlineKeyboardMarkup(coding)).message_id

            case "py":
                new_message_id = update.callback_query.message.reply_text("Программа обучения Python\n\nПользуясь этими материалами вам будет более понятно и просто учить ЯП - Python",
                                                                          reply_markup=InlineKeyboardMarkup(python)).message_id

            case "+":
                new_message_id = update.callback_query.message.reply_text("Программа обучения C++\n\nПользуясь этими материалами вам будет более понятно и просто учить ЯП - C++",
                                                                          reply_markup=InlineKeyboardMarkup(cpp)).message_id

            case "js":
                new_message_id = update.callback_query.message.reply_text("Программа обучения JavaScript\n\nПользуясь этими материалами вам будет более понятно и просто учить ЯП - JavaScript",
                                                                          reply_markup=InlineKeyboardMarkup(js)).message_id
#       ADMIN
            case "admin":
                new_message_id = update.callback_query.message.reply_text("Выберите деятельность...", reply_markup=InlineKeyboardMarkup(admin)).message_id
#       WEB
            case "web":
                new_message_id = update.callback_query.message.reply_text("Выберите способ разработки...", reply_markup=InlineKeyboardMarkup(web)).message_id

            case "html_m":
                new_message_id = update.callback_query.message.reply_text("Программа обучения HTML и CSS", reply_markup=InlineKeyboardMarkup(html_m)).message_id

            case "php":
                new_message_id = update.callback_query.message.reply_text("Программа обучения PHP", reply_markup=InlineKeyboardMarkup(php)).message_id

            case "django":
                new_message_id = update.callback_query.message.reply_text("Программа обучения Django", reply_markup=InlineKeyboardMarkup(django)).message_id

#       S_ADMIN
            case "s_admin":
                new_message_id = update.callback_query.message.reply_text("Обучение Сис. администрированию\n\nПользуясь этими материалами вам будет более понятно и просто учить СА", reply_markup=InlineKeyboardMarkup(s_admin)).message_id
#       DATA_SCIENS
            case "data_sciens":
                new_message_id = update.callback_query.message.reply_text("Обучение Data Sciens\n\nПользуясь этими материалами вам будет более понятно и просто учить DS", reply_markup=InlineKeyboardMarkup(data_sciens)).message_id

            case "sql":
                new_message_id = update.callback_query.message.reply_text("Обучение работе с SQL", reply_markup=InlineKeyboardMarkup(sql)).message_id
#   3D-LEARN
            case "3d":
                new_message_id = update.callback_query.message.reply_text("Обучение 3D моделированию", reply_markup=InlineKeyboardMarkup(modeling)).message_id

        if not conflict:
            context.chat_data['message_id'] = new_message_id
    conflict = False
    echo(update, context) #ОТЛАДКА

def inline_query(update, context):
    query = update.inline_query.query

    if not query:
        return

    result = [
        InlineQueryResultArticle(id=str(uuid4()), title="Caps",
                                 input_message_content=InputTextMessageContent(query.upper())
                                 ),
        InlineQueryResultArticle(id=str(uuid4()), title="Bold",
                                 input_message_content=InputTextMessageContent(f"<b>{escape(query)}</b>", parse_mode=telegram.ParseMode.HTML)
                                 ),
        InlineQueryResultArticle(id=str(uuid4()), title="Italic",
                                 input_message_content=InputTextMessageContent(f"<i>{escape(query)}</i>", parse_mode=telegram.ParseMode.HTML)
                                 ),
        ]

    update.inline_query.answer(result)

updater.dispatcher.add_handler(CommandHandler('start', start_handler))
updater.dispatcher.add_handler(CommandHandler('info', info_handler))
updater.dispatcher.add_handler(CommandHandler('help', help_handler))
updater.dispatcher.add_handler(CommandHandler('FAQ', faq_handler))
updater.dispatcher.add_handler(CommandHandler('fun', fun_handler))
updater.dispatcher.add_handler(CommandHandler('pack', pack_handler))
updater.dispatcher.add_handler(CommandHandler('links', link_handler))
updater.dispatcher.add_handler(CommandHandler('learning', learn_handler))
updater.dispatcher.add_handler(CommandHandler('support', support_handler))

updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo_handler))

updater.dispatcher.add_handler(CommandHandler('menu', back_handler))
updater.dispatcher.add_handler(CommandHandler("back", back_handler))

updater.dispatcher.add_handler(CommandHandler('mem', game2_handler))
#updater.dispatcher.add_handler(CommandHandler('game3', game3_handler))
#updater.dispatcher.add_handler(CommandHandler('game4', game4_handler))

updater.dispatcher.add_handler(CallbackQueryHandler(echo_button))
updater.dispatcher.add_handler(InlineQueryHandler(inline_query))

updater.start_polling()
updater.idle()