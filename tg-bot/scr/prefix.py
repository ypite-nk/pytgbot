﻿# -*- coding: utf-8 -*-
import keyboardbot as kb
from telegram import InlineKeyboardMarkup
from spec import check_acces

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
            update.message.reply_text(f"Город: {city}\nТемпература: {str(result[0])}\nНебо: {str(result[1])}\nВетер: {str(result[2])} м/с",
                                      reply_markup=InlineKeyboardMarkup(kb.back))
        except: update.message.reply_text("Такого города не существует! Возможно, вы ошиблись в названии или у OpenWeatherMap нету таких данных.",
                                      reply_markup=InlineKeyboardMarkup(kb.back))

import login
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

    path_flag = f"base/cities/photo/{uid}flag.jpg"
    if path.exists(path_flag): update.callback_query.message.reply_photo(open(path_flag, 'rb'))

    path_logo = f"base/cities/photo/{uid}sign.jpg"
    if path.exists(path_logo): update.callback_query.message.reply_photo(open(path_logo, 'rb'))
    
    return update.callback_query.message.reply_text(f"===Ваш город===\n{info}\n===Управление===\n{data}",
                                                    reply_markup=InlineKeyboardMarkup(kb.city_admin)).message_id

def myprofile(update, context):
    user = login.User(str(update.callback_query.message.chat_id)).get_user_profile()
    keys, values, profile = [], [], ""

    for key in user.keys(): keys.append(key)
    for value in user.values(): values.append(value)
    for i in range(len(keys)): profile += str(keys[i]) + " : " + str(values[i]) + "\n"

    return update.callback_query.message.reply_text(f"===Ваш профиль===\n{profile}",
                                                    reply_markup=InlineKeyboardMarkup(kb.profile)).message_id

def inline_profile(update, context):
    user = login.User(str(update.inline_query.from_user.id)).get_user_profile()
    keys, values, profile = [], [], ""

    keylist = ['ID', 'Никнейм', 'День рождения', 'Интересы','Город', 'Рейтинг', 'Юшки']

    for key in user.keys():
        if key in keylist: keys.append(key)

    for i in keys: values.append(user[i])

    for i in range(len(keys)): profile += str(keys[i]) + " : " + str(values[i]) + "\n"

    return profile

def inline_city(update, context):
    uid = str(update.inline_query.from_user.id)
    City = login.City(uid)
    City.authorize()

    user_city_info = City.get_city_info()

    info_keys, info_values, info = [], [], ""

    for key in user_city_info.keys(): info_keys.append(key)
    for value in user_city_info.values(): info_values.append(value)

    for i in range(len(info_keys)): info += str(info_keys[i]) + " : " + str(info_values[i]) + "\n"

    return info

def update(update, context):
    users_uid = login.users_city_info()

    for i in users_uid:
        city = login.City(str(i))
        user = login.User(str(i)).get_user_profile()

        city_data = city.get_city_data()

        money = (city_data['Доход'] - city_data['Расходы'])
        city_data['Бюджет'] += money
            
        if user['VIP'] == 'None':
            context.bot.send_message(chat_id=i,
                                     text=f"💰payday💰\n\nТвой город заработал - {str(money)}\nБюджет: {str(city_data['Бюджет'])}",
                                     reply_markup=InlineKeyboardMarkup(kb.backcity)
                                     )
        else:
            city_data['Бюджет'] += money

            context.bot.send_message(chat_id=i,
                                     text=f"💰VIP payday💰\n\nТвой город заработал - {str(money*2)}\nБюджет: {str(city_data['Бюджет'])}",
                                     reply_markup=InlineKeyboardMarkup(kb.backcity)
                                     )

        city.write_city_data(city_data)

def update_event(update, context):
    from spec import RandomTasks
    users_uid = login.users_city_info()

    for i in users_uid:
        city = login.City(str(i))
        city_change = city.get_city_change()

        for key in city_change.keys(): city_change[key] = 0
        city.write_city_change(city_change)

        task = RandomTasks(i)
        task.taskUpdate()
        
        context.bot.send_message(chat_id=i,
                                 text=task.text,
                                 reply_markup=InlineKeyboardMarkup(kb.backcity)
                                 )