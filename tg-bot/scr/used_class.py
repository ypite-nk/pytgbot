# -*- coding: utf-8 -*-
links = open("links/mem_links.txt", "r", encoding="utf-8").readlines(0)
len_data = len(links)

class Mem():
    def __init__(self, iden):
        self.id = int(iden)
        self.link = links[self.id]
        with open("count/likecount.txt", "r", encoding="utf-8") as lc:
            self.like_count = lc.readlines(0)[self.id]
        with open("count/dislikecount.txt", "r", encoding="utf-8") as dlc:
            self.dislike_count = dlc.readlines(0)[self.id]
        self.raitng = int(self.like_count) - int(self.dislike_count)

    def update(self):
        with open("count/likecount.txt", "r", encoding="utf-8") as lc:
            self.like_count = lc.readlines(0)[self.id]
        with open("count/dislikecount.txt", "r", encoding="utf-8") as dlc:
            self.dislike_count = dlc.readlines(0)[self.id]

    def data(self):
        self.update()
        self.list = [self.link, self.raitng, self.like_count, self.dislike_count]
        return self.list

    def change_raiting(self, like_count, dislike_count):
        self.update()
        with open("count/likecount.txt", "r",  encoding="utf-8") as file:
            Like = file.readlines()
            Like[self.id] = like_count
        with open("count/likecount.txt", "w",  encoding="utf-8") as file:
            print(str(Like))
            for i in range(len_data):
                if Like[i] == like_count:
                    file.write(str(Like[i]) + "\n")
                    print(str(Like[i]) + "\n")
                else:
                    file.write(str(Like[i]))

        with open("count/dislikecount.txt", "r",  encoding="utf-8") as file:
            Dislike = file.readlines()
            Dislike[self.id] = dislike_count
        with open("count/dislikecount.txt", "w",  encoding="utf-8") as file:
            for i in range(len_data):
                if Dislike[i] == dislike_count:
                    file.write(str(Dislike[i]) + "\n")
                else:
                    file.write(str(Dislike[i]))

        self.like_count = like_count
        self.dislike_count = dislike_count

        self.raiting = int(self.like_count) - int(self.dislike_count)
'''
                                    FOR ANY DATA BLOCK
class Data():
    def __init__(self, iden, link):
        self.id = int(iden)
        self.link = link

    def return_link(self):
        return self.link

'''