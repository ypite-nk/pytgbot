# -*- coding: utf-8 -*-
from telegram import InlineKeyboardButton

menudel = InlineKeyboardButton("Меню", callback_data="/backdel")
backdel = [[menudel]]

ypiterFAQ = [[InlineKeyboardButton("Общее", callback_data='all'), InlineKeyboardButton("Рецензии", callback_data='marks')],
             [InlineKeyboardButton("14 лет", callback_data='14'), InlineKeyboardButton("15 лет", callback_data='15')],
             [InlineKeyboardButton("Назад", callback_data="faq"), menudel]]

FAQ = [[InlineKeyboardButton("О боте", callback_data="botinfo"), InlineKeyboardButton("О ypiter", callback_data="ypiinfo")],
       [InlineKeyboardButton("Команды", callback_data="commands"), menudel]]

rap = [[InlineKeyboardButton("50 Cent", callback_data="50 Cent"), InlineKeyboardButton("Lil Peep", callback_data="Lil Peep"),
        InlineKeyboardButton("Egor Creed", callback_data="Egor Creed"), InlineKeyboardButton("100 gecs", callback_data="100 gecs"),
        InlineKeyboardButton("Snoop Dogg", callback_data="dog")],
       [InlineKeyboardButton("...назад", callback_data="/fun"), menudel]]

start_key = [[InlineKeyboardButton("FAQ", callback_data="faq"), InlineKeyboardButton("Инфо", callback_data="info"), InlineKeyboardButton("Команды", callback_data="commands")],
             [InlineKeyboardButton("Обратная связь", callback_data="helper")]]

def set_mark(list):
    marks = []
    marks_span = []
    nextline = False
    for i in list:
        if "-" in i:
            if not nextline:
                marks_span.append(InlineKeyboardButton(i.split("-")[1] + "::" + i.split("-")[0], callback_data=i))
                if int(i.split("-")[1]) == 4:
                    nextline = True
            if nextline:
                marks.append(marks_span)
                marks_span = []
                nextline = False
    if not nextline:
        marks.append(marks_span)
    marks.append([InlineKeyboardButton("...назад", callback_data="ypiinfo"), menudel, InlineKeyboardButton("Оставить рецензию...", callback_data="getmark")])
    return marks

commands_out = [[InlineKeyboardButton("Команды", callback_data="commands"), menudel]]

learns = [[InlineKeyboardButton("Образование", callback_data="learning"), InlineKeyboardButton("Книги", callback_data="books")],
             [menudel]]

learn = [[InlineKeyboardButton("IT", callback_data="it"), InlineKeyboardButton("3D", callback_data="3d")],
         [InlineKeyboardButton("...назад", callback_data="learn"), menudel]]

booklist = [[InlineKeyboardButton("...назад", callback_data="backbook1"), menudel]]

booklist1 = [[InlineKeyboardButton("Классика", callback_data="classic"), InlineKeyboardButton("Зарубежные", callback_data="foreign"), InlineKeyboardButton("Русская", callback_data="rus")],
        [InlineKeyboardButton("Детективы", callback_data="detective"), InlineKeyboardButton("Фэнтези", callback_data="fantasy"), InlineKeyboardButton("Фантастика", callback_data="fantastik")],
        [InlineKeyboardButton("Проза", callback_data="prose"), InlineKeyboardButton("Ужасы", callback_data="scary"), InlineKeyboardButton("Приключения", callback_data="adv")],
        [InlineKeyboardButton("...назад", callback_data="learn"), InlineKeyboardButton("Далее...", callback_data="booklist2")]]

booklist2 = [[InlineKeyboardButton("Боевики", callback_data="action"), InlineKeyboardButton("Повести", callback_data="stories"), InlineKeyboardButton("Поэзия", callback_data="poem")],
        [InlineKeyboardButton("Научпоп", callback_data="science"), InlineKeyboardButton("Психология", callback_data="psycho"), InlineKeyboardButton("Комиксы", callback_data="comics")],
        [InlineKeyboardButton("Манга", callback_data="manga"), InlineKeyboardButton("Эзотерика", callback_data="esotericism"), InlineKeyboardButton("Культура", callback_data="culture")],
        [InlineKeyboardButton("...назад", callback_data="backbook1"), InlineKeyboardButton("Далее...", callback_data="booklist3")]]

booklist3 = [[InlineKeyboardButton("Романы", callback_data="romans"), InlineKeyboardButton("Словари", callback_data="books"), InlineKeyboardButton("Справочники", callback_data="bookfaq")],
        [InlineKeyboardButton("Религия", callback_data="religion"), InlineKeyboardButton("Юмор", callback_data="funny"), InlineKeyboardButton("Рассказы", callback_data="tale")],
        [InlineKeyboardButton("Для детей", callback_data="kids"), InlineKeyboardButton("Бизнес", callback_data="buisness"), InlineKeyboardButton("Дом", callback_data="home")],
        [InlineKeyboardButton("...назад", callback_data="backbook2"), menudel]]

class GenresKeyboard():
    def __init__(self, path, filename):
        self.file = open(path + filename + ".txt", "r", encoding="utf-8").readlines(0)
        self.name_link = []
        for id_link in self.file:
            self.id, self.link = id_link.split("-")
            self.name_link.append(str(self.id.replace("\n", "")))
            self.name_link.append(str(self.link.replace("\n", "")))
        
        self.keyboard = [[InlineKeyboardButton(text=self.name_link[0], url=self.name_link[1]), InlineKeyboardButton(text=self.name_link[2], url=self.name_link[3]),
                          InlineKeyboardButton(text=self.name_link[4], url=self.name_link[5]), InlineKeyboardButton(text=self.name_link[6], url=self.name_link[7]),
                          InlineKeyboardButton(text=self.name_link[8], url=self.name_link[9])
                          ],
                         [InlineKeyboardButton(text=self.name_link[10], url=self.name_link[11]), InlineKeyboardButton(text=self.name_link[12], url=self.name_link[13]),
                          InlineKeyboardButton(text=self.name_link[14], url=self.name_link[15]), InlineKeyboardButton(text=self.name_link[16], url=self.name_link[17]),
                          InlineKeyboardButton(text=self.name_link[18], url=self.name_link[19])
                          ],
                          [InlineKeyboardButton("...назад", callback_data="backbook1"), menudel]
                         ]

file = open("learn/name.txt", "r", encoding="utf-8").readlines(0)
pathlist = ["learn/book/"]
for name in file:
    pathlist.append(str(name.replace("\n", "")))
genreskb = {'action' : GenresKeyboard(pathlist[0], pathlist[1]).keyboard, 'adv' : GenresKeyboard(pathlist[0], pathlist[2]).keyboard,
            'bookfaq' : GenresKeyboard(pathlist[0], pathlist[3]).keyboard, 'books' : GenresKeyboard(pathlist[0], pathlist[4]).keyboard,
            'buisness' : GenresKeyboard(pathlist[0], pathlist[5]).keyboard, 'classic' : GenresKeyboard(pathlist[0], pathlist[6]).keyboard,
            'comics' : GenresKeyboard(pathlist[0], pathlist[7]).keyboard, 'culture' : GenresKeyboard(pathlist[0], pathlist[8]).keyboard,
            'detective' : GenresKeyboard(pathlist[0], pathlist[9]).keyboard, 'esotericism' : GenresKeyboard(pathlist[0], pathlist[10]).keyboard,
            'fantastik' : GenresKeyboard(pathlist[0], pathlist[11]).keyboard, 'fantasy' : GenresKeyboard(pathlist[0], pathlist[12]).keyboard,
            'foreign' : GenresKeyboard(pathlist[0], pathlist[13]).keyboard, 'funny' : GenresKeyboard(pathlist[0], pathlist[14]).keyboard,
            'home' : GenresKeyboard(pathlist[0], pathlist[15]).keyboard, 'kids' : GenresKeyboard(pathlist[0], pathlist[16]).keyboard,
            'manga' : GenresKeyboard(pathlist[0], pathlist[17]).keyboard, 'poem' : GenresKeyboard(pathlist[0], pathlist[18]).keyboard,
            'prose' : GenresKeyboard(pathlist[0], pathlist[19]).keyboard, 'psycho' : GenresKeyboard(pathlist[0], pathlist[20]).keyboard,
            'religion' : GenresKeyboard(pathlist[0], pathlist[21]).keyboard, 'romans' : GenresKeyboard(pathlist[0], pathlist[22]).keyboard,
            'rus' : GenresKeyboard(pathlist[0], pathlist[23]).keyboard, 'scary' : GenresKeyboard(pathlist[0], pathlist[24]).keyboard,
            'science' : GenresKeyboard(pathlist[0], pathlist[25]).keyboard, 'stories' : GenresKeyboard(pathlist[0], pathlist[26]).keyboard,
            'tale' : GenresKeyboard(pathlist[0], pathlist[27]).keyboard
            }

it = [[InlineKeyboardButton("Программирование", callback_data="coding")], [InlineKeyboardButton("Веб-разработка", callback_data="web")],
      [InlineKeyboardButton("Сис. Администрирование", callback_data="admin"), InlineKeyboardButton("Базы данных", callback_data="sql")],
      [InlineKeyboardButton("...назад", callback_data="learning"), menudel]]

coding = [[InlineKeyboardButton("Python", callback_data="py"), InlineKeyboardButton("C++", callback_data="+"), InlineKeyboardButton("JavaScript", callback_data="js")],
          [InlineKeyboardButton("...назад", callback_data="it"), menudel]]

python = [[InlineKeyboardButton(text="Материалы", url="https://www.python.org/")], #                                                                                            PYTHON
          [InlineKeyboardButton("...назад", callback_data="coding"), menudel]]

cpp = [[InlineKeyboardButton(text="Материалы", url="https://learn.microsoft.com/ru-ru/cpp/cpp/cpp-language-reference?view=msvc-170")],#                                         C++
          [InlineKeyboardButton("...назад", callback_data="coding"), menudel]]

js = [[InlineKeyboardButton(text="Материалы", url="https://learn.javascript.ru/")],#                                                                                            JAVA SCRIPT
          [InlineKeyboardButton("...назад", callback_data="coding"), menudel]]

web = [[InlineKeyboardButton("HTML&CSS", callback_data="html_m"), InlineKeyboardButton("PHP", callback_data="php"), InlineKeyboardButton("django", callback_data="django")],
       [InlineKeyboardButton("...назад", callback_data="it"), menudel]]

html_m = [[InlineKeyboardButton(text="Материалы", url="https://developer.mozilla.org/ru/docs/Learn/Getting_started_with_the_web/HTML_basics")],#                                HTML
          [InlineKeyboardButton("...назад", callback_data="web"), menudel]]

php = [[InlineKeyboardButton(text="Материалы", url="https://developer.mozilla.org/ru/docs/Learn/Getting_started_with_the_web/HTML_basics")],#                                   PHP
          [InlineKeyboardButton("...назад", callback_data="web"), menudel]]

django = [[InlineKeyboardButton(text="Материалы", url="https://developer.mozilla.org/ru/docs/Learn/Getting_started_with_the_web/HTML_basics")],#                                DJANGO
          [InlineKeyboardButton("...назад", callback_data="web"), menudel]]

admin = [[InlineKeyboardButton("Системный администратор", callback_data="s_admin"), InlineKeyboardButton("Data Sciens", callback_data="data_sciens")],
          [InlineKeyboardButton("...назад", callback_data="it"), menudel]]

s_admin = [[InlineKeyboardButton(text="Материалы", url="https://habr.com/ru/companies/ruvds/articles/486204/")],#                                                               ADMIN
           [InlineKeyboardButton("...назад", callback_data="admin"), menudel]]

data_sciens = [[InlineKeyboardButton(text="Материалы", url="https://habr.com/ru/articles/668428/")],#                                                                           DATA SCIENS
          [InlineKeyboardButton("...назад", callback_data="admin"), menudel]]

sql = [[InlineKeyboardButton(text="Материалы", url="https://habr.com/ru/articles/564390/")],#                                                                                   SQL
       [InlineKeyboardButton("...назад", callback_data="it"), menudel]]

modeling = [[InlineKeyboardButton(text="Материалы", url="https://habr.com/ru/companies/otus/articles/675410/")],#                                                               MODELING
            [InlineKeyboardButton("...назад", callback_data="learning"), menudel]]

support = [[InlineKeyboardButton(text="Поддержать", url="https://www.donationalerts.com/r/ypiter_nk")],
               [InlineKeyboardButton("Команды", callback_data="commands"), menudel]]

key = [[InlineKeyboardButton("rap", callback_data="rap"), InlineKeyboardButton("Фото мем", callback_data="photomem"),
        InlineKeyboardButton("Видео мем", callback_data="videomem"), InlineKeyboardButton("Анекдоты", callback_data="jokes"),
        InlineKeyboardButton("Цитаты", callback_data="citaty")],
       [InlineKeyboardButton("Команды", callback_data="commands"), menudel]]

link = [[InlineKeyboardButton(text="Канал ТГ", url="https://t.me/ypite"), InlineKeyboardButton(text="Группа Вк", url="https://vk.com/cloud_ypiter"), InlineKeyboardButton(text="GitHub", url="https://github.com/ypite-nk")],
        [InlineKeyboardButton(text="Вконтакте", url="https://vk.com/ypite"), InlineKeyboardButton(text="Телеграмм", url="https://t.me/r_ypiter")],
        [InlineKeyboardButton(text="Youtube", url="https://www.youtube.com/channel/UCQunVaPHyI2MvS0rU56_MhA"), InlineKeyboardButton(text="TikTok", url="https://vm.tiktok.com/ZT81sSebh/")],
        [InlineKeyboardButton("Команды", callback_data="commands"), menudel]]

def mem(LikeCount, DisLikeCount):
    mem = [[InlineKeyboardButton("Мем", callback_data="photomem"),
        InlineKeyboardButton("👍  " + str(LikeCount), callback_data="like-" + str(LikeCount)),
        InlineKeyboardButton("👎  " + str(DisLikeCount), callback_data="dislike-" + str(DisLikeCount))],
       [InlineKeyboardButton("Назад", callback_data="/fun"), menudel]]

    return mem

vid = [[InlineKeyboardButton("Видео", callback_data="videomem")],
       [InlineKeyboardButton("Назад", callback_data="/fun"), menudel]]

jokes = [[InlineKeyboardButton("Анекдот", callback_data="jokes")],
         [InlineKeyboardButton("Назад", callback_data="/fun"), menudel]]

citaty = [[InlineKeyboardButton("Цитата", callback_data="citaty")],
          [InlineKeyboardButton("Назад", callback_data="/fun"), menudel]]