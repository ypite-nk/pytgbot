# -*- coding: utf-8 -*-
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
    City = login.City(uid)
    City.authorize()

    user_city_info = City.get_city_info()
    user_city_data = City.get_city_data()

    info_keys, info_values, info = [], [], ""
    data_keys, data_values, data = [], [], ""

    for key in user_city_info.keys(): info_keys.append(key)
    for value in user_city_info.values(): info_values.append(value)

    for i in range(len(info_keys)): info += str(info_keys[i]) + " : " + str(info_values[i]) + "\n"

    for key in user_city_data.keys(): data_keys.append(key)
    for value in user_city_data.values(): data_values.append(value)

    for i in range(len(data_keys)): data += str(data_keys[i]) + " : " + str(data_values[i]) + "\n"

    path_logo = "base/cities/photo/" + uid + "city.jpg"
    if path.exists(path_logo): update.callback_query.message.reply_photo(open(path_logo, 'rb'))
    
    return update.callback_query.message.reply_text("===Ваш город===" + "\n" + info + "\n===Управление===\n" + data,
                                                    reply_markup=InlineKeyboardMarkup(kb.city_admin)).message_id

def myprofile(update, context):
    user = login.User(str(update.callback_query.message.chat_id)).get_user_profile()
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
        city = login.City(str(i)).get_city_data()

        if city is not None:
            money = (city['Доход'] - city['Расходы'])
            city['Бюджет'] += money
            login.City(str(i)).write_city_data(city)
            context.bot.send_message(chat_id=i, text="💰payday💰\n\nТвой город заработал - " + str(money) +
                                     "\nБюджет: " + str(city['Бюджет']),
                                     reply_markup=InlineKeyboardMarkup(kb.backcity))

from spec import RandomTasks
def update_event(update, context):
    users_uid = login.users_info()

    for i in users_uid:
        city = login.City(str(i)).get_city_info()

        if city is not None:
            task = RandomTasks(i)
            task.taskUpdate()
            context.bot.send_message(chat_id=i,
                                     text=task.text,
                                     reply_markup=InlineKeyboardMarkup(kb.backcity))