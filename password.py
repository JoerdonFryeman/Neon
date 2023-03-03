from os import remove
from os import listdir
from random import randrange
from interface import Visual
from interface import Action
from interface import Widgets
from configuration import Config


class Passwords:
    __slots__ = (
        'passmenu', 'websitename', 'website', 'notfound', 'websitewithname', 'alreadyexists', 'enterusername',
        'enterpassword', 'newlogin', 'andpassword', 'saved', 'websitedelete', 'removed', 'wrongname'
    )

    def __init__(self):
        if Config().language() == 'russian' or Config().language() == 'русский':
            self.passmenu = "Открыть, новый, удалить, сгенерировать"
            self.websitename = "Введите название Веб-сайта: "
            self.website = "Веб-сайт"
            self.notfound = "не найден!"
            self.websitewithname = "Веб-сайт с именем"
            self.alreadyexists = "уже существует!"
            self.enterusername = "Введите имя пользователя: "
            self.enterpassword = "Введите пароль: "
            self.newlogin = "Новые логин"
            self.andpassword = "и пароль"
            self.saved = "сохранены!"
            self.websitedelete = "Введите название удаляемого Веб-сайта: "
            self.removed = "был удалён!"
            self.wrongname = 'Имя файла не должно содержать: \\/:*?"<>|'
        else:
            self.passmenu = "Open, new, delete, generate"
            self.websitename = "Enter name of the website: "
            self.website = "Website"
            self.notfound = "not found!"
            self.websitewithname = "A website with the name "
            self.alreadyexists = "already exists!"
            self.enterusername = "Enter username: "
            self.enterpassword = "Enter password: "
            self.newlogin = "New login"
            self.andpassword = "and password "
            self.saved = "saved!"
            self.websitedelete = "Enter the name of the Website you want to delete: "
            self.removed = "has been removed!"
            self.wrongname = 'The file name must not contain: \\/:*?"<>|'

    def commandpass(self):
        counterone = 0
        countertwo = 0

        while True:
            passwordsdirectory = listdir(f'{Config().part()}/TUI/User/Passwords/')

            Widgets().showtaskbar()
            if not passwordsdirectory:
                Action().nothinghere()
                break

            elif passwordsdirectory:
                Widgets().showtaskbar()
                for i in passwordsdirectory:
                    if counterone % 5 == 0:
                        countertwo = 0

                    if 0 <= counterone <= 4:
                        Visual().coordinates(Visual().mtw - 5, Visual().mth + countertwo, Visual().mtw - 5,
                                             Visual().mth + countertwo)
                    elif 5 <= counterone <= 9:
                        Visual().coordinates(Visual().mtw + 16, Visual().mth + countertwo, Visual().mtw + 20,
                                             Visual().mth + countertwo)
                    elif 10 <= counterone <= 14:
                        Visual().coordinates(Visual().mtw + 36, Visual().mth + countertwo, Visual().mtw + 45,
                                             Visual().mth + countertwo)
                    elif 15 <= counterone <= 19:
                        Visual().coordinates(Visual().mtw + 56, Visual().mth + countertwo, Visual().mtw + 70,
                                             Visual().mth + countertwo)
                    elif 20 <= counterone <= 24:
                        Visual().coordinates(Visual().mtw + 76, Visual().mth + countertwo, Visual().mtw + 95,
                                             Visual().mth + countertwo)
                    elif counterone == 25:
                        break

                    Visual().color.print(f'{Visual().firstcolor}{i[0:-5]}')
                    counterone += 1
                    countertwo += 1

                input()
                break

        while True:
            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            Visual().color.print(f'{Visual().firstcolor}{self.passmenu}')

            commandpassword = Action().enteraction()
            if commandpassword == '':
                break

            while True:
                if commandpassword.lower() == 'открыть' or commandpassword.lower() == 'open' or \
                        commandpassword.lower() == 'о' or commandpassword.lower() == 'o':
                    self.openpass()
                    break
                elif commandpassword.lower() == 'новый' or commandpassword.lower() == 'new' or \
                        commandpassword.lower() == 'н' or commandpassword.lower() == 'n':
                    self.newpass()
                    break
                elif commandpassword.lower() == 'удалить' or commandpassword.lower() == 'delete' or \
                        commandpassword.lower() == 'у' or commandpassword.lower() == 'd':
                    self.deletepass()
                    break
                elif commandpassword.lower() == 'сгенерировать' or commandpassword.lower() == 'generate' or \
                        commandpassword.lower() == 'с' or commandpassword.lower() == 'g':
                    self.passgen()
                    break
                else:
                    Action().invalidinput()
                    break

    def openpass(self):
        while True:
            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            website = Visual().color.input(f'{Visual().firstcolor}{self.websitename}')

            if website == '':
                Action().invalidanswer()
                break

            try:
                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                Visual().color.input(
                    f'{Visual().firstcolor}{Config().decoding(f"{Config().part()}/TUI/User/Passwords/{website}.spec")}'
                )
                break

            except FileNotFoundError:
                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                Visual().color.input(f"{Visual().firstcolor}{self.website} \"{website}\" {self.notfound}")
                break

    def newpass(self):
        while True:
            passwordsdirectory = listdir(f'{Config().part()}/TUI/User/Passwords/')

            try:
                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                website = Visual().color.input(f'{Visual().firstcolor}{self.websitename}')

                if website == '':
                    Action().invalidanswer()
                    break

                if f'{website}.spec' in passwordsdirectory:
                    Widgets().showtaskbar()
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    Visual().color.input(
                        f"{Visual().firstcolor}{self.websitewithname} \"{website}\" {self.alreadyexists}")
                    break

                else:
                    Widgets().showtaskbar()
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    savedlogin = Visual().color.input(f'{Visual().firstcolor}{self.enterusername}')

                    if savedlogin == '':
                        Action().invalidanswer()
                        break

                    Widgets().showtaskbar()
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    savedpass = Visual().color.input(f'{Visual().firstcolor}{self.enterpassword}')

                    if savedpass == '':
                        Action().invalidanswer()
                        break

                    Config().coding(f'{Config().part()}/TUI/User/Passwords/{website}.spec',
                                    f'{savedlogin} — {savedpass}')

                    Widgets().showtaskbar()
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    Visual().color.input(f"{Visual().firstcolor}{self.newlogin} \"{savedlogin}\" "
                                         f"{self.andpassword} \"{savedpass}\" {self.saved}")
                    break

            except OSError:
                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                Visual().color.input(f'{Visual().firstcolor}{self.wrongname}')
                break

    def deletepass(self):
        while True:
            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            website = Visual().color.input(f'{Visual().firstcolor}{self.websitedelete}')

            if website == '':
                Action().invalidanswer()
                break

            try:
                remove(f'{Config().part()}/TUI/User/Passwords/{website}.spec')

                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                Visual().color.input(f"{Visual().firstcolor}{self.website} \"{website}\" {self.removed}")
                break

            except FileNotFoundError:
                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                Visual().color.input(f"{Visual().firstcolor}{self.website} \"{website}\" {self.notfound}")
                break

    @staticmethod
    def passgen():
        for i in range(1):
            a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
            b = ('!', '@', '#', '$', '%', '&', '*', '(', ')', '_', '-')
            c = (
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            )
            d = (
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
            )

            passlist = []
            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)

            while len(passlist) < 16:
                x = (a[randrange(0, 9)])
                y = (b[randrange(0, 10)])
                z = (c[randrange(0, 26)])
                s = (d[randrange(0, 26)])

                passlist.append(x)
                passlist.append(y)
                passlist.append(z)
                passlist.append(s)

                if len(passlist) == 16:
                    for i in passlist:
                        print(i, end='')
                    input()
