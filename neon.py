from neo import Neo
from rps import RPS
from info import Info
from os import system
from time import sleep
from os import listdir
from bext import width
from clock import Time
from bext import height
from notes import Notes
from keyboard import press
from random import randint
from getpass import getpass
from interface import Start
from keyboard import release
from interface import Matrix
from interface import Visual
from threading import Thread
from interface import Action
from interface import Raccoon
from interface import Widgets
from contacts import Contacts
from catalogs import Catalogs
from compiler import Compiler
from terminal import Terminal
from weather import WeatherNow
from password import Passwords
from configuration import Config
from youtube import YouTubeSaver
from calculator import Calculator
from translation import Translation
from calendarium import Calendarium
from keyboard import press_and_release


class Settings:
    __slots__ = (
        'username', 'nameletters', 'usercity', 'cityletters', 'currentlogin', 'loginletters', 'currentpassword',
        'passwordletters', 'newlogin', 'enterlogin', 'enterpassword', 'newpassword', 'repeatpassword', 'confirmation',
        'languagename', 'resolution', 'changecolor', 'colors', 'transparency', 'weather'
    )

    def __init__(self):
        if Config().language() == 'russian' or Config().language() == 'русский':
            self.username = "Введите новое имя: "
            self.nameletters = "Имя не должно быть меньше 2-х или больше 11-ти символов!"
            self.cityletters = "Название города не может быть меньше 2-х символов"
            self.loginletters = "Логин не может быть меньше 2-х символов!"
            self.passwordletters = "Пароль не может быть меньше 7-ми символов!"
            self.usercity = "Обновите Ваш город: "
            self.currentlogin = "Введите текущий логин (ввод не отображается...)"
            self.currentpassword = "Введите пароль (ввод не отображается...)"
            self.newlogin = "Введите новый логин: "
            self.enterlogin = "Введите логин (ввод не отображается...)"
            self.enterpassword = "Введите текущий пароль (ввод не отображается...)"
            self.newpassword = "Введите новый пароль (ввод не отображается...)"
            self.repeatpassword = "Повторите пароль (ввод не отображается...)"
            self.confirmation = "Подтверждение не совпадает с паролем!"
            self.languagename = "Введите название языка буквами — russian или english..."
            self.resolution = "Выберите \"Оконный режим\" или \"Полный экран\": "
            self.changecolor = "Выберите цвет номер"
            self.colors = "Красный, зелёный, синий, белый, жёлтый, сиреневый: "
            self.transparency = "Уровень прозрачности терминала (1, 2, 3, 4, 5, 6): "
            self.weather = "Введите ключ погоды (https://openweathermap.org/): "
        else:
            self.username = "Enter new username: "
            self.nameletters = "The name must not be less than 2 or more than 11 letters!"
            self.cityletters = "The name of the city must not be less than 2 letters!"
            self.loginletters = "Login must not be less than 2 letters!"
            self.passwordletters = "Password must not be less than 7 letters!"
            self.usercity = "Change your city: "
            self.currentlogin = "Enter the current login (input is not displayed...)"
            self.currentpassword = "Enter password (input not displayed...)"
            self.newlogin = "Enter the new login: "
            self.enterlogin = "Enter login (input is not displayed...)"
            self.enterpassword = "Enter the current password (the input is not displayed...)"
            self.newpassword = "Enter the new password (input not displayed...)"
            self.repeatpassword = "Repeat the password (input not displayed...)"
            self.confirmation = "Confirmation does not match the password!"
            self.languagename = "Enter the name of the language in letters — russian or english...!"
            self.resolution = "Select \"Window Mode\" or \"Full Screen\": "
            self.changecolor = "Change color number"
            self.colors = "Red, green, blue, white, yellow, purple: "
            self.transparency = "Terminal transparency level (1, 2, 3, 4, 5, 6): "
            self.weather = "Enter weather key (https://openweathermap.org/): "

    def commandedit(self):
        while True:
            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw - 6, Visual().mth, Visual().mtw, Visual().mth)

            if Config().language() == 'russian' or Config().language() == 'русский':
                Visual().color.print(f"{Visual().firstcolor}Имя, город, логин, пароль, язык, "
                                     f"цвет, режим экрана, прозрачность, погода, установить ТПИ")
            else:
                Visual().color.print(f"{Visual().firstcolor}Name, city, login, password, language, "
                                     f"color, window mode, transparency, weather, install TUI")

            commandoptions = Action().enteraction()
            if commandoptions == '':
                break

            while True:
                if commandoptions.lower() == 'имя' or commandoptions.lower() == 'name' or \
                        commandoptions.lower() == 'и' or commandoptions.lower() == 'n':
                    self.editname()
                    break
                if commandoptions.lower() == 'город' or commandoptions.lower() == 'city' or \
                        commandoptions.lower() == 'г' or commandoptions.lower() == 'c':
                    self.editcity()
                    break
                if commandoptions.lower() == 'логин' or commandoptions.lower() == 'login' or \
                        commandoptions.lower() == 'л' or commandoptions.lower() == 'l':
                    self.editlogin()
                    break
                if commandoptions.lower() == 'пароль' or commandoptions.lower() == 'password' or \
                        commandoptions.lower() == 'п' or commandoptions.lower() == 'p':
                    self.editpassword()
                    break
                if commandoptions.lower() == 'язык' or commandoptions.lower() == 'language' or \
                        commandoptions.lower() == 'я' or commandoptions.lower() == 'la':
                    self.editlanguage()
                    break
                if commandoptions.lower() == 'цвет' or commandoptions.lower() == 'color' or \
                        commandoptions.lower() == 'ц' or commandoptions.lower() == 'co':
                    self.editcolor()
                    break
                if commandoptions.lower() == 'режим экрана' or commandoptions.lower() == 'window mode' or \
                        commandoptions.lower() == 'р' or commandoptions.lower() == 'w':
                    self.editwindowmode()
                    break
                if commandoptions.lower() == 'погода' or commandoptions.lower() == 'weather' or \
                        commandoptions.lower() == 'по' or commandoptions.lower() == 'we':
                    self.editweatherkey()
                    break
                if commandoptions.lower() == 'прозрачность' or commandoptions.lower() == 'transparency' or \
                        commandoptions.lower() == 'пр' or commandoptions.lower() == 't':
                    self.edittransparency()
                    break
                if commandoptions.lower() == 'установить' or commandoptions.lower() == 'install' or \
                        commandoptions.lower() == 'у' or commandoptions.lower() == 'i':
                    try:
                        import installation
                    except ImportError:
                        pass
                    break
                else:
                    Action().invalidinput()
                    break

    @staticmethod
    def part():
        with open('system73.spec') as partread:
            return partread.read()

    def editname(self):
        while True:
            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            username = Visual().color.input(f"{Visual().firstcolor}{self.username}")

            if username == '':
                Action().invalidanswer()
                break

            elif len(username) < 2 or len(username) > 11:
                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                Visual().color.input(f"{Visual().firstcolor}{self.nameletters}")
                break

            Config().coding(f'{self.part()}/TUI/System/system54.spec', username)
            Action().dataupdate()
            break

    def editcity(self):
        while True:
            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            usercity = Visual().color.input(f"{Visual().firstcolor}{self.usercity}")

            if usercity == '':
                Action().invalidanswer()
                break

            elif len(usercity) < 2:
                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                Visual().color.input(f"{Visual().firstcolor}{self.cityletters}")
                break

            Config().coding(f'{self.part()}/TUI/System/system17.spec', usercity)
            Action().dataupdate()
            break

    def editlogin(self):
        while True:
            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            Visual().color.print(f"{Visual().firstcolor}{self.currentlogin}")

            login = getpass('')

            if login != '':
                if login == Config().login():
                    Widgets().showtaskbar()
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    Visual().color.print(f'{Visual().firstcolor}{self.currentpassword}')

                    password = getpass('')

                    if password != '':
                        if password == Config().password():
                            Widgets().showtaskbar()
                            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                            newlogin = Visual().color.input(f'{Visual().firstcolor}{self.newlogin}')

                            if newlogin == '':
                                Action().invalidanswer()
                                break

                            if len(newlogin) < 2:
                                Widgets().showtaskbar()
                                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                                Visual().color.input(f"{Visual().firstcolor}{self.loginletters}")
                                break

                            Config().coding(f'{self.part()}/TUI/System/system23.spec', newlogin)
                            Action().dataupdate()
                            break

                        else:
                            Action().invalidpassword()
                            break
                    else:
                        Action().invalidanswer()
                        break
                else:
                    Action().invalidlogin()
                    break
            else:
                Action().invalidanswer()
                break

    def editpassword(self):
        while True:
            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            Visual().color.print(f'{Visual().firstcolor}{self.enterlogin}')

            login = getpass('')

            if login != '':
                if login == Config().login():
                    Widgets().showtaskbar()
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    Visual().color.print(f'{Visual().firstcolor}{self.enterpassword}')

                    password = getpass('')

                    if password != '':
                        if password == Config().password():
                            Widgets().showtaskbar()
                            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                            Visual().color.print(f'{Visual().firstcolor}{self.newpassword}')

                            newpassword = getpass('')

                            if newpassword == '':
                                Action().invalidanswer()
                                break

                            if len(newpassword) < 7:
                                Widgets().showtaskbar()
                                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                                Visual().color.input(f"{Visual().firstcolor}{self.passwordletters}")
                                break

                            Widgets().showtaskbar()
                            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                            Visual().color.print(f'{Visual().firstcolor}{self.repeatpassword}')

                            newpasswordretry = getpass('')

                            if newpassword != newpasswordretry:
                                Widgets().showtaskbar()
                                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                                Visual().color.print(f'{Visual().firstcolor}{self.confirmation}')
                                input()
                                break

                            Config().coding(f'{self.part()}/TUI/System/system41.spec', newpassword)
                            Action().dataupdate()
                            break

                        else:
                            Action().invalidpassword()
                            break
                    else:
                        Action().invalidanswer()
                        break
                else:
                    Action().invalidlogin()
                    break
            else:
                Action().invalidanswer()
                break

    def editlanguage(self):
        while True:
            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)

            if Config().language() == 'russian' or Config().language() == 'русский':
                language = Visual().color.input(f"{Visual().firstcolor}Выберите язык — русский или английский: ")
            else:
                language = Visual().color.input(f"{Visual().firstcolor}Select a language — russian or english: ")

            if language == '':
                Action().invalidanswer()
                break

            if language.lower() == 'russian' or language.lower() == 'русский' \
                    or language.lower() == 'english' or language.lower() == 'английский':

                Config().coding(f'{self.part()}/TUI/System/system62.spec', language)
                Action().dataupdate()
                break

            else:
                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                Visual().color.input(f'{Visual().firstcolor}{self.languagename}')
                break

    @staticmethod
    def verifycolor(color):
        if color == 'белый': color = 'white'
        if color == 'красный': color = 'red'
        if color == 'зелёный' or color == 'зеленый': color = 'green'
        if color == 'синий' or color == 'голубой' or color == 'blue': color = 'bold blue'
        if color == 'жёлтый' or color == 'желтый': color = 'yellow'
        if color == 'фиолетовый' or color == 'сиреневый' or color == 'лиловый': color = 'purple'
        return color

    def editcolor(self):
        counter = 0
        colorlist = []

        for i in range(3):
            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            color = Visual().color.input(f'{Visual().firstcolor}{self.changecolor} {counter + 1}... {self.colors}')

            if color == '':
                Action().invalidanswer()
                break

            colorlist.append(f'[{self.verifycolor(color)}]')

            if self.verifycolor(color) == 'red' or self.verifycolor(color) == 'green' or \
                    self.verifycolor(color) == 'bold blue' or self.verifycolor(color) == 'yellow' or \
                    self.verifycolor(color) == 'purple' or self.verifycolor(color) == 'white':
                counter += 1

                if counter == 3:
                    with open(f'{self.part()}/TUI/System/system89.spec', 'w') as writecolor:
                        writecolor.write(str(colorlist))
                    Action().changeupdate()
                    break

            else:
                Action().invalidcolor()
                break

    def editwindowmode(self):
        while True:
            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            resolution = Visual().color.input(f'{Visual().firstcolor}{self.resolution}')

            if resolution == '':
                Action().invalidanswer()
                break

            if resolution.lower() == 'оконный режим' or resolution.lower() == 'о' or \
                    resolution.lower() == 'window mode' or resolution.lower() == 'w':

                with open(f'{self.part()}/TUI/System/system30.spec', 'w') as resolutionwrite:
                    resolutionwrite.write(str([120, 30]))
                Action().dataupdate()
                Action().commandreboot()
                break

            elif resolution.lower() == 'полный экран' or resolution.lower() == 'п' or \
                    resolution.lower() == 'full Screen' or resolution.lower() == 'f':

                press_and_release('alt+enter')

                with open(f'{self.part()}/TUI/System/system30.spec', 'w') as resolutionwrite:
                    resolutionwrite.write(str([width(), height() - 1]))

                press_and_release('alt+enter')

                Action().dataupdate()
                Action().commandreboot()
                break

            else:
                Action().invalidinput()

    def editweatherkey(self):
        while True:
            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            weatherkey = Visual().color.input(f'{Visual().firstcolor}{self.weather}')

            if weatherkey == '':
                Action().invalidanswer()
                break

            Config().coding(f'{Config().part()}/TUI/System/system36.spec', weatherkey)

            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            Action().changeupdate()
            break

    def edittransparency(self):
        while True:
            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            try:
                level = Visual().color.input(f'{Visual().firstcolor}{self.transparency}')

                if level != '':
                    if 0 < int(level) < 7:
                        with open(f'{Config().part()}/TUI/System/system98.spec', 'w') as number:
                            number.write(str(level))

                        Widgets().showtaskbar()
                        Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                        Action().changeupdate()
                        break

                    else:
                        Action().invalidinput()
                        break
                else:
                    Action().invalidanswer()
                    break

            except ValueError:
                Action().invalidinput()
                break


class Authentication:
    __slots__ = ('login', 'password', 'wronglogin', 'wrongpassword', 'invalidanswer')

    def __init__(self):
        if Config().language() == 'russian' or Config().language() == 'русский':
            self.login = f'{Visual().firstcolor}{"Введите логин (ввод не отображается...)"}'
            self.password = f'{Visual().firstcolor}{"Введите пароль (ввод не отображается...)"}'
            self.wronglogin = f'{Visual().firstcolor}{"Неверный логин!"}'
            self.wrongpassword = f'{Visual().firstcolor}{"Неверный пароль!"}'
            self.invalidanswer = f'{Visual().firstcolor}{"Вы ничего не ответили!"}'
        else:
            self.login = f'{Visual().firstcolor}{"Enter login (input is not displayed...)"}'
            self.password = f'{Visual().firstcolor}{"Enter password (input is not displayed...)"}'
            self.wronglogin = f'{Visual().firstcolor}{"Invalid login!"}'
            self.wrongpassword = f'{Visual().firstcolor}{"Invalid password!"}'
            self.invalidanswer = f'{Visual().firstcolor}{"You did not answer!"}'

    def entry(self):
        while True:
            system('cls')
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            Visual().color.print(self.login)
            login = getpass('')

            if login != '':
                if login == Config().login():
                    system('cls')
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    Visual().color.print(self.password)
                    password = getpass('')

                    if password != '':
                        if password == Config().password():
                            system('cls')
                            break
                        else:
                            system('cls')
                            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                            Visual().color.print(self.wrongpassword)
                            Action().presstoreturn()
                    else:
                        system('cls')
                        Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                        Visual().color.print(self.invalidanswer)
                        Action().presstoreturn()
                else:
                    system('cls')
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    Visual().color.print(self.wronglogin)
                    Action().presstoreturn()
            else:
                system('cls')
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                Visual().color.print(self.invalidanswer)
                Action().presstoreturn()


class Beginning:
    @staticmethod
    def commandprograms():
        while True:
            Action().programslist()
            cmdinpt = Action().enteraction()

            if cmdinpt.lower() == 'калькулятор' or cmdinpt.lower() == 'ка' or cmdinpt.lower() == 'calculator' \
                    or cmdinpt.lower() == 'ca':
                Calculator().commandcalculator()
            elif cmdinpt.lower() == 'пароли' or cmdinpt.lower() == 'п' or cmdinpt.lower() == 'passwords' \
                    or cmdinpt.lower() == 'p':
                Authentication().entry()
                Passwords().commandpass()
            elif cmdinpt.lower() == 'контакты' or cmdinpt.lower() == 'к' or cmdinpt.lower() == 'contacts' \
                    or cmdinpt.lower() == 'c':
                Contacts().commandcontacts()
            elif cmdinpt.lower() == 'перевод' or cmdinpt.lower() == 'пе' or cmdinpt.lower() == 'translate' \
                    or cmdinpt.lower() == 't':
                Translation().translate()
            elif cmdinpt.lower() == 'компилятор' or cmdinpt.lower() == 'ко' or cmdinpt.lower() == 'compiler' \
                    or cmdinpt.lower() == 'co':
                Compiler().commandbuild()
            elif cmdinpt.lower() == 'кнб' or cmdinpt.lower() == 'rps':
                RPS().commandrps()
            elif cmdinpt == '':
                break
            else:
                Action().invalidinput()

    def maincommand(self):
        cmdinpt = Action().enteraction()

        if cmdinpt.lower() == 'календарь' or cmdinpt.lower() == 'ка' or cmdinpt.lower() == 'calendar' \
                or cmdinpt.lower() == 'ca':
            Calendarium().commandcalendar()
        elif cmdinpt.lower() == 'погода' or cmdinpt.lower() == 'по' or cmdinpt.lower() == 'weather' \
                or cmdinpt.lower() == 'w':
            WeatherNow().commandweather()
        elif cmdinpt.lower() == 'кмд' or cmdinpt.lower() == 'cmd' or cmdinpt.lower() == 'команды' \
                or cmdinpt.lower() == 'commands':
            Terminal().commandterminal()
        elif cmdinpt.lower() == 'выход' or cmdinpt.lower() == 'вхд' or cmdinpt.lower() == 'exit' \
                or cmdinpt.lower() == 'ext':
            Action().commandexit()
        elif cmdinpt.lower() == 'время' or cmdinpt.lower() == 'в' or cmdinpt.lower() == 'time' \
                or cmdinpt.lower() == 't':

            system('cls')
            Thread(target=Time().runner).start()
            Thread(target=Time().commandtime).start()
            Thread(target=Time().breaker).start()
            input()
            sleep(0.3)

        elif cmdinpt.lower() == 'программы' or cmdinpt.lower() == 'п' or cmdinpt.lower() == 'programs' \
                or cmdinpt.lower() == 'p':
            self.commandprograms()
        elif cmdinpt.lower() == 'каталог' or cmdinpt.lower() == 'к' or cmdinpt.lower() == 'catalog' \
                or cmdinpt.lower() == 'c':
            Catalogs().showalldir()
        elif cmdinpt.lower() == 'опции' or cmdinpt.lower() == 'о' or cmdinpt.lower() == 'settings' \
                or cmdinpt.lower() == 's':
            Widgets().options()
            Settings().commandedit()
        elif cmdinpt.lower() == 'перезагрузка' or cmdinpt.lower() == 'прз' or cmdinpt.lower() == 'reboot' \
                or cmdinpt.lower() == 'reb':
            Action().commandreboot()
        elif cmdinpt.lower() == 'заметки' or cmdinpt.lower() == 'з' or cmdinpt.lower() == 'notes' \
                or cmdinpt.lower() == 'n':
            Notes().commandnote()
        elif cmdinpt.lower() == 'инфо' or cmdinpt.lower() == 'и' or cmdinpt.lower() == 'info' \
                or cmdinpt.lower() == 'i':
            Info().infoview()
        elif cmdinpt.lower() == 'ютьюб' or cmdinpt.lower() == 'ю' or cmdinpt.lower() == 'youtube' \
                or cmdinpt.lower() == 'y':
            YouTubeSaver().savevideo()
        elif cmdinpt.lower() == 'нео' or cmdinpt.lower() == 'neo':
            Neo().neo()
        elif cmdinpt.lower() == 'матрица' or cmdinpt.lower() == 'matrix' or cmdinpt.lower() == 'м' \
                or cmdinpt.lower() == 'm':

            system('cls')
            Thread(target=Matrix().runner).start()
            Matrix().matrixmove(-1, Visual().heightread - 1, float(f'{0.0}{randint(6, 9)}'))
            Thread(target=Matrix().breaker).start()
            input()

        elif cmdinpt == '':
            Action().invalidanswer()
        else:
            Action().invalidinput()

    @staticmethod
    def pressandrelease(value):
        for i in range(value):
            press_and_release("-")

    @staticmethod
    def verifytransparency():
        with open(f'{Config().part()}/TUI/System/system98.spec') as number:
            return int(number.read())

    def consistency(self):
        press('ctrl+shift')

        number = self.verifytransparency()
        if number == 1:
            self.pressandrelease(1)
        if number == 2:
            self.pressandrelease(2)
        if number == 3:
            self.pressandrelease(3)
        if number == 4:
            self.pressandrelease(4)
        if number == 5:
            self.pressandrelease(5)
        if number == 6:
            self.pressandrelease(6)

        release('ctrl+shift')

    def start(self):
        while True:
            Widgets().showtaskbar()
            Visual().coordinates(0, 8, 0, int(Visual().heightread // 2.47))
            print(Calendarium().calendarmonth())
            Raccoon().raccoon()
            Widgets().battery()
            Notes().widgetnote()
            self.maincommand()


visual = Visual()
start = Start()
authentication = Authentication()
action = Action()
beginning = Beginning()

if __name__ == '__main__':
    try:
        listdir(f'{Config().part()}/TUI')

        visual.fullscreen()
        beginning.consistency()
        visual.title()
        start.starting()
        authentication.entry()
        action.welcome()
        beginning.start()

    except IndexError:
        system('cls')
        visual.coordinates(visual.mtw, visual.mth, visual.mtw, visual.mth)
        visual.color.print(f"{visual.firstcolor}Необходимо настроить режим экрана")
        visual.coordinates(visual.mtw, visual.mth + 1, visual.mtw, visual.mth + 1)
        visual.color.input(f"{visual.firstcolor}You need to adjust the screen mode")
