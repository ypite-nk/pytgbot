# -*- coding: utf-8 -*-
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

def write_marks(update, context):
    stat = login.authorize(update.message.chat['id'])
    if stat['marks_collect'] == 0:
        return False
    uid = str(update.message.chat['id'])
    marks_id_memory = []

    with open("info/ypiter/marks/memory.txt", "r", encoding="utf-8") as file:
        file = file.readlines()
        for i in file:
            marks_id_memory.append(i.replace("\n", ""))
    if uid in marks_id_memory:
        update.message.reply_text("Вы уже отправляли рецензию!")
        return True
    if stat['marks_collect'] > 0 and stat['marks_collect'] < 5:
        user_text = openf("base", uid + "marks")

        if stat['marks_collect'] == 1:
            with open("base/" + uid + "marks.txt", "w+", encoding="utf-8") as f:
                f.write(user_text + update.message.text + "\n")
                update.message.reply_text(openf("descriptext", "marks2"))

        elif stat['marks_collect'] == 2:
            with open("base/" + uid + "marks.txt", "w+", encoding="utf-8") as f:
                f.write(user_text + update.message.text + "\n")
            update.message.reply_text(openf("descriptext", "marks3"))

        elif stat['marks_collect'] == 3:
            if update.message.text.lower() == "да":
                update.message.reply_text(openf("descriptext", "marks4_5"))
                stat['marks_collect'] = stat['marks_collect'] + 1
            elif update.message.text.lower() == "нет":
                update.message.reply_text(openf("descriptext", "marks4"))

        if stat['marks_collect'] == 4:
            update.message.reply_text(openf("descriptext", "marks_complete") + "\n" +
                openf("base", uid + "marks") + "\nХотите изменить?(Да/нет)")
        stat['marks_collect'] = stat['marks_collect'] + 1
        login.update(update.message.chat['id'], stat)
        return True

    if stat['marks_collect'] == 5:
        if update.message.text.lower() == "да":
            stat['marks_collect'] = 1
            login.update(uid, stat)
            write_marks(update, context)
            return True
        elif update.message.text.lower() == "нет":
            stat['marks_collect'] = 0
            login.update(uid, stat)
            with open("info/ypiter/marks/memory.txt", "w", encoding="utf-8") as file:
                marks_id_memory.append(str(update.message.chat['id']))
                for i in range(len(marks_id_memory)):
                    if i != len(marks_id_memory):
                        file.write(marks_id_memory[i] + "\n")
                    else:
                        file.write(marks_id_memory[i])
            with open("base/"+ uid +"marks.txt", "w", encoding="utf-8") as file:
                file.write(" ")
            update.message.reply_text(openf("info/ypiter/marks", "markssucces"))
            return False

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