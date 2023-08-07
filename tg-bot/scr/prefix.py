﻿# -*- coding: utf-8 -*-
import login
import keyboardbot as kb
from telegram import InlineKeyboardMarkup
from spec import check_acces
from spec import openfile

@check_acces
def prefix_marks(update, context):
    marks_id_memory = []
    with open("info/ypiter/marks/memory.txt", "r", encoding="utf-8") as file:
        file = file.readlines()
        for i in file: marks_id_memory.append(i.replace("\n", ""))

    if str(update.message.chat_id) in marks_id_memory: update.message.reply_text("Вы уже отправляли рецензию!",
                                                                                 reply_markup = InlineKeyboardMarkup(kb.back))
    else:
        user = login.authorize(update.message.chat_id)
        user['marks_collect'] = 1
        login.update(update.message.chat_id, user)

        update.message.reply_text(openfile("descriptext", "marks1"))

from pyowm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('e8d3ccc3b3a95bec547a312f27610381', config_dict).weather_manager().weather_at_place

@check_acces
def prefix_weather(update, context, city = None):
    if update is None:
        try:
            w = owm(city).weather
            return [w.temperature('celsius')['temp'], w.detailed_status, w.wind()['speed']]
        except: return None
    else:
        try: prefix, city = update.message.text.split(" ")
        except:
            try:
                prefix, city1, city2 = update.message.text.split(" ")
                city = city1 + " " + city2
            except:
                prefix, city1, city2, city3 = update.message.text.split(" ")
                city = city1 + " " + city2 + " " + city3
        try:
            w = owm(city).weather
            result = [w.temperature('celsius')['temp'], w.detailed_status, w.wind()['speed']]
            update.message.reply_text("Город: " + city + "\nТемпература: " + str(result[0]) + "\nНебо: " + str(result[1]) + "\nВетер: " + str(result[2]) + " м/с",
                                      reply_markup=InlineKeyboardMarkup(kb.back))
        except: update.message.reply_text("Такого города не существует! Возможно, вы ошиблись в названии или у OpenWeatherMap нету таких данных.",
                                      reply_markup=InlineKeyboardMarkup(kb.back))

from os import path
def mycity(update, context):
    uid = str(update.callback_query.message.chat_id)

    if login.authorize_city(uid) == None:
        first_part = "cityname:Город x"
        second_part = "\ncountry:Россия\nsubject:Иркутская область\ncreate_data:2023\nsize:1\npeople:0\n---optional---:---Опциональные---\nmayor:Нет\nsign:Нет\ngymn:Нет\nhistory:Нет\n"
        all_part = first_part + second_part
        status = "cityname:0\nsign:0\ngymn:0\nhistory:0\nmayor:0"
        data = "money_have:1000000\nenergy_have:0\nwater_have:0\nmoney:80000\nmoney_need:0\nenergy_need:0\nwater_need:0"
        login.city_create(uid, all_part, status, data)

    user_city_info = login.authorize_city(uid)
    user_city_data = login.city_data(uid)

    city_info, city_info_key, city_info_value = "", [], []
    city_data, city_data_key, city_data_value = "", [], []

    city_info_tr = {
                    "cityname": "Имя",
                    "country": "Страна",
                    "subject": "Область",
                    "create_data": "Дата создания",
                    "size": "Площадь",
                    "people": "Количество людей",
                    "mayor": "Мэр",
                    "---optional---": "\n---Опциональные---",
                    "sign": "Герб",
                    "gymn": "Гимн",
                    "history": "История"
               }
    city_data_tr = {
                    "money_have":"Бюджет",
                    "energy_have":"Электроэнергия",
                    "water_have":"Водоснабжение",
                    "money":"Доход",
                    "money_need":"Расход бюджета",
                    "energy_need":"Расход электроэнергии",
                    "water_need":"Расход водоснабжения"
                    }

    for key in user_city_info.keys(): city_info_key.append(key)
    for value in user_city_info.values(): city_info_value.append(value)
    for i in range(len(city_info_key)): city_info += str(city_info_tr[city_info_key[i]]) + " : " + str(city_info_value[i]) + "\n"

    for key in user_city_data.keys(): city_data_key.append(key)
    for value in user_city_data.values(): city_data_value.append(value)
    for i in range(len(city_data_key)): city_data += str(city_data_tr[city_data_key[i]]) + " : " + str(city_data_value[i]) + "\n"

    path_logo = "base/cities/photo/" + uid + "city.jpg"
    if path.exists(path_logo): update.callback_query.message.reply_photo(open(path_logo, 'rb'))
    
    return update.callback_query.message.reply_text("===Ваш город===" + "\n" + city_info + "\n===Управление===\n" + city_data,
                                                    reply_markup=InlineKeyboardMarkup(kb.city_admin)).message_id

def myprofile(update, context):
    user = login.user(str(update.callback_query.message.chat_id))
    keys, values = [], []
    profile = ""

    for key in user.keys(): keys.append(key)
    for value in user.values(): values.append(value)
    for i in range(len(keys)): profile += str(keys[i]) + " : " + str(values[i]) + "\n"

    return update.callback_query.message.reply_text("===Ваш профиль===\n" + profile,
                                                    reply_markup = InlineKeyboardMarkup(kb.profile)).message_id

def update(update, context):
    users_uid = login.users_info()

    for i in users_uid:
        user = login.city_data(i)

        if user is not None:
            money = (user['money'] - user['money_need'])
            user['money_have'] += money
            login.city_data_change(i, user)
            context.bot.send_message(chat_id=i, text="💰payday💰\n\nТвой город заработал - " + str(money) +
                                     "\nБюджет: " + str(user['money_have']),
                                     reply_markup=InlineKeyboardMarkup(kb.backcity))

from spec import RandomTasks
def update_event(update, context):
    users_uid = login.users_info()

    for i in users_uid:
        user = login.city_data(i)

        if user is not None:
            task = RandomTasks(i)
            task.taskUpdate()
            context.bot.send_message(chat_id=i,
                                     text=task.text,
                                     reply_markup=InlineKeyboardMarkup(kb.backcity))