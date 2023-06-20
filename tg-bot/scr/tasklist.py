# -*- coding: utf-8 -*-
import telegram

from telegram.ext import CommandHandler, MessageHandler, Filters, Updater

token = "5873796392:AAEE1i9cwQ5Y2T6Mk-TJkTHruANhCmPr_uU"
bot = telegram.Bot(token=token)
updater = Updater(token=token, use_context=True)

spendlist = {}
spendl = ""
userlist = {}
user = []

class Spend():
    def __init__(self, name, cost, status):
        self.name = name
        self.cost = cost
        self.status = status

    def change(self, d, new):
        if d.lower() == "цена":
            self.cost = new
        elif d.lower() == "статус":
            self.status = new

    def return_data(self):
        return self.name, self.cost, self.status

def start_handler(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Для создания списка покупок вводите ИМЯТОВАРА-ЦЕНА-СТАТУС-(ДОБАВИТЬ/УДАЛИТЬ)\nЧтобы изменить товар из списка, введите ИМЯТОВАРА:(ЦЕНА/СТАТУС):(НОВАЯЦЕНА/НОВЫЙСТАТУС)")

def spend_handler(update, context):
    global spendl
    try:
        for key in userlist[update.message.chat_id]:
            if userlist[update.message.chat_id][key].return_data()[0] in spendl:
                pass
            else:
                user.append("Товар: "+ userlist[update.message.chat_id][key].return_data()[0] +
                                     "\nЦена: " + userlist[update.message.chat_id][key].return_data()[1] +
                                     "\nСтатус: " + userlist[update.message.chat_id][key].return_data()[2])
        spendl = ""
        for i in range(len(user)):
            spendl = spendl + str(user[i]) + "\n"
        context.bot.send_message(chat_id=update.message.chat_id,
                                     text="Ваш список покупок:\n" + spendl)
    except KeyError:
        context.bot.send_message(chat_id=update.message.chat_id,
                                     text="Ваш список товаров пуст!")

def echo_handler(update, context):
    global userlist
    if "-" in update.message.text:
        make, name, cost, status = update.message.text.split("-")
        if make == "Добавить":
            try:
                if userlist[update.message.chat_id][name].return_data()[0] == name:
                    context.bot.send_message(chat_id=update.message.chat_id, text="Такой товар уже существует!")
                else:
                    spendlist[name] = Spend(name, cost, status)
                    print(spendlist)
                    userlist[update.message.chat_id] = spendlist
                    print(userlist)
                    print(userlist[update.message.chat_id][name])
                    context.bot.send_message(chat_id=update.message.chat_id,
                                     text="Товар добавлен в список покупок!\n\nТовар: "+ userlist[update.message.chat_id][name].return_data()[0] +
                                     "\nЦена: " + userlist[update.message.chat_id][name].return_data()[1] +
                                     "\nСтатус: " + userlist[update.message.chat_id][name].return_data()[2] + "\n\n" +
                                     "Используйте /spendlist чтобы посмотреть свой список покупок")
            except KeyError:
                spendlist[name] = Spend(name, cost, status)
                print(spendlist)
                userlist[update.message.chat_id] = spendlist
                print(userlist)
                print(userlist[update.message.chat_id][name])
                context.bot.send_message(chat_id=update.message.chat_id,
                                     text="Товар добавлен в список покупок!\n\nТовар: "+ userlist[update.message.chat_id][name].return_data()[0] +
                                     "\nЦена: " + userlist[update.message.chat_id][name].return_data()[1] +
                                     "\nСтатус: " + userlist[update.message.chat_id][name].return_data()[2] + "\n\n" +
                                     "Используйте /spendlist чтобы посмотреть свой список покупок")
        else:
            if userlist[update.message.chat_id] != None:
                userlist[update.message.chat_id][name] = None
                context.bot.send_message(chat_id=update.message.chat_id, text="Товар " + name + " успешно удален!\n\n" + "Используйте /spendlist чтобы посмотреть свой список покупок")

    elif ":" in update.message.text:
        name, d, new = update.message.text.split(":")
        userlist[update.message.chat_id][name].change(d, new)
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text="Данные обновлены!\nТовар: "+ userlist[update.message.chat_id][name].return_data()[0] +
                                        "\nЦена: " + userlist[update.message.chat_id][name].return_data()[1] +
                                        "\nСтатус: " + userlist[update.message.chat_id][name].return_data()[2])

    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="Пожалуйста действуйте в соответствии с инструкцией /start ...")

updater.dispatcher.add_handler(CommandHandler('start', start_handler))
updater.dispatcher.add_handler(CommandHandler('spendlist', spend_handler))
updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo_handler))
updater.start_polling()
updater.idle()