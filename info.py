from interface import Visual
from interface import Action
from interface import Widgets
from configuration import Config


class Info:
    __slots__ = (
        'maincmd', 'setts', 'notesone', 'programsone', 'info', 'name', 'language', 'windowmode', 'install', 'open',
        'calculator', 'rps', 'options', 'city', 'new', 'contacts', 'matrix', 'catalog', 'login', 'rename', 'passwords',
        'commands', 'passwordone', 'delete', 'translate', 'notestwo', 'programstwo', 'weather', 'time', 'calendar',
        'exit', 'reboot', 'kepler54', 'resinfo', 'youtube', 'compiler', 'remove', 'point', 'color', 'transparency',
        'weatherkey'
    )

    def __init__(self):
        if Config().language() == 'russian' or Config().language() == 'русский':
            self.maincmd = "Главные команды"
            self.setts = "Опции"
            self.notesone = "Заметки"
            self.programsone = "Программы"
            self.point = '...'
            self.info = "инфо - и"
            self.name = "имя - и"
            self.language = "язык - я"
            self.color = "цвет - ц"
            self.youtube = "youtube - y"
            self.windowmode = "режим экрана - р"
            self.install = "установить ОС - у"
            self.open = "открыть - о"
            self.calculator = "калькулятор - ка"
            self.compiler = "компилятор - ко"
            self.rps = "кнб - кнб"
            self.options = "опции - о"
            self.city = "город - г"
            self.new = "новая - н"
            self.contacts = "контакты - к"
            self.matrix = "матрица - м"
            self.catalog = "каталог - к"
            self.login = "логин - л"
            self.rename = "переименовать - п"
            self.passwords = "пароли - п"
            self.commands = "команды - кмд"
            self.passwordone = "пароль - п"
            self.delete = "удалить - у"
            self.remove = "убрать - уб"
            self.translate = "перевод - пе"
            self.notestwo = "заметки - з"
            self.programstwo = "программы - п"
            self.weather = "погода - по"
            self.time = "время - в"
            self.calendar = "календарь - ка"
            self.exit = "выход - вхд"
            self.reboot = "перезагрузка - прз"
            self.weatherkey = "погода - по"
            self.transparency = "прозрачность - пр"
            self.kepler54 = "ТПИ Неон от kepler54 © 2023"
            self.resinfo = "Поддерживаемые разрешения: 1366 х 768 (16:9), Full HD 1920 х 1080 (16:9)"
        else:
            self.maincmd = "Main commands"
            self.setts = "Settings"
            self.notesone = "Notes"
            self.programsone = "Programs"
            self.point = '...'
            self.info = "info - i"
            self.name = "name - n"
            self.language = "language - la"
            self.color = "color - co"
            self.youtube = "youtube - y"
            self.windowmode = "window mode = w"
            self.install = "install OS - i"
            self.open = "open - o"
            self.calculator = "calculator - ca"
            self.compiler = "compiler - co"
            self.rps = "rps - rps"
            self.options = "settings - s"
            self.city = "city - c"
            self.new = "new - n"
            self.contacts = "contacts - c"
            self.matrix = "matrix - m"
            self.catalog = "catalog - c"
            self.login = "login - l"
            self.rename = "rename - r"
            self.passwords = "passwords - p"
            self.commands = "commands - cmd"
            self.passwordone = "password - p"
            self.delete = "delete - d"
            self.remove = "remove - re"
            self.translate = "translate - t"
            self.notestwo = "notes - n"
            self.programstwo = "programs - p"
            self.weather = "weather - w"
            self.time = "time - t"
            self.calendar = "calendar - ca"
            self.exit = "exit - ext"
            self.reboot = "reboot - reb"
            self.weatherkey = "weather - we"
            self.transparency = "transparency - t"
            self.kepler54 = "TUI Neon by kepler54 © 2023"
            self.resinfo = "Supported Resolution: WXGA 1366 х 768 (16:9), Full HD 1920 х 1080 (16:9)"

    @staticmethod
    def column(widthone, widthtwo, liste):
        counter = 0
        for i in liste:
            Visual().coordinates(widthone, 8 + counter, widthtwo, int(Visual().heightread // 2.6) + counter)
            Visual().color.print(i)
            counter += 1

    def infoview(self):
        Widgets().showtaskbar()

        self.column(15, int(Visual().widthread // 6), self.maincommand())
        self.column(45, int(Visual().widthread // 2.66), self.settings())
        self.column(70, int(Visual().widthread // 1.78), self.note())
        self.column(92, int(Visual().widthread // 1.35), self.programs())

        self.kepler()
        self.getsuppres()

        Action().presstoreturn()

    def maincommand(self):
        listmaincmd = (
            f'{Visual().secondcolor}{self.maincmd}', '', f'{Visual().firstcolor}{self.matrix}',
            f'{Visual().firstcolor}{self.info}',
            f'{Visual().firstcolor}{self.options}', f'{Visual().firstcolor}{self.catalog}',
            f'{Visual().firstcolor}{self.commands}',
            f'{Visual().firstcolor}{self.notestwo}', f'{Visual().firstcolor}{self.programstwo}',
            f'{Visual().firstcolor}{self.youtube}',
            f'{Visual().firstcolor}{self.weather}', f'{Visual().firstcolor}{self.calendar}',
            f'{Visual().firstcolor}{self.time}',
            f'{Visual().firstcolor}{self.exit}', f'{Visual().firstcolor}{self.reboot}',
            f'{Visual().firstcolor}{self.point}'
        )
        return listmaincmd

    def settings(self):
        listsetts = (
            f'{Visual().secondcolor}{self.setts}', '', f'{Visual().firstcolor}{self.name}',
            f'{Visual().firstcolor}{self.city}', f'{Visual().firstcolor}{self.login}',
            f'{Visual().firstcolor}{self.passwordone}', f'{Visual().firstcolor}{self.language}',
            f'{Visual().firstcolor}{self.color}', f'{Visual().firstcolor}{self.windowmode}',
            f'{Visual().firstcolor}{self.transparency}', f'{Visual().firstcolor}{self.weatherkey}',
            f'{Visual().firstcolor}{self.install}'
        )
        return listsetts

    def note(self):
        listnotes = (
            f"{Visual().secondcolor}{self.notesone}", '', f"{Visual().firstcolor}{self.open}",
            f"{Visual().firstcolor}{self.new}", f"{Visual().firstcolor}{self.rename}",
            f"{Visual().firstcolor}{self.delete}", f"{Visual().firstcolor}{self.remove}"
        )
        return listnotes

    def programs(self):
        listprograms = (
            f"{Visual().secondcolor}{self.programsone}", '', f"{Visual().firstcolor}{self.calculator}",
            f"{Visual().firstcolor}{self.compiler}", f"{Visual().firstcolor}{self.contacts}",
            f"{Visual().firstcolor}{self.passwords}", f"{Visual().firstcolor}{self.translate}",
            f"{Visual().firstcolor}{self.rps}"
        )
        return listprograms

    def getsuppres(self):
        Visual().coordinates(int(Visual().widthread - 74), 26,
                             int(Visual().widthread - 74), int(Visual().heightread // 1.06))
        Visual().color.print(f"{Visual().firstcolor}{self.resinfo}")

    def kepler(self):
        Visual().coordinates(int(Visual().widthread - 29), 28,
                             int(Visual().widthread - 29), int(Visual().heightread // 1.02))
        Visual().color.print(f"{Visual().secondcolor}{self.kepler54}")
