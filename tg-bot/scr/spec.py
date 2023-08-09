# -*- coding: utf-8 -*-
def openfile(path: str, name: str, method: int = 0):
    if method:
        with open(path + "/" + name + ".txt", "r", encoding="utf-8") as f: return "\n".join(f.readlines(0))
    if path != "":
        with open(path + "/" + name + ".txt", "r", encoding="utf-8") as f: return "".join(f.readlines(0))
    else:
        with open(name + ".txt", "r", encoding="utf-8") as f: return "".join(f.readlines(0))

def convert_int(data: dict):
    for i in data.keys(): data[i] = int(data[i])
    return data

import login
import urllib.request
import keyboardbot as kb

from telegram import InlineKeyboardMarkup

def raiting(update, context):
    uid = str(update.callback_query.message.chat_id)
    user = login.User(uid).get_user_profile()

    return update.callback_query.message.reply_text("Ваш рейтинг: " + str(user['Рейтинг']),
                                             reply_markup = InlineKeyboardMarkup(kb.profile_back)).message_id

class Echo_Checker():
    def __init__(self, update, context):
        self.update = update
        self.context = context
        if self.update.message.text is not None:
            self.prefix, *self.text = self.update.message.text.split(" ")
            if len(self.text) == 3: self.update.message.text = self.text[2]

        self.uid = str(self.update.message.chat_id)

        self.user = InlineKeyboardMarkup(kb.profile_back)
        self.citykb = InlineKeyboardMarkup(kb.backcity)

        self.city = login.City(self.uid)

        self.city_status = {
            'cityname':'0',
            'sign':'0',
            'gymn':'0',
            'history':'0',
            'mayor':'0'
            }

        self.user_status = {
            'nickname':'0',
            'name':'0',
            'birthday':'0',
            'buisness':'0'
            }

        self.old_data = None

        self.message = "Error"
        self.reply_markup = InlineKeyboardMarkup(kb.back)
   
    def write_mark(self):
        stat = login.authorize(self.uid)
        if stat['marks_collect'] == 0 or self.update.message.text is not None: return False
        marks_id_memory = []

        with open("menu/faq/ypiter/marks/memory.txt", "r", encoding="utf-8") as file:
            file = file.readlines()
            for i in file: marks_id_memory.append(i.replace("\n", ""))
        if self.uid in marks_id_memory:
            self.message = "Вы уже отправляли рецензию!"
            return True
        if stat['marks_collect'] > 0 and stat['marks_collect'] < 5:
            user_text = openfile("base", self.uid + "marks")

            if stat['marks_collect'] == 1:
                with open("base/" + self.uid + "marks.txt", "w+", encoding="utf-8") as f: f.write(user_text + self.update.message.text + "\n")
                self.message = openfile("menu/faq/ypiter/marks", "marks2")

            elif stat['marks_collect'] == 2:
                with open("base/" + self.uid + "marks.txt", "w+", encoding="utf-8") as f: f.write(user_text + self.update.message.text + "\n")
                self.message = openfile("menu/faq/ypiter/marks", "marks3")

            elif stat['marks_collect'] == 3:
                if self.update.message.text.lower() == "да":
                    self.message = openfile("menu/faq/ypiter/marks", "marks4_5")
                    stat['marks_collect'] = stat['marks_collect'] + 1
                elif self.update.message.text.lower() == "нет":
                    self.message = openfile("menu/faq/ypiter/marks", "marks4")

            if stat['marks_collect'] == 4:
                self.message = str(openfile("menu/faq/ypiter/marks", "marks_complete") + "\n" +
                    openfile("base", self.uid + "marks") + "\nХотите изменить?(Да/нет)")
            stat['marks_collect'] = stat['marks_collect'] + 1
            login.update(self.update.message.chat_id, stat)
            return True

        if stat['marks_collect'] == 5:
            if self.update.message.text.lower() == "да":
                stat['marks_collect'] = 1
                login.update(self.uid, stat)
                self.write_mark
                return True
            elif self.update.message.text.lower() == "нет":
                stat['marks_collect'] = 0
                login.update(self.uid, stat)
                with open("menu/faq/ypiter/marks/memory.txt", "w", encoding="utf-8") as file:
                    marks_id_memory.append(str(self.update.message.chat_id))
                    for i in range(len(marks_id_memory)):
                        if i != len(marks_id_memory): file.write(marks_id_memory[i] + "\n")
                        else: file.write(marks_id_memory[i])
                with open("base/"+ self.uid +"marks.txt", "w", encoding="utf-8") as file: file.write(" ")
                self.message = openfile("menu/faq/ypiter/marks", "markssucces")
                return False
            
        return False

    def write_user(self):
        User = login.User(self.uid)
        user_profile = User.get_user_profile()
        user_status = User.get_user_status()
        if self.text is not None: new_data = self.text.replace("\n", "")

        if user_status['nickname']:
            self.old_data = user_profile['Никнейм']
            user_profile['Никнейм'] = new_data

        elif user_status['name']:
            self.old_data = user_profile['Имя']
            user_profile['Имя'] = new_data

        elif user_status['birthday']:
            self.old_data = user_profile['День рождения']
            user_profile['День рождения'] = new_data

        elif user_status['buisness']:
            self.old_data = user_profile['Интересы']
            user_profile['Интересы'] = new_data

        else: return False

        User.write_user_profile(user_profile)
        User.write_user_status(self.user_status)

        self.message = "Данные успешно обновлены!\n\n" + self.old_data + " >>> " + new_data
        self.reply_markup = self.user
        return True

    def write_city(self):
        user_city = self.city.get_city_info()
        user_city_status = self.city.get_city_status()
        if self.text is not None: new_data = self.text.replace("\n", "").replace(",", "‚")

        if user_city_status is None: return False

        if user_city_status['cityname']:
            self.old_data = user_city['Имя']
            user_city['Имя'] = new_data

        elif user_city_status['sign'] == 1 and self.text is None:

            file = self.context.bot.get_file(self.update.message.photo[-1])
            file_size = self.update.message.photo[-1]

            if file_size.width <= 400 and file_size.height <= 400:
                user_city['Герб'] = "Есть"

                response = urllib.request.urlopen(file.file_path)
                with open("base/cities/photo/" + self.uid + "city.jpg", 'wb') as new_file: new_file.write(response.read())
                self.message = "Данные успешно обновлены!"
            else:
                self.message = "Размеры файла превышают максимальные! (400x400)"
                return False

        elif user_city_status['gymn']: user_city['Гимн'] = new_data
        elif user_city_status['history']: user_city['История'] = new_data
        elif user_city_status['mayor']: user_city['Мэр'] = new_data

        else: return False

        self.city.write_city_profile(user_city)
        self.city.write_city_status(user_city_status)

        self.message = "Данные успешно обновлены!"
        self.reply_markup = self.citykb

        if self.old_data is not None: self.message = "Данные успешно обновлены!\n\n" + self.old_data + " >>> " + new_data
        
        return True

    def echo_check(self):
        self.text = self.update.message.text

        if self.write_user(): return True
        elif self.write_city(): return True
        #elif self.write_mark(): return True

        else: return False

class Status_changer():
    def __init__(self, update, context):
        self.update = update
        self.context = context

        self.uid = str(self.update.callback_query.message.chat_id)

        self.user_data_list = ['nickname', 'name', 'buisness', 'birthday']
        self.city_data_list = ['cityname', 'sign', 'gymn', 'history', 'mayor']

        self.user_status = {
            'nickname':'0',
            'name':'0',
            'birthday':'0',
            'buisness':'0'
            }

        self.city_status = {
            'cityname':'0',
            'sign':'0',
            'gymn':'0',
            'history':'0',
            'mayor':'0'
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

    def house1(self):
        user_city = self.city.get_city_info()
        user_city_data = self.city.get_city_data()

        money_cost = 500000
        money_expenses = 67200
        energy_expenses = 400
        water_expenses = 1200

        export_people = 4000
        
        user_city['Население'] = int(user_city['Население'])

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

                    self.update.callback_query.message.reply_text(openfile("data/city/descrip/create", "create_house_1"),
                                                                  reply_markup=InlineKeyboardMarkup(kb.backcity))
                else:
                    self.update.callback_query.message.reply_text("Для постройки этого района нехватает водоснабжения! Постройте новые станции водоснабжения", 
                                                          reply_markup=InlineKeyboardMarkup(kb.backcity))
            else:
                self.update.callback_query.message.reply_text("Для постройки этого района нехватает электроэнергии! Постройте новые электростанции", 
                                                          reply_markup=InlineKeyboardMarkup(kb.backcity))
        else:
            self.update.callback_query.message.reply_text("Средства города не способны содерждать этот район... Пополните бюджет или увеличьте доход", 
                                                          reply_markup=InlineKeyboardMarkup(kb.backcity))

    def house2(self):
        user_city = self.city.get_city_info()
        user_city_data = self.city.get_city_data()

        money_cost = 1500000
        money_expenses = 151200
        energy_expenses = 900
        water_expenses = 2700

        export_people = 9000
        
        user_city['Население'] = int(user_city['Население'])

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

                    self.update.callback_query.message.reply_text(openfile("data/city/descrip/create", "create_house_2"),
                                                                  reply_markup=InlineKeyboardMarkup(kb.backcity))
                else:
                    self.update.callback_query.message.reply_text("Для постройки этого района нехватает водоснабжения! Постройте новые станции водоснабжения", 
                                                          reply_markup=InlineKeyboardMarkup(kb.backcity))
            else:
                self.update.callback_query.message.reply_text("Для постройки этого района нехватает электроэнергии! Постройте новые электростанции", 
                                                          reply_markup=InlineKeyboardMarkup(kb.backcity))
        else:
            self.update.callback_query.message.reply_text("Средства города не способны содерждать этот район... Пополните бюджет или увеличьте доход", 
                                                          reply_markup=InlineKeyboardMarkup(kb.backcity))

    def house3(self):
        user_city = self.city.get_city_info()
        user_city_data = self.city.get_city_data()

        money_cost = 3500000
        money_expenses = 336000
        energy_expenses = 2000
        water_expenses = 6000

        export_people = 20000
        
        user_city['Население'] = int(user_city['Население'])

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

                    self.update.callback_query.message.reply_text(openfile("data/city/descrip/create", "create_house_3"),
                                                                  reply_markup=InlineKeyboardMarkup(kb.backcity))
                else:
                    self.update.callback_query.message.reply_text("Для постройки этого района нехватает водоснабжения! Постройте новые станции водоснабжения", 
                                                          reply_markup=InlineKeyboardMarkup(kb.backcity))
            else:
                self.update.callback_query.message.reply_text("Для постройки этого района нехватает электроэнергии! Постройте новые электростанции", 
                                                          reply_markup=InlineKeyboardMarkup(kb.backcity))
        else:
            self.update.callback_query.message.reply_text("Средства города не способны содерждать этот район... Пополните бюджет или увеличьте доход", 
                                                          reply_markup=InlineKeyboardMarkup(kb.backcity))

    def comm1(self):
        user_city_data = self.city.get_city_data()

        money_cost = 140000
        export_money = 18000

        if user_city_data['Бюджет'] > money_cost:
            user_city_data['Бюджет'] -= money_cost
            user_city_data['Доход'] += export_money

            self.city.write_city_data(user_city_data)

            self.update.callback_query.message.reply_text(openfile("data/city/descrip/create", "create_comm_1"),
                                                            reply_markup=InlineKeyboardMarkup(kb.backcity))
        else:
            self.update.callback_query.message.reply_text("Средства города не способны содерждать этот район... Пополните бюджет или увеличьте доход", 
                                                          reply_markup=InlineKeyboardMarkup(kb.backcity))

    def comm2(self):
        user_city_data = self.city.get_city_data()

        money_cost = 780000
        export_money = 58000

        if user_city_data['Бюджет'] > money_cost:
            user_city_data['Бюджет'] -= money_cost
            user_city_data['Доход'] += export_money

            self.city.write_city_data(user_city_data)

            self.update.callback_query.message.reply_text(openfile("data/city/descrip/create", "create_comm_2"),
                                                            reply_markup=InlineKeyboardMarkup(kb.backcity))
        else:
            self.update.callback_query.message.reply_text("Средства города не способны содерждать этот район... Пополните бюджет или увеличьте доход", 
                                                          reply_markup=InlineKeyboardMarkup(kb.backcity))

    def comm3(self):
        user_city_data = self.city.get_city_data()

        money_cost = 2300000
        export_money = 152000

        if user_city_data['Бюджет'] > money_cost:
            user_city_data['Бюджет'] -= money_cost
            user_city_data['Доход'] += export_money

            self.city.write_city_data(user_city_data)

            self.update.callback_query.message.reply_text(openfile("data/city/descrip/create", "create_comm_3"),
                                                            reply_markup=InlineKeyboardMarkup(kb.backcity))
        else:
            self.update.callback_query.message.reply_text("Средства города не способны содерждать этот район... Пополните бюджет или увеличьте доход", 
                                                          reply_markup=InlineKeyboardMarkup(kb.backcity))

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

            self.update.callback_query.message.reply_text(openfile("data/city/descrip/create", "create_ind_en_1"),
                                                            reply_markup=InlineKeyboardMarkup(kb.backcity))
        else:
            self.update.callback_query.message.reply_text("Средства города не способны содерждать этот объект... Пополните бюджет или увеличьте доход", 
                                                          reply_markup=InlineKeyboardMarkup(kb.backcity))

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

            self.update.callback_query.message.reply_text(openfile("data/city/descrip/create", "create_ind_en_2"),
                                                            reply_markup=InlineKeyboardMarkup(kb.backcity))
        else:
            self.update.callback_query.message.reply_text("Средства города не способны содерждать этот объект... Пополните бюджет или увеличьте доход", 
                                                          reply_markup=InlineKeyboardMarkup(kb.backcity))

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

            self.update.callback_query.message.reply_text(openfile("data/city/descrip/create", "create_ind_en_3"),
                                                            reply_markup=InlineKeyboardMarkup(kb.backcity))
        else:
            self.update.callback_query.message.reply_text("Средства города не способны содерждать этот объект... Пополните бюджет или увеличьте доход", 
                                                          reply_markup=InlineKeyboardMarkup(kb.backcity))

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

                self.update.callback_query.message.reply_text(openfile("data/city/descrip/create", "create_ind_wat_1"),
                                                            reply_markup=InlineKeyboardMarkup(kb.backcity))
            else:
                self.update.callback_query.message.reply_text("Для постройки этого объекта нехватает электроэнергии! Постройте новые электростанции",
                                                              reply_markup=InlineKeyboardMarkup(kb.backcity))
        else:
            self.update.callback_query.message.reply_text("Средства города не способны содерждать этот объект... Пополните бюджет или увеличьте доход", 
                                                          reply_markup=InlineKeyboardMarkup(kb.backcity))

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

                self.update.callback_query.message.reply_text(openfile("data/city/descrip/create", "create_ind_wat_2"),
                                                            reply_markup=InlineKeyboardMarkup(kb.backcity))
            else:
                self.update.callback_query.message.reply_text("Для постройки этого объекта нехватает электроэнергии! Постройте новые электростанции",
                                                              reply_markup=InlineKeyboardMarkup(kb.backcity))
        else:
            self.update.callback_query.message.reply_text("Средства города не способны содерждать этот объект... Пополните бюджет или увеличьте доход", 
                                                          reply_markup=InlineKeyboardMarkup(kb.backcity))

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

                self.update.callback_query.message.reply_text(openfile("data/city/descrip/create", "create_ind_wat_3"),
                                                            reply_markup=InlineKeyboardMarkup(kb.backcity))
            else:
                self.update.callback_query.message.reply_text("Для постройки этого объекта нехватает электроэнергии! Постройте новые электростанции",
                                                              reply_markup=InlineKeyboardMarkup(kb.backcity))
        else:
            self.update.callback_query.message.reply_text("Средства города не способны содерждать этот объект... Пополните бюджет или увеличьте доход", 
                                                          reply_markup=InlineKeyboardMarkup(kb.backcity))

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

                    self.update.callback_query.message.reply_text(openfile("data/city/descrip/create", "create_ind_mat_1"),
                                                                  reply_markup=InlineKeyboardMarkup(kb.backcity))
                else:
                    self.update.callback_query.message.reply_text("Для постройки этого района нехватает водоснабжения! Постройте новые станции водоснабжения",
                                                                  reply_markup=InlineKeyboardMarkup(kb.backcity))
            else:
                self.update.callback_query.message.reply_text("Для постройки этого района нехватает электроэнергии! Постройте новые электростанции",
                                                              reply_markup=InlineKeyboardMarkup(kb.backcity))
        else:
            self.update.callback_query.message.reply_text("Средства города не способны содерждать этот район... Пополните бюджет или увеличьте доход", 
                                                          reply_markup=InlineKeyboardMarkup(kb.backcity))

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

                    self.update.callback_query.message.reply_text(openfile("data/city/descrip/create", "create_ind_mat_2"),
                                                                  reply_markup=InlineKeyboardMarkup(kb.backcity))
                else:
                    self.update.callback_query.message.reply_text("Для постройки этого района нехватает водоснабжения! Постройте новые станции водоснабжения",
                                                                  reply_markup=InlineKeyboardMarkup(kb.backcity))
            else:
                self.update.callback_query.message.reply_text("Для постройки этого района нехватает электроэнергии! Постройте новые электростанции",
                                                              reply_markup=InlineKeyboardMarkup(kb.backcity))
        else:
            self.update.callback_query.message.reply_text("Средства города не способны содерждать этот район... Пополните бюджет или увеличьте доход", 
                                                          reply_markup=InlineKeyboardMarkup(kb.backcity))

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

                    self.update.callback_query.message.reply_text(openfile("data/city/descrip/create", "create_ind_mat_3"),
                                                                  reply_markup=InlineKeyboardMarkup(kb.backcity))
                else:
                    self.update.callback_query.message.reply_text("Для постройки этого района нехватает водоснабжения! Постройте новые станции водоснабжения",
                                                                  reply_markup=InlineKeyboardMarkup(kb.backcity))
            else:
                self.update.callback_query.message.reply_text("Для постройки этого района нехватает электроэнергии! Постройте новые электростанции",
                                                              reply_markup=InlineKeyboardMarkup(kb.backcity))
        else:
            self.update.callback_query.message.reply_text("Средства города не способны содерждать этот район... Пополните бюджет или увеличьте доход", 
                                                          reply_markup=InlineKeyboardMarkup(kb.backcity))

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
        
        user_city['Население'] = int(user_city['Население'])

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

        self.command, self.uid = self.update.message.text.split(" ")

        self.user = login.User(str(self.uid)).get_user_control()
        self.active_user = login.User(str(update.message.chat_id)).get_user_control()

    def ban(self):
        if self.active_user['admin']:
            self.active_user = self.update.message.chat_id
            self.user['ban'] = 1

            login.User(self.uid).write_user_control(self.user)

            self.update.message.reply_text("User: " + self.uid + " banned. Admin: " + str(self.active_user))
            self.context.bot.send_message(chat_id=-1001955905639,
                                          text="User: " + self.uid + " banned. Admin: " + str(self.active_user))
        else: self.update.message.reply_text("You are not admin")

    def unban(self):
        if self.active_user['admin']:
            self.active_user = self.update.message.chat_id
            self.user['ban'] = 0

            login.User(self.uid).write_user_control(self.user)

            self.update.message.reply_text("User: " + self.uid + " unbanned. Admin: " + str(self.active_user))
            self.context.bot.send_message(chat_id=-1001955905639,
                                          text="User: " + self.uid + " unbanned. Admin: " + str(self.active_user))
        else: self.update.message.reply_text("You are not admin")

    def addbeta(self):
        if self.active_user['admin']:
            self.active_user = self.update.message.chat_id
            self.user['beta'] = 1

            login.User(self.uid).write_user_control(self.user)

            self.update.message.reply_text("User: " + self.uid + " added to beta-test. Admin: " + str(self.active_user))
            self.context.bot.send_message(chat_id=-1001955905639,
                                          text="User: " + self.uid + " added to beta-test. Admin: " + str(self.active_user))
        else: self.update.message.reply_text("You are not admin")

    def delbeta(self):
        if self.active_user['admin']:
            self.active_user = self.update.message.chat_id
            self.user['beta'] = 0

            login.User(self.uid).write_user_control(self.user)

            self.update.message.reply_text("User: " + self.uid + " delete from beta-test. Admin: " + str(self.active_user))
            self.context.bot.send_message(chat_id=-1001955905639,
                                          text="User: " + self.uid + " delete from beta-test. Admin: " + str(self.active_user))
        else: self.update.message.reply_text("You are not admin")

def admin(update, context):
    admin = Admins(update, context)

    if '/ban' in update.message.text: admin.ban()
    elif '/unban' in update.message.text: admin.unban()
    elif '/addbeta' in update.message.text: admin.addbeta()
    elif '/delbeta' in update.message.text: admin.delbeta()

from echo import echo

def checkbeta(update, context, user):
    try:
        if not user['beta']:
            update.message.reply_text("You are not member beta-test!! If you want to test this bot --> @r_ypiter")
            context.bot.send_message(chat_id=-1001955905639, text="User: " + str(update.message.chat['username']) + " trying to use bot... (not member beta-test)")
            return True
    except:
        if not user['beta']:
            update.callback_query.message.reply_text("You are not member beta-test!! If you want to test this bot --> @r_ypiter")
            context.bot.send_message(chat_id=-1001955905639, text="User: " + str(update.callback_query.message.chat['username']) + " trying to use bot... (not member beta-test)")
            return True
    return False

def checkban(update, context):
    echo(update, context)
    callback = False
    inline = False

    try:
        user, callback = login.User(str(update.callback_query.message.chat_id)).get_user_control(), True
        if user is None: user = login.User(str(update.callback_query.message.chat_id)).authorize()

    except:

        try:
            user = login.User(str(update.message.chat_id)).get_user_control()
            if user is None: user = login.User(str(update.message.chat_id)).authorize()

        except:
            user, inline = login.User(str(update.inline_query.from_user_id)).get_user_control(), True
            if user is None: user = login.User(str(update.inline_query.from_user_id)).authorize()

    if not callback and not inline:
        if user['ban']:
            update.message.reply_text("You are banned in this place")
            context.bot.send_message(chat_id=-1001955905639, text="User: " + str(update.message.chat['username']) + " trying to use bot... (banned)")
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
            context.bot.send_message(chat_id=-1001955905639, text="User: " + str(update.callback_query.message.chat['username']) + " trying to use bot... (banned)")
            return True

        elif checkbeta(update, context, user): return True
        else: return False

def check_acces(func):
    def _checker(update, context):
        if checkban(update, context): return
        else: func(update, context)
    return _checker