# -*- coding: utf-8 -*-
linksphoto = open("menu/more/fun/photo/links.txt", "r", encoding="utf-8").readlines(0)
len_data_photo = len(linksphoto)

class MemPhoto():
    def __init__(self, uid: int):
        self.id = int(uid)
        self.link = linksphoto[self.id]
        with open("menu/more/fun/photo/likecount.txt", "r", encoding="utf-8") as lc:
            self.like_count = lc.readlines(0)[self.id]
        with open("menu/more/fun/photo/dislikecount.txt", "r", encoding="utf-8") as dlc:
            self.dislike_count = dlc.readlines(0)[self.id]
        self.raitng = int(self.like_count) - int(self.dislike_count)

    def update(self):
        with open("menu/more/fun/photo/likecount.txt", "r", encoding="utf-8") as lc: self.like_count = lc.readlines(0)[self.id]
        with open("menu/more/fun/photo/dislikecount.txt", "r", encoding="utf-8") as dlc: self.dislike_count = dlc.readlines(0)[self.id]

    def data(self):
        self.update()
        return [self.link, self.raitng, self.like_count, self.dislike_count]

    def change_raiting(self, like_count, dislike_count):
        self.update()
        with open("menu/more/fun/photo/likecount.txt", "r",  encoding="utf-8") as file:
            Like = file.readlines()
            Like[self.id] = like_count
        with open("menu/more/fun/photo/likecount.txt", "w",  encoding="utf-8") as file:
            for i in range(len_data_photo):
                if Like[i] == like_count: file.write(str(Like[i]) + "\n")
                else: file.write(str(Like[i]))

        with open("menu/more/fun/photo/dislikecount.txt", "r",  encoding="utf-8") as file:
            Dislike = file.readlines()
            Dislike[self.id] = dislike_count
        with open("menu/more/fun/photo/dislikecount.txt", "w",  encoding="utf-8") as file:
            for i in range(len_data_photo):
                if Dislike[i] == dislike_count: file.write(str(Dislike[i]) + "\n")
                else: file.write(str(Dislike[i]))

        self.like_count = like_count
        self.dislike_count = dislike_count
        self.raiting = int(self.like_count) - int(self.dislike_count)