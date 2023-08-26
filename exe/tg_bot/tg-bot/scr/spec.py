# -*- coding: utf-8 -*-
def openfile(path: str, name: str, method: int = 0):
    if method:
        with open(path + "/" + name + ".txt", "r", encoding="utf-8") as f: return "\n".join(f.readlines(0))
    if path != "":
        with open(path + "/" + name + ".txt", "r", encoding="utf-8") as f: return "".join(f.readlines(0))
    else:
        with open(name + ".txt", "r", encoding="utf-8") as f: return "".join(f.readlines(0))

import login
import urllib.request
import keyboardbot as kb

from telegram import InlineKeyboardMarkup

def global_raiting(update, context):
    uid = str(update.callback_query.message.chat_id)

    user_active = login.User(uid).get_user_profile()
    user_id_list = login.users_profile_info()
    user_dict = {}
    output = ""

    for user_id in user_id_list:
        if "-" not in user_id:
            user = login.User(user_id).get_user_profile()
            if user['VIP'] != "None":
                user_dict[user['Никнейм'] + "♳"] = user['Рейтинг']
            else:
                user_dict[user['Никнейм']] = user['Рейтинг']

    user_dict = sorted(user_dict.items(), key=lambda x: x[1], reverse=True)
    for i in range(len(user_dict)):
        key, value = str(user_dict[i]).replace("(", "").replace(")", "").replace("'", "").split(", ")
        output += f"{str(i+1)}) {str(key)} : {str(value)}\n"
    
    if user_active['VIP'] == 'None':
        return f"🌏 Ваш рейтинг: {str(user_active['Рейтинг'])}\n\nГлобальный рейтинг:\n{output}"
    else:
        return f"🌏 Ваш рейтинг: ♳{str(user_active['Рейтинг'])}\n\nГлобальный рейтинг:\n{output}"
    
def buy(callback, cost: int, uid: str):
    user = login.User(uid)
    user_bank = login.Bank(uid)
    
    profile = user.get_user_profile()
    actions = user_bank.get_user_bank()
    
    autobuy = ['VIP', 'JxSpeed', 'MacroMotor', 'LifeX10']
    bank_buy = ['JxSpeed', 'MacroMotor']

    if profile['Юшки'] >= cost:
        
        profile['Юшки'] -= cost
        
        if callback in autobuy:

            if callback in bank_buy:
                if actions is None: return None
                if actions[callback] == "False": actions[callback] == "True"
                else: return True
                
            else:
                if callback == 'LifeX10':
                    profile['Попытки'] += 10
                if callback != 'LifeX10' and profile[callback] == "None":
                    profile[callback] = "Есть"
        
        user.write_user_profile(profile)
        user_bank.write_user_bank(actions)
        login.budget_write("spend", cost)
        return True
    
    return False

def bank_test(update, context, test: any = 0):
    new_message_id = 0
    userBank = login.Bank(str(update.callback_query.message.chat_id))
    userBank.authorize()
    bank = userBank.get_user_bank()
    
    if bank['test'] == 0 and test == 0:
        return [openfile("base/bank", "bank"), InlineKeyboardMarkup(kb.bank['start'])]
        
    if bank['test'] == 0 and test == 1:
        user = login.User(str(update.callback_query.message.chat_id))
        user_profile = user.get_user_profile()
        if user_profile['Юшки'] >= 19:
            user_profile['Юшки'] -= 19
        
            user.write_user_profile(user_profile)
        
            bank['test'] = 1
            bank['test_lvl'] = 1
        
            login.budget_write("spend", 19)
            userBank.write_user_bank(bank)
            
        else:
            return ["На вашем счету недостаточно средств!", InlineKeyboardMarkup(kb.bank['start'])]
        
    if test > 1:
        bank['test_lvl'] = test
        if test == 4:
            bank['test'] = 2
            userBank.write_user_bank(bank)
            
    if bank['test'] == 2:
        return [openfile("base/bank", "access"), InlineKeyboardMarkup(kb.First_menu().menu['bank'])]
        
    if bank['test'] == 1:
        if bank['test_lvl'] == 1:
            return [openfile("base/bank/test", "test_1"), InlineKeyboardMarkup(kb.bank['test1'])]
        
        if bank['test_lvl'] == 2:
            return [openfile("base/bank/test", "test_2"), InlineKeyboardMarkup(kb.bank['test2'])]
        
        if bank['test_lvl'] == 3:
            return [openfile("base/bank/test", "test_3"), InlineKeyboardMarkup(kb.bank['test3'])]
    userBank.write_user_bank(bank)

def bank_test_back(update, context):
    userBank = login.Bank(str(update.callback_query.message.chat_id))
    bank = userBank.get_user_bank()
    bank['test'] = 0
    bank['test_lvl'] = 0
    userBank.write_user_bank(bank)
    
def quest_start(update, context):
    quest = login.Quest(str(update.callback_query.message.chat_id))
    quest.authorize()

class Echo_Checker():
    def __init__(self, update, context):
        self.update = update
        self.context = context
        if self.update.message.text is not None:
            self.prefix, *self.text = self.update.message.text.split(" ")
            if len(self.text) == 3: self.update.message.text = self.text[2]

        self.uid = str(self.update.message.chat_id)

        self.userkb = InlineKeyboardMarkup(kb.profile_back)
        self.citykb = InlineKeyboardMarkup(kb.backcity_kb)
        self.wordlykb = InlineKeyboardMarkup(kb.back_to_menu_second)

        self.user = login.User(self.uid)
        self.city = login.City(self.uid)

        self.city_status = {
            'cityname':0,
            'sign':0,
            'gymn':0,
            'flag':0,
            'history':0,
            'mayor':0
            }

        self.user_status = {
            'nickname':0,
            'name':0,
            'birthday':0,
            'buisness':0,
            'wordly':0
            }

        self.old_data = None

        self.message = "Error"
        self.reply_markup = InlineKeyboardMarkup(kb.back_to_menu_first)

    def write_user(self):
        user_profile = self.user.get_user_profile()
        user_status = self.user.get_user_status()
        user_change = self.user.get_user_change()

        if self.text is not None: new_data = self.text.replace("\n", "").replace(",", "‚")

        if user_status['nickname']:
            if user_change['nickname'] >= 2 and user_profile['VIP'] == 'None':
                self.message = "Вы достигли дневного лимита изменения данного значения!!\n\nЧтобы снять лимиты на изменения --> купите VIP♳"
                self.reply_markup = self.userkb

                return True
            else:
                self.old_data = user_profile['Никнейм']
                user_profile['Никнейм'] = new_data
                user_change['nickname'] += 1

        elif user_status['name']:
            if user_change['name'] >= 2 and user_profile['VIP'] == 'None':
                self.message = "Вы достигли дневного лимита изменения данного значения!!\n\nЧтобы снять лимиты на изменения --> купите VIP♳"
                self.reply_markup = self.userkb

                return True
            else:
                self.old_data = user_profile['Имя']
                user_profile['Имя'] = new_data
                user_change['name'] += 1

        elif user_status['birthday']:
            if user_change['birthday'] >= 2 and user_profile['VIP'] == 'None':
                self.message = "Вы достигли дневного лимита изменения данного значения!!\n\nЧтобы снять лимиты на изменения --> купите VIP♳"
                self.reply_markup = self.userkb

                return True
            else:
                self.old_data = user_profile['День рождения']
                user_profile['День рождения'] = new_data
                user_change['birthday'] += 1

        elif user_status['buisness']:
            if user_change['buisness'] >= 2 and user_profile['VIP'] == 'None':
                self.message = "Вы достигли дневного лимита изменения данного значения!!\n\nЧтобы снять лимиты на изменения --> купите VIP♳"
                self.reply_markup = self.userkb

                return True
            else:
                self.old_data = user_profile['Интересы']
                user_profile['Интересы'] = new_data
                user_change['buisness'] += 1

        else: return False

        self.user.write_user_profile(user_profile)
        self.user.write_user_change(user_change)

        self.message = f"Данные успешно обновлены!\n\n{self.old_data} >>> {new_data}"
        self.reply_markup = self.userkb

        return True
    
    def wordly(self):
        user_status = self.user.get_user_status()
        if user_status['wordly']:
            from wordly import Wordly
            
            wordly = Wordly(self.uid)
            wordly.check_word(self.text.replace("\n", "").replace(",", "‚"))
            self.message = wordly.output
            self.reply_markup = self.wordlykb
            
            if "!" in self.message:
                return True
            else:
                return False
        else:
            return None

    def write_city(self):
        user = self.user.get_user_profile()
        user_city = self.city.get_city_info()
        user_city_status = self.city.get_city_status()
        user_city_change = self.city.get_city_change()

        if self.text is not None: new_data = self.text.replace("\n", "").replace(",", "‚")

        if user_city_status is None: return False

        if user_city_status['cityname']:
            if user_city_change['cityname'] >=2 and user['VIP'] == 'None':
                self.message = "Вы достигли дневного лимита изменения данного значения!!\n\nЧтобы снять лимиты на изменения --> купите VIP♳"
                self.reply_markup = self.citykb

                return True

            else:
                self.old_data = user_city['Имя']
                user_city['Имя'] = new_data
                user_city_change['cityname'] += 1

        elif user_city_status['sign'] == 1 and self.text is None:
            if user_city_change['sign'] >= 2 and user['VIP'] == 'None':
                self.message = "Вы достигли дневного лимита изменения данного значения!!\n\nЧтобы снять лимиты на изменения --> купите VIP♳"
                self.reply_markup = self.citykb

                return True

            else:
                file = self.context.bot.get_file(self.update.message.photo[-1])
                file_size = self.update.message.photo[-1]

                if file_size.width <= 400 and file_size.height <= 400:
                    user_city['Герб'] = "Есть"
                    user_city_change['sign'] += 1

                    response = urllib.request.urlopen(file.file_path)
                    with open("base/cities/photo/" + self.uid + "sign.jpg", 'wb') as new_file: new_file.write(response.read())
                    self.message = "Данные успешно обновлены!"
                else:
                    self.message = "Размеры файла превышают максимальные! (400x400)"
                    return False

        elif user_city_status['flag'] == 1 and self.text is None:
            if user_city_change['flag'] >= 2 and user['VIP'] == 'None':
                self.message = "Вы достигли дневного лимита изменения данного значения!!\n\nЧтобы снять лимиты на изменения --> купите VIP♳"
                self.reply_markup = self.citykb

                return True
            else:
                file = self.context.bot.get_file(self.update.message.photo[-1])
                file_size = self.update.message.photo[-1]

                if file_size.width <= 400 and file_size.height <= 200:
                    user_city['Флаг'] = "Есть"
                    user_city_change['flag'] += 1

                    response = urllib.request.urlopen(file.file_path)
                    with open("base/cities/photo/" + self.uid + "flag.jpg", 'wb') as new_file: new_file.write(response.read())
                    self.message = "Данные успешно обновлены!"
                else:
                    self.message = "Размеры файла превышают максимальные! (400x200)"
                    return False

        elif user_city_status['gymn']:
            if user_city_change['gymn'] >= 2 and user['VIP'] == 'None':
                self.message = "Вы достигли дневного лимита изменения данного значения!!\n\nЧтобы снять лимиты на изменения --> купите VIP♳"
                self.reply_markup = self.citykb

                return True

            else:
                user_city['Гимн'] = new_data
                user_city_change['gymn'] += 1

        elif user_city_status['history']:
            if user_city_change['history'] >= 2 and user['VIP'] == 'None':
                self.message = "Вы достигли дневного лимита изменения данного значения!!\n\nЧтобы снять лимиты на изменения --> купите VIP♳"
                self.reply_markup = self.citykb

                return True

            else:
                user_city['История'] = new_data
                user_city_change['history'] += 1

        elif user_city_status['mayor']:
            if user_city_change['mayor'] >= 2 and user['VIP'] == 'None':
                self.message = "Вы достигли дневного лимита изменения данного значения!!\n\nЧтобы снять лимиты на изменения --> купите VIP♳"
                self.reply_markup = self.citykb

                return True

            else:
                user_city['Мэр'] = new_data
                user_city_change['mayor'] += 1

        else: return False

        self.city.write_city_profile(user_city)

        self.message = "Данные успешно обновлены!"
        self.reply_markup = self.citykb

        if self.old_data is not None: self.message = f"Данные успешно обновлены!\n\n{self.old_data} >>> {new_data}"
        
        return True

    def echo_check(self):
        self.text = self.update.message.text

        if self.write_user():
            self.user.write_user_status(self.user_status)

            return True

        elif self.write_city():
            self.city.write_city_status(self.city_status)
            
            return True

        dash = self.wordly()
        if dash:
            self.user.write_user_status(self.user_status)
            return True
        elif not dash:
            return True
        else:
            return False

class Status_changer():
    def __init__(self, update, context):
        self.update = update
        self.context = context

        self.uid = str(self.update.callback_query.message.chat_id)

        self.user_data_list = ['nickname', 'name', 'buisness', 'birthday', 'wordly']
        self.city_data_list = ['cityname', 'sign', 'flag', 'gymn', 'history', 'mayor']

        self.user_status = {
            'nickname':0,
            'name':0,
            'birthday':0,
            'buisness':0,
            'wordly':0
            }

        self.city_status = {
            'cityname':0,
            'sign':0,
            'flag':0,
            'gymn':0,
            'history':0,
            'mayor':0
            }

        self.message = "Введите новое значение"
        self.keyboard = InlineKeyboardMarkup(kb.changerback)

    def profile(self):
        user_status = login.User(self.uid).get_user_status()
        user_status[self.value] = 1
        
        login.User(self.uid).write_user_status(user_status)

    def city(self):
        user_city_status = login.City(self.uid).get_city_status()
        user_city_status[self.value] = 1
        
        if self.value == "sign":
            self.message = "Отправьте изображение вашего герба, не превышающее размеры 400*400 пикселей"
        elif self.value == "flag":
            self.message = "Отправьте изображение вашего флага, не превышающее размеры 400*200 пикселей"
            
        login.City(self.uid).write_city_status(user_city_status)

    def change(self, value: str):
        self.value = value

        if self.value in self.user_data_list: self.profile()
        elif self.value in self.city_data_list: self.city()

        else: self.message = "Error"

    def clear_status(self):
        login.User(self.uid).write_user_status(self.user_status)
        login.City(self.uid).write_city_status(self.city_status)

class Create():
    def __init__(self, update, context):
        self.update = update
        self.context = context

        self.uid = str(self.update.callback_query.message.chat_id)
        self.city = login.City(self.uid)
        
        self.keyboard = InlineKeyboardMarkup(kb.backcity_kb)
        self.message = "Error #CREATE=0.5.1"

    def house1(self):
        user_city = self.city.get_city_info()
        user_city_data = self.city.get_city_data()

        money_cost = 500000
        money_expenses = 67200
        energy_expenses = 400
        water_expenses = 1200

        export_people = 4000

        if user_city_data['Бюджет'] > money_cost and (user_city_data['Доход'] - user_city_data['Расходы']) > money_expenses:
            if (user_city_data['Электроэнергия'] - user_city_data['Электропотребление']) > energy_expenses:
                if (user_city_data['Водоснабжение'] - user_city_data['Водопотребление']) > water_expenses:
                    
                    user_city_data['Бюджет'] -= money_cost
                    user_city_data['Расходы'] += money_expenses
                    user_city_data['Электропотребление'] += energy_expenses
                    user_city_data['Водопотребление'] += water_expenses

                    user_city['Население'] += export_people

                    self.city.write_city_data(user_city_data)
                    self.city.write_city_profile(user_city)

                    self.message = openfile("data/city/descrip/create", "create_house_1")

                else: self.message = "Для постройки этого района нехватает водоснабжения! Постройте новые станции водоснабжения"

            else: self.message =  "Для постройки этого района нехватает электроэнергии! Постройте новые электростанции"

        else: self.message = "Средства города не способны содерждать этот район... Пополните бюджет или увеличьте доход"

    def house2(self):
        user_city = self.city.get_city_info()
        user_city_data = self.city.get_city_data()

        money_cost = 1500000
        money_expenses = 151200
        energy_expenses = 900
        water_expenses = 2700

        export_people = 9000

        if user_city_data['Бюджет'] > money_cost and (user_city_data['Доход'] - user_city_data['Расходы']) > money_expenses:
            if (user_city_data['Электроэнергия'] - user_city_data['Электропотребление']) > energy_expenses:
                if (user_city_data['Водоснабжение'] - user_city_data['Водопотребление']) > water_expenses:
                    
                    user_city_data['Бюджет'] -= money_cost
                    user_city_data['Расходы'] += money_expenses
                    user_city_data['Электропотребление'] += energy_expenses
                    user_city_data['Водопотребление'] += water_expenses

                    user_city['Население'] += export_people

                    self.city.write_city_data(user_city_data)
                    self.city.write_city_profile(user_city)

                    self.message = openfile("data/city/descrip/create", "create_house_2")
                    
                else: self.message = "Для постройки этого района нехватает водоснабжения! Постройте новые станции водоснабжения"

            else: self.message =  "Для постройки этого района нехватает электроэнергии! Постройте новые электростанции"

        else: self.message = "Средства города не способны содерждать этот район... Пополните бюджет или увеличьте доход"

    def house3(self):
        user_city = self.city.get_city_info()
        user_city_data = self.city.get_city_data()

        money_cost = 3500000
        money_expenses = 336000
        energy_expenses = 2000
        water_expenses = 6000

        export_people = 20000

        if user_city_data['Бюджет'] > money_cost and (user_city_data['Доход'] - user_city_data['Расходы']) > money_expenses:
            if (user_city_data['Электроэнергия'] - user_city_data['Электропотребление']) > energy_expenses:
                if (user_city_data['Водоснабжение'] - user_city_data['Водопотребление']) > water_expenses:
                    
                    user_city_data['Бюджет'] -= money_cost
                    user_city_data['Расходы'] += money_expenses
                    user_city_data['Электропотребление'] += energy_expenses
                    user_city_data['Водопотребление'] += water_expenses

                    user_city['Население'] += export_people

                    self.city.write_city_data(user_city_data)
                    self.city.write_city_profile(user_city)

                    self.message = openfile("data/city/descrip/create", "create_house_3")
                    
                else: self.message = "Для постройки этого района нехватает водоснабжения! Постройте новые станции водоснабжения"

            else: self.message =  "Для постройки этого района нехватает электроэнергии! Постройте новые электростанции"

        else: self.message = "Средства города не способны содерждать этот район... Пополните бюджет или увеличьте доход"

    def comm1(self):
        user_city_data = self.city.get_city_data()

        money_cost = 140000
        export_money = 18000

        if user_city_data['Бюджет'] > money_cost:
            user_city_data['Бюджет'] -= money_cost
            user_city_data['Доход'] += export_money

            self.city.write_city_data(user_city_data)

            self.message = openfile("data/city/descrip/create", "create_comm_1")

        else: self.message = "Средства города не способны содерждать этот район... Пополните бюджет или увеличьте доход"

    def comm2(self):
        user_city_data = self.city.get_city_data()

        money_cost = 780000
        export_money = 58000

        if user_city_data['Бюджет'] > money_cost:
            user_city_data['Бюджет'] -= money_cost
            user_city_data['Доход'] += export_money

            self.city.write_city_data(user_city_data)

            self.message = openfile("data/city/descrip/create", "create_comm_2")

        else: self.message = "Средства города не способны содерждать этот район... Пополните бюджет или увеличьте доход"

    def comm3(self):
        user_city_data = self.city.get_city_data()

        money_cost = 2300000
        export_money = 152000

        if user_city_data['Бюджет'] > money_cost:
            user_city_data['Бюджет'] -= money_cost
            user_city_data['Доход'] += export_money

            self.city.write_city_data(user_city_data)

            self.message = openfile("data/city/descrip/create", "create_comm_3")

        else: self.message = "Средства города не способны содерждать этот район... Пополните бюджет или увеличьте доход"

    def ind1_1(self):
        user_city_data = self.city.get_city_data()

        money_cost = 20000
        money_expenses = 4230

        export_energy = 850

        if user_city_data['Бюджет'] > money_cost and (user_city_data['Доход'] - user_city_data['Расходы']) > money_expenses:
            user_city_data['Бюджет'] -= money_cost
            user_city_data['Расходы'] += money_expenses
            user_city_data['Электроэнергия'] += export_energy

            self.city.write_city_data(user_city_data)

            self.message = openfile("data/city/descrip/create", "create_ind_en_1")
            
        else: self.message = "Средства города не способны содерждать этот объект... Пополните бюджет или увеличьте доход"

    def ind1_2(self):
        user_city_data = self.city.get_city_data()

        money_cost = 100000
        money_expenses = 9100

        export_energy = 1850

        if user_city_data['Бюджет'] > money_cost and (user_city_data['Доход'] - user_city_data['Расходы']) > money_expenses:
            user_city_data['Бюджет'] -= money_cost
            user_city_data['Расходы'] += money_expenses
            user_city_data['Электроэнергия'] += export_energy

            self.city.write_city_data(user_city_data)

            self.message = openfile("data/city/descrip/create", "create_ind_en_2")
            
        else: self.message = "Средства города не способны содерждать этот объект... Пополните бюджет или увеличьте доход"

    def ind1_3(self):
        user_city_data = self.city.get_city_data()

        money_cost = 500000
        money_expenses = 19000

        export_energy = 5000

        if user_city_data['Бюджет'] > money_cost and (user_city_data['Доход'] - user_city_data['Расходы']) > money_expenses:
            user_city_data['Бюджет'] -= money_cost
            user_city_data['Расходы'] += money_expenses
            user_city_data['Электроэнергия'] += export_energy

            self.city.write_city_data(user_city_data)

            self.message = openfile("data/city/descrip/create", "create_ind_en_3")

        else: self.message = "Средства города не способны содерждать этот объект... Пополните бюджет или увеличьте доход"

    def ind2_1(self):
        user_city_data = self.city.get_city_data()

        money_cost = 20000
        money_expenses = 2800
        energy_expenses = 2

        export_water = 1480

        if user_city_data['Бюджет'] > money_cost and (user_city_data['Доход'] - user_city_data['Расходы']) > money_expenses:
            if (user_city_data['Электроэнергия'] -user_city_data['Электропотребление']) > energy_expenses:
                
                user_city_data['Бюджет'] -= money_cost
                user_city_data['Расходы'] += money_expenses
                user_city_data['Электропотребление'] += energy_expenses

                user_city_data['Водоснабжение'] += export_water

                self.city.write_city_data(user_city_data)

                self.message = openfile("data/city/descrip/create", "create_ind_wat_1")
                
            else: self.message = "Для постройки этого объекта нехватает электроэнергии! Постройте новые электростанции"

        else: self.message = "Средства города не способны содерждать этот объект... Пополните бюджет или увеличьте доход"

    def ind2_2(self):
        user_city_data = self.city.get_city_data()

        money_cost = 100000
        money_expenses = 5400
        energy_expenses = 4

        export_water = 3200

        if user_city_data['Бюджет'] > money_cost and (user_city_data['Доход'] - user_city_data['Расходы']) > money_expenses:
            if (user_city_data['Электроэнергия'] -user_city_data['Электропотребление']) > energy_expenses:
                user_city_data['Бюджет'] -= money_cost
                user_city_data['Расходы'] += money_expenses
                user_city_data['Электропотребление'] += energy_expenses

                user_city_data['Водоснабжение'] += export_water

                self.city.write_city_data(user_city_data)

                self.message = openfile("data/city/descrip/create", "create_ind_wat_2")
                
            else: self.message = "Для постройки этого объекта нехватает электроэнергии! Постройте новые электростанции"

        else: self.message = "Средства города не способны содерждать этот объект... Пополните бюджет или увеличьте доход"

    def ind2_3(self):
        user_city_data = self.city.get_city_data()

        money_cost = 500000
        money_expenses = 16000
        energy_expenses = 8

        export_water = 7100

        if user_city_data['Бюджет'] > money_cost and (user_city_data['Доход'] - user_city_data['Расходы']) > money_expenses:
            if (user_city_data['Электроэнергия'] -user_city_data['Электропотребление']) > energy_expenses:
                user_city_data['Бюджет'] -= money_cost
                user_city_data['Расходы'] += money_expenses
                user_city_data['Электропотребление'] += energy_expenses

                user_city_data['Водоснабжение'] += export_water

                self.city.write_city_data(user_city_data)

                self.message = openfile("data/city/descrip/create", "create_ind_wat_3")
                
            else: self.message = "Для постройки этого объекта нехватает электроэнергии! Постройте новые электростанции"

        else: self.message = "Средства города не способны содерждать этот объект... Пополните бюджет или увеличьте доход"

    def ind3_1(self):
        user_city_data = self.city.get_city_data()

        money_cost = 160000
        energy_expenses = 5
        water_expenses = 100

        export_money = 8400

        if user_city_data['Бюджет'] > money_cost:
            if (user_city_data['Электроэнергия'] - user_city_data['Электропотребление']) > energy_expenses:
                if (user_city_data['Водоснабжение'] - user_city_data['Водопотребление']) > water_expenses:
                    
                    user_city_data['Бюджет'] -= money_cost
                    user_city_data['Электропотребление'] += energy_expenses
                    user_city_data['Водопотребление'] += water_expenses

                    user_city_data['Доход'] += export_money

                    self.city.write_city_data(user_city_data)

                    self.message = openfile("data/city/descrip/create", "create_ind_mat_1")

                else: self.message = "Для постройки этого района нехватает водоснабжения! Постройте новые станции водоснабжения"

            else: self.message = "Для постройки этого района нехватает электроэнергии! Постройте новые электростанции"

        else: self.message = "Средства города не способны содерждать этот район... Пополните бюджет или увеличьте доход"

    def ind3_2(self):
        user_city_data = self.city.get_city_data()

        money_cost = 1700000
        energy_expenses = 13 
        water_expenses = 400

        export_money = 30100

        if user_city_data['Бюджет'] > money_cost:
            if (user_city_data['Электроэнергия'] - user_city_data['Электропотребление']) > energy_expenses:
                if (user_city_data['Водоснабжение'] - user_city_data['Водопотребление']) > water_expenses:
                    
                    user_city_data['Бюджет'] -= money_cost
                    user_city_data['Электропотребление'] += energy_expenses
                    user_city_data['Водопотребление'] += water_expenses

                    user_city_data['Доход'] += export_money

                    self.city.write_city_data(user_city_data)

                    self.message = openfile("data/city/descrip/create", "create_ind_mat_2")

                else: self.message = "Для постройки этого района нехватает водоснабжения! Постройте новые станции водоснабжения"

            else: self.message = "Для постройки этого района нехватает электроэнергии! Постройте новые электростанции"

        else: self.message = "Средства города не способны содерждать этот район... Пополните бюджет или увеличьте доход"

    def ind3_3(self):
        user_city_data = self.city.get_city_data()

        money_cost = 6350000
        energy_expenses = 25
        water_expenses = 700

        export_money = 185800

        if user_city_data['Бюджет'] > money_cost:
            if (user_city_data['Электроэнергия'] - user_city_data['Электропотребление']) > energy_expenses:
                if (user_city_data['Водоснабжение'] - user_city_data['Водопотребление']) > water_expenses:
                    
                    user_city_data['Бюджет'] -= money_cost
                    user_city_data['Электропотребление'] += energy_expenses
                    user_city_data['Водопотребление'] += water_expenses

                    user_city_data['Доход'] += export_money

                    self.city.write_city_data(user_city_data)

                    self.message = openfile("data/city/descrip/create", "create_ind_mat_3")

                else: self.message = "Для постройки этого района нехватает водоснабжения! Постройте новые станции водоснабжения"

            else: self.message = "Для постройки этого района нехватает электроэнергии! Постройте новые электростанции"

        else: self.message = "Средства города не способны содерждать этот район... Пополните бюджет или увеличьте доход"

import random

class RandomTasks():
    def __init__(self, uid: str):

        self.uid = str(uid)
        self.city = login.City(uid)

        self.house = [
                      'house',
                      'fire',
                      'terrorism',
                      'holiday'
                     ]

        self.weather = [
                        'weather',
                        'hurricane',
                        'flood',
                        'earthshake'
                       ]

        self.type = [self.house, self.weather]

    def generateRandomTask(self):
        self.type = random.choices(self.type, weights=[30, 70])[0]
        if self.type[0] == 'house':
            self.type = [self.type[1], self.type[2], self.type[3]]
            self.task = random.choices(self.type, weights=[30, 10, 60])[0]
        elif self.type[0] == 'weather':
            self.type = [self.type[1], self.type[2], self.type[3]]
            self.task = random.choices(self.type, weights=[20, 40, 40])[0]

        self.type = [self.house, self.weather]

    def taskUpdate(self):
        self.generateRandomTask()

        self.text = "Error"

        user_city = self.city.get_city_info()
        user_city_data = self.city.get_city_data()

        match self.task:

            case "fire":
                self.text = openfile("data/city/descrip", "fire")

                user_city_data['Бюджет'] -= 140000

            case "terrorism":
                self.text = openfile("data/city/descrip", "terrorism")

                user_city['Население'] -= 4000
                user_city_data['Бюджет'] -= 70000

            case "holiday":
                self.text = openfile("data/city/descrip", "holiday")

            case "hurricane":
                self.text = openfile("data/city/descrip", "hurricane")

                user_city['Население'] -= 200
                user_city_data['Бюджет'] -= 80000

            case "flood":
                self.text = openfile("data/city/descrip", "flood")

                user_city_data['Бюджет'] -= 30000

            case "earthshake":
                self.text = openfile("data/city/descrip", "earthshake")

                user_city_data['Бюджет'] -= 100000

        self.city.write_city_profile(user_city)
        self.city.write_city_data(user_city_data)

class Admins():
    def __init__(self, update, context):
        self.update = update
        self.context = context

        self.active_user = login.User(str(update.message.chat_id)).get_user_control()

    def ban(self):

        self.command, self.uid = self.update.message.text.split(" ")
        self.user = login.User(str(self.uid)).get_user_control()

        if self.active_user['admin']:
            self.active_user = self.update.message.chat_id
            self.user['ban'] = 1

            login.User(self.uid).write_user_control(self.user)

            self.update.message.reply_text(f"User: {self.uid} banned. Admin: {str(self.active_user)}")
            self.context.bot.send_message(chat_id=-1001955905639,
                                          text=f"User: {self.uid} banned. Admin: {str(self.active_user)}")
        else: self.update.message.reply_text("You are not admin")

    def unban(self):

        self.command, self.uid = self.update.message.text.split(" ")
        self.user = login.User(str(self.uid)).get_user_control()

        if self.active_user['admin']:
            self.active_user = self.update.message.chat_id
            self.user['ban'] = 0

            login.User(self.uid).write_user_control(self.user)

            self.update.message.reply_text(f"User: {self.uid} unbanned. Admin: {str(self.active_user)}")
            self.context.bot.send_message(chat_id=-1001955905639,
                                          text=f"User: {self.uid} unbanned. Admin: {str(self.active_user)}")
        else: self.update.message.reply_text("You are not admin")

    def addbeta(self):

        self.command, self.uid = self.update.message.text.split(" ")
        self.user = login.User(str(self.uid)).get_user_control()

        if self.active_user['admin']:
            self.active_user = self.update.message.chat_id
            self.user['beta'] = 1

            login.User(self.uid).write_user_control(self.user)

            self.update.message.reply_text(f"User: {self.uid} added to beta-test. Admin: {str(self.active_user)}")
            self.context.bot.send_message(chat_id=-1001955905639,
                                          text=f"User: {self.uid} added to beta-test. Admin: {str(self.active_user)}")
        else: self.update.message.reply_text("You are not admin")

    def delbeta(self):

        self.command, self.uid = self.update.message.text.split(" ")
        self.user = login.User(str(self.uid)).get_user_control()

        if self.active_user['admin']:
            self.active_user = self.update.message.chat_id
            self.user['beta'] = 0

            login.User(self.uid).write_user_control(self.user)

            self.update.message.reply_text(f"User: {self.uid} delete from beta-test. Admin: {str(self.active_user)}")
            self.context.bot.send_message(chat_id=-1001955905639,
                                          text=f"User: {self.uid} delete from beta-test. Admin: {str(self.active_user)}")
        else: self.update.message.reply_text("You are not admin")

    def message(self):
        if self.active_user['admin']:
            if " : " in self.update.message.text:
                command, text = self.update.message.text.split(":")

                users = login.users_profile_info()
                for i in users:
                    self.context.bot.send_message(chat_id=str(i), text=text)
            else:
                self.context.bot.send_message(chat_id=-1001955905639,
                                              text=f"Admin: {str(self.update.message.chat_id)} wrong send_message")
        else: self.update.message.reply_text("You are not admin")
        
    def wordly(self):
        if self.active_user['admin']:
            if " : " in self.update.message.text:
                command, word_id = self.update.message.text.split(" : ")
                from wordly import Wordly
                classW = Wordly(str(self.update.message.chat_id))
                classW.set_word(word_id)
                self.context.bot.send_message(chat_id=-1001955905639,
                                              text=f"Word was setted --> {word_id}")
            else:
                self.context.bot.send_message(chat_id=-1001955905639,
                                              text=f"Admin: {str(self.update.message.chat_id)} wrong wordly_day_change")
        else: self.update.message.reply_text("You are not admin")
        
    def Gvip(self):
        if self.active_user['admin']:
            self.command, self.uid = self.update.message.text.split(" ")
            self.user = login.User(str(self.uid)).get_user_profile()
            
            self.active_user = self.update.message.chat_id
            self.user['VIP'] = "Есть"

            login.User(self.uid).write_user_profile(self.user)

            self.update.message.reply_text(f"User: {self.uid} gived VIP. Admin: {str(self.active_user)}")
            self.context.bot.send_message(chat_id=-1001955905639,
                                          text=f"User: {self.uid} gived VIP. Admin: {str(self.active_user)}")
        else: self.update.message.reply_text("You are not admin")
        
    def Dvip(self):
        if self.active_user['admin']:
            self.command, self.uid = self.update.message.text.split(" ")
            self.user = login.User(str(self.uid)).get_user_profile()
            
            self.active_user = self.update.message.chat_id
            self.user['VIP'] = "None"

            login.User(self.uid).write_user_profile(self.user)

            self.update.message.reply_text(f"User: {self.uid} lost VIP. Admin: {str(self.active_user)}")
            self.context.bot.send_message(chat_id=-1001955905639,
                                          text=f"User: {self.uid} lost VIP. Admin: {str(self.active_user)}")
        else: self.update.message.reply_text("You are not admin")

def admin(update, context):
    admin = Admins(update, context)

    if '/message' in update.message.text: admin.message()
    elif '/givevip' in update.message.text: admin.Gvip()
    elif '/delvip' in update.message.text: admin.Dvip()
    elif '/wordly' in update.message.text: admin.wordly()
    elif '/ban' in update.message.text: admin.ban()
    elif '/unban' in update.message.text: admin.unban()
    elif '/addbeta' in update.message.text: admin.addbeta()
    elif '/delbeta' in update.message.text: admin.delbeta()

from echo import echo

def checkbeta(update, context, user):
    try:
        if not user['beta']:
            update.message.reply_text("You are not member beta-test!! If you want to test this bot --> buy VIP")
            context.bot.send_message(chat_id=-1001955905639,
                                     text=f"User: {str(update.message.chat['username'])} trying to use bot... (not member beta-test)")
            return True
    except:
        if not user['beta']:
            update.callback_query.message.reply_text("You are not member beta-test!! If you want to test this bot --> buy VIP")
            context.bot.send_message(chat_id=-1001955905639,
                                     text=f"User: {str(update.callback_query.message.chat['username'])} trying to use bot... (not member beta-test)")
            return True
    return False

def checkban(update, context):
    echo(update, context)
    callback = False
    inline = False

    try:
        user, callback = login.User(str(update.callback_query.message.chat_id)).get_user_control(), True
        if user is None: 
            login.User(str(update.callback_query.message.chat_id)).authorize()
            user = login.User(str(update.callback_query.message.chat_id)).get_user_control()

    except:

        try:
            user = login.User(str(update.message.chat_id)).get_user_control()
            if user is None: 
                login.User(str(update.message.chat_id)).authorize()
                user = login.User(str(update.message.chat_id)).get_user_control()

        except:
            user, inline = login.User(str(update.inline_query.from_user.id)).get_user_control(), True
            if user is None: 
                login.User(str(update.inline_query.from_user_id)).authorize()
                user = login.User(str(update.inline_query.from_user_id)).get_user_control()

    if not callback and not inline:
        if user['ban']:
            update.message.reply_text("You are banned in this place")
            context.bot.send_message(chat_id=-1001955905639,
                                     text=f"User: {str(update.message.chat['username'])} trying to use bot... (banned)")
            return True

        elif checkbeta(update, context, user): return True
        else: return False

    elif inline:
        if update != None:
            
            if user['ban']: return True
            elif not user['beta']: return True
            else: return False

        else: return False

    elif callback:
        if user['ban']:
            update.callback_query.message.reply_text("You are banned in this place")
            context.bot.send_message(chat_id=-1001955905639,
                                     text=f"User: {str(update.callback_query.message.chat['username'])} trying to use bot... (banned)")
            return True

        elif checkbeta(update, context, user): return True
        else: return False

def check_acces(func):
    def _checker(update, context):
        if checkban(update, context): return
        else: func(update, context)
    return _checker