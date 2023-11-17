from os import startfile
from ast import literal_eval
from bext import goto, title
from sqlite3 import OperationalError
from keyboard import press_and_release, release, press
from data_base import DataBase
from pykeplib import Visual, Descriptor


class Files(DataBase, Visual):
    __slots__ = ('ver', 'tui_neon_shell_ru', 'tui_neon_shell_eng', 'user_data')

    def __init__(self):
        super().__init__()
        self.ver = 1.0
        self.neon = f"{''.join(f'Neon{self.ver}'.split('.'))}.exe"
        self.tui_neon_shell_ru = "ТПИ об. Неон, вер. "
        self.tui_neon_shell_eng = "TUI Neon shell, v. "
        try:
            self.user_data = self.get_value_list()
        except OperationalError:
            self.add_db_value()
            startfile(self.neon)
            exit()

    def get_user_data(self, data):
        return self.decoding(self.user_data[data])

    def get_resolution_and_color(self, data):
        return literal_eval(self.user_data[data])


class System(Files):
    middle_width = Descriptor()
    middle_height = Descriptor()
    under_height = Descriptor()
    under_width = Descriptor()

    __slots__ = (
        'width', 'height', '_middle_width', '_middle_height', '_under_height',
        '_under_width', 'first_color', 'second_color', 'third_color'
    )

    def __init__(self):
        super().__init__()

        self.width = int(self.get_resolution_and_color(self.resolution)[0])
        self.height = int(self.get_resolution_and_color(self.resolution)[1])

        self._middle_width = int(self.width // 5)
        self._middle_height = int(self.height // 2)
        self._under_height = int(2)
        self._under_width = int(self.height - 2)

        self.first_color = self.get_resolution_and_color(self.color)[0]
        self.second_color = self.get_resolution_and_color(self.color)[1]
        self.third_color = self.get_resolution_and_color(self.color)[2]

    def get_coordinates(self, wdt_wind, hgt_wind, wdt_full, hgt_full):
        if self.width == 120 and self.height == 30:
            width_and_height_coord = goto(wdt_wind, hgt_wind)
            return width_and_height_coord
        else:
            width_and_height_coord = goto(wdt_full, hgt_full)
            return width_and_height_coord

    def change_language(self, language_one, language_two):
        if self.get_user_data(self.language) == 'russian' or self.get_user_data(self.language) == 'русский':
            return language_one
        elif self.get_user_data(self.language) == 'english' or self.get_user_data(self.language) == 'английский':
            return language_two
        else:
            return language_two

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
