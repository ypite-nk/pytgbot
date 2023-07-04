admin_id = [1086638338]

def openf(path, name):
    if path != "":
        return "".join(open(path + "/" + name + ".txt", "r", encoding="utf-8").readlines(0))
    else:
        return "".join(open(name + ".txt", "r", encoding="utf-8").readlines(0))

def banlist(update, context):
    if update.message.chat['id'] in admin_id:
        banlists = []
        with open("info/banlist.txt", "r", encoding="utf-8") as file:
            file = file.readlines()
            for i in file:
                banlists.append(i.replace("\n", ""))
        update.message.reply_text(str(banlists))
    else:
        update.message.reply_text("You are not admin")

def ban(update, context):
    banlist = []
    with open("info/banlist.txt", "r", encoding="utf-8") as file:
        file = file.readlines()
        for i in file:
            banlist.append(i.replace("\n", ""))
    print(update.message.chat['id'])
    if update.message.chat['id'] in admin_id:
        admin = update.message.chat['id']
        command, user_id = update.message.text.split(" ")
        if user_id not in banlist:
            banlist.append(user_id)
            with open("info/banlist.txt", "w", encoding="utf-8") as file:
                for i in range(len(banlist)):
                    if i != len(banlist):
                        file.write(str(banlist[i]) + "\n")
                    else:
                        file.write(str(banlist[i]))
            update.message.reply_text("User: " + str(user_id) + " banned. Admin: " + str(admin))
            context.bot.send_message(chat_id=-1001955905639, text="User: " + str(user_id) + " was banned. Admin: " + str(admin))
        else:
            update.message.reply_text("User: " + str(user_id) + " was banned. Admin: " + str(admin))
    else:
        update.message.reply_text("You are not admin")

def checkban(update, context):
    banlist = []
    #beta_list = ['1086638338', '1661744004', '1913240001', '', '']
    beta_list = ['1086638338', '', '', '', '']
    with open("info/banlist.txt", "r", encoding="utf-8") as file:
        file = file.readlines()
        for i in file:
            banlist.append(i.replace("\n", ""))
    try:
        if str(update.callback_query.message.chat['id']) in banlist:
            update.callback_query.message.reply_text("You are banned in this place")
            context.bot.send_message(chat_id=-1001955905639, text="User: " + str(update.callback_query.message.chat['username']) + " trying to use bot... (banned)")
            return True
        elif str(update.callback_query.message.chat['id']) not in beta_list:
            update.callback_query.message.reply_text("You are not member beta-test!! If you want to test this bot --> @r_ypiter")
            context.bot.send_message(chat_id=-1001955905639, text="User: " + str(update.callback_query.message.chat['username']) + " trying to use bot... (not member beta-test)")
            return True
        else:
            return False
    except AttributeError:
        try:
            if str(update.message.chat['id']) in banlist:
                update.message.reply_text("You are banned in this place")
                context.bot.send_message(chat_id=-1001955905639, text="User: " + str(update.message.chat['username']) + " trying to use bot... (banned)")
                return True
            elif str(update.message.chat['id']) not in beta_list:
                update.message.reply_text("You are not member beta-test!! If you want to test this bot --> @r_ypiter")
                context.bot.send_message(chat_id=-1001955905639, text="User: " + str(update.message.chat['username']) + " trying to use bot... (not member beta-test)")
                return True
            else:
                return False

        except:
            if update != None:
                if str(update.inline_query.from_user['id']) in banlist:
                    return True
                elif str(update.inline_query.from_user['id']) not in beta_list:
                    return True
                else:
                    return False
            else:
                return False

def unban(update, context):
    banlist = []
    with open("info/banlist.txt", "r", encoding="utf-8") as file:
        file = file.readlines()
        for i in file:
            banlist.append(i.replace("\n", ""))
    print(update.message.chat['id'])
    if update.message.chat['id'] in admin_id:
        admin = update.message.chat['id']
        command, user_id = update.message.text.split(" ")
        if user_id in banlist:
            banlist.remove(user_id)
            with open("info/banlist.txt", "w", encoding="utf-8") as file:
                for i in range(len(banlist)):
                    if i != len(banlist):
                        file.write(str(banlist[i]) + "\n")
                    else:
                        file.write(str(banlist[i]))
            update.message.reply_text("User: " + str(user_id) + " unbanned. Admin: " + str(admin))
            context.bot.send_message(chat_id=-1001955905639, text="User: " + str(user_id) + " unbanned. Admin: " + str(admin))
        else:
            update.message.reply_text("User: " + str(user_id) + " wasn't banned. Admin: " + str(admin))
    else:
        update.message.reply_text("You are not admin")