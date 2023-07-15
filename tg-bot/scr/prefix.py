# -*- coding: utf-8 -*-

from telegram import InlineKeyboardMarkup

from keyboardbot import backdel
from spec import checkban, openf

import login

def prefix_marks(update, context):
    if checkban(update, context):
        return
    marks_id_memory = []
    with open("info/ypiter/marks/memory.txt", "r", encoding="utf-8") as file:
        file = file.readlines()
        for i in file:
            marks_id_memory.append(i.replace("\n", ""))
    if str(update.message.chat['id']) in marks_id_memory:
        update.message.reply_text("Вы уже отправляли рецензию!")
    else:
        user = login.authorize(update.message.chat['id'])
        user['marks_collect'] = 1
        login.update(update.message.chat['id'], user)

        update.message.reply_text(openf("descriptext", "marks1"))

from pyowm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('e8d3ccc3b3a95bec547a312f27610381', config_dict)
mng = owm.weather_manager()
l_weather = mng.weather_at_place

def prefix_weather(update, context, city = None):
    if checkban(update, context):
        return
    if update is None:
        try:
            w = l_weather(city).weather
            return [w.temperature('celsius')['temp'], w.detailed_status, w.wind()['speed']]
        except:
            return None
    else:
        try:
            prefix, city = update.message.text.split(" ")
        except:
            try:
                prefix, city1, city2 = update.message.text.split(" ")
                city = city1 + " " + city2
            except:
                prefix, city1, city2, city3 = update.message.text.split(" ")
                city = city1 + " " + city2 + " " + city3
        try:
            w = l_weather(city).weather
            result = [w.temperature('celsius')['temp'], w.detailed_status, w.wind()['speed']]
            update.message.reply_text("Город: " + city + "\nТемпература: " + str(result[0]) + "\nНебо: " + str(result[1]) + "\nВетер: " + str(result[2]) + " м/с",
                                      reply_markup=InlineKeyboardMarkup(backdel))
        except:
            update.message.reply_text("Такого города не существует! Возможно, вы ошиблись в написании или у OpenWeatherMap нету таких данных.",
                                      reply_markup=InlineKeyboardMarkup(backdel))

def city_create(update, context):
    if checkban(update, context):
        return
    
    uid = str(update.message.chat['id'])
    user = login.authorize(uid)
    
    if not user['city']:
        update.message.reply_text("Город успешно создан!")
        user['city'] = 1
        login.update(uid, user)
    else:
        update.message.reply_text("У вас уже есть город!")
        return
    
    prefix, *name = update.message.text.split(' ')
    city_name = ""
    
    for i in name:
        city_name += i
    first_part = "name:" + city_name
    second_part = "\nbudget:10000\npeople:1\nkids:0\ntenager:0\nadults:1\nancient:0\ncreated:12.07.23\nroad:100\nlearning:100\nmedecine:100\nsafety:100\ninflation:4\nhapiest:100\nwater:100\nenergy_have:0\nenergy_need:0"
    all_part = first_part + second_part
    status = "nameCH:0\nsignCH:0\ngymnCH:0\nhistoryCH:0"
    login.city_create(uid, all_part, status)

def mycity(update, context):
    if checkban(update, context):
        return

    uid = str(update.message.chat['id'])
    user_city = login.city_info(uid)
    if user_city is None:
        update.message.reply_text("Вы еще не создали город! Для создания введите !city имягорода")
        return
    city_key = []
    city_value = []
    info_city = ""
    city_tr = {"name": "Имя",
               "country": "Страна",
               "subject": "Область",
               "create_data": "Дата создания",
               "size": "Площадь",
               "people": "Количество людей",
               "mayor": "Мэр",
               "optional": "\nОпционально",
               "sign": "Герб",
               "gymn": "Гимн",
               "history": "История"}
    for i in user_city.keys():
        city_key.append(i)
    for i in user_city.values():
        city_value.append(i)
    for i in range(len(city_key)):
        info_city += city_tr[city_key[i]] + " : " + city_value[i] + "\n"
    update.message.reply_text("Ваш город: " + "\n\n" + info_city + "\nДля изменения имени города введите:\n!mycity changename новоеимя")

def change(update, context):
    if checkban(update, context):
        return
    try:
        uid = str(update.message.chat['id'])
        prefix, *message = update.message.text.split(" ")

        match message[0].lower():
            case "профиль":
                user = login.authorize(uid)
                match message[1].lower():
                    case "имя":
                        pass
            case "город":
                user_city_status = login.authorize_city(uid)
                if user_city_status is None:
                    update.message.reply_text("Вы еще не создали город! Для создания введите !city имягорода")
                    return
                match message[1].lower():
                    case "имя": # name
                        user_city_status['name'] = 1
                        login.city_status_change(uid, user_city_status)
                    case "герб": # sign
                        user_city_status['sign'] = 1
                        login.city_status_change(uid, user_city_status)
                    case "гимн": # gymn
                        user_city_status['gymn'] = 1
                        login.city_status_change(uid, user_city_status)
                    case "история": # history
                        user_city_status['history'] = 1
                        login.city_status_change(uid, user_city_status)

            case _:
                update.message.reply_text("Команда '/change' или '/изменить' должна содержать в себе аттрибуты: '/change профиль||город имя||(имя|герб|гимн|история)'")
    except:
        update.message.reply_text("Произошла неизвестная ошибка, попробуйте заного")