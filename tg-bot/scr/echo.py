# -*- coding: utf-8 -*-
def echo(update, context): # ОТЛАДКА
    info = {'userdata' : "Text:{" + update.callback_query['data'] + "}, " + "from:{" + update.callback_query.message.chat['username'] + '}',
            'bot_data' : "Message ID: " + str(update.callback_query.message.message_id)}
    print(info)