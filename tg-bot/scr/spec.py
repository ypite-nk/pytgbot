admin_id = [1086638338]
def banlist(update, context):
    if update.message.chat['id'] in admin_id:
        banlists = []
        with open("info/banlist.txt", "r", encoding="utf-8") as file:
            file = file.readlines()
            for i in file:
                banlists.append(i.replace("\n", ""))
        update.message.reply_text(str(banlists))
    else:
        update.message.reply_text("You don't have a key for this command")

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
        update.message.reply_text("You don't have a key for this command")

def checkban(update, context):
    banlist = []
    beta_list = ['1661744004', '1086638338', '', '', '']
    with open("info/banlist.txt", "r", encoding="utf-8") as file:
        file = file.readlines() 
        for i in file:
            banlist.append(i.replace("\n", ""))
    try:
        if str(update.callback_query.message.chat['id']) in banlist:
            update.callback_query.message.reply_text("You are banned in this place")
            return True
        elif str(update.callback_query.message.chat['id']) not in beta_list:
            update.callback_query.message.reply_text("You are not member beta-test!! If you want to test this bot --> @r_ypiter")
            return True
        else:
            return False
    except AttributeError:
        if str(update.message.chat['id']) in banlist:
            update.message.reply_text("You are banned in this place")
            return True
        elif str(update.message.chat['id']) not in beta_list:
            update.message.reply_text("You are not member beta-test!! If you want to test this bot --> @r_ypiter")
            return True
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
        update.message.reply_text("You don't have a key for this command")