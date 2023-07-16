# -*- coding: utf-8 -*-
import urllib.request
import login

from echo import echo

admin_id = [1086638338]

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

class Echo_Checker():
    '''
    Класс для проверки различных статусов записи.

    Пример: Если активна запись рецензии - выполниться код. И так далее...
    '''
    def __init__(self, update, context):
        self.update = update
        self.context = context

        self.prefix, *self.text = self.update.message.text.split(" ")

        if len(self.text) == 3:
            self.update.message.text = self.text[2]

        self.uid = str(self.update.message.chat['id'])

        self.status = { 'name':'0',
                        'sign':'0',
                        'gymn':'0',
                        'history':'0' }

    def write_marks(self):
        stat = login.authorize(self.update.message.chat['id'])
        if stat['marks_collect'] == 0 or self.update.message.text is not None:
            return False
        marks_id_memory = []

        with open("info/ypiter/marks/memory.txt", "r", encoding="utf-8") as file:
            file = file.readlines()
            for i in file:
                marks_id_memory.append(i.replace("\n", ""))
        if self.uid in marks_id_memory:
            self.update.message.reply_text("Вы уже отправляли рецензию!")
            return True
        if stat['marks_collect'] > 0 and stat['marks_collect'] < 5:
            user_text = openf("base", self.uid + "marks")

            if stat['marks_collect'] == 1:
                with open("base/" + self.uid + "marks.txt", "w+", encoding="utf-8") as f:
                    f.write(user_text + self.update.message.text + "\n")
                    self.update.message.reply_text(openf("descriptext", "marks2"))

            elif stat['marks_collect'] == 2:
                with open("base/" + self.uid + "marks.txt", "w+", encoding="utf-8") as f:
                    f.write(user_text + self.update.message.text + "\n")
                self.update.message.reply_text(openf("descriptext", "marks3"))

            elif stat['marks_collect'] == 3:
                if self.update.message.text.lower() == "да":
                    self.update.message.reply_text(openf("descriptext", "marks4_5"))
                    stat['marks_collect'] = stat['marks_collect'] + 1
                elif self.update.message.text.lower() == "нет":
                    self.update.message.reply_text(openf("descriptext", "marks4"))

            if stat['marks_collect'] == 4:
                self.update.message.reply_text(openf("descriptext", "marks_complete") + "\n" +
                    openf("base", self.uid + "marks") + "\nХотите изменить?(Да/нет)")
            stat['marks_collect'] = stat['marks_collect'] + 1
            login.update(self.update.message.chat['id'], stat)
            return True

        if stat['marks_collect'] == 5:
            if self.update.message.text.lower() == "да":
                stat['marks_collect'] = 1
                login.update(self.uid, stat)
                self.write_marks
                return True
            elif self.update.message.text.lower() == "нет":
                stat['marks_collect'] = 0
                login.update(self.uid, stat)
                with open("info/ypiter/marks/memory.txt", "w", encoding="utf-8") as file:
                    marks_id_memory.append(str(self.update.message.chat['id']))
                    for i in range(len(marks_id_memory)):
                        if i != len(marks_id_memory):
                            file.write(marks_id_memory[i] + "\n")
                        else:
                            file.write(marks_id_memory[i])
                with open("base/"+ self.uid +"marks.txt", "w", encoding="utf-8") as file:
                    file.write(" ")
                self.update.message.reply_text(openf("info/ypiter/marks", "markssucces"))
                return False

        return False

    def write_name(self):
        return False

    def clear_city_status(self):
        login.city_status_change(self.uid, self.status)

    def write_city_name(self):
        user_city_status = login.authorize_city(self.uid)
        if user_city_status is None:
            return False
        if user_city_status['name'] and self.update.message.text is not None:
            user_city = login.city_info(self.uid)

            self.update.message.reply_text("Имя города успешно изменено!\n" + user_city['name'] + " --> " + self.update.message.text)

            user_city['name'] = self.update.message.text
            login.city_change(self.uid, user_city)
            self.clear_city_status()
            return True
        else:
            return False

    def write_city_sign(self):
        user_city_status = login.authorize_city(self.uid)

        if user_city_status is None:
            return False

        if user_city_status['sign'] == 1 and self.update.message.text is None:
            
            file = self.context.bot.get_file(self.update.message.photo[-1])
            file_size = self.update.message.photo[-1]
            
            if file_size.width <= 400 and file_size.height <= 400:
                self.update.message.reply_text("Герб города успешно изменен!")
                response = urllib.request.urlopen(file.file_path)
                path = "D:/proj/pytgbotGH/tg-bot/base/cities/photo/" + self.uid + ".jpg"

                with open(path, 'wb') as new_file:
                    new_file.write(response.read())
                self.clear_city_status()

                return True
            else:
                self.update.message.reply_text("Размеры файла превышают максимальные! (400x400)")
                return False
        else:
            return False

    def write_city_gymn(self):
        user_city_status = login.authorize_city(self.uid)
        if user_city_status is None:
            return False
        if user_city_status['gymn'] and self.update.message.text is not None:
            self.update.message.reply_text("Гимн города умпешно изменен!")

            user_city = login.city_info(self.uid)
            user_city['gymn'] = self.update.message.text
            login.city_change(self.uid, user_city)
            self.clear_city_status()
            return True
        else:
            return False

    def write_city_history(self):
        user_city_status = login.authorize_city(self.uid)
        if user_city_status is None:
            return False
        if user_city_status['history'] and self.update.message.text is not None:
            self.update.message.reply_text("История города успешно изменена!")

            user_city = login.city_info(self.uid)
            user_city['history'] = self.update.message.text
            login.city_change(self.uid, user_city)
            self.clear_city_status()
            return True
        else:
            return False

    def echo_check(self):

        ''' Check-write-status function '''

        if self.write_marks():
            return True
        if self.write_name():
            return True
        if self.write_city_name():
            return True
        if self.write_city_sign():
            return True
        if self.write_city_gymn():
            return True
        if self.write_city_history():
            return True
        
        if self.update.message.text is None:
            return True
        else:
            return False

def ban(update, context):
    command, user_id = update.message.text.split(" ")
    user = login.authorize(str(user_id))
    active_user = login.authorize(str(update.message.chat['id']))
    
    if active_user['admin']:
        active_user = update.message.chat['id']
        user['ban'] = 1
        login.update(user_id, user)
        update.message.reply_text("User: " + str(user_id) + " banned. Admin: " + str(active_user))
        context.bot.send_message(chat_id=-1001955905639, text="User: " + str(user_id) + " banned. Admin: " + str(active_user))
    else:
        update.message.reply_text("You are not admin")

def unban(update, context):
    command, user_id = update.message.text.split(" ")
    user = login.authorize(str(user_id))
    active_user = login.authorize(str(update.message.chat['id']))

    if active_user['admin']:
        active_user = update.message.chat['id']
        user['ban'] = 0
        login.update(user_id, user)
        update.message.reply_text("User: " + str(user_id) + " unbanned. Admin: " + str(active_user))
        context.bot.send_message(chat_id=-1001955905639, text="User: " + str(user_id) + " unbanned. Admin: " + str(active_user))
    else:
        update.message.reply_text("You are not admin")

def add_beta(update, context):
    command, user_id = update.message.text.split(" ")
    user = login.authorize(str(user_id))
    active_user = login.authorize(str(update.message.chat['id']))

    if active_user['admin']:
        active_user = update.message.chat['id']
        user['bt'] = 1
        login.update(user_id, user)
        update.message.reply_text("User: " + str(user_id) + " added to beta-test. Admin: " + str(active_user))
        context.bot.send_message(chat_id=-1001955905639, text="User: " + str(user_id) + " added to beta-test. Admin: " + str(active_user))
    else:
        update.message.reply_text("You are not admin")

def del_beta(update, context):
    command, user_id = update.message.text.split(" ")
    user = login.authorize(str(user_id))
    active_user = login.authorize(str(update.message.chat['id']))

    if active_user['admin']:
        active_user = update.message.chat['id']
        user['bt'] = 0
        login.update(user_id, user)
        update.message.reply_text("User: " + str(user_id) + " delete from beta-test. Admin: " + str(active_user))
        context.bot.send_message(chat_id=-1001955905639, text="User: " + str(user_id) + " added to beta-test. Admin: " + str(active_user))
    else:
        update.message.reply_text("You are not admin")

def checkban(update, context):
    echo(update, context)
    callback = False
    inline = False
    try:
        user = login.authorize(str(update.callback_query.message.chat['id']))
        callback = True
    except:
        try:
            user = login.authorize(str(update.message.chat['id']))
        except:
            user = login.authorize(str(update.inline_query.from_user['id']))
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