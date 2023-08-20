﻿# -*- coding: utf-8 -*-
from telegram import InlineKeyboardButton as IKB

backmenu = IKB("Меню", callback_data="/back")
backmenu2 = IKB("Меню", callback_data="more")
back = [[backmenu]]

rap = [
    [
    IKB("50 Cent", callback_data="50 Cent"), IKB("Lil Peep", callback_data="Lil Peep"),
    IKB("Egor Creed", callback_data="Egor Creed"), IKB("100 gecs", callback_data="100 gecs"),
    IKB("Snoop Dogg", callback_data="dog")],
    [IKB("<<<", callback_data="fun"), backmenu]
    ]

start_key = [
    [IKB("Профиль", callback_data="profile"), IKB("Город", callback_data="mycity"), IKB("Магазин", callback_data="shop")],
    [IKB("Банк", callback_data="bank")],
    [IKB("Проекты", callback_data="projects"), IKB("Соцсети", callback_data="social")],
    [IKB("Обратная связь", callback_data="helper"), IKB("Версия", callback_data="info"), IKB(">>>", callback_data="more")]
    ]

more = [
    [IKB("Стикерпаки", callback_data="packs"), IKB("Развлечения", callback_data="fun"), IKB("Боты", callback_data="bots")],
    [IKB("Образование", callback_data="learn")],
    [IKB("<<<", callback_data="/back"), IKB("Поддержать", callback_data="donate")]
    ]

profile = [
    [IKB("Изменить", callback_data="profile_change"), IKB("Купить VIP", callback_data="buyvip"), IKB("Рейтинг", callback_data="raiting")],
    [backmenu]
    ]

profile_change = [
    [IKB("Никнейм", callback_data="!changer_nickname"), IKB("Имя", callback_data="!changer_name")],
    [IKB("Интересы", callback_data="!changer_buisness"), IKB("День рождения", callback_data="!changer_birthday")],
    [IKB("<<<", callback_data="profile"), backmenu]
    ]

profile_back = [[IKB("<<<", callback_data="profile")]]

changerback = [[IKB("❌Отмена❌", callback_data="discard")]]

bots = [
    [IKB("ch:помощник", url="https://t.me/ch_helper_bot"), IKB("ChatGPT", url="https://t.me/gptdevbot?start=1086638338"), IKB("LeakedCheck", url="https://t.me/LeackedCheck_bot?start=qgSPpU")],
    [IKB("<<<", callback_data="more")],
    ]

commands_out = [
    [IKB("<<<", callback_data="more"), backmenu]
    ]

learns = [
    [IKB("Образование", callback_data="learning"), IKB("Книги", callback_data="books")],
    [IKB("<<<", callback_data="more"), backmenu]
    ]

learn = [
    [IKB("IT", callback_data="it"), IKB("3D", callback_data="3d"), IKB("Языки", callback_data="lang")],
    [IKB("<<<", callback_data="learn"), backmenu]
    ]

lang = [[IKB("Английский", callback_data="learn_eng"), IKB("Польский", callback_data="learn_pol")],
        [IKB("<<<", callback_data="learn"), IKB("Немецкий", callback_data="learn_dts")]]

booklist = [[IKB("<<<", callback_data="backbook1"), backmenu]]

booklist1 = [
    [IKB("Классика", callback_data="classic"), IKB("Зарубежные", callback_data="foreign"), IKB("Русская", callback_data="rus")],
    [IKB("Детективы", callback_data="detective"), IKB("Фэнтези", callback_data="fantasy"), IKB("Фантастика", callback_data="fantastik")],
    [IKB("Проза", callback_data="prose"), IKB("Ужасы", callback_data="scary"), IKB("Приключения", callback_data="adv")],
    [IKB("<<<", callback_data="learn"), IKB(">>>", callback_data="booklist2")]
    ]

booklist2 = [
    [IKB("Боевики", callback_data="action"), IKB("Повести", callback_data="stories"), IKB("Поэзия", callback_data="poem")],
    [IKB("Научпоп", callback_data="science"), IKB("Психология", callback_data="psycho"), IKB("Комиксы", callback_data="comics")],
    [IKB("Манга", callback_data="manga"), IKB("Эзотерика", callback_data="esotericism"), IKB("Культура", callback_data="culture")],
    [IKB("<<<", callback_data="backbook1"), IKB(">>>", callback_data="booklist3")]
    ]

booklist3 = [
    [IKB("Романы", callback_data="romans"), IKB("Справочники", callback_data="bookfaq"), IKB("Дом", callback_data="home")],
    [IKB("Религия", callback_data="religion"), IKB("Юмор", callback_data="funny"), IKB("Бизнес", callback_data="buisness")],
    [IKB("<<<", callback_data="backbook2"), backmenu]
    ]

genreskb = [[IKB("<<<", callback_data="backbook1"), backmenu]]

it = [
    [IKB("Программирование", callback_data="coding")], [IKB("Веб-разработка", callback_data="web")],
    [IKB("Сис. Администрирование", callback_data="admin"), IKB("Базы данных", callback_data="sql")],
    [IKB("<<<", callback_data="learning"), backmenu]
    ]

coding = [
    [IKB("Python", callback_data="py"), IKB("C++", callback_data="+"), IKB("JavaScript", callback_data="js")],
    [IKB("<<<", callback_data="it"), backmenu]
    ]

python = [
    [IKB(text="Материалы", url="https://www.python.org/")], #                                                                                            PYTHON
    [IKB("<<<", callback_data="coding"), backmenu]
    ]

cpp = [
    [IKB(text="Материалы", url="https://learn.microsoft.com/ru-ru/cpp/cpp/cpp-language-reference?view=msvc-170")],#                                         C++
    [IKB("<<<", callback_data="coding"), backmenu]
    ]

js = [
    [IKB(text="Материалы", url="https://learn.javascript.ru/")],#                                                                                            JAVA SCRIPT
    [IKB("<<<", callback_data="coding"), backmenu]
    ]

web = [
    [IKB("HTML&CSS", callback_data="html_m"), IKB("PHP", callback_data="php"), IKB("django", callback_data="django")],
    [IKB("<<<", callback_data="it"), backmenu]
    ]

html_m = [
    [IKB(text="Материалы", url="https://developer.mozilla.org/ru/docs/Learn/Getting_started_with_the_web/HTML_basics")],#                                HTML
    [IKB("<<<", callback_data="web"), backmenu]
    ]

php = [
    [IKB(text="Материалы", url="https://developer.mozilla.org/ru/docs/Learn/Getting_started_with_the_web/HTML_basics")],#                                   PHP
    [IKB("<<<", callback_data="web"), backmenu]
    ]

django = [
    [IKB(text="Материалы", url="https://developer.mozilla.org/ru/docs/Learn/Getting_started_with_the_web/HTML_basics")],#                                DJANGO
    [IKB("<<<", callback_data="web"), backmenu]
    ]

admin = [
    [IKB("Системный администратор", callback_data="s_admin"), IKB("Data Sciens", callback_data="data_sciens")],
    [IKB("<<<", callback_data="it"), backmenu]
    ]

s_admin = [
    [IKB(text="Материалы", url="https://habr.com/ru/companies/ruvds/articles/486204/")],#                                                               ADMIN
    [IKB("<<<", callback_data="admin"), backmenu]
    ]

data_sciens = [
    [IKB(text="Материалы", url="https://habr.com/ru/articles/668428/")],#                                                                           DATA SCIENS
    [IKB("<<<", callback_data="admin"), backmenu]
    ]

sql = [
    [IKB(text="Материалы", url="https://habr.com/ru/articles/564390/")],#                                                                                   SQL
    [IKB("<<<", callback_data="it"), backmenu]
    ]

modeling = [
    [IKB(text="Материалы", url="https://habr.com/ru/companies/otus/articles/675410/")],#                                                               MODELING
    [IKB("<<<", callback_data="learning"), backmenu]
    ]

support = [
    [IKB(text="Boosty", url="https://boosty.to/ypite"), IKB(text="DonationAlerts", url="https://www.donationalerts.com/r/ypiter_nk")],
    [IKB("<<<", callback_data="more"), backmenu]
    ]

key = [
    [IKB("rap", callback_data="rap"), IKB("Фото мем", callback_data="photomem"), IKB("Текстовые квесты", callback_data="quests")],
    [IKB("<<<", callback_data="more"), backmenu]
    ]

link = [
    [IKB(text="Канал Тг", url="https://t.me/ypite"), IKB(text="Группа Вк", url="https://vk.com/cloud_ypiter"), IKB(text="GitHub", url="https://github.com/ypite-nk")],
    [IKB(text="Вконтакте", url="https://vk.com/ypite"), IKB(text="Телеграмм", url="https://t.me/r_ypite")],
    [IKB(text="Youtube", url="https://www.youtube.com/channel/UCQunVaPHyI2MvS0rU56_MA"), IKB(text="TikTok", url="https://vm.tiktok.com/ZT81sSebh/"), IKB(text="Twitch", url="https://www.twitch.tv/ypiternk")],
    [IKB("<<<", callback_data="/back")]
    ]

def mem(LikeCount, DisLikeCount):
    mem = [
        [IKB("Мем", callback_data="photomem"), IKB("👍  " + str(LikeCount), callback_data="m_like-" + str(LikeCount)), IKB("👎  " + str(DisLikeCount), callback_data="m_dislike-" + str(DisLikeCount))],
        [IKB("<<<", callback_data="fun"), backmenu]
        ]
    return mem

projects = [
    [IKB("Список проектов", callback_data="projlist"), IKB("Дополнительно...", callback_data="profmore")],
    [backmenu]
    ]

quests = [
    [IKB("Квест 1", callback_data="quest1"), IKB("квест 2", callback_data="quest2")],
    [IKB("<<<", callback_data="fun")]
    ]

city_admin = [[IKB("Изменить", callback_data="city_change"), IKB("Постройка", callback_data="create")],
              [backmenu]]

BCB = IKB("<<<", callback_data="cityBack")
backcity = [[IKB("<<<", callback_data="cityBack")]]

city_change = [
    [IKB("Имя", callback_data="!changer_cityname"), IKB("Герб", callback_data="!changer_sign"), IKB("Гимн", callback_data="!changer_gymn")],
    [BCB, IKB("Мэра", callback_data="!changer_mayor"), IKB("Историю", callback_data="!changer_history"), IKB("Флаг", callback_data="!changer_flag")]
    ]

city_createtypes = [
                    [IKB("Жилье", callback_data="house"), IKB("Коммерция", callback_data="commercical")],
                    [IKB("Промышленность", callback_data="industry")],
                    [BCB, backmenu]
                   ]

city_create_house = [
                     [IKB("Малый район", callback_data="house1")],
                     [IKB("Средний район", callback_data="house2")],
                     [IKB("Большой район", callback_data="house3")],
                     [BCB, backmenu]
                    ]

city_create_commercical = [
                     [IKB("Малый район", callback_data="comm1")],
                     [IKB("Средний район", callback_data="comm2")],
                     [IKB("Большой район", callback_data="comm3")],
                     [BCB, backmenu]
                    ]

city_create_industry = [
                     [IKB("Электроэнергия", callback_data="ind1")],
                     [IKB("Водоснабжение", callback_data="ind2")],
                     [IKB("Товаропроизводство", callback_data="ind3")],
                     [BCB, backmenu]
                    ]

city_create_ind1 = [
                     [IKB("Малая станция", callback_data="1indenergy")],
                     [IKB("Средняя станция", callback_data="2indenergy")],
                     [IKB("Большая станция", callback_data="3indenergy")],
                     [BCB, backmenu]
                    ]

city_create_ind2 = [
                     [IKB("Малая станция", callback_data="1indwater")],
                     [IKB("Средняя станция", callback_data="2indwater")],
                     [IKB("Большая станция", callback_data="3indwater")],
                     [BCB, backmenu]
                    ]

city_create_ind3 = [
                     [IKB("Малый район", callback_data="1indmat")],
                     [IKB("Средний район", callback_data="2indmat")],
                     [IKB("Большой район", callback_data="3indmat")],
                     [BCB, backmenu]
                    ]

def shops(callback):
    return [
            [IKB("За рубли", callback_data=f"buy=R={callback}"), IKB("За Юшки", callback_data=f"buy=Y={callback}")],
            [IKB("<<<", callback_data="shop")]
            ]

def buy_R(callback, cost):
    return [
        [IKB(f"Купить {callback} за {cost}₽ с помощью DonationAlerts",
             url="https://www.donationalerts.com/r/ypiter_nk")],
        [IKB("<<<", callback_data=f"shop={callback}")]
        ]

def buy_Y(callback, cost):
    return [
        [IKB(f"Купить {callback} за {cost}Ю",
             callback_data=f"shopbuy:{callback}:{cost}")],
        [IKB("<<<", callback_data=f"shop={callback}")]
        ]

shop = [
    [IKB("VIP", callback_data="shop=VIP"), IKB("JxSpeed", callback_data="shop=JxSpeed"), IKB("MacroMotor", callback_data="shop=MacroMotor"), IKB("LifeX10", callback_data="shop=LifeX10")],
    [backmenu]
    ]

bankstart = [
    [IKB("Начать тест! (19Ю)", callback_data="start_test_19")],
    [backmenu]
    ]

test1 = [
    [IKB("Вариант 1", callback_data="1#1"), IKB("Вариант 2", callback_data="1#2")],
    [IKB("❌Отмена теста❌", callback_data="discard_test")]
    ]

test2 = [
    [IKB("Вариант 1", callback_data="2#1"), IKB("Вариант 2", callback_data="2#2")],
    [IKB("Вариант 3", callback_data="2#3"), IKB("Вариант 4", callback_data="2#4")],
    [IKB("❌Отмена теста❌", callback_data="discard_test")]
    ]

test3 = [
    [IKB("Вариант 1", callback_data="3#1"), IKB("Вариант 2", callback_data="3#2")],
    [IKB("Вариант 3", callback_data="3#3"), IKB("Вариант 4", callback_data="3#4")],
    [IKB("❌Отмена теста❌", callback_data="discard_test")]
    ]

testC = [
    [IKB("Перейти в банк...", callback_data="bank")]
    ]

bank = [[IKB("Профиль", callback_data="mybank"), IKB("Графики", callback_data="bank_graphic")],
        [IKB("Информация", callback_data="bank_stat"), IKB("Акции", callback_data="bank_actions")],
        [backmenu, IKB("Конвертер", callback_data="bank_convert")]]