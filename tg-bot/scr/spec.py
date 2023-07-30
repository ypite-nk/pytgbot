﻿# -*- coding: utf-8 -*-
def openf(path, name, method: int = 0):
    if method:
        with open(path + "/" + name + ".txt", "r", encoding="utf-8") as f:
            return "\n".join(f.readlines(0))
    if path != "":
        with open(path + "/" + name + ".txt", "r", encoding="utf-8") as f:
            return "".join(f.readlines(0))
    else:
        with open(name + ".txt", "r", encoding="utf-8") as f:
            return "".join(f.readlines(0))

def convert_int(data: dict):
    for i in data.keys():
        data[i] = int(data[i])
    return data

import login
import keyboardbot as kb

from telegram import InlineKeyboardMarkup
from urllib.request import request as r

class Echo_Checker():
    def __init__(self, update, context):
        self.update = update
        self.context = context

        self.prefix, *self.text = self.update.message.text.split(" ")

        if len(self.text) == 3:
            self.update.message.text = self.text[2]

        self.uid = str(self.update.message.chat_id)

        self.user = InlineKeyboardMarkup(kb.profile)
        self.city = InlineKeyboardMarkup(kb.backcity)

        self.city_status = {
            'name':'0',
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
            user_text = openf("base", self.uid + "marks")

            if stat['marks_collect'] == 1:
                with open("base/" + self.uid + "marks.txt", "w+", encoding="utf-8") as f: f.write(user_text + self.update.message.text + "\n")
                self.message = openf("menu/faq/ypiter/marks", "marks2")

            elif stat['marks_collect'] == 2:
                with open("base/" + self.uid + "marks.txt", "w+", encoding="utf-8") as f: f.write(user_text + self.update.message.text + "\n")
                self.message = openf("menu/faq/ypiter/marks", "marks3")

            elif stat['marks_collect'] == 3:
                if self.update.message.text.lower() == "да":
                    self.message = openf("menu/faq/ypiter/marks", "marks4_5")
                    stat['marks_collect'] = stat['marks_collect'] + 1
                elif self.update.message.text.lower() == "нет":
                    self.message = openf("menu/faq/ypiter/marks", "marks4")

            if stat['marks_collect'] == 4:
                self.message = str(openf("menu/faq/ypiter/marks", "marks_complete") + "\n" +
                    openf("base", self.uid + "marks") + "\nХотите изменить?(Да/нет)")
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
                self.message = openf("menu/faq/ypiter/marks", "markssucces")
                return False

        return False

    def clear_user_status(self):
        login.user_status_change(self.uid, self.user_status)

    def write_user(self):
        user_profile = login.user(self.uid)
        user_status = login.user_status(self.uid)

        new_data = self.text

        if user_status['nickname']:
            old_data = user_profile['Никнейм']
            user_profile['Никнейм'] = new_data

        elif user_status['name']:
            old_data = user_profile['Имя']
            user_profile['Имя'] = new_data

        elif user_status['birthday']:
            old_data = user_profile['День рождения']
            user_profile['День рождения'] = new_data

        elif user_status['buisness']:
            old_data = user_profile['Интересы']
            user_profile['Интересы'] = new_data
        else:
            return False

        login.user_change(self.uid, user_profile)
        self.clear_user_status()

        self.message = "Данные успешно обновлены!\n\n" + old_data + " >>> " + new_data
        self.reply_markup = self.user
        return True

    def clear_city_status(self):
        login.city_status_change(self.uid, self.city_status)

    def write_city(self):
        user_city = login.authorize_city(self.uid)
        user_city_status = login.city_status(self.uid)

        new_data = self.update.message.text

        if user_city_status is None: return False

        if user_city_status['name']:
            old_data = user_city['name']
            user_city['name'] = self.text

        elif user_city_status['sign'] == 1 and self.update.message.text is None:
            old_data = None

            file = self.context.bot.get_file(self.update.message.photo[-1])
            file_size = self.update.message.photo[-1]

            if file_size.width <= 400 and file_size.height <= 400:
                user_city['sign'] = "Есть"
                with open("base/cities/photo/" + self.uid + "city.jpg", 'wb') as new_file: new_file.write(r.urlopen(file.file_path).read())
                
            else:
                self.message = "Размеры файла превышают максимальные! (400x400)"
                return False

        elif user_city_status['gymn']: user_city['gymn'] = self.text
        
        elif user_city_status['history']: user_city['history'] = self.text
        
        elif user_city_status['mayor']: user_city['mayor'] = self.text

        else: return False

        login.city_change(self.uid, user_city)
        self.clear_city_status()

        if old_data is not None: self.message = "Данные успешно обновлены!\n\n" + old_data + " >>> " + new_data
        
        else: self.message = "Данные успешно обновлены!"
        
        self.reply_markup = self.city
        return True

    def echo_check(self):
        self.text = self.update.message.text

        if self.text is None: return True

        if self.write_user(): return True
        if self.write_city(): return True
        if self.write_mark(): return True

        else: return False

import random

class Create():
    def __init__(self, update, context):
        self.update = update
        self.context = context

        self.uid = str(self.update.callback_query.message.chat_id)

    def house1(self):
        user_city = login.authorize_city(self.uid)
        user_city_data = convert_int(login.city_data(self.uid))

        money_cost = 500000
        money_expenses = 67200
        energy_expenses = 400
        water_expenses = 1200

        export_people = 4000
        
        user_city['people'] = int(user_city['people'])

        if user_city_data['money_have'] > money_cost and (user_city_data['money'] - user_city_data['money_need']) > money_expenses:
            if (user_city_data['energy_have'] - user_city_data['energy_need']) > energy_expenses:
                if (user_city_data['water_have'] - user_city_data['water_need']) > water_expenses:
                    
                    user_city_data['money_have'] -= money_cost
                    user_city_data['money_need'] += money_expenses
                    user_city_data['energy_need'] += energy_expenses
                    user_city_data['water_need'] += water_expenses

                    user_city['people'] += export_people

                    login.city_data_change(self.uid, user_city_data)
                    login.city_change(self.uid, user_city)

                    self.update.callback_query.message.reply_text(openf("data/city/descrip/create", "create_house_1"),
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
        user_city = login.authorize_city(self.uid)
        user_city_data = convert_int(login.city_data(self.uid))

        money_cost = 1500000
        money_expenses = 151200
        energy_expenses = 900
        water_expenses = 2700

        export_people = 9000
        
        user_city['people'] = int(user_city['people'])

        if user_city_data['money_have'] > money_cost and (user_city_data['money'] - user_city_data['money_need']) > money_expenses:
            if (user_city_data['energy_have'] - user_city_data['energy_need']) > energy_expenses:
                if (user_city_data['water_have'] - user_city_data['water_need']) > water_expenses:
                    
                    user_city_data['money_have'] -= money_cost
                    user_city_data['money_need'] += money_expenses
                    user_city_data['energy_need'] += energy_expenses
                    user_city_data['water_need'] += water_expenses

                    user_city['people'] += export_people

                    login.city_data_change(self.uid, user_city_data)
                    login.city_change(self.uid, user_city)

                    self.update.callback_query.message.reply_text(openf("data/city/descrip/create", "create_house_2"),
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
        user_city = login.authorize_city(self.uid)
        user_city_data = convert_int(login.city_data(self.uid))

        money_cost = 3500000
        money_expenses = 336000
        energy_expenses = 2000
        water_expenses = 6000

        export_people = 20000
        
        user_city['people'] = int(user_city['people'])

        if user_city_data['money_have'] > money_cost and (user_city_data['money'] - user_city_data['money_need']) > money_expenses:
            if (user_city_data['energy_have'] - user_city_data['energy_need']) > energy_expenses:
                if (user_city_data['water_have'] - user_city_data['water_need']) > water_expenses:
                    
                    user_city_data['money_have'] -= money_cost
                    user_city_data['money_need'] += money_expenses
                    user_city_data['energy_need'] += energy_expenses
                    user_city_data['water_need'] += water_expenses

                    user_city['people'] += export_people

                    login.city_data_change(self.uid, user_city_data)
                    login.city_change(self.uid, user_city)

                    self.update.callback_query.message.reply_text(openf("data/city/descrip/create", "create_house_3"),
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
        user_city_data = convert_int(login.city_data(self.uid))

        money_cost = 140000
        export_money = 18000

        if user_city_data['money_have'] > money_cost:
            user_city_data['money_have'] -= money_cost
            user_city_data['money'] += export_money

            login.city_data_change(self.uid, user_city_data)

            self.update.callback_query.message.reply_text(openf("data/city/descrip/create", "create_comm_1"),
                                                            reply_markup=InlineKeyboardMarkup(kb.backcity))
        else:
            self.update.callback_query.message.reply_text("Средства города не способны содерждать этот район... Пополните бюджет или увеличьте доход", 
                                                          reply_markup=InlineKeyboardMarkup(kb.backcity))

    def comm2(self):
        user_city_data = convert_int(login.city_data(self.uid))

        money_cost = 780000
        export_money = 58000

        if user_city_data['money_have'] > money_cost:
            user_city_data['money_have'] -= money_cost
            user_city_data['money'] += export_money

            login.city_data_change(self.uid, user_city_data)

            self.update.callback_query.message.reply_text(openf("data/city/descrip/create", "create_comm_2"),
                                                            reply_markup=InlineKeyboardMarkup(kb.backcity))
        else:
            self.update.callback_query.message.reply_text("Средства города не способны содерждать этот район... Пополните бюджет или увеличьте доход", 
                                                          reply_markup=InlineKeyboardMarkup(kb.backcity))

    def comm3(self):
        user_city_data = convert_int(login.city_data(self.uid))

        money_cost = 2300000
        export_money = 152000

        if user_city_data['money_have'] > money_cost:
            user_city_data['money_have'] -= money_cost
            user_city_data['money'] += export_money

            login.city_data_change(self.uid, user_city_data)

            self.update.callback_query.message.reply_text(openf("data/city/descrip/create", "create_comm_3"),
                                                            reply_markup=InlineKeyboardMarkup(kb.backcity))
        else:
            self.update.callback_query.message.reply_text("Средства города не способны содерждать этот район... Пополните бюджет или увеличьте доход", 
                                                          reply_markup=InlineKeyboardMarkup(kb.backcity))

    def ind1_1(self):
        user_city_data = convert_int(login.city_data(self.uid))

        money_cost = 20000
        money_expenses = 4230

        export_energy = 850

        if user_city_data['money_have'] > money_cost and (user_city_data['money'] - user_city_data['money_need']) > money_expenses:
            user_city_data['money_have'] -= money_cost
            user_city_data['money_need'] += money_expenses
            user_city_data['energy_have'] += export_energy

            login.city_data_change(self.uid, user_city_data)

            self.update.callback_query.message.reply_text(openf("data/city/descrip/create", "create_ind_en_1"),
                                                            reply_markup=InlineKeyboardMarkup(kb.backcity))
        else:
            self.update.callback_query.message.reply_text("Средства города не способны содерждать этот объект... Пополните бюджет или увеличьте доход", 
                                                          reply_markup=InlineKeyboardMarkup(kb.backcity))

    def ind1_2(self):
        user_city_data = convert_int(login.city_data(self.uid))

        money_cost = 100000
        money_expenses = 9100

        export_energy = 1850

        if user_city_data['money_have'] > money_cost and (user_city_data['money'] - user_city_data['money_need']) > money_expenses:
            user_city_data['money_have'] -= money_cost
            user_city_data['money_need'] += money_expenses
            user_city_data['energy_have'] += export_energy

            login.city_data_change(self.uid, user_city_data)

            self.update.callback_query.message.reply_text(openf("data/city/descrip/create", "create_ind_en_2"),
                                                            reply_markup=InlineKeyboardMarkup(kb.backcity))
        else:
            self.update.callback_query.message.reply_text("Средства города не способны содерждать этот объект... Пополните бюджет или увеличьте доход", 
                                                          reply_markup=InlineKeyboardMarkup(kb.backcity))

    def ind1_3(self):
        user_city_data = convert_int(login.city_data(self.uid))

        money_cost = 500000
        money_expenses = 19000

        export_energy = 5000

        if user_city_data['money_have'] > money_cost and (user_city_data['money'] - user_city_data['money_need']) > money_expenses:
            user_city_data['money_have'] -= money_cost
            user_city_data['money_need'] += money_expenses
            user_city_data['energy_have'] += export_energy

            login.city_data_change(self.uid, user_city_data)

            self.update.callback_query.message.reply_text(openf("data/city/descrip/create", "create_ind_en_3"),
                                                            reply_markup=InlineKeyboardMarkup(kb.backcity))
        else:
            self.update.callback_query.message.reply_text("Средства города не способны содерждать этот объект... Пополните бюджет или увеличьте доход", 
                                                          reply_markup=InlineKeyboardMarkup(kb.backcity))

    def ind2_1(self):
        user_city_data = convert_int(login.city_data(self.uid))

        money_cost = 20000
        money_expenses = 2800
        energy_expenses = 2

        export_water = 1480

        if user_city_data['money_have'] > money_cost and (user_city_data['money'] - user_city_data['money_need']) > money_expenses:
            if (user_city_data['energy_have'] -user_city_data['energy_need']) > energy_expenses:
                
                user_city_data['money_have'] -= money_cost
                user_city_data['money_need'] += money_expenses
                user_city_data['energy_need'] += energy_expenses

                user_city_data['water_have'] += export_water

                login.city_data_change(self.uid, user_city_data)

                self.update.callback_query.message.reply_text(openf("data/city/descrip/create", "create_ind_wat_1"),
                                                            reply_markup=InlineKeyboardMarkup(kb.backcity))
            else:
                self.update.callback_query.message.reply_text("Для постройки этого объекта нехватает электроэнергии! Постройте новые электростанции",
                                                              reply_markup=InlineKeyboardMarkup(kb.backcity))
        else:
            self.update.callback_query.message.reply_text("Средства города не способны содерждать этот объект... Пополните бюджет или увеличьте доход", 
                                                          reply_markup=InlineKeyboardMarkup(kb.backcity))

    def ind2_2(self):
        user_city_data = convert_int(login.city_data(self.uid))

        money_cost = 100000
        money_expenses = 5400
        energy_expenses = 4

        export_water = 3200

        if user_city_data['money_have'] > money_cost and (user_city_data['money'] - user_city_data['money_need']) > money_expenses:
            if (user_city_data['energy_have'] -user_city_data['energy_need']) > energy_expenses:
                user_city_data['money_have'] -= money_cost
                user_city_data['money_need'] += money_expenses
                user_city_data['energy_need'] += energy_expenses

                user_city_data['water_have'] += export_water

                login.city_data_change(self.uid, user_city_data)

                self.update.callback_query.message.reply_text(openf("data/city/descrip/create", "create_ind_wat_2"),
                                                            reply_markup=InlineKeyboardMarkup(kb.backcity))
            else:
                self.update.callback_query.message.reply_text("Для постройки этого объекта нехватает электроэнергии! Постройте новые электростанции",
                                                              reply_markup=InlineKeyboardMarkup(kb.backcity))
        else:
            self.update.callback_query.message.reply_text("Средства города не способны содерждать этот объект... Пополните бюджет или увеличьте доход", 
                                                          reply_markup=InlineKeyboardMarkup(kb.backcity))

    def ind2_3(self):
        user_city_data = convert_int(login.city_data(self.uid))

        money_cost = 500000
        money_expenses = 16000
        energy_expenses = 8

        export_water = 7100

        if user_city_data['money_have'] > money_cost and (user_city_data['money'] - user_city_data['money_need']) > money_expenses:
            if (user_city_data['energy_have'] -user_city_data['energy_need']) > energy_expenses:
                user_city_data['money_have'] -= money_cost
                user_city_data['money_need'] += money_expenses
                user_city_data['energy_need'] += energy_expenses

                user_city_data['water_have'] += export_water

                login.city_data_change(self.uid, user_city_data)

                self.update.callback_query.message.reply_text(openf("data/city/descrip/create", "create_ind_wat_3"),
                                                            reply_markup=InlineKeyboardMarkup(kb.backcity))
            else:
                self.update.callback_query.message.reply_text("Для постройки этого объекта нехватает электроэнергии! Постройте новые электростанции",
                                                              reply_markup=InlineKeyboardMarkup(kb.backcity))
        else:
            self.update.callback_query.message.reply_text("Средства города не способны содерждать этот объект... Пополните бюджет или увеличьте доход", 
                                                          reply_markup=InlineKeyboardMarkup(kb.backcity))

    def ind3_1(self):
        user_city_data = convert_int(login.city_data(self.uid))

        money_cost = 160000
        energy_expenses = 5
        water_expenses = 100

        export_money = 8400

        if user_city_data['money_have'] > money_cost:
            if (user_city_data['energy_have'] - user_city_data['energy_need']) > energy_expenses:
                if (user_city_data['water_have'] - user_city_data['water_need']) > water_expenses:
                    
                    user_city_data['money_have'] -= money_cost
                    user_city_data['energy_need'] += energy_expenses
                    user_city_data['water_need'] += water_expenses

                    user_city_data['money'] += export_money

                    login.city_data_change(self.uid, user_city_data)

                    self.update.callback_query.message.reply_text(openf("data/city/descrip/create", "create_ind_mat_1"),
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
        user_city_data = convert_int(login.city_data(self.uid))

        money_cost = 1700000
        energy_expenses = 13 
        water_expenses = 400

        export_money = 30100

        if user_city_data['money_have'] > money_cost:
            if (user_city_data['energy_have'] - user_city_data['energy_need']) > energy_expenses:
                if (user_city_data['water_have'] - user_city_data['water_need']) > water_expenses:
                    
                    user_city_data['money_have'] -= money_cost
                    user_city_data['energy_need'] += energy_expenses
                    user_city_data['water_need'] += water_expenses

                    user_city_data['money'] += export_money

                    login.city_data_change(self.uid, user_city_data)

                    self.update.callback_query.message.reply_text(openf("data/city/descrip/create", "create_ind_mat_2"),
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
        user_city_data = convert_int(login.city_data(self.uid))

        money_cost = 6350000
        energy_expenses = 25
        water_expenses = 700

        export_money = 185800

        if user_city_data['money_have'] > money_cost:
            if (user_city_data['energy_have'] - user_city_data['energy_need']) > energy_expenses:
                if (user_city_data['water_have'] - user_city_data['water_need']) > water_expenses:
                    
                    user_city_data['money_have'] -= money_cost
                    user_city_data['energy_need'] += energy_expenses
                    user_city_data['water_need'] += water_expenses

                    user_city_data['money'] += export_money

                    login.city_data_change(self.uid, user_city_data)

                    self.update.callback_query.message.reply_text(openf("data/city/descrip/create", "create_ind_mat_3"),
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

class RandomTasks():
    def __init__(self, uid: str):

        self.uid = str(uid)

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

        user_city = login.authorize_city(self.uid)
        user_city_data = convert_int(login.city_data(self.uid))
        
        user_city['people'] = int(user_city['people'])

        match self.task:

            case "fire":
                self.text = openf("data/city/descrip", "fire")

                user_city_data['money_have'] -= 140000

            case "terrorism":
                self.text = openf("data/city/descrip", "terrorism")

                user_city['people'] -= 4000
                user_city_data['money_have'] -= 70000

            case "holiday":
                self.text = openf("data/city/descrip", "holiday")

            case "hurricane":
                self.text = openf("data/city/descrip", "hurricane")

                user_city['people'] -= 200
                user_city_data['money_have'] -= 80000

            case "flood":
                self.text = openf("data/city/descrip", "flood")

                user_city_data['money_have'] -= 30000

            case "earthshake":
                self.text = openf("data/city/descrip", "earthshake")

                user_city_data['money_have'] -= 100000

        login.city_data_change(self.uid, user_city_data)
        login.city_change(self.uid, user_city)

class Admins():
    def __init__(self, update, context):
        self.update = update
        self.context = context

        self.command, self.uid = self.update.message.text.split(" ")
        self.uid = str(self.uid)

        self.user = login.authorize(str(self.uid))
        self.active_user = login.authorize(str(update.message.chat_id))

    def ban(self):
        if self.active_user['admin']:
            self.active_user = self.update.message.chat_id
            self.user['ban'] = 1

            login.update(self.uid, self.user)

            self.update.message.reply_text("User: " + self.uid + " banned. Admin: " + str(self.active_user))
            self.context.bot.send_message(chat_id=-1001955905639,
                                          text="User: " + self.uid + " banned. Admin: " + str(self.active_user))
        else: self.update.message.reply_text("You are not admin")

    def unban(self):
        if self.active_user['admin']:
            self.active_user = self.update.message.chat_id
            self.user['ban'] = 0

            login.update(self.uid, self.user)

            self.update.message.reply_text("User: " + self.uid + " unbanned. Admin: " + str(self.active_user))
            self.context.bot.send_message(chat_id=-1001955905639,
                                          text="User: " + self.uid + " unbanned. Admin: " + str(self.active_user))
        else: self.update.message.reply_text("You are not admin")

    def addbeta(self):
        if self.active_user['admin']:
            self.active_user = self.update.message.chat_id
            self.user['bt'] = 1

            login.update(self.uid, self.user)

            self.update.message.reply_text("User: " + self.uid + " added to beta-test. Admin: " + str(self.active_user))
            self.context.bot.send_message(chat_id=-1001955905639,
                                          text="User: " + self.uid + " added to beta-test. Admin: " + str(self.active_user))
        else: self.update.message.reply_text("You are not admin")

    def delbeta(self):
        if self.active_user['admin']:
            self.active_user = self.update.message.chat_id
            self.user['bt'] = 0

            login.update(self.uid, self.user)

            self.update.message.reply_text("User: " + self.uid + " delete from beta-test. Admin: " + str(self.active_user))
            self.context.bot.send_message(chat_id=-1001955905639,
                                          text="User: " + self.uid + " delete from beta-test. Admin: " + str(self.active_user))
        else: self.update.message.reply_text("You are not admin")

def admin(update, context):
    admin = Admins(update, context)
    text = update.message.text

    if '/ban' in text: admin.ban()
    elif '/unban' in text: admin.unban()
    elif '/addbeta' in text: admin.addbeta()
    elif '/delbeta' in text: admin.delbeta()

from echo import echo

def checkban(update, context):
    echo(update, context)
    callback = False
    inline = False
    try:
        user = login.authorize(str(update.callback_query.message.chat_id))
        callback = True
    except:
        try:
            user = login.authorize(str(update.message.chat_id))
        except:
            user = login.authorize(str(update.inline_query.from_user_id))
            inline = True

    if not callback and not inline:
        if user['ban']:
            update.message.reply_text("You are banned in this place")
            context.bot.send_message(chat_id=-1001955905639, text="User: " + str(update.message.chat['username']) + " trying to use bot... (banned)")
            return True
        elif not user['bt']:
            update.message.reply_text("You are not member beta-test!! If you want to test this bot --> @r_ypiter")
            context.bot.send_message(chat_id=-1001955905639, text="User: " + str(update.message.chat['username']) + " trying to use bot... (not member beta-test)")
            return True
        else:
            return False

    elif inline:
        if update != None:
            if user['ban']:
                return True
            elif not user['bt']:
                return True
            else:
                return False
        else:
            return False

    elif callback:
        if user['ban']:
            update.callback_query.message.reply_text("You are banned in this place")
            context.bot.send_message(chat_id=-1001955905639, text="User: " + str(update.callback_query.message.chat['username']) + " trying to use bot... (banned)")
            return True
        elif not user['bt']:
            update.callback_query.message.reply_text("You are not member beta-test!! If you want to test this bot --> @r_ypiter")
            context.bot.send_message(chat_id=-1001955905639, text="User: " + str(update.callback_query.message.chat['username']) + " trying to use bot... (not member beta-test)")
            return True
        else:
            return False