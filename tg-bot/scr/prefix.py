# -*- coding: utf-8 -*-

from telegram import InlineKeyboardMarkup

from spec import checkban, openf

import login

import keyboardbot as kb

def prefix_marks(update, context):
    if checkban(update, context): return

    marks_id_memory = []
    with open("info/ypiter/marks/memory.txt", "r", encoding="utf-8") as file:
        file = file.readlines()
        for i in file: marks_id_memory.append(i.replace("\n", ""))

    if str(update.message.chat_id) in marks_id_memory: update.message.reply_text("Вы уже отправляли рецензию!")
    else:
        user = login.authorize(update.message.chat_id)
        user['marks_collect'] = 1
        login.update(update.message.chat_id, user)

        update.message.reply_text(openf("descriptext", "marks1"))

from pyowm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('e8d3ccc3b3a95bec547a312f27610381', config_dict).weather_manager().weather_at_place

def prefix_weather(update, context, city = None):
    if checkban(update, context): return

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
        except: update.message.reply_text("Такого города не существует! Возможно, вы ошиблись в написании или у OpenWeatherMap нету таких данных.",
                                      reply_markup=InlineKeyboardMarkup(kb.back))

def city_create(update, context):
    if checkban(update, context): return
    
    uid = str(update.message.chat_id)
    user = login.authorize(uid)
    
    if not user['city']:
        update.message.reply_text("Город успешно создан!",
                                  reply_markup=InlineKeyboardMarkup(kb.backcity))
        user['city'] = 1
        login.update(uid, user)
    else:
        update.message.reply_text("У вас уже есть город!",
                                  reply_markup=InlineKeyboardMarkup(kb.backcity))
        return
    try:
        prefix, *name = update.message.text.split(' ')
        city_name = ""
        for i in name:
            city_name += i
        first_part = "name:" + city_name
    except:
        first_part = "name:" + "Город x"
    second_part = "\ncountry:Россия\nsubject:Иркутская область\ncreate_data:2023\nsize:1\npeople:0\n---optional---:---Опциональные---\nmayor:Нет\nsign:Нет\ngymn:Нет\nhistory:Нет\n"
    all_part = first_part + second_part
    status = "name:0\nsign:0\ngymn:0\nhistory:0\nmayor:0"
    data = "money_have:1000000\nenergy_have:0\nwater_have:0\nmoney:80000\nmoney_need:0\nenergy_need:0\nwater_need:0"
    login.city_create(uid, all_part, status, data)

def mycity(update, context):
    if checkban(update, context): return
    
    try: uid = str(update.message.chat_id)
    except: uid = str(update.callback_query.message.chat_id)

    user_city_info = login.authorize_city(uid)
    user_city_data = login.city_data(uid)

    if user_city_info == None:
        first_part = "name:Город x"
        second_part = "\ncountry:Россия\nsubject:Иркутская область\ncreate_data:2023\nsize:1\npeople:0\n---optional---:---Опциональные---\nmayor:Нет\nsign:Нет\ngymn:Нет\nhistory:Нет\n"
        all_part = first_part + second_part
        status = "name:0\nsign:0\ngymn:0\nhistory:0\nmayor:0"
        data = "money_have:1000000\nenergy_have:0\nwater_have:0\nmoney:80000\nmoney_need:0\nenergy_need:0\nwater_need:0"
        try:
            update.message.reply_text("Создаю город...")
            login.city_create(uid, all_part, status, data)
        except:
            new_message_id = update.callback_query.message.reply_text("Создаю город...").message_id
            login.city_create(uid, all_part, status, data)

    user_city_info = login.authorize_city(uid)
    user_city_data = login.city_data(uid)

    city_info, city_info_key, city_info_value = "", [], []
    city_data, city_data_key, city_data_value = "", [], []

    city_info_tr = {
                    "name": "Имя",
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

    try: update.message.reply_text("===Ваш город===\n" + city_info +
                              "\nДля изменения опциональных данных города введите:\n" + 
                              "/изменить город 'имя/герб/гимн/история' 'ваш текст'" + "\n" +
                              "\n===Управление===\n"+
                              city_data, reply_markup=InlineKeyboardMarkup(kb.city_admin))
    except:
        new_message_id = update.callback_query.message.reply_text("===Ваш город===" + "\n" + city_info +
                              "\nДля изменения опциональных данных города введите:\n" + 
                              "/изменить город 'имя/герб/гимн/история' 'ваш текст'" + "\n" +
                              "\n===Управление===\n"+
                              city_data, reply_markup=InlineKeyboardMarkup(kb.city_admin)).message_id
        return new_message_id

def myprofile(update, context):
    if checkban(update, context): return

    try: uid = str(update.message.chat_id)
    except: uid = str(update.callback_query.message.chat_id)

    user = login.user(uid)
    keys, values = [], []
    profile = ""

    for key in user.keys(): keys.append(key)
    for value in user.values(): values.append(value)
    for i in range(len(keys)): profile += str(keys[i]) + " : " + str(values[i])

    try: update.message.reply_text("===Ваш профиль===\n" + profile +
                                  "\nДля изменения данных используйте: /изменить профиль никнейм|имя|интересы|день рождения",
                                  reply_markup = InlineKeyboardMarkup(kb.back))
    except: update.callback_query.message.reply_text("===Ваш профиль===\n" + profile +
                                  "\nДля изменения данных используйте: /изменить профиль никнейм|имя|интересы|день рождения",
                                  reply_markup = InlineKeyboardMarkup(kb.back))

def change(update, context):
    if checkban(update, context):
        return
    try:
        uid = str(update.message.chat_id)
        prefix, *message = update.message.text.split(" ")
        reply_text = update.message.reply_text
        menu = InlineKeyboardMarkup(kb.start_key)
        match message[0].lower():
            case "профиль":
                user_status = login.user_status(uid)
                try:
                    if message[1].lower() + " " + message[2].lower() == "день рождения":
                        user_status['birthday'] = 1
                        reply_text("Напишите ваш день рождения в формате день.месяц.год, например 30.07.2023", reply_markup=menu)
                except:
                    pass
                    match message[1].lower():
                        case "никнейм":
                            user_status['nickname'] = 1
                            reply_text("Введите новый никнейм",
                                       reply_markup=menu)
                        case "имя":
                            user_status['name'] = 1
                            reply_text("Введите новое имя",
                                       reply_markup=menu)
                        case "интересы":
                            user_status['buisness'] = 1
                            reply_text("Напишите ваши интересы",
                                       reply_markup=menu)
                        case _:
                            reply_text("Команда '/изменить профиль' должна содержать в себе аттрибуты: '/изменить профиль никнейм|имя|интересы|день рождения'")
                login.user_status_change(uid, user_status)
            case "город":
                user_city_status = login.city_status(uid)
                if user_city_status is None:
                    reply_text("Вы еще не создали город! Для создания введите /город имягорода")
                    return
                match message[1].lower():
                    case "имя":
                        user_city_status['name'] = 1
                        reply_text("Введите новое имя для вашего города")
                    case "герб":
                        user_city_status['sign'] = 1
                        reply_text("Отправьте изображение вашего герба (не более 400*400)")
                    case "гимн":
                        user_city_status['gymn'] = 1
                        reply_text("Отправьте текст гимна")
                    case "история":
                        user_city_status['history'] = 1
                        reply_text("Отправьте текст истории")
                    case "мэр":
                        user_city_status['mayor'] = 1
                        reply_text("Отправьте ФИО нового мэра")
                    case _:
                        update.message.reply_text("Команда '/изменить город' должна содержать в себе аттрибуты: '/изменить город имя|герб|гимн|история'")
                login.city_status_change(uid, user_city_status)
            case _:
                update.message.reply_text("Команда '/изменить' должна содержать в себе аттрибуты: '/изменить (профиль|город) (имя|герб|гимн|история)|(никнейм|имя|интересы|день рождения)'")
    except:
        update.message.reply_text("Произошла неизвестная ошибка, попробуйте заного",
                                  reply_markup=InlineKeyboardMarkup(kb.back))

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