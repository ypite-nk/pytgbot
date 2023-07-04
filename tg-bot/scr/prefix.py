# -*- coding: utf-8 -*-

from telegram import InlineKeyboardMarkup

from keyboardbot import backdel
from echo import echo
from spec import checkban, openf

def prefix_marks(update, context):
    echo(update, context)
    if checkban(update, context):
        return 0
    marks_id_memory = []
    with open("info/ypiter/marks/memory.txt", "r", encoding="utf-8") as file:
        file = file.readlines()
        for i in file:
            marks_id_memory.append(i.replace("\n", ""))
    if str(update.message.chat['id']) in marks_id_memory:
        update.message.reply_text("Вы уже отправляли рецензию!")
    else:
        if "\n" in update.message.text and len(update.message.text.split("\n")) == 5:
            with open("info/ypiter/marks/memory.txt", "w", encoding="utf-8") as file:
                marks_id_memory.append(str(update.message.chat['id']))
                for i in range(len(marks_id_memory)):
                    if i != len(marks_id_memory):
                        file.write(marks_id_memory[i] + "\n")
                    else:
                        file.write(marks_id_memory[i])
            marksget = update.message.text.split("\n")
            context.bot.send_message(chat_id=-1001955905639, text="Type: " + marksget[0] + "\n" + 
                                                                        "Link: " + marksget[1] + "\n" + 
                                                                        "ID: " + str(update.message.chat['id']) + "\n" +
                                                                        "Text: " + marksget[2] + "\n" + 
                                                                        "A: " + marksget[3] + "\n" + 
                                                                        "P: " + marksget[4] + "\n")
            update.message.reply_text(openf("info/ypiter/marks", "markssucces"), reply_markup=InlineKeyboardMarkup(backdel))
        else:
            update.message.reply_text(openf("info/ypiter/marks", "markserror"), reply_markup=InlineKeyboardMarkup(backdel))

from pyowm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('e8d3ccc3b3a95bec547a312f27610381', config_dict)
mng = owm.weather_manager()
l_weather = mng.weather_at_place

def prefix_weather(update, context, city = None):
    echo(update, context)
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