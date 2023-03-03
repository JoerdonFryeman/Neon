from os import mkdir
from bext import hide
from bext import goto
from os import system
from time import sleep
from os import listdir
from os import startfile
from colorama import Fore
from getpass import getpass
from configuration import Config
from rich.console import Console


class Variables:
    letters = (
        'А:', 'Б:', 'В:', 'Г:', 'Д:', 'Е:', 'Ё:', 'Ж:', 'З:', 'И:', 'Й:', 'К:', 'Л:', 'М:', 'Н:', 'О:', 'П:', 'Р:',
        'С:', 'Т:', 'У:', 'Ф:', 'Х:', 'Ц:', 'Ч:', 'Ш:', 'Щ:', 'Ъ:', 'Ы:', 'Ь:', 'Э:', 'Ю:', 'Я:', 'A:', 'B:', 'C:',
        'D:', 'E:', 'F:', 'G:', 'H:', 'I:', 'J:', 'K:', 'L:', 'M:', 'N:', 'O:', 'P:', 'Q:', 'R:', 'S:', 'T:', 'U:',
        'V:', 'W:', 'X:', 'Y:', 'Z:'
    )

    hgtone = 14
    hgttwo = 15
    hgtthree = 16
    wdt = 24

    def text(self, rus, eng):
        color = Console()
        b1 = '[bold blue]'
        system('cls')
        goto(self.wdt, self.hgtone)
        color.print(b1 + rus)
        goto(self.wdt, self.hgttwo)
        color.print(b1 + eng)


var = Variables()


class Data:
    hide()

    var.text("Спасибо, что выбрали Неон!", "Thank you for choosing Neon!")
    input()

    while True:
        var.text("Как можно к Вам обращаться?", "How do I address you?")
        goto(var.wdt, var.hgtthree)
        username = input(Fore.GREEN)

        if username == '':
            var.text("Необходимо ввести имя!", "Name required!")
            input()

        elif len(username) < 2 or len(username) > 11:
            var.text("Имя не может быть меньше 2 или больше 11 символов!",
                     "The name must not be less than 2 or more than 11 letters!")
            input()

        else:
            while True:
                var.text("Введите Ваш город (Необходимо для предоставления сведений о погоде)",
                         "Enter your city (Required to provide weather information)")
                goto(var.wdt, var.hgtthree)
                usercity = input()

                if usercity == '':
                    var.text("Необходимо ввести название города!", "You must enter the name of your city!")
                    input()

                elif len(usercity) < 2:
                    var.text("Название города не может быть меньше 2 символов!",
                             "The name of the city must not be less than 2 letters!")
                    input()

                else:
                    while True:
                        var.text("Придумайте логин", "Create a login")
                        goto(var.wdt, var.hgtthree)
                        userlogin = input()

                        if userlogin == '':
                            var.text("Необходимо ввести логин!", "Login required!")
                            input()

                        elif len(userlogin) < 2:
                            var.text("Логин не может быть меньше 2 символов!",
                                     "Login must not be less than 2 letters!")
                            input()

                        else:
                            while True:
                                var.text("Придумайте пароль (ввод не отображается...)",
                                         "Create a password (input is not displayed...)")

                                userpassword = getpass('')

                                if userpassword != '':

                                    if len(userpassword) >= 7:
                                        var.text("Повторите пароль (ввод не отображается...)",
                                                 "Repeat your password (input is not displayed...)")

                                        userpasswordretry = getpass('')

                                        if userpassword != userpasswordretry:
                                            var.text("Подтверждение не совпадает с паролем!",
                                                     "Confirmation doesn't match the password!")
                                            input()

                                        else:
                                            var.text("Ввод персональных данных завершен...",
                                                     "Entering personal data is completed...")
                                            sleep(1)
                                            system('cls')
                                            break

                                    else:
                                        var.text("Пароль не может быть меньше 7 символов!",
                                                 "Password must not be less than 7 letters!")
                                        input()

                                else:
                                    var.text("Необходимо ввести пароль!", "You have to enter a password!")
                                    input()
                            break
                    break
            break

    while True:
        var.text("Выберите язык — русский или английский", "Select a language — russian or english")
        goto(var.wdt, var.hgtthree)
        userlanguage = input()

        if userlanguage != '':
            if userlanguage.lower() == 'russian' or userlanguage.lower() == 'русский' \
                    or userlanguage.lower() == 'english' or userlanguage.lower() == 'английский':
                system('cls')
                break
            else:
                var.text("Необходимо ввести название языка буквами — русский или английский...",
                         "You must enter the name of the language in letters — russian or english...")
                input()
        else:
            var.text("Вы ничего не ответили!", "You did not answer!")
            input()

    while True:
        var.text("Введите имя корневого каталога / диска для установки системы",
                 "Enter the name of the root directory / hard disk for installing the system")

        goto(var.wdt, var.hgtthree)
        partition = f'{input()}:'

        if partition == '' or partition == ':':
            var.text("Вы ничего не ответили!", "You did not answer!")
            input()

        elif partition in var.letters:
            try:
                listdir(f'{partition}/TUI')
                var.text(f"Неон ОС уже установлена в корневом каталоге / на диске \"{partition}\"!",
                         f"Neon OS is already installed in the root directory / on the hard disk '{partition}'!")
                input()

            except FileNotFoundError:
                try:
                    listdir(f'{partition}/')
                    break

                except FileNotFoundError:
                    var.text(f"Корневой каталог / диск \"{partition}\" не найден!",
                             f"Root directory / hard disk \"{partition}\" not found!")
                    input()

        else:
            var.text(f"Имя корневого каталога / диска \"{partition}\" не подходит для установки системы!",
                     f"Root directory / drive name \"{partition}\" is not suitable for system installation!")
            input()


class Installation(Data):
    def part(self):
        with open(f'{self.partition}/TUI/System/system73.spec', 'w') as partitionfile:
            partitionfile.write(self.partition)

    def name(self):
        return Config().coding(f'{self.partition}/TUI/System/system54.spec', self.username)

    def city(self):
        return Config().coding(f'{self.partition}/TUI/System/system17.spec', self.usercity)

    def login(self):
        return Config().coding(f'{self.partition}/TUI/System/system23.spec', self.userlogin)

    def password(self):
        return Config().coding(f'{self.partition}/TUI/System/system41.spec', self.userpassword)

    def language(self):
        return Config().coding(f'{self.partition}/TUI/System/system62.spec', self.userlanguage)

    def weatherkey(self):
        return Config().coding(f'{self.partition}/TUI/System/system36.spec', 'f90efe966671bc256131e56a0cf9a5e7')

    def build(self):
        mkdir(f'{self.partition}/TUI/')
        mkdir(f'{self.partition}/TUI/System/')
        mkdir(f'{self.partition}/TUI/Programs/')
        mkdir(f'{self.partition}/TUI/User/')
        mkdir(f'{self.partition}/TUI/User/Notes/')
        mkdir(f'{self.partition}/TUI/User/Contacts/')
        mkdir(f'{self.partition}/TUI/User/Passwords/')
        mkdir(f'{self.partition}/TUI/User/Downloads/')

        var.text("Создание каталогов системы завершено...", "Creation of system directories completed...")
        sleep(1)

        with open('neon.exe', 'rb') as neonexe:
            with open(f'{self.partition}/TUI/System/neon.exe', 'wb') as copyneonexe:
                copyneonexe.write(neonexe.read())
        with open(f'{self.partition}/TUI/System/system30.spec', 'w') as resolutionfile:
            resolutionfile.write(str([120, 30]))
        with open(f'{self.partition}/TUI/System/system89.spec', 'w') as colorfile:
            colorfile.write(str(['[bold blue]', '[purple]', '[purple]']))
        with open(f'{self.partition}/TUI/Programs/system13.spec', 'w') as translatefile:
            translatefile.write('')
        with open(f'{self.partition}/TUI/System/system32.spec', 'w') as notesfile:
            notesfile.write('*2#)7%(')
        with open(f'{self.partition}/TUI/System/system98.spec', 'w') as resolutionfile:
            resolutionfile.write('2')
        with open(f'{self.partition}/TUI/System/system45.spec', 'w') as partitionfile:
            partitionfile.write('["https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe", '
                                '"https://www.python.org/ftp/python/3.9.13/python-3.9.13-embed-win32.zip"]')

        self.part()
        self.name()
        self.city()
        self.login()
        self.password()
        self.language()
        self.weatherkey()

        var.text("Создание файловой системы завершено...", "File system creation complete...")
        sleep(1)

        var.text("Установка завершена!", "Installation is completed!")
        sleep(1)

        startfile(f'{self.partition}/TUI/System/neon.exe')


Installation().build()
