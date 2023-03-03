from os import system
from interface import Visual
from interface import Action
from platform import machine
from ast import literal_eval
from interface import Widgets
from configuration import Config


class Terminal:
    __slots__ = ('cmd', 'commandmenu', 'pyinstall', 'install')

    def __init__(self):
        if Config().language() == 'russian' or Config().language() == 'русский':
            self.cmd = "Для возврата введите команду \"exit\"..."
            self.commandmenu = "Терминал, установить Пайтон, ..."
            self.pyinstall = "Отсутствует подключение к интернету или другая непредвиденная ошибка!"
            self.install = "Идёт загрузка!"
        else:
            self.cmd = "To exit enter the command \"exit\"..."
            self.commandmenu = "Terminal, install Python, ..."
            self.pyinstall = "No internet connection or other unexpected error!"
            self.install = "Loading in progress!"

    def commandterminal(self):
        while True:
            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            Visual().color.print(f'{Visual().firstcolor}{self.commandmenu}')

            command = Action().enteraction()
            if command == '':
                break

            if command.lower() == 'терминал' or command.lower() == 'terminal' or \
                    command.lower() == 'т' or command.lower() == 't':
                self.commandconsole()
            elif command.lower() == 'установить' or command.lower() == 'install' or \
                    command.lower() == 'у' or command.lower() == 'i':
                self.pythoninstall()
            elif command.lower() == 'пайтон дзен' or command.lower() == 'zen of python' or \
                    command.lower() == 'дзен' or command.lower() == 'zen' or command.lower() == 'this':
                self.getthis()

    def pythoninstall(self):
        with open(f'{Config().part()}/TUI/System/system45.spec') as link:
            link = literal_eval(link.read())[0:]

            try:
                if machine()[-2:] == '64':
                    system(f'start {link[0]}')
                if machine()[-2:] == '32':
                    system(f'start {link[1]}')

                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                Visual().color.input(f'{Visual().firstcolor}{self.install}')

            except:
                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                Visual().color.input(f'{Visual().firstcolor}{self.pyinstall}')

    def commandconsole(self):
        system('cls')
        Visual().color.print(f'{Visual().firstcolor}\n{self.cmd}\n')
        system('cmd')

    @staticmethod
    def getthis():
        system('cls')
        try:
            import this
        except:
            pass
        finally:
            input()
