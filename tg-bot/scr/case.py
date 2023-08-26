# -*- coding: utf-8 -*-

'''
def echo_button(update, context):
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
'''
import keyboardbot as kb
from telegram import InlineKeyboardMarkup, ParseMode
from scr.wordly import Wordly

from spec import check_acces, openfile, global_raiting, buy
from spec import bank_test, bank_test_back

from spec import Create, Status_changer

from prefix import mycity, myprofile, mybank

from login import cost_rubles, cost_youshk

mem_m, old_message_id = ['', '', '', '', ''], 0
likestat, dislikestat = False, False

Message_idd = None

def photo_handler(update, context):
    global mem_m, active_mem, LikeCount, DisLikeCount
    
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
    
    messageId = update.callback_query.message.reply_photo(active_mem.data()[0],
                                                                reply_markup=InlineKeyboardMarkup(kb.mem(LikeCount,
                                                                                                         DisLikeCount)
                                                                                                  )).message_id
    
    mem_m[4], mem_m[3], mem_m[2], mem_m[1] = mem_m[3], mem_m[2], mem_m[1], mem_m[0]
    mem_m[0] = active_mem.data()[0]
    
    return messageId

class Callback_checker():
    #@check_acces
    def __init__(self, update, context):

        self.update = update
        self.context = context
        
        self.reply_text = self.update.callback_query.message.reply_text
        self.callback = self.update.callback_query['data']
        self._uid = str(self.update.callback_query.message.chat_id)
        
        self.message_id = self.update.callback_query.message.message_id
        self.status = False
        
        from keyboardbot import First_menu, Second_menu
        self.first_menu = First_menu()
        self.second_menu = Second_menu()
        
        self.any_checker = ["raiting"]
        
        self.checker = [
            self.change_menu,
            self.check_first_menu,
            self.check_second_menu,
            self.check_bank,
            self.check_test,
            self.check_changers,
            self.check_discards,
            self.check_game,
            self.check_likes,
            self.check_shop,
            self.check_quests,
            self.check_create,
            self.anycheck,
            self.close
            ]

        self.i = 0
        while not self.status and self.i < len(self.checker):
            self.checker[self.i]()
            self.i += 1
        
    def edit_message(self, text: str = "None", reply_markup: object = None):
        try:
            self.message_id = self.context.bot.edit_message_text(
                text = text,
                chat_id = int(self._uid),
                message_id = self.message_id,
                reply_markup = reply_markup,
                parse_mode = ParseMode.HTML
                ).message_id
        except:
            self.context.bot.send_message(chat_id = self._uid,
                                          text = text,
                                          reply_markup = reply_markup,
                                          parse_mode = ParseMode.HTML)

        self.status = True
        
    def change_menu(self):
        keys = ['menu1', 'menu2']
        
        if self.callback in keys:
            match self.callback:
                case "menu1":
                    self.edit_message(text = openfile('menu', 'menu'),
                                      reply_markup = InlineKeyboardMarkup(self.first_menu.menu[self.callback])
                                      )
                case "menu2":
                    self.edit_message(text = openfile('menu', 'menu'),
                                      reply_markup = InlineKeyboardMarkup(self.second_menu.menu[self.callback])
                                      )
                
    def check_first_menu(self):
        keys = self.first_menu.keys

        if self.callback in keys:
            match self.callback:
                case "profile":
                    self.edit_message(text = myprofile(self.update, self.context),
                                      reply_markup = InlineKeyboardMarkup(self.first_menu.menu[self.callback])
                                      )
                case "city":
                    self.edit_message(text = mycity(self.update, self.context),
                                      reply_markup = InlineKeyboardMarkup(self.first_menu.menu[self.callback])
                                      )
                case "shop":
                    self.edit_message(text = openfile("menu/shop", "shop"),
                                      reply_markup = InlineKeyboardMarkup(self.first_menu.menu[self.callback])
                                      )
                case "bank":
                    list = bank_test(self.update, self.context)
                    self.edit_message(text = list[0],
                                      reply_markup = list[1]
                                      )
                case "project":
                    self.edit_message(text = openfile("menu", "projects"),
                                      reply_markup = InlineKeyboardMarkup(self.first_menu.menu[self.callback])
                                      )
                case "social":
                    self.edit_message(text = openfile("menu/more", "social"),
                                      reply_markup = InlineKeyboardMarkup(self.first_menu.menu[self.callback])
                                      )
                case "callback":
                    self.edit_message(text = openfile("menu", "callback"),
                                      reply_markup = InlineKeyboardMarkup(self.first_menu.menu[self.callback])
                                      )
                case "version":
                    self.edit_message(text = openfile('menu', "info"),
                                      reply_markup = InlineKeyboardMarkup(self.first_menu.menu[self.callback])
                                      )
                
    def check_second_menu(self):
        keys = self.second_menu.keys

        if self.callback in keys:
            match self.callback:
                case "packs": 
                    self.edit_message(text = openfile("menu/more", "pack"),
                                      reply_markup = InlineKeyboardMarkup(self.second_menu.menu[self.callback])
                                      )
                case "fun": 
                    self.edit_message(text = openfile("menu/more/fun", "fun"),
                                      reply_markup = InlineKeyboardMarkup(self.second_menu.menu[self.callback])
                                      )
                case "bots": 
                    self.edit_message(text = openfile("menu/more/bots", "bots"),
                                      reply_markup = InlineKeyboardMarkup(self.second_menu.menu[self.callback])
                                      )
                case "learn": 
                    self.edit_message(text = openfile("learn", "description"),
                                      reply_markup = InlineKeyboardMarkup(self.second_menu.menu[self.callback])
                                      )
                case "donate": 
                    self.edit_message(text = openfile("menu/more", "donate"),
                                      reply_markup = InlineKeyboardMarkup(self.second_menu.menu[self.callback])
                                      )
                    
    def check_bank(self):
        if "bank_" in self.callback:
            bank, command = self.callback.split("_")
            match command:
                case "my":
                    self.edit_message(text = mybank(self.update, self.context),
                                      reply_markup = InlineKeyboardMarkup(self.first_menu.menu['bank'])
                                      )
                case "graphic": pass # NOT REALESE
                case "stat": pass # NOT REALESE
                case "actions": pass # NOT REALESE
                case "convert": pass # NOT REALESE
                    
    def check_test(self):
        if "#" in self.callback:
            match self.callback:
                case "0#0":
                    list = bank_test(self.update, self.context, 1)
                    self.edit_message(text = list[0],
                                      reply_markup = list[1]
                                      )
                case "1#1":
                    self.edit_message(text = "Неверный ответ!",
                                      reply_markup=InlineKeyboardMarkup(kb.back_to_menu_first)
                                      )
                    bank_test_back(self.update, self.context)
                case "1#2":
                    data = bank_test(self.update, self.context, 2)
                    self.edit_message(text = data[0],
                                      reply_markup = data[1]
                                      )
                case "2#1":
                    self.edit_message(text = "Неверный ответ!",
                                      reply_markup=InlineKeyboardMarkup(kb.back_to_menu_first)
                                      )
                    bank_test_back(self.update, self.context)
                case "2#2":
                    self.edit_message(text = "Неверный ответ!",
                                      reply_markup=InlineKeyboardMarkup(kb.back_to_menu_first)
                                      )
                    bank_test_back(self.update, self.context)
                case "2#3":
                    self.edit_message(text = "Неверный ответ!",
                                      reply_markup=InlineKeyboardMarkup(kb.back_to_menu_first)
                                      )
                    bank_test_back(self.update, self.context)
                case "2#4":
                    data = bank_test(self.update, self.context, 3)
                    self.edit_message(text = data[0],
                                      reply_markup = data[1]
                                      )
                case "3#1":
                    self.edit_message(text = "Неверный ответ!",
                                      reply_markup=InlineKeyboardMarkup(kb.back_to_menu_first)
                                      )
                    bank_test_back(self.update, self.context)
                case "3#2":
                    self.edit_message(text = "Неверный ответ!",
                                      reply_markup=InlineKeyboardMarkup(kb.back_to_menu_first)
                                      )
                    bank_test_back(self.update, self.context)
                case "3#3":
                    self.edit_message(text = "Неверный ответ!",
                                      reply_markup=InlineKeyboardMarkup(kb.back_to_menu_first)
                                      )
                    bank_test_back(self.update, self.context)
                case "3#4":
                    data = bank_test(self.update, self.context, 4)
                    self.edit_message(text = data[0],
                                      reply_markup = data[1]
                                      )
                    
    def check_changers(self):
        if "change" in self.callback:
            if "_change" in self.callback:
                change_obj, postfix = self.callback.split("_")
                if change_obj == "profile":
                    self.edit_message(text = openfile("menu/profile", "change"),
                                      reply_markup = InlineKeyboardMarkup(kb.profile_change)
                                      )
                elif change_obj == "city":
                    self.edit_message(text = openfile("data/city/descrip", "change"),
                                      reply_markup = InlineKeyboardMarkup(kb.city_change)
                                      )
            elif "!changer" in self.callback:
                callback = self.callback.split("_")[1]

                changer = Status_changer(self.update, self.context)
                changer.change(callback)
            
                self.edit_message(text = changer.message,
                                  reply_markup = changer.keyboard
                                  )
                    
    def check_discards(self):
        if "discard" in self.callback:
            match self.callback:
                case "discard":
                    Status_changer(self.update, self.context).clear_status()
                    self.edit_message(text = "Изменения отменены",
                                      reply_markup = InlineKeyboardMarkup(kb.back_to_menu_first)
                                      )
                case "discard_test":
                    bank_test_back(self.update, self.context)
                    self.edit_message(text = "Тест отменен",
                                      reply_markup = InlineKeyboardMarkup(kb.bank['start'])
                                      )
                    
    def check_game(self):
        if "game_" in self.callback:
            prefix, callback = self.callback.split("_")
            sticker_links = {'50 Cent' : open("menu/more/fun/rap/fifticent.txt").readlines(0),
                             'Lil Peep' : open("menu/more/fun/rap/lilpeep.txt").readlines(0),
                             '100 gecs' : open("menu/more/fun/rap/100gecs.txt").readlines(0),
                             'Egor Creed' : open("menu/more/fun/rap/egorcreed.txt").readlines(0),
                             'dog' : open("menu/more/fun/rap/dog.txt").readlines(0)
                             }
            match callback:
                case "rap":
                    self.edit_message(text = openfile('menu/more/fun/rap', "Game_Description1"),
                                      reply_markup = InlineKeyboardMarkup(kb.game_rap)
                                      )
                case "50 Cent":
                    self.update.callback_query.message.reply_sticker(sticker_links[self.callback][0],
                                                                     reply_markup=InlineKeyboardMarkup(kb.game_rap))
                case "Lil Peep":
                    self.update.callback_query.message.reply_sticker(sticker_links[self.callback][0],
                                                                     reply_markup=InlineKeyboardMarkup(kb.game_rap))
                case "Egor Creed":
                    self.update.callback_query.message.reply_sticker(sticker_links[self.callback][0],
                                                                     reply_markup=InlineKeyboardMarkup(kb.game_rap))
                case "100 gecs":
                    self.update.callback_query.message.reply_sticker(sticker_links[self.callback][0],
                                                                     reply_markup=InlineKeyboardMarkup(kb.game_rap))
                case "dog":
                    self.update.callback_query.message.reply_sticker(sticker_links[self.callback][0],
                                                                     reply_markup=InlineKeyboardMarkup(kb.game_rap))
                case "wordly":
                    changer = Status_changer(self.update, self.context)
                    changer.change(callback)
                    
                    self.edit_message(text = "Напишите предпологаемое слово, состоящее из 5 букв:\n\n",
                                      reply_markup = changer.keyboard
                                      )
                case "photomem": self.message_id = photo_handler(self.update, self.context)
                
                case "quests": 
                    self.edit_message(text = openfile("menu/more/fun/quests", "quests"),
                                      reply_markup = InlineKeyboardMarkup(kb.quests)
                                      )
                
    def check_quests(self):
        if "quest" in self.callback:
            
            from login import Quest
            prefix, number = self.callback.split("_")

            quest = Quest(self._uid)
            quest.authorize()

            profile = quest.get_user_quest()
            
            match number:
                case "1":
                    if profile['Первый квест'] == "Не пройден":
                        self.edit_message(text = "Error: 4.0.4 - no quest found",
                                          reply_markup = InlineKeyboardMarkup(kb.back_to_menu_first)
                                          )
                        profile['Первый квест'] == "В процессе"
                        
                    elif profile['Первый квест'] == "В процессе":
                        self.edit_message(text = "Вы уже начинали этот квест! Прогресс сброшен.",
                                          reply_markup = InlineKeyboardMarkup(kb.back_to_menu_first)
                                          )
                        profile['Первый квест'] == "Не пройден"

                    elif profile['Первый квест'] == "Пройден":
                        self.edit_message(text = "Вы уже проходили первый квест",
                                          reply_markup = InlineKeyboardMarkup(kb.quests)
                                          )

                case "2":
                    if profile['Второй квест'] == "Не пройден":
                        self.edit_message(text = "Error: 4.0.4 - no quest found",
                                          reply_markup = InlineKeyboardMarkup(kb.back_to_menu_first)
                                          )
                        profile['Второй квест'] == "В процессе"
                        
                    elif profile['Второй квест'] == "В процессе":
                        self.edit_message(text = "Вы уже начинали этот квест! Прогресс сброшен.",
                                          reply_markup = InlineKeyboardMarkup(kb.back_to_menu_first)
                                          )
                        profile['Второй квест'] == "Не пройден"

                    elif profile['Второй квест'] == "Пройден":
                        self.edit_message(text = "Вы уже проходили второй квест",
                                          reply_markup = InlineKeyboardMarkup(kb.quests)
                                          )
                        
    def check_project(self):
        if "proj" in self.callback:
            if self.callback == "projlist":
                self.edit_message(text = "Error project=0.5.5",
                                  reply_markup = InlineKeyboardMarkup(kb.back_to_menu_first)
                                  )
                
            elif self.callback == "projmore":
                self.edit_message(text = "Error project=0.5.6",
                                  reply_markup = InlineKeyboardMarkup(kb.back_to_menu_first)
                                  )
                    
    def check_likes(self):
        global old_message_id, likestat, dislikestat
        
        if "-" in self.callback:
            action, value = self.callback.split("-")
            if "m_" in action:
                prefix, action = action.split("_")

                if action == "like":
                    if str(self.message_id) != str(old_message_id) and dislikestat is not True:
                        active_mem.change_raiting(int(value) + 1, int(DisLikeCount))

                        old_message_id, likestat = self.message_id, True

                    elif str(self.message_id) == str(old_message_id) and dislikestat is not True:
                        active_mem.change_raiting(int(value) - 1, int(DisLikeCount))
                
                        old_message_id, likestat = "", False
            
                elif action == "dislike":
                    if str(self.message_id) != str(old_message_id) and likestat is not True:
                        active_mem.change_raiting(int(LikeCount), int(value) + 1)

                        old_message_id, dislikestat = self.message_id, True

                    elif str(self.message_id) == str(old_message_id) and likestat is not True:
                        active_mem.change_raiting(int(LikeCount), int(value) - 1)
                
                        old_message_id, dislikestat = "", False

                self.context.bot.edit_message_reply_markup(chat_id=self.update.callback_query.message.chat_id,
                                                           message_id=self.message_id,
                                                           reply_markup=InlineKeyboardMarkup(kb.mem(
                                                                                                    active_mem.data()[2],
                                                                                                    active_mem.data()[3]
                                                                                                    )
                                                                                             )
                                                           )
                
    def check_shop(self):
        if "shop" in self.callback:
            if "shop=" in self.callback:
                text = self.callback.split("=")[1]
                self.edit_message(text = f"Выберите способ покупки {text}",
                                  reply_markup = InlineKeyboardMarkup(kb.shops(text))
                                  )
            elif "shopbuy:" in self.callback:
                command, text, cost = self.callback.split(":")
                shopbuy = buy(text, int(cost), self._uid)
            
                if shopbuy:
                    self.edit_message(text = f"Вы успешно приобрели {text}",
                                      reply_markup = InlineKeyboardMarkup(self.first_menu.menu['shop'])
                                      )
                elif shopbuy is None:
                    self.edit_message(text = f"У вас не зарегестрирован банк!\nДля его регестрации пройдите в Меню -> Банк",
                                      reply_markup = InlineKeyboardMarkup(kb.back_to_menu_first)
                                      )
                else:
                    self.edit_message(text = f"Вам нехватило Юшек для приобретения {text} или у вас уже есть этот товар!",
                                      reply_markup = InlineKeyboardMarkup(self.first_menu.menu['shop'])
                                      )
        if "buy=" in self.callback:
            command, typ, text = self.callback.split("=")
            
            if typ == "R": 
                costs = cost_rubles()
                self.edit_message(text = f"Чтобы купить {text}, оплатите стоимость товара по ссылке ниже, подписав сообщение текстом b/{text} и выбрав 'Бот' в качестве цели, и отправьте скриншот оплаты и текст b/{text} @r_ypite\n\nК сожалению, более удобные способы оплаты пока что не доступны",
                                  reply_markup = InlineKeyboardMarkup(kb.buy_R(text,
                                                                               costs[text]
                                                                               )
                                                                      )
                                  )
                    
            elif typ == "Y":
                costs = cost_youshk()
                
                self.edit_message(text = f"Стоимость {text}: {costs[text]}",
                                  reply_markup = InlineKeyboardMarkup(kb.buy_Y(text,
                                                                               costs[text]
                                                                               )
                                                                      )
                                  )
                
    def check_create(self):
        if "create_" in self.callback:
            create, typed = self.callback.split("_")
            
            if typed in ['house', 'commercical', 'industry']:
                self.edit_message(text = openfile("data/city/descrip", f"create_{typed}"),
                                  reply_markup = InlineKeyboardMarkup(kb.create[create][typed])
                                  )
            else:
                if create == '!create':
                    self.edit_message(text = openfile("data/city/descrip/create", self.callback),
                                      reply_markup = InlineKeyboardMarkup(kb.create[self.callback])
                                      )
                else:
                    #self.edit_message(text = openfile("data/city/descrip/create", "create"),
                    #                  reply_markup = InlineKeyboardMarkup(kb.backcity_kb)
                    #                  )
                    create = Create(self.update, self.context)
                    
                    match typed:
                        case "house1": create.house1()
                        case "house2": create.house2()
                        case "house3": create.house3()

                        case "commercical1": create.comm1()
                        case "commercical2": create.comm2()
                        case "commercical3": create.comm3()

                        case "energy1": create.ind1_1()
                        case "energy2": create.ind1_2()
                        case "energy3": create.ind1_3()
                        
                        case "water1": create.ind2_1()
                        case "water2": create.ind2_2()
                        case "water3": create.ind2_3()

                        case "material1": create.ind3_1()
                        case "material2": create.ind3_2()
                        case "material3": create.ind3_3()
                            
                    self.edit_message(text = create.message,
                                      reply_markup = create.keyboard
                                      )
        elif self.callback == "create":
            self.edit_message(text = openfile("data/city/descrip", "create"),
                              reply_markup = InlineKeyboardMarkup(kb.create['create']['types'])
                              )
                    
    def anycheck(self):
        if self.callback in self.any_checker:
            if self.callback == "raiting":
                message = global_raiting(self.update, self.context)
                self.edit_message(text = message,
                                  reply_markup = InlineKeyboardMarkup(kb.profile_back)
                                  )
                
    def close(self):
        self.status = True