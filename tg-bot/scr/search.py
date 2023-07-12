# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def search(update, context):
    prefix, *value = update.message.text.split(" ")
    query = ""
    for i in value:
        query += i
    url = "https://yandex.ru/search/"
    params = {
        "text": query
        }
    r = requests.get(url, params=params)

    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        results = soup.find_all('a', href=True)
        result_texts = [result.text for result in results]
        print(result_texts)
        update.message.reply_text("Результаты поиска:\n" + result_texts)
    else:
        return None