# -*- coding: utf-8 -*-
def close(func):
    def _closing(self):
        func(self)
        self.close
        return
    return _closing

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

from telegram import InlineKeyboardMarkup

import keyboardbot as kb
from spec import openfile

class Callback_checker():
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

        from spec import Checker
        
        self.check = Checker(self._uid, "Callback").check()
        if self.check[1]:
            self.edit_message(text = self.check[0],
                              reply_markup = InlineKeyboardMarkup(kb.back_to_menu_first)
                              )
            self.status = True
        
        self.science_text_dict = {
            'menu' : 'Выберите:',
            '3d' : openfile("learn/descriptext", "3d"),
            'adm' : openfile("learn/descriptext", "admin"),
            'sql' : openfile("learn/descriptext", "sql"),
            'python' : openfile("learn/descriptext", "py"),
            'c++' : openfile("learn/descriptext", "+"),
            'html' : openfile("learn/descriptext", "html"),
            'php' : openfile("learn/descriptext", "php"),
            'django' : openfile("learn/descriptext", "django"),
            'english' : openfile("learn/language", "english"),
            'polski' : openfile("learn/language", "polski"),
            'deutsch' : openfile("learn/language", "deutsch"),
            'list1' : 'Выберите жанр:',
            'list2' : 'Выберите жанр:',
            'list3' : 'Выберите жанр:',
            }
        
        self.genres_text_dict = {
            'classic' : openfile("learn/genres", "classic"),
            'foreign' : openfile("learn/genres", "foreign"),
            'rus' : openfile("learn/genres", "rus"),
            'detective' : openfile("learn/genres", "detective"),
            'fantasy' : openfile("learn/genres", "fantasy"),
            'fantastik' : openfile("learn/genres", "fantastik"),
            'prose' : openfile("learn/genres", "prose"),
            'scary' : openfile("learn/genres", "scary"),
            'adv' : openfile("learn/genres", "adv"),
            'action' : openfile("learn/genres", "action"),
            'stories' : openfile("learn/genres", "stories"),
            'poem' : openfile("learn/genres", "poem"),
            'science' : openfile("learn/genres", "science"),
            'psycho' : openfile("learn/genres", "psycho"),
            'comics' : openfile("learn/genres", "comics"),
            'manga' : openfile("learn/genres", "manga"),
            'esotericism' : openfile("learn/genres", "esotericism"),
            'culture' : openfile("learn/genres", "culture"),
            'romans' : openfile("learn/genres", "romans"),
            'bookfaq' : openfile("learn/genres", "bookfaq"),
            'home' : openfile("learn/genres", "home"),
            'religion' : openfile("learn/genres", "religion"),
            'funny' : openfile("learn/genres", "funny"),
            'buisness' : openfile("learn/genres", "buisness")
            }
        
        self.any_checker = ["raiting"]
        
        self.checker = [
            self.change_menu, self.check_first_menu, self.check_second_menu,
            self.check_bank, self.check_test,
            self.check_changers, self.check_discards,
            self.check_game, self.check_likes,
            self.check_shop,
            self.check_quests,
            self.check_create, self.check_city,
            self.check_science,
            self.anycheck,
            self.close
            ]

        self.i = 0
        while not self.status and self.i < len(self.checker):
            #print(str(self.i))
            self.checker[self.i]()
            self.i += 1
        
    def edit_message(self, text: str = "None", reply_markup: object = None):
        from telegram import ParseMode
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
        
    @close
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
                
    @close
    def check_first_menu(self):
        keys = self.first_menu.keys

        if self.callback in keys:
            match self.callback:
                case "profile":
                    from prefix import myprofile
                    self.edit_message(text = myprofile(self._uid),
                                      reply_markup = InlineKeyboardMarkup(self.first_menu.menu[self.callback])
                                      )
                case "city":
                    from prefix import mycity
                    self.edit_message(text = mycity(self.update, self.context),
                                      reply_markup = InlineKeyboardMarkup(self.first_menu.menu[self.callback])
                                      )
                case "shop":
                    self.edit_message(text = openfile("menu/shop", "shop"),
                                      reply_markup = InlineKeyboardMarkup(self.first_menu.menu[self.callback])
                                      )
                case "bank":
                    from spec import bank_test
                    bank_list = bank_test(self.update, self.context)
                    self.edit_message(text = bank_list[0],
                                      reply_markup = bank_list[1]
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
                
    @close
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
                case "science": 
                    self.edit_message(text = openfile("learn", "description"),
                                      reply_markup = InlineKeyboardMarkup(self.second_menu.menu[self.callback])
                                      )
                case "donate": 
                    self.edit_message(text = openfile("menu/more", "donate"),
                                      reply_markup = InlineKeyboardMarkup(self.second_menu.menu[self.callback])
                                      )
                    
    @close
    def check_bank(self):
        if "bank_" in self.callback:
            bank, command = self.callback.split("_")
            match command:
                case "my":
                    from prefix import mybank
                    
                    self.edit_message(text = mybank(self._uid),
                                      reply_markup = InlineKeyboardMarkup(self.first_menu.menu['bank'])
                                      )
                case "graphic":
                    self.edit_message(text = "Стоимость какой акции вас интерисует?",
                                      reply_markup = InlineKeyboardMarkup(kb.bank['actions'])
                                      )
                case "stat": pass # NOT REALESE
                case "actions": pass # NOT REALESE
                case "convert": pass # NOT REALESE
                
        elif 'graphic_' in self.callback:
            from bank_math import show_graph

            action = self.callback.replace("graphic_", "")            
            path = show_graph(self._uid, action)
            
            self.update.callback_query.message.reply_photo(open(path, 'rb'))
            self.update.callback_query.message.reply_text(f"Вот доступный вам график стоимости акции {action} за последнюю неделю",
                                                          reply_markup = InlineKeyboardMarkup(self.first_menu.menu['bank'])
                                                          )
                    
    @close
    def check_test(self):
        if "#" in self.callback:
            from spec import bank_test, bank_test_back
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
                    
    @close
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
                from spec import Status_changer
                callback = self.callback.split("_")[1]

                changer = Status_changer(self.update, self.context)
                changer.change(callback)
            
                self.edit_message(text = changer.message,
                                  reply_markup = changer.keyboard
                                  )
                    
    @close
    def check_discards(self):
        if "discard" in self.callback:
            match self.callback:
                case "discard":
                    from spec import Status_changer
                    Status_changer(self.update, self.context).clear_status()
                    self.edit_message(text = "Изменения отменены",
                                      reply_markup = InlineKeyboardMarkup(kb.back_to_menu_first)
                                      )
                case "discard_test":
                    from spec import bank_test_back
                    bank_test_back(self.update, self.context)
                    self.edit_message(text = "Тест отменен",
                                      reply_markup = InlineKeyboardMarkup(kb.bank['start'])
                                      )
                    
    @close
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
                    from spec import Status_changer
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
                
    @close
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
                        
    @close
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
                    
    @close
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
                
    @close
    def check_shop(self):
        if "shop" in self.callback:
            if "shop=" in self.callback:
                text = self.callback.split("=")[1]
                self.edit_message(text = f"Выберите способ покупки {text}",
                                  reply_markup = InlineKeyboardMarkup(kb.shops(text))
                                  )
            elif "shopbuy:" in self.callback:
                from spec import buy
                
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
                from login import cost_rubles
                
                costs = cost_rubles()
                self.edit_message(text = f"Чтобы купить {text}, оплатите стоимость товара по ссылке ниже, подписав сообщение текстом b/{text} и выбрав 'Бот' в качестве цели, и отправьте скриншот оплаты и текст b/{text} @r_ypite\n\nК сожалению, более удобные способы оплаты пока что не доступны",
                                  reply_markup = InlineKeyboardMarkup(kb.buy_R(text,
                                                                               costs[text]
                                                                               )
                                                                      )
                                  )
                    
            elif typ == "Y":
                from login import cost_youshk
                
                costs = cost_youshk()
                
                self.edit_message(text = f"Стоимость {text}: {costs[text]}",
                                  reply_markup = InlineKeyboardMarkup(kb.buy_Y(text,
                                                                               costs[text]
                                                                               )
                                                                      )
                                  )
                
    @close
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
                    from spec import Create
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
                    
    @close
    def check_city(self):
        if "!city" in self.callback:
            if self.callback.split("_")[1] == "create":

                self.edit_message(text = openfile("data/city/descrip", "create"),
                                  reply_markup = InlineKeyboardMarkup(kb.create['create']['types'])
                                  )
                
    @close
    def check_science(self):
        if "!science_" in self.callback:
            self.edit_message(text = self.genres_text_dict[self.callback.split("_")[1]],
                              reply_markup = InlineKeyboardMarkup(kb.science['books']['back'])
                              )
            
        elif 'science_' in self.callback:
            callback_list = self.callback.split("_")
            callback_len = len(callback_list)
            
            if self.callback == 'science_menu':
                text = openfile("learn", "description")
                new_kb = self.second_menu.menu['science']

            elif callback_len == 3: new_kb = kb.science[callback_list[1]][callback_list[2]]

            elif callback_len == 4: new_kb = kb.science[callback_list[1]][callback_list[2]][callback_list[3]]

            elif callback_len == 5: new_kb = kb.science[callback_list[1]][callback_list[2]][callback_list[3]][callback_list[4]]
            
            elif callback_len == 6: new_kb = kb.science[callback_list[1]][callback_list[2]][callback_list[3]][callback_list[4]][callback_list[5]]

            text = self.science_text_dict[callback_list[-1]]
            
            self.edit_message(text = text,
                              reply_markup = InlineKeyboardMarkup(new_kb)
                              )
                    
    @close
    def anycheck(self):
        if self.callback in self.any_checker:
            if self.callback == "raiting":
                from spec import global_raiting
                message = global_raiting(self.update, self.context)
                self.edit_message(text = message,
                                  reply_markup = InlineKeyboardMarkup(kb.profile_back)
                                  )
                
    def close(self): self.status = True