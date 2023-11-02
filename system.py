from colorama import Fore
from ast import literal_eval
from rich.console import Console
from bext import goto, hide, title
from sqlite3 import OperationalError
from keyboard import press_and_release, release, press
from data_base import DataBase
from pykeplib import Visual, Descriptor


class Files(DataBase, Visual):
    name = Descriptor()
    city = Descriptor()
    login = Descriptor()
    password = Descriptor()
    language = Descriptor()
    weather_key = Descriptor()
    resolution = Descriptor()
    color = Descriptor()
    transparency = Descriptor()

    __slots__ = (
        'ver', '_name', '_city', '_login', '_password', '_language', '_weather_key', '_resolution', '_color',
        '_transparency', 'get_hide', 'get_green', 'user_data', 'tui_neon_shell_ru', 'tui_neon_shell_eng'
    )

    def __init__(
            self, name=0, city=1, login=2, password=3, language=4,
            weather_key=5, resolution=6, color=7, transparency=8
    ):
        super().__init__()
        self.ver = 1.0
        self._name = name
        self._city = city
        self._login = login
        self._password = password
        self._language = language
        self._weather_key = weather_key
        self._resolution = resolution
        self._color = color
        self._transparency = transparency
        self.get_hide = hide()
        self.console_color = Console()
        self.get_green = Fore.GREEN
        self.tui_neon_shell_ru = "ТПИ об. Неон, вер. "
        self.tui_neon_shell_eng = "TUI Neon shell, v. "
        try:
            self.user_data = self.get_value_list()
        except OperationalError:
            self.add_db_value()

    def get_user_data(self, data):
        return self.decoding(self.user_data[data])

    def get_resolution_and_color(self, data):
        return literal_eval(self.user_data[data])


class System(Files):
    sf = Files()

    width = int(sf.get_resolution_and_color(sf.resolution)[0])
    height = int(sf.get_resolution_and_color(sf.resolution)[1])

    _middle_width = int(width // 5)
    _middle_height = int(height // 2)
    _under_height = int(2)
    _under_width = int(height - 2)

    first_color = sf.get_resolution_and_color(sf.color)[0]
    second_color = sf.get_resolution_and_color(sf.color)[1]
    third_color = sf.get_resolution_and_color(sf.color)[2]

    def get_coordinates(self, wdt_wind, hgt_wind, wdt_full, hgt_full):
        if self.width == 120 and self.height == 30:
            width_and_height_coord = goto(wdt_wind, hgt_wind)
            return width_and_height_coord
        else:
            width_and_height_coord = goto(wdt_full, hgt_full)
            return width_and_height_coord

    def get_symbol_resolution(self, hd, full_hd):
        if self.width < 237 and self.height < 66:
            value = hd
        else:
            value = full_hd
        return value

    def get_screen_mode(self):
        title(str(f'{self.change_language(self.tui_neon_shell_ru, self.tui_neon_shell_eng)}{self.ver}'))
        if self.width == 120 and self.height == 30:
            pass
        else:
            return press_and_release('alt+enter')

    @staticmethod
    def press_symbol(value):
        for i in range(value):
            press_and_release("-")

    def verify_transparency(self):
        press('ctrl+shift')
        number = self.user_data[self.transparency]
        if number == 1:
            self.press_symbol(1)
        if number == 2:
            self.press_symbol(2)
        if number == 3:
            self.press_symbol(3)
        if number == 4:
            self.press_symbol(4)
        if number == 5:
            self.press_symbol(5)
        if number == 6:
            self.press_symbol(6)
        release('ctrl+shift')

    def change_language(self, language_one, language_two):
        if self.get_user_data(self.language) == 'russian' or self.get_user_data(self.language) == 'русский':
            return language_one
        elif self.get_user_data(self.language) == 'english' or self.get_user_data(self.language) == 'английский':
            return language_two
        else:
            return language_two

    def get_enter_action(self, language_one, language_two):
        self.get_coordinates(self._under_height, self._under_width, self._under_height, self._under_width + 1)
        if self.get_user_data(self.language) == 'russian' or self.get_user_data(self.language) == 'русский':
            return self.console_color.input(self.first_color + language_one)
        elif self.get_user_data(self.language) == 'english' or self.get_user_data(self.language) == 'английский':
            return self.console_color.input(self.first_color + language_two)
        else:
            return self.console_color.input(self.first_color + language_two)

    def get_message_handler(self, language_one, language_two):
        self.get_coordinates(self._middle_width, self._middle_height, self._middle_width, self._middle_height)
        self.console_color.print(self.first_color + self.change_language(language_one, language_two))
