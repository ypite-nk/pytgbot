# -*- coding: utf-8 -*-

import random
from os import path

class Wordly():
    def __init__(self, uid: str, identificator: int = None) -> None:
        
        self._uid = uid
        self.id = identificator
        self.checkSymbol = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.word_check_out = []
        self.output = "Напишите предпологаемое слово, состоящее из 5 букв:\n\n"

        with open("base/wordly/words.txt", "r", encoding="utf-8") as file: self.words = file.readlines(0)
        with open("base/wordly/daily.txt", "r", encoding="utf-8") as file: self.daily = file.readlines(0)
        with open("base/wordly/memory.txt", "r", encoding="utf-8") as file: self.memory = file.readlines(0)

        if self._uid is not None:
            from login import User
            self.user = User(self._uid)
            
        if self.id == None: self.id = random.randint(0, len(self.words))

        if self.daily[0].replace("\n", "") == "None":

            while self.words[self.id].replace("\n", "") in self.memory and self.words[self.id].replace("\n", "") != self.daily:
                self.id = random.randint(0, len(self.words))

            with open("base/wordly/daily.txt", "w", encoding="utf-8") as file:
                file.write(self.words[self.id].replace("\n", ""))

            for symbol in self.words[self.id].replace("\n", ""): self.word_check_out.append(symbol.upper())

        else:
            for symbol in self.daily[0].replace("\n", ""): self.word_check_out.append(symbol.upper())

        if not path.exists(f"base/wordly/counter{self._uid}.txt"):
            with open(f"base/wordly/counter{self._uid}.txt", "w+", encoding="utf-8") as file: file.write("0\n0")
        if not path.exists(f"base/wordly/checkout{self._uid}.txt"):
            with open(f"base/wordly/checkout{self._uid}.txt", "w+", encoding="utf-8") as file: file.write("0\n0\n0\n0\n0")

    def check_word(self, input_text: str):

        self.profile = self.user.get_user_profile()
        if self.profile['Попытки'] == 0:
            self.output = "У вас закончились попытки!\nВернитесь завтра или купите LifeX10 в магазине!"
            return False

        input_text_check = []
        for symbol in input_text: input_text_check.append(symbol.upper())

        for symbol in self.checkSymbol:
            if symbol in input_text_check: return None

        if len(input_text_check) > 5: return None
        
        self.export_checkout = ""
        self.export_count = ""
        
        self.checkout = []
        self.counter = []

        with open(f"base/wordly/counter{self._uid}.txt", "r", encoding="utf-8") as file:
            file = file.readlines(0)
            for count in file: self.counter.append(int(count.replace("\n", "")))

        with open(f"base/wordly/checkout{self._uid}.txt", "r", encoding="utf-8") as file:
            file = file.readlines(0)
            for count in file: self.checkout.append(int(count.replace("\n", "")))

        for i in range(5):
            if input_text_check[i] == self.word_check_out[i]: self.checkout[i] = 1
            elif input_text_check[i] in self.word_check_out: self.checkout[i] = -1

        for i in range(len(self.checkout)):
            if self.checkout[i] == 0:
                self.output += f"{i+1}) Буквы {input_text_check[i].upper()} нет в этом слове\n"

            elif self.checkout[i] == 1:
                self.output += f"{+1}) Буква {input_text_check[i].upper()} есть в этом слове и стоит на этом месте\n"
                self.counter[0] += 1

            elif self.checkout[i] == -1:
                self.output += f"{+1}) Буква {input_text_check[i].upper()} есть в этом слове но стоит не на этом месте\n"
        self.counter[1] += 1

        if self.counter[0] == 5:
            self.output += f"\n Поздравляю! Вы отгадали слово! Вам было начислено 10 Юшек"

            self.profile['Попытки'] -= 1
            self.profile['Юшки'] += 10
            self.user.write_user_profile(self.profile)
            
            with open(f"base/wordly/counter{self._uid}.txt", "w", encoding="utf-8") as file: file.write("0\n0")
            with open(f"base/wordly/checkout{self._uid}.txt", "w", encoding="utf-8") as file: file.write("0\n0\n0\n0\n0")
            
            return True
            
        if self.counter[1] == 5:
            self.output = "К сожалению, вы проиграли! Попробуйте еще раз, я выдал вам дополнительную попытку!"

            self.user.write_user_profile(self.profile)
            
            with open(f"base/wordly/counter{self._uid}.txt", "w", encoding="utf-8") as file: file.write("0\n0")
            with open(f"base/wordly/checkout{self._uid}.txt", "w", encoding="utf-8") as file: file.write("0\n0\n0\n0\n0")
            
            return True
            
        with open(f"base/wordly/counter{self._uid}.txt", "w", encoding="utf-8") as file: file.write("0\n"+str(self.counter[1]))
        
        #for i in self.checkout: self.export_checkout += f"{str(i)}\n"
        with open(f"base/wordly/checkout{self._uid}.txt", "w", encoding="utf-8") as file: file.write("0\n0\n0\n0\n0")

        return True
    
    def set_word(self, word: str) -> None:
        with open("base/wordly/daily.txt", "w", encoding="utf-8") as file: file.write(word)
        
    def update_word(self) -> None:
        if self._uid == None: self.id = random.randint(0, len(self.words))
        
        while self.words[self.id].replace("\n", "") in self.memory and self.words[self.id].replace("\n", "") != self.daily:
            self.id = random.randint(0, len(self.words))

        with open("base/wordly/daily.txt", "w", encoding="utf-8") as file: file.write(self.words[self.id].replace("\n", ""))