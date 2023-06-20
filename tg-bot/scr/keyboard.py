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
        InlineKeyboardButton("Egor Creed", callback_data="Egor Creed"), InlineKeyboardButton("100 gecs", callback_data="100 gecs")],
       [InlineKeyboardButton("...назад", callback_data="/fun"), menudel]]

start_key = [[InlineKeyboardButton("FAQ", callback_data="faq"), InlineKeyboardButton("Инфо", callback_data="info"), InlineKeyboardButton("Команды", callback_data="commands")],
             [InlineKeyboardButton("Обратная связь", callback_data="helper")]]

marks = [[InlineKeyboardButton("1::A", callback_data="A-1"), InlineKeyboardButton("2::A", callback_data="A-2"), InlineKeyboardButton("3::A", callback_data="A-3")],
         [InlineKeyboardButton("...назад", callback_data="ypiinfo"), menudel]]

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

it = [[InlineKeyboardButton("Программирование", callback_data="coding")], [InlineKeyboardButton("Веб-разработка", callback_data="web")],
      [InlineKeyboardButton("Сис. Администрирование", callback_data="admin"), InlineKeyboardButton("Базы данных", callback_data="sql")],
      [InlineKeyboardButton("...назад", callback_data="learning"), menudel]]

coding = [[InlineKeyboardButton("Python", callback_data="py"), InlineKeyboardButton("C++", callback_data="+"), InlineKeyboardButton("JavaScript", callback_data="js")],
          [InlineKeyboardButton("...назад", callback_data="it"), menudel]]

python = [[InlineKeyboardButton(text="Материалы", url="https://www.python.org/")],
          [InlineKeyboardButton("...назад", callback_data="coding"), menudel]]

cpp = [[InlineKeyboardButton(text="Материалы", url="https://learn.microsoft.com/ru-ru/cpp/cpp/cpp-language-reference?view=msvc-170")],
          [InlineKeyboardButton("...назад", callback_data="coding"), menudel]]

js = [[InlineKeyboardButton(text="Материалы", url="https://learn.javascript.ru/")],
          [InlineKeyboardButton("...назад", callback_data="coding"), menudel]]

web = [[InlineKeyboardButton("HTML&CSS", callback_data="html_m"), InlineKeyboardButton("PHP", callback_data="php"), InlineKeyboardButton("django", callback_data="django")],
       [InlineKeyboardButton("...назад", callback_data="it"), menudel]]

html_m = [[InlineKeyboardButton(text="Материалы", url="https://developer.mozilla.org/ru/docs/Learn/Getting_started_with_the_web/HTML_basics")],
          [InlineKeyboardButton("...назад", callback_data="web"), menudel]]

php = [[InlineKeyboardButton(text="Материалы", url="https://developer.mozilla.org/ru/docs/Learn/Getting_started_with_the_web/HTML_basics")],
          [InlineKeyboardButton("...назад", callback_data="web"), menudel]]

django = [[InlineKeyboardButton(text="Материалы", url="https://developer.mozilla.org/ru/docs/Learn/Getting_started_with_the_web/HTML_basics")],
          [InlineKeyboardButton("...назад", callback_data="web"), menudel]]

admin = [[InlineKeyboardButton("Системный администратор", callback_data="s_admin"), InlineKeyboardButton("Data Sciens", callback_data="data_sciens")],
          [InlineKeyboardButton("...назад", callback_data="it"), menudel]]

s_admin = [[InlineKeyboardButton(text="Материалы", url="https://habr.com/ru/companies/ruvds/articles/486204/")],
           [InlineKeyboardButton("...назад", callback_data="admin"), menudel]]

data_sciens = [[InlineKeyboardButton(text="Материалы", url="https://habr.com/ru/articles/668428/")],
          [InlineKeyboardButton("...назад", callback_data="admin"), menudel]]

sql = [[InlineKeyboardButton(text="Материалы", url="https://habr.com/ru/articles/564390/")],
       [InlineKeyboardButton("...назад", callback_data="it"), menudel]]

modeling = [[InlineKeyboardButton(text="Материалы", url="https://habr.com/ru/companies/otus/articles/675410/")],
            [InlineKeyboardButton("...назад", callback_data="learning"), menudel]]

# IN DEF

support = [[InlineKeyboardButton(text="Поддержать", url="https://pay.freekassa.ru/?m=&oa=&o=&s=6813a8f3dde2603e317b5b405dd3c4c3&currency=RUB")],
               [InlineKeyboardButton("Команды", callback_data="commands"), menudel]]

key = [[InlineKeyboardButton("rap", callback_data="rap"), InlineKeyboardButton("mem", callback_data="mem"),
            InlineKeyboardButton("3", callback_data="3"), InlineKeyboardButton("4", callback_data="4")],
            [InlineKeyboardButton("Команды", callback_data="commands"), menudel]]

button = [[InlineKeyboardButton(text="Вконтакте", url="https://vk.com/ypite"), InlineKeyboardButton(text="Группа Вк", url="https://vk.com/cloud_ypiter")],
              [InlineKeyboardButton(text="Youtube", url="https://www.youtube.com/channel/UCQunVaPHyI2MvS0rU56_MhA"), InlineKeyboardButton(text="TikTok", url="https://vm.tiktok.com/ZT81sSebh/")],
              [InlineKeyboardButton("Команды", callback_data="commands"), menudel]]

def mem(LikeCount, DisLikeCount):
    mem = [[InlineKeyboardButton("Мем", callback_data="mem"),
        InlineKeyboardButton(str(LikeCount), callback_data="like-" + str(LikeCount)),
        InlineKeyboardButton(str(DisLikeCount), callback_data="dislike-" + str(DisLikeCount))],
       [InlineKeyboardButton("Назад", callback_data="/fun"), menudel]]

    return mem

