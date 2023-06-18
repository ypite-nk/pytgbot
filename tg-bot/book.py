# -*- coding: utf-8 -*-
import random as r

class Book():
    def __init__(self):
        self.link = "".join(open("book/booklink.txt", "r", encoding="utf").readlines(0))

    def back(self):
        return r.choice(self.link)