
#!/usr/bin/env python3
# coding: utf-8
# -*- coding: utf-8 -*-

import mail_function as functions
import mail_config as config
import email
from email.header import decode_header
import sys
import asyncio
import traceback

ENCODING = config.encoding

def main():
    imap = functions.connection()

    status, messages = imap.select("INBOX")
    res, unseen_msg = imap.uid("search", "UNSEEN", "ALL")
    unseen_msg = unseen_msg[0].decode(ENCODING).split(" ")

    if unseen_msg[0]:
        for letter in unseen_msg:
            attachments = []
            res, msg = imap.uid("fetch", letter, "(RFC822)")
            if res == "OK":
                msg = email.message_from_bytes(msg[0][1])
                msg_date = functions.date_parse(email.utils.parsedate_tz(msg["Date"]))
                msg_from = functions.from_subj_decode(msg["From"])
                msg_subj = functions.from_subj_decode(msg["Subject"])
                if msg["Message-ID"]:
                    msg_id = msg["Message-ID"].lstrip("<").rstrip(">")
                else:
                    msg_id = msg["Received"]
                if msg["Return-path"]:
                    msg_email = msg["Return-path"].lstrip("<").rstrip(">")
                else:
                    msg_email = msg_from

                letter_text = functions.get_letter_text(msg)
                attachments = functions.get_attachments(msg)

                post_text = functions.post_construct(
                    msg_subj, msg_from, msg_email, letter_text, attachments
                )
                if len(post_text) > 4000:
                    post_text = post_text[:4000]

                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)

                reply_id = loop.run_until_complete(
                    functions.send_message(config.bot_key, post_text, config.chat_id)
                )
                if config.send_attach:
                    functions.send_attach(msg, msg_subj, reply_id)

if __name__ == "__main__":
    try:
        main()
    except (Exception) as exp:
        text = str("ошибка: " + str(exp))
        print(traceback.format_exc())
        loop = asyncio.get_event_loop()
        loop.run_until_complete(functions.send_message(config.bot_key, text, config.chat_id))