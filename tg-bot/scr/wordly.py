# -*- coding: utf-8 -*-

import random

class Wordly():
    def __init__(self, uid: str, identificator: int = None) -> None:
        self._uid = uid
        self.id = identificator
        self.checkSymbol = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.word_check_out = []
        self.export = ""
        self.output = "Напишите предпологаемое слово, состоящее из 5 букв:\n\n"
        # Get words-list, daily-word, user-try and memory-list
        with open("base/wordly/words.txt", "r", encoding="utf-8") as file: self.words = file.readlines(0)
        with open("base/wordly/memory.txt", "r", encoding="utf-8") as file: self.memory = file.readlines(0)
        with open("base/wordly/daily.txt", "r", encoding="utf-8") as file: self.daily = file.readlines(0)
        # Import user-profile
        from login import User
        self.user = User(self._uid)
        # Check active word-id
        if self.id == None: self.id = random.randint(0, len(self.words))
        # Check non-retry word
        while self.words[self.id].replace("\n", "") in self.memory and self.words[self.id].replace("\n", "") != self.daily:
            self.id = random.randint(0, len(self.words))
        with open("base/wordly/daily.txt", "w", encoding="utf-8") as file: file.write(self.words[self.id].replace("\n", ""))
        # Convert memory to 1 str for write-def remember(self)
        for word in self.memory: export += word
        # split word to symbol; write in word_check_out
        for symbol in self.words: self.word_check_out.append(symbol.upper())

    def check_word(self, input_text: str):
        # Check Try-options user
        self.profile = self.user.get_user_profile()
        if self.profile['Попытки'] == 0:
            self.output = "У вас закончились попытки!\nВернитесь завтра или купите LifeX10 в магазине!"
            return False
        # split user-word to symbol; write in input_text_check
        input_text_check = []
        for symbol in input_text: input_text_check.append(symbol.upper())
        # Check warn-symbol; return None
        for symbol in self.checkSymbol:
            if symbol in input_text_check: return None
        # Check length user-word
        if len(input_text_check) > 5: return None
        
        self.export_checkout = ""
        self.export_count = ""
        
        self.checkout = []
        self.counter = []
        # Get user-Counter
        with open(f"base/wordly/counter{self._uid}.txt", "r", encoding="utf-8") as file:
            file = file.readlines(0)
            for count in file: self.counter.append(int(count.replace("\n", "")))
        #Get user-Check
        with open(f"base/wordly/checkout{self._uid}.txt", "r", encoding="utf-8") as file:
            file = file.readlines(0)
            for count in file: self.checkout.append(int(count.replace("\n", "")))
        # Check  ==
        for i in range(5):
            if input_text_check[i] == self.word_check_out[i]: self.checkout[i] = 1
            elif input_text_check[i] in self.word_check_out: self.checkout[i] = -1
        # Write output
        for i in self.checkout:
            if i == 0:
                output += f"{i+1}) Буквы {input_text_check[i].upper()} нет в этом слове\n"
                self.counter[1] += 1

            elif i == 1:
                output += f"{+1}) Буква {input_text_check[i].upper()} есть в этом слове и стоит на этом месте\n"
                self.counter[0] += 1
                self.counter[1] += 1

            elif i == -1:
                output += f"{+1}) Буква {input_text_check[i].upper()} есть в этом слове но стоит не на этом месте\n"
                self.counter[1] += 1
                
        # Check 5 output write's for win
        if self.counter[0] == 5:
            self.output += f"\n Поздравляю! Вы отгадали слово! Вам было начислено 10 Юшек"

            self.profile['Попытки'] -= 1
            self.profile['Юшки'] += 10
            self.user.write_user_profile(self.profile)
            
        if self.counter[1] == 5:
            self.output = "К сожалению, вы проиграли! Попробуйте еще раз, я выдал вам дополнительную попытку!"

            self.user.write_user_profile(self.profile)
            
        for i in self.counter: self.export_count += f"{str(i)}\n"
        with open(f"base/wordly/counter{self._uid}.txt", "w", encoding="utf-8") as file: file.write(self.export_count)
        for i in self.checkout: self.export_checkout += f"{str(i)}\n"
        with open(f"base/wordly/checkout{self._uid}.txt", "w", encoding="utf-8") as file: file.write(self.export_checkout)

        return True
    
    def set_word(self, word_id: int):
        with open("base/wordly/daily.txt", "w", encoding="utf-8") as file: file.write(self.words[word_id])