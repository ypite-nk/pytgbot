import login
admin_id = [1086638338]

def openf(path, name):
    if path != "":
        return "".join(open(path + "/" + name + ".txt", "r", encoding="utf-8").readlines(0))
    else:
        return "".join(open(name + ".txt", "r", encoding="utf-8").readlines(0))

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
        