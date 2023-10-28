from colorama import Fore
from ast import literal_eval
from rich.console import Console
from bext import goto, hide, title
from keyboard import press_and_release, release, press
from pykeplib import Enigma, Visual
from data_base import DataBase


class Files(DataBase, Enigma, Visual):
    __slots__ = (
        'ver', '_name', '_city', '_login', '_password', '_weather_key', '_language', '_resolution',
        '_color', '_transparency', 'get_hide', 'get_green', 'user_data', 'tui_neon_shell_ru', 'tui_neon_shell_eng'
    )

    def __init__(self):
        self.ver = 1.0
        self._name = 0
        self._city = 1
        self._login = 2
        self._password = 3
        self._weather_key = 4
        self._language = 5
        self._resolution = 6
        self._color = 7
        self._transparency = 8
        self.get_hide = hide()
        self.get_green = Fore.GREEN
        self.user_data = self.get_value_list()
        self.tui_neon_shell_ru = "ТПИ об. Неон, вер. "
        self.tui_neon_shell_eng = "TUI Neon shell, v. "

    def get_user_data(self, data):
        return self.decoding(self.user_data[data])

    def get_resolution_and_color(self, data):
        return literal_eval(self.user_data[data])


class System(Files):
    sf = Files()
    color = Console()

    width = int(sf.get_resolution_and_color(sf._resolution)[0])
    height = int(sf.get_resolution_and_color(sf._resolution)[1])

    middle_width = int(width // 5)
    middle_height = int(height // 2)
    under_height = 2
    under_width = int(height - 2)

    first_color = sf.get_resolution_and_color(sf._color)[0]
    second_color = sf.get_resolution_and_color(sf._color)[1]
    third_color = sf.get_resolution_and_color(sf._color)[2]

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
        number = self.user_data[self._transparency]
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
        if self.get_user_data(self._language) == 'russian' or self.get_user_data(self._language) == 'русский':
            return language_one
        elif self.get_user_data(self._language) == 'english' or self.get_user_data(self._language) == 'английский':
            return language_two
        else:
            return language_two

    def get_enter_action(self, language_one, language_two):
        self.get_coordinates(self.under_height, self.under_width, self.under_height, self.under_width + 1)
        if self.get_user_data(self._language) == 'russian' or self.get_user_data(self._language) == 'русский':
            return self.color.input(self.first_color + language_one)
        elif self.get_user_data(self._language) == 'english' or self.get_user_data(self._language) == 'английский':
            return self.color.input(self.first_color + language_two)
        else:
            return self.color.input(self.first_color + language_two)

    def get_message_handler(self, language_one, language_two):
        self.get_coordinates(self.middle_width, self.middle_height, self.middle_width, self.middle_height)
        self.color.print(self.first_color + self.change_language(language_one, language_two))
