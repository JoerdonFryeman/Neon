import os
from bext import goto
from bext import hide
from bext import title
from time import sleep
from colorama import Fore
from threading import Lock
from random import randint
from platform import system
from platform import release
from platform import machine
from platform import version
from ast import literal_eval
from threading import Thread
from datetime import datetime
from rich.console import Console
from configuration import Config
from psutil import sensors_battery
from keyboard import press_and_release


class Visual:
    version = 0.9
    hide()
    locker = Lock()

    color = Console()

    try:
        with open(f'{Config().part()}/TUI/System/system89.spec') as readcolor:
            clr = literal_eval(readcolor.read())

        firstcolor = clr[0]
        secondcolor = clr[1]
        thirdcolor = clr[2]

        widthread = Config().resolution()[0]
        heightread = Config().resolution()[1]

        mtw = int(widthread // 5)  # middletextwidth
        mth = int(heightread // 2)  # middletextheight
        utw = 2  # undertextheight
        uth = int(heightread - 2)  # undertextwidth

    except (FileNotFoundError, NameError):
        goto(24, 14)
        color.print(f"{'[bold blue]'}Необходимо установить ТПИ!")
        goto(24, 15)
        color.input(f"{'[bold blue]'}You need to install the TUI!")
        import installation

    __slots__ = ('osversionone', 'PC', 'osversiontwo', 'pc', 'cpu', 'resolution', 'system', 'os', 'temp')

    def __init__(self):
        if Config().language() == 'russian' or Config().language() == 'русский':
            self.osversionone = f"ТПИ об. Неон, вер. {self.version}"
            self.PC = "-ЭВМ"
            self.osversiontwo = self.osversionone
            self.pc = f"{Config().name()}-ЭВМ"
            self.cpu = f"{self.firstcolor}Процессор: {self.secondcolor}{machine()}"
            self.resolution = f"{self.firstcolor}Разрешение: {self.secondcolor}{self.widthread} x {self.heightread}"
            self.system = f"{self.firstcolor}Текстовый интерфейс: {self.secondcolor}{self.osversionone}"
            self.os = f"{self.firstcolor}Операционная система: " \
                      f"{self.secondcolor}{system()} {release()} (Версия {version()})"
            try:
                self.temp = f"{self.firstcolor}Аккумулятор заряжен на {self.secondcolor}{sensors_battery()[0]}%"
            except:
                pass
        else:
            self.osversionone = f"TUI Neon shell, v. {self.version}"
            self.PC = "-PC "
            self.osversiontwo = self.osversionone
            self.pc = f"{Config().name()}-PC"
            self.cpu = f"{self.firstcolor}CPU: {self.secondcolor}{machine()}"
            self.resolution = f"{self.firstcolor}Resolution: {self.secondcolor}{self.widthread} x {self.heightread}"
            self.system = f"{self.firstcolor}Text interface: {self.secondcolor}{self.osversionone}"
            self.os = f"{self.firstcolor}Operating system: " \
                      f"{self.secondcolor}{system()} {release()} (Version {version()})"
            try:
                self.temp = f"{self.firstcolor}The battery is charged for {self.secondcolor}{sensors_battery()[0]}%"
            except:
                pass

    def title(self):
        return title(self.osversionone)

    @classmethod
    def fullscreen(cls):
        if cls.widthread == 120 and cls.heightread == 30:
            pass
        else:
            return press_and_release('alt+enter')

    @classmethod
    def coordinates(cls, wdtwind, hgtwind, wdtfull, hgtfull):
        if cls.widthread == 120 and cls.heightread == 30:
            coords = goto(wdtwind, hgtwind)
            return coords
        else:
            coords = goto(wdtfull, hgtfull)
            return coords

    @classmethod
    def symbolresolution(cls, hd, fullhd):
        if cls.widthread < 237 and cls.heightread < 66:
            value = hd
        else:
            value = fullhd
        return value


class Raccoon(Visual):
    def raccoon(self):
        self.coordinates(self.widthread // 2, self.mth - 7, self.widthread // 2, self.mth - 6)
        self.color.print(f'{self.firstcolor}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')
        self.coordinates(self.widthread // 2, self.mth - 6, self.widthread // 2, self.mth - 5)
        self.color.print(f'{self.firstcolor}░░░░░░░░░░░░░░░░▄{self.secondcolor}▄▄█▄██▄▄{self.firstcolor}'
                         f'░░░░░░░░░░░░░░░░░░')
        self.coordinates(self.widthread // 2, self.mth - 5, self.widthread // 2, self.mth - 4)
        self.color.print(
            f'{self.firstcolor}░░░▄█▀███▄▄█████{self.secondcolor}███████████████▄▄███▀█{self.firstcolor}'
            f'░░░░░')
        self.coordinates(self.widthread // 2, self.mth - 4, self.widthread // 2, self.mth - 3)
        self.color.print(f'{self.firstcolor}░░░░█{self.secondcolor}░░{self.firstcolor}▀█████{self.secondcolor}'
                         f'██████████████████████'
                         f'{self.firstcolor}█{self.secondcolor}░░█{self.firstcolor}░░░░')
        self.coordinates(self.widthread // 2, self.mth - 3, self.widthread // 2, self.mth - 2)
        self.color.print(f'{self.firstcolor}░░░░░█▄{self.secondcolor}░░{self.firstcolor}▀█████{self.secondcolor}'
                         f'████████{self.firstcolor}███'
                         f'{self.secondcolor}███████{self.firstcolor}█{self.secondcolor}░░░▄▀{self.firstcolor}░░░░')
        self.coordinates(self.widthread // 2, self.mth - 2, self.widthread // 2, self.mth - 1)
        self.color.print(f'{self.firstcolor}░░░░░░▀█▄▄████▀▀▀{self.secondcolor}░░░░█{self.firstcolor}█'
                         f'{self.secondcolor}░░░{self.firstcolor}▀▀▀'
                         f'{self.secondcolor}█████▄▄█▀{self.firstcolor}░░░░░')
        self.coordinates(self.widthread // 2, self.mth - 1, self.widthread // 2, self.mth)
        self.color.print(f'{self.firstcolor}░░░░░░▄███▀▀{self.secondcolor}░░░░░░░░░█{self.firstcolor}█'
                         f'{self.secondcolor}░░░░░░░░░▀███▄{self.firstcolor}░░░░░░')
        self.coordinates(self.widthread // 2, self.mth, self.widthread // 2, self.mth + 1)
        self.color.print(
            f'{self.firstcolor}░░░░░▄██▀{self.secondcolor}░░░░░▄▄▄██▄▄██░▄██▄▄▄░░░░░▀██▄{self.firstcolor}'
            f'░░░░')
        self.coordinates(self.widthread // 2, self.mth + 1, self.widthread // 2, self.mth + 2)
        self.color.print(f'{self.firstcolor}░░░▄██▀{self.secondcolor}░░░▄▄▄███ ▄█████████ ▄██▄▄▄{self.secondcolor}'
                         f'░░░▀█▄{self.firstcolor}░░░')
        self.coordinates(self.widthread // 2, self.mth + 2, self.widthread // 2, self.mth + 3)
        self.color.print(
            f'{self.firstcolor}░░░▀██▄▄████{self.secondcolor}██████▀░███▀▀▀█████████▄▄▄█▀{self.firstcolor}'
            f'░░░')
        self.coordinates(self.widthread // 2, self.mth + 3, self.widthread // 2, self.mth + 4)
        self.color.print(
            f'{self.firstcolor}░░░░░▀█████████{self.secondcolor}█▀░░░█{self.firstcolor}█{self.secondcolor}'
            f'█░░░▀███████████▀{self.firstcolor}░░░░')
        self.coordinates(self.widthread // 2, self.mth + 4, self.widthread // 2, self.mth + 5)
        self.color.print(
            f'{self.firstcolor}░░░░░░░▀▀▀██████{self.secondcolor}░░░{self.firstcolor}██{self.secondcolor}'
            f'███▄░░▀██████▀▀{self.firstcolor}░░░░░░░')
        self.coordinates(self.widthread // 2, self.mth + 5, self.widthread // 2, self.mth + 6)
        self.color.print(
            f'{self.firstcolor}░░░░░░░░░░░░▀▀▀▀▄{self.secondcolor}░░█{self.firstcolor}██{self.secondcolor}'
            f'██▀░▄█▀▀▀{self.firstcolor}░░░░░░░░░░░░')
        self.coordinates(self.widthread // 2, self.mth + 6, self.widthread // 2, self.mth + 7)
        self.color.print(f'{self.firstcolor}░░░░░░░░░░░░░░░░░▀▀▄▄▄▄▄▀▀{self.firstcolor}░░░░░░░░░░░░░░░░░')
        self.coordinates(self.widthread // 2, self.mth + 7, self.widthread // 2, self.mth + 8)
        self.color.print(f'{self.firstcolor}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')


class Action(Visual):
    def loadingpoint(self, ruaction, engaction, taskbar):
        zero = ''
        count = 0

        for i in range(4):
            count += 1
            if count == 1:
                zero = zero
            elif count == 2:
                zero = '.'
            elif count == 3:
                zero = '..'
            elif count == 4:
                zero = '...'

            assert isinstance(taskbar, object)
            self.coordinates(self.mtw, self.mth, self.mtw, self.mth)
            self.actionprint(f'{ruaction}{zero}', f'{engaction}{zero}')
            sleep(0.3)

    @classmethod
    def actioninput(cls, rus, eng):
        if Config().language() == 'russian' or Config().language() == 'русский':
            return cls.color.input(cls.firstcolor + rus)
        else:
            return cls.color.input(cls.firstcolor + eng)

    @classmethod
    def actionprint(cls, rus, eng):
        if Config().language() == 'russian' or Config().language() == 'русский':
            cls.color.print(cls.firstcolor + rus)
        else:
            cls.color.print(cls.firstcolor + eng)

    def enteraction(self):
        self.coordinates(self.utw, self.uth, self.utw, self.uth + 1)
        return self.actioninput("Введите действие: ", "Enter action: ")

    def presstocontinue(self):
        self.coordinates(self.utw, self.uth, self.utw, self.uth + 1)
        return self.actioninput("Нажмите ввод для продолжения...", "Press to continue...")

    def presstoreturn(self):
        self.coordinates(self.utw, self.uth, self.utw, self.uth + 1)
        return self.actioninput("Нажмите действие для возврата...", "Press to return...")

    def welcome(self):
        self.coordinates(self.mtw, self.mth, self.mtw, self.mth)
        return self.actionprint(f"Добро пожаловать, {Config().name()}!", f"Welcome, {Config().name()}!"), sleep(2)

    def commandexit(self):
        self.loadingpoint("Завершение работы", "Shutdown", os.system('cls'))
        exit()

    def commandreboot(self):
        self.loadingpoint("Перезагрузка", "Reboot", os.system('cls'))
        os.startfile('neon.exe')
        exit()

    def gamelist(self):
        Widgets().showtaskbar()
        self.coordinates(self.mtw, self.mth, self.mtw, self.mth)
        return self.actionprint("КНБ", "RPS")

    def programslist(self):
        Widgets().showtaskbar()
        self.coordinates(self.mtw, self.mth, self.mtw, self.mth)
        return self.actionprint("Калькулятор, компилятор, перевод, контакты, пароли, кнб",
                                "Calculator, compiler, translate, contacts, passwords, rps")

    def invalidcolor(self):
        Widgets().showtaskbar()
        self.coordinates(self.mtw, self.mth, self.mtw, self.mth)
        return self.actionprint("Можно использовать только: Красный, зелёный, синий, белый, жёлтый, сиреневый...",
                                "Red, green, blue, white, yellow, purple..."), self.presstoreturn()

    def invalidanswer(self):
        Widgets().showtaskbar()
        self.coordinates(self.mtw, self.mth, self.mtw, self.mth)
        return self.actionprint("Вы ничего не ответили!", "You didn't answer!"), self.presstoreturn()

    def invalidinput(self):
        Widgets().showtaskbar()
        self.coordinates(self.mtw, self.mth, self.mtw, self.mth)
        return self.actionprint("Неверная команда!", "Wrong command!"), self.presstoreturn()

    def nothinghere(self):
        Widgets().showtaskbar()
        self.coordinates(self.mtw, self.mth, self.mtw, self.mth)
        return self.actionprint("Пока здесь ничего нет...", "So far, there is nothing there..."), self.presstoreturn()

    def invalidlogin(self):
        Widgets().showtaskbar()
        self.coordinates(self.mtw, self.mth, self.mtw, self.mth)
        return self.actionprint("Неверный логин!", "Invalid login!"), self.presstoreturn()

    def invalidpassword(self):
        Widgets().showtaskbar()
        self.coordinates(self.mtw, self.mth, self.mtw, self.mth)
        return self.actionprint("Неверный пароль!", "Invalid password!"), self.presstoreturn()

    def dataupdate(self):
        Widgets().showtaskbar()
        self.coordinates(self.mtw, self.mth, self.mtw, self.mth)
        return self.actionprint("Изменения сохранены!", "Changes saved!"), self.presstoreturn()

    def changeupdate(self):
        Widgets().showtaskbar()
        self.coordinates(self.mtw, self.mth, self.mtw, self.mth)
        return self.actionprint("Для внесения изменений необходима перезагрузка!",
                                "A reboot is required to make changes!"), self.presstoreturn()


class Widgets(Visual):
    def options(self):
        Widgets().showtaskbar()

        self.coordinates(self.mtw, self.mth - 2, self.mtw, self.mth - 1)
        self.color.print(self.pc)
        self.coordinates(self.mtw, self.mth - 1, self.mtw, self.mth)
        self.color.print(self.cpu)
        self.coordinates(self.mtw, self.mth, self.mtw, self.mth + 1)
        self.color.print(self.resolution)
        self.coordinates(self.mtw, self.mth + 1, self.mtw, self.mth + 2)
        self.color.print(self.system)
        self.coordinates(self.mtw, self.mth + 2, self.mtw, self.mth + 3)
        self.color.print(self.os)

        Action().presstocontinue()

    def battery(self):
        self.coordinates(2, 24, int(Visual().widthread // Visual().widthread + 1),
                         int(Visual().heightread - Visual().heightread // 4.27))
        try:
            self.color.print(self.temp)
        except:
            print('')

    def showtaskbar(self):
        os.system('cls')
        self.coordinates(1, 0, 1, 0)

        if self.widthread == 120 and self.heightread == 30:
            value = 1.03
        else:
            value = 1.02

        self.color.print(f'{self.thirdcolor}┌{(int(self.widthread // value)) * "─"}┐')
        self.coordinates(1, 1, 1, 1)
        self.color.print(f'{self.thirdcolor}│')

        if Config().language() == 'russian' or Config().language() == 'русский':
            self.coordinates(4, 1, int(self.widthread // 6), 1)
            self.color.print(f"{self.firstcolor}Инфо")
            self.coordinates(11, 1, int(self.widthread // 4.8), 1)
            self.color.print(f"{self.firstcolor}Опции")
            self.coordinates(19, 1, int(self.widthread // 3.90), 1)
            self.color.print(f"{self.firstcolor}Каталог")
            self.coordinates(29, 1, int(self.widthread // 3.12), 1)
            self.color.print(f"{self.firstcolor}Команды")
            self.coordinates(39, 1, int(self.widthread // 2.63), 1)
            self.color.print(f"{self.firstcolor}Заметки")
            self.coordinates(49, 1, int(self.widthread // 2.30), 1)
            self.color.print(f"{self.firstcolor}Программы")
            self.coordinates(61, 1, int(self.widthread // 1.97), 1)
            self.color.print(f"{self.firstcolor}YouTube")
            self.coordinates(71, 1, int(self.widthread // 1.76), 1)
            self.color.print(f"{self.firstcolor}Погода")
            self.coordinates(80, 1, int(self.widthread // 1.61), 1)
            self.color.print(f"{self.firstcolor}Календарь")
            self.coordinates(92, 1, int(self.widthread // 1.44), 1)
            self.color.print(f'{self.firstcolor}{datetime.now():{f"Время"} %H:%M}')
            self.coordinates(106, 1, int(self.widthread // 1.29), 1)
            self.color.print(f'{self.firstcolor}{datetime.now():%d.%m.%Y}')
        else:
            self.coordinates(4, 1, int(self.widthread // 6), 1)
            self.color.print(f"{self.firstcolor}Info")
            self.coordinates(11, 1, int(self.widthread // 4.8), 1)
            self.color.print(f"{self.firstcolor}Settings")
            self.coordinates(22, 1, int(self.widthread // 3.65), 1)
            self.color.print(f"{self.firstcolor}Catalog")
            self.coordinates(32, 1, int(self.widthread // 3), 1)
            self.color.print(f"{self.firstcolor}Сommands")
            self.coordinates(43, 1, int(self.widthread // 2.50), 1)
            self.color.print(f"{self.firstcolor}Notes")
            self.coordinates(51, 1, int(self.widthread // 2.23), 1)
            self.color.print(f"{self.firstcolor}Programs")
            self.coordinates(62, 1, int(self.widthread // 1.95), 1)
            self.color.print(f"{self.firstcolor}YouTube")
            self.coordinates(72, 1, int(self.widthread // 1.75), 1)
            self.color.print(f"{self.firstcolor}Weather")
            self.coordinates(82, 1, int(self.widthread // 1.58), 1)
            self.color.print(f"{self.firstcolor}Сalendar")
            self.coordinates(93, 1, int(self.widthread // 1.43), 1)
            self.color.print(f'{self.firstcolor}{datetime.now():{f"Time"} %H:%M}')
            self.coordinates(106, 1, int(self.widthread // 1.29), 1)
            self.color.print(f'{self.firstcolor}{datetime.now():%d.%m.%Y}')

        self.coordinates(self.widthread - 2, 1, int(self.widthread // 1.01), 1)
        self.color.print(f'{self.thirdcolor}│')
        self.coordinates(1, 2, 1, 2)
        self.color.print(f'{self.thirdcolor}└{(int(self.widthread // value)) * "─"}┘')


class Start(Visual):
    countcpu = int(len(machine()))
    countname = int(len(Config().name()))

    def countverticalbar(self, wdtwind, counthgtwind, wdtfull, counthgtfull):
        global counter

        if self.widthread == 120 and self.heightread == 30:
            counter = counthgtwind
        else:
            counter = counthgtfull

        for i in range(int(self.heightread // 3.75)):
            if self.widthread == 120 and self.heightread == 30:
                goto(wdtwind, counter)
            else:
                goto(wdtfull, counter)
            self.color.print(f'{self.thirdcolor}│{self.widthread // 4 * " "}│')
            counter += 1

    def starting(self):
        os.system('cls')

        self.coordinates(0, 7, 0, int(self.heightread // 3.3))
        self.color.print(f'{self.firstcolor}{(self.widthread - 1) * "─"}')

        self.coordinates(45, 10, int(self.widthread // 2.66), int(self.heightread // self.symbolresolution(2.76, 2.64)))
        self.color.print(f'{self.thirdcolor}┌{self.widthread // 4 * "─"}┐')

        self.countverticalbar(45, 11, int(self.widthread // 2.66), int(self.heightread // 2.61))

        self.coordinates(50, 13, int(self.widthread // 2.25), int(self.heightread // 2.15))
        self.color.print(f'{self.firstcolor}{machine()}, {Config().name()}{self.PC}')
        self.coordinates(50, 16, int(self.widthread // 2.25), int(self.heightread // 1.80))
        self.color.print(f'{self.firstcolor}{self.osversiontwo}')

        self.coordinates(45, 19, int(self.widthread // 2.66), int(self.heightread // 1.54))
        self.color.print(f'{self.thirdcolor}└{self.widthread // 4 * "─"}┘')
        self.coordinates(0, 22, 0, int(self.heightread // 1.42))
        self.color.print(f'{self.firstcolor}{(self.widthread - 1) * "─"}')

        if self.widthread == 120 and self.heightread == 30:
            Matrix().matrixmove(-1, self.heightread // 4.61, float(f'{0.0}{randint(6, 9)}'))
            Matrix().matrixmove(22, self.heightread // 4.61, float(f'{0.0}{randint(6, 9)}'))
            press_and_release('enter')
            Thread(target=Matrix().breaker).start()
            sleep(3.5)
            input()

        else:
            Matrix().matrixmove(0, self.heightread // 4, float(f'{0.0}{randint(6, 9)}'))
            Matrix().matrixmove(int(self.heightread // 1.38), self.heightread // 4,
                                float(f'{0.0}{randint(6, 9)}'))
            press_and_release('enter')
            Thread(target=Matrix().breaker).start()
            sleep(6)
            input()


class Matrix(Visual):
    v = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    w = ('Ω', 'λ', 'β', 'γ', 'θ', 'π', 'Σ', 'Ψ', '¥', 'ω')
    x = ('@', '№', '#', '%', '&', '§', '?', '₽', '€', '$')
    y = ('j', 'S', 'X', 'Y', 'Z', 'W', 'd', 'x', 'y', 'z')
    z = ('Ё', 'У', 'р', 'Ф', 'q', 'ё', 'R', 'й', 'Ь', 'ю')
    o = (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')

    switch = False
    maincounter = 0
    horizcoordcounter = 1  # счетчик и начальная координата по горизонтали

    @classmethod
    def breaker(cls):
        input()
        cls.switch = True

    @classmethod
    def runner(cls):
        cls.switch = False

    def matrixsymbol(self):
        f = (
            self.v[(randint(0, 9))],
            self.w[(randint(0, 9))],
            self.x[(randint(0, 9))],
            self.y[(randint(0, 9))],
            self.z[(randint(0, 9))],
            self.o[(randint(0, 9))]
        )
        return f[randint(0, 5)]

    def matrixvoid(self):
        f = (self.o[(randint(0, 9))], self.o[(randint(0, 9))])
        return f[randint(0, 1)]

    def matrixdrop(self, dropheight, horizcoord, coordofthedropbeginn, timesleep):
        while not self.switch:  # общий цикл процесса
            for b in range(6):  # цикл жизни капли
                verticalcoordcounter = coordofthedropbeginn
                self.maincounter += 1  # счетчик главного цикла
                for c in range(randint(0, dropheight)):  # случайная координата конечной высоты капли
                    verticalcoordcounter += 1  # в каждом новом цикле высота капли умножается на 1
                    with self.locker:
                        goto(horizcoord, verticalcoordcounter)  # координаты ширины и высоты капли
                        if self.maincounter % 3 == 0:  # если число главного цикла делится на 0
                            print(f'{Fore.GREEN}{self.matrixvoid()}')  # выводится пустота
                        else:
                            print(f'{Fore.GREEN}{self.matrixsymbol()}')  # в противном случае генерируется капелька
                    sleep(timesleep)
            self.maincounter = 0

    def matrixmove(self, coordofthedropbeginn, dropheight, timesleep):
        hide()
        for q in range(self.widthread // 2):
            Thread(
                target=Matrix().matrixdrop, args=(dropheight, self.horizcoordcounter, coordofthedropbeginn, timesleep)
            ).start()
            self.horizcoordcounter += 2  # шаг между потоками капель
