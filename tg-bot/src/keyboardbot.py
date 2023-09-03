# -*- coding: utf-8 -*-
from telegram import InlineKeyboardButton as IKB

back_to_menu_first_kb = IKB("Меню", callback_data="menu1")
back_to_menu_second_kb = IKB("Меню", callback_data="menu2")
back_to_menu_first = [[back_to_menu_first_kb]]
back_to_menu_second = [[back_to_menu_second_kb]]

class First_menu():
    def __init__(self):
        self.menu = {
            'menu1': [[IKB("Профиль", callback_data="profile"), IKB("Город", callback_data="city")],
                        [IKB("Магазин", callback_data="shop"), IKB("Банк", callback_data="bank")],
                        [IKB("Проекты", callback_data="project"), IKB("Соцсети", callback_data="social")],
                        [IKB("Обратная связь", callback_data="callback"), IKB("Версия", callback_data="version"), IKB(">>>", callback_data="menu2")]
                        ],

            'profile': [[IKB("Изменить профиль", callback_data="profile_change"), IKB("Глобальный Рейтинг", callback_data="raiting")],
                        [back_to_menu_first_kb]
                        ],

            'city': [[IKB("Изменить", callback_data="city_change"), IKB("Постройка", callback_data="!city_create")],
                     [back_to_menu_first_kb]
                     ],

            'shop': [[IKB("VIP", callback_data="shop=VIP"), IKB("JxSpeed", callback_data="shop=JxSpeed"), IKB("MacroMotor", callback_data="shop=MacroMotor"), IKB("LifeX10", callback_data="shop=LifeX10")],
                     [back_to_menu_first_kb]
                     ],

            'bank': [[IKB("Профиль", callback_data="bank_my"), IKB("Графики", callback_data="bank_graphic")],
                     [IKB("Информация", callback_data="bank_stat"), IKB("Акции", callback_data="bank_actions")],
                     [back_to_menu_first_kb, IKB("Конвертер", callback_data="bank_convert")]
                     ],

            'project': [[IKB("Список проектов", callback_data="projlist"), IKB("Дополнительно...", callback_data="projmore")],
                        [back_to_menu_first_kb]
                        ],

            'social': [[IKB(text="Канал Тг", url="https://t.me/ypite"), IKB(text="Группа Вк", url="https://vk.com/cloud_ypiter"), IKB(text="GitHub", url="https://github.com/ypite-nk")],
                       [IKB(text="Вконтакте", url="https://vk.com/ypite"), IKB(text="Телеграмм", url="https://t.me/r_ypite")],
                       [IKB(text="Youtube", url="https://www.youtube.com/channel/UCQunVaPHyI2MvS0rU56_MA"), IKB(text="TikTok", url="https://vm.tiktok.com/ZT81sSebh/"), IKB(text="Twitch", url="https://www.twitch.tv/ypiternk")],
                       [back_to_menu_first_kb]
                       ],

            'callback': back_to_menu_first,

            'version': back_to_menu_first
            }
        
        self.keys = []
        for key in self.menu.keys(): self.keys.append(key)

class Second_menu():
    def __init__(self):
        self.menu = {
            'menu2': [[IKB("Стикерпаки", callback_data="packs"), IKB("Развлечения", callback_data="fun"), IKB("Боты", callback_data="bots")],
                      [IKB("Образование", callback_data="science")],
                      [IKB("<<<", callback_data="menu1"), IKB("Поддержать", callback_data="donate")]
                      ],

            'packs': [[IKB("<<<", callback_data="menu2"), back_to_menu_first_kb]
                      ],

            'fun': [[IKB("rap", callback_data="game_rap"), IKB("Фото мем", callback_data="game_photomem"), IKB("Текстовые квесты", callback_data="game_quests")],
                    [IKB("Wordly", callback_data="game_wordly")],
                    [IKB("<<<", callback_data="menu2"), back_to_menu_first_kb]
                    ],

            'bots': [[IKB("ch:помощник", url="https://t.me/ch_helper_bot"), IKB("ChatGPT", url="https://t.me/gptdevbot?start=1086638338"), IKB("LeakedCheck", url="https://t.me/LeackedCheck_bot?start=qgSPpU")],
                     [IKB("<<<", callback_data="menu2")]
                     ],

            'science': [[IKB("Обучение", callback_data="science_learn_menu"), IKB("Книги", callback_data="science_books_list1")],
                        [IKB("<<<", callback_data="menu2"), back_to_menu_first_kb]],
                        
            'donate': [[IKB(text="Boosty", url="https://boosty.to/ypite"), IKB(text="DonationAlerts", url="https://www.donationalerts.com/r/ypiter_nk")],
                       [IKB("<<<", callback_data="menu2"), back_to_menu_first_kb]
                       ]
            }
        
        self.keys = []
        for key in self.menu.keys(): self.keys.append(key)

game_rap = [
    [
    IKB("50 Cent", callback_data="game_50 Cent"), IKB("Lil Peep", callback_data="game_Lil Peep"),
    IKB("Egor Creed", callback_data="game_Egor Creed"), IKB("100 gecs", callback_data="game_100 gecs"),
    IKB("Snoop Dogg", callback_data="game_dog")],
    [IKB("<<<", callback_data="fun"), back_to_menu_first_kb]
    ]

profile_change = [
    [IKB("Никнейм", callback_data="!changer_nickname"), IKB("Имя", callback_data="!changer_name")],
    [IKB("Интересы", callback_data="!changer_buisness"), IKB("День рождения", callback_data="!changer_birthday")],
    [IKB("<<<", callback_data="profile"), back_to_menu_first_kb]
    ]

profile_back = [[IKB("<<<", callback_data="profile")]]

changerback = [[IKB("❌Отмена❌", callback_data="discard")]]

science = {
    'menu' : [[IKB("Обучение", callback_data="science_learn_menu"),
               IKB("Книги", callback_data="science_books_list1")],
              [IKB("<<<", callback_data="menu2")]],
              
    'learn' : {
        'menu': [[IKB("IT", callback_data="science_learn_computer_it_menu"),
                  IKB("3D", callback_data="science_learn_computer_3d"),
                  IKB("Языки", callback_data="science_learn_language_menu")],
                 [IKB("<<<", callback_data="science_menu"), back_to_menu_first_kb]],
                 
        'computer' : {
            'it' : {
                'menu' : [[IKB("Программирование", callback_data="science_learn_computer_it_prog_menu")],
                          [IKB("Системное администрирование", callback_data="science_learn_computer_it_adm")],
                          [IKB("Веб-разработка", callback_data="science_learn_computer_it_web_menu"),
                           IKB("SQLite3", callback_data="science_learn_computer_it_sql")],
                          [IKB("<<<", callback_data="science_learn_menu"), back_to_menu_first_kb]],
                          
                'prog' : {
                    'menu' : [[IKB("Python", callback_data="science_learn_computer_it_prog_python"),
                               IKB("C++", callback_data="science_learn_computer_it_prog_c++")],
                              [IKB("<<<", callback_data="science_learn_computer_it_menu"), back_to_menu_first_kb]],

                    'python' : [[IKB(text = "Изучать", url = "https://clck.ru/35WiHL")],
                                [IKB("<<<", callback_data="science_learn_computer_it_prog_menu")]],

                    'c++' : [[IKB(text = "Изучать", url = "https://clck.ru/yTjJf")],
                             [IKB("<<<", callback_data="science_learn_computer_it_prog_menu")]]
                    },

                'adm' : [[IKB(text = "Изучать", url = "https://stepik.org/course/176437/promo")],
                         [IKB("<<<", callback_data="science_learn_computer_it_menu"), back_to_menu_first_kb]],

                'web' : {
                    'menu' : [[IKB("HTML", callback_data="science_learn_computer_it_web_html"),
                               IKB("PHP", callback_data="science_learn_computer_it_web_php"),
                               IKB("Django", callback_data="science_learn_computer_it_web_django")],
                              [IKB("<<<", callback_data="science_learn_computer_it_menu"), back_to_menu_first_kb]],

                    'html' : [[IKB(text = "Изучать", url = "https://clck.ru/35WiGG")],
                              [IKB("<<<", callback_data="science_learn_computer_it_web_menu")]],

                    'php' : [[IKB(text = "Изучать", url = "https://clck.ru/35WiFC")],
                             [IKB("<<<", callback_data="science_learn_computer_it_web_menu")]],

                    'django' : [[IKB(text = "Изучать", url = "https://clck.ru/35WiEf")],
                                [IKB("<<<", callback_data="science_learn_computer_it_web_menu")]]
                    },

                'sql' : [[IKB(text = "Изучать", url = "https://clck.ru/35WiDf")],
                         [IKB("<<<", callback_data="science_learn_computer_it_menu"), back_to_menu_first_kb]]
                },
                
            '3d' : [[IKB(text = "Изучать", url = "https://clck.ru/35WiCW")],
                    [IKB("<<<", callback_data="science_learn_menu"), back_to_menu_first_kb]]

            },
            
        'language' : {
            'menu' : [[IKB("Английский", callback_data="science_learn_language_english"),
                       IKB("Польский", callback_data="science_learn_language_polski"),
                       IKB("Немецкий", callback_data="science_learn_language_deutsch")],
                      [IKB("<<<", callback_data="science_learn_menu"), back_to_menu_first_kb]],
                       
            'english' : [[IKB(text = "Изучать", url = "https://clck.ru/35WiKz")],
                         [IKB("<<<", callback_data = "science_learn_language_menu"), back_to_menu_first_kb]],

            'polski' : [[IKB(text = "Изучать", url = "https://dzen.ru/ypiter")],
                        [IKB("<<<", callback_data = "science_learn_language_menu"), back_to_menu_first_kb]],

            'deutsch' : [[IKB(text = "Изучать", url = "https://dzen.ru/ypiter")],
                         [IKB("<<<", callback_data = "science_learn_language_menu"), back_to_menu_first_kb]]
            }
        },
    'books' : {
        'list1': [[IKB("Классика", callback_data="!science_classic"),
                   IKB("Зарубежные", callback_data="!science_foreign"),
                   IKB("Русская", callback_data="!science_rus")],
                  [IKB("Детективы", callback_data="!science_detective"),
                   IKB("Фэнтези", callback_data="!science_fantasy"),
                   IKB("Фантастика", callback_data="!science_fantastik")],
                  [IKB("Проза", callback_data="!science_prose"),
                   IKB("Ужасы", callback_data="!science_scary"),
                   IKB("Приключения", callback_data="!science_adv")],
                  [IKB("<<<", callback_data="science_menu"), IKB(">>>", callback_data="science_books_list2")]],

        'list2': [[IKB("Боевики", callback_data="!science_action"),
                   IKB("Повести", callback_data="!science_stories"),
                   IKB("Поэзия", callback_data="!science_poem")],
                  [IKB("Научпоп", callback_data="!science_science"),
                   IKB("Психология", callback_data="!science_psycho"),
                   IKB("Комиксы", callback_data="!science_comics")],
                  [IKB("Манга", callback_data="!science_manga"),
                   IKB("Эзотерика", callback_data="!science_esotericism"),
                   IKB("Культура", callback_data="!science_culture")],
                  [IKB("<<<", callback_data="science_books_list1"), IKB(">>>", callback_data="science_books_list3")]],

        'list3': [[IKB("Романы", callback_data="!science_romans"),
                   IKB("Справочники", callback_data="!science_bookfaq"),
                   IKB("Дом", callback_data="!science_home")],
                  [IKB("Религия", callback_data="!science_religion"),
                   IKB("Юмор", callback_data="!science_funny"),
                   IKB("Бизнес", callback_data="!science_buisness")],
                  [IKB("<<<", callback_data="science_books_list2"), back_to_menu_first_kb]],
        
        'back': [[IKB("<<<", callback_data="science_books_list1"), back_to_menu_first_kb]]
        }
    }

def mem(LikeCount, DisLikeCount):
    mem = [
        [IKB("Мем", callback_data="game_photomem"), IKB("👍  " + str(LikeCount), callback_data="m_like-" + str(LikeCount)), IKB("👎  " + str(DisLikeCount), callback_data="m_dislike-" + str(DisLikeCount))],
        [IKB("<<<", callback_data="fun"), back_to_menu_first_kb]
        ]
    return mem 

quests = [
    [IKB("Квест 1", callback_data="quest_1"), IKB("квест 2", callback_data="quest_2")],
    [IKB("<<<", callback_data="fun")]
    ]

backcity = IKB("<<<", callback_data="city")
backcity_kb = [[IKB("<<<", callback_data="city")]]

create = {'create' : {'types' : [[IKB("Жилье", callback_data="create_house"), IKB("Коммерция", callback_data="create_commercical")],
                                  [IKB("Промышленность", callback_data="create_industry")],
                                  [backcity, back_to_menu_first_kb]
                                  ],
                       'house' : [[IKB("Малый район", callback_data="create_house1")],
                                  [IKB("Средний район", callback_data="create_house2")],
                                  [IKB("Большой район", callback_data="create_house3")],
                                  [backcity, back_to_menu_first_kb]
                                  ],
                       'commercical' : [[IKB("Малый район", callback_data="create_commercical1")],
                                        [IKB("Средний район", callback_data="create_commercical2")],
                                        [IKB("Большой район", callback_data="create_commercical3")],
                                        [backcity, back_to_menu_first_kb]
                                        ],
                       'industry' : [[IKB("Электроэнергия", callback_data="!create_energy")],
                                     [IKB("Водоснабжение", callback_data="!create_water")],
                                     [IKB("Товаропроизводство", callback_data="!create_material")],
                                     [backcity, back_to_menu_first_kb]
                                     ]
                       },
        '!create_energy' : [[IKB("Малая станция", callback_data="create_1indenergy")],
                              [IKB("Средняя станция", callback_data="create_2indenergy")],
                              [IKB("Большая станция", callback_data="create_3indenergy")],
                              [backcity, back_to_menu_first_kb]
                              ],
        '!create_water' : [[IKB("Малая станция", callback_data="create_1indwater")],
                             [IKB("Средняя станция", callback_data="create_2indwater")],
                             [IKB("Большая станция", callback_data="create_3indwater")],
                             [backcity, back_to_menu_first_kb]
                             ],
        '!create_material' : [[IKB("Малый район", callback_data="create_1indmaterial")],
                                [IKB("Средний район", callback_data="create_2indmaterial")],
                                [IKB("Большой район", callback_data="create_3indmaterial")],
                                [backcity, back_to_menu_first_kb]
                                ]
        }

city_change = [
    [IKB("Имя", callback_data="!changer_cityname"), IKB("Герб", callback_data="!changer_sign"), IKB("Гимн", callback_data="!changer_gymn")],
    [backcity, IKB("Мэра", callback_data="!changer_mayor"), IKB("Историю", callback_data="!changer_history"), IKB("Флаг", callback_data="!changer_flag")]
    ]

def shops(callback):
    return [
            [IKB("За рубли", callback_data=f"buy=R={callback}"), IKB("За Юшки", callback_data=f"buy=Y={callback}")],
            [IKB("<<<", callback_data="shop")]
            ]

def buy_R(callback, cost):
    return [
        [IKB(f"Купить {callback} за {cost}₽ с помощью DonationAlerts", url="https://www.donationalerts.com/r/ypiter_nk")],
        [IKB("<<<", callback_data=f"shop={callback}")]
        ]

def buy_Y(callback, cost):
    return [
        [IKB(f"Купить {callback} за {cost}Ю",
             callback_data=f"shopbuy:{callback}:{cost}")],
        [IKB("<<<", callback_data=f"shop={callback}")]
        ]

bank = {
    "start": [[IKB("Начать тест! (19Ю)", callback_data="0#0")],
              [back_to_menu_first_kb]],

    "test1": [[IKB("Вариант 1", callback_data="1#1"), IKB("Вариант 2", callback_data="1#2")],
              [IKB("❌Отмена теста❌", callback_data="discard_test")]],

    "test2": [[IKB("Вариант 1", callback_data="2#1"), IKB("Вариант 2", callback_data="2#2")],
              [IKB("Вариант 3", callback_data="2#3"), IKB("Вариант 4", callback_data="2#4")],
              [IKB("❌Отмена теста❌", callback_data="discard_test")]],

    "test3": [[IKB("Вариант 1", callback_data="3#1"), IKB("Вариант 2", callback_data="3#2")],
              [IKB("Вариант 3", callback_data="3#3"), IKB("Вариант 4", callback_data="3#4")],
              [IKB("❌Отмена теста❌", callback_data="discard_test")]],

    "complete": [[IKB("Перейти в банк...", callback_data="bank")]],

    "actions" : [[IKB("JxSpeed", callback_data="graphic_JxSpeed"), IKB("MacroMotor", callback_data="graphic_MacroMotor")],
                 [IKB("<<<", callback_data="bank")]
                 ]

    }