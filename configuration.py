from time import sleep
from colorama import Fore
from bext import goto, hide
from random import randint
from datetime import datetime
from os import system as sys
from threading import Thread
from ast import literal_eval
from rich.console import Console
from psutil import sensors_battery
from keyboard import press_and_release, release, press
from platform import system, machine, version, release as os_release
from cryptography import Enigma
from matrix import Matrix


class FilesConfig(Enigma):
    @staticmethod
    def get_system_path():
        with open('system73.spec') as path:
            return path.read()

    def _get_user_name(self):
        return self.decoding(f'{self.get_system_path()}/TUI/System/system54.spec')

    def _get_user_city(self):
        return self.decoding(f'{self.get_system_path()}/TUI/System/system17.spec')

    def _get_user_login(self):
        return self.decoding(f'{self.get_system_path()}/TUI/System/system23.spec')

    def _get_user_password(self):
        return self.decoding(f'{self.get_system_path()}/TUI/System/system41.spec')

    def _get_user_weather_key(self):
        return self.decoding(f'{self.get_system_path()}/TUI/System/system36.spec')

    def get_system_language(self):
        return self.decoding(f'{self.get_system_path()}/TUI/System/system62.spec')

    def get_system_resolution(self):
        with open(f'{self.get_system_path()}/TUI/System/system30.spec') as res:
            resolution = literal_eval(res.read())
        return resolution

    def get_system_color(self):
        with open(f'{self.get_system_path()}/TUI/System/system89.spec') as clr:
            color = literal_eval(clr.read())
        return color

    def get_transparency(self):
        with open(f'{self.get_system_path()}/TUI/System/system98.spec') as num:
            number = int(num.read())
        return number


class SystemConfig(FilesConfig):
    sf = FilesConfig()
    color = Console()

    __slots__ = ('ver', 'get_green', 'get_hide')

    def __init__(
            self, ver=1.0,
            get_green=Fore.GREEN,
            get_hide=hide(),
            tui_neon_shell_ru="ТПИ об. Неон, вер. ",
            tui_neon_shell_eng="TUI Neon shell, v. "
    ):
        self.ver = ver
        self.get_green = get_green
        self.get_hide = get_hide
        self.tui_neon_shell_ru = tui_neon_shell_ru
        self.tui_neon_shell_eng = tui_neon_shell_eng

    width = sf.get_system_resolution()[0]
    height = sf.get_system_resolution()[1]

    middle_width = int(width // 5)
    middle_height = int(height // 2)
    under_height = 2
    under_width = int(height - 2)

    first_color = sf.get_system_color()[0]
    second_color = sf.get_system_color()[1]
    third_color = sf.get_system_color()[2]

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

    def change_language(self, language_one, language_two):
        if self.get_system_language() == 'russian' or self.get_system_language() == 'русский':
            return language_one
        elif self.get_system_language() == 'english' or self.get_system_language() == 'английский':
            return language_two
        else:
            return language_two

    def change_commands_input_language(self, language_one, language_two):
        if self.get_system_language() == 'russian' or self.get_system_language() == 'русский':
            return self.color.input(self.first_color + language_one)
        elif self.get_system_language() == 'english' or self.get_system_language() == 'английский':
            return self.color.input(self.first_color + language_two)
        else:
            return self.color.input(self.first_color + language_two)

    def get_screen_mode(self):
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

        number = self.get_transparency()
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


class WidgetsConfig(SystemConfig, Matrix):
    count_cpu_name = int(len(machine()))
    count_user_name = int(len(SystemConfig()._get_user_name()))

    def get_vertical_bar(self, wdtwind, counthgtwind, wdtfull, counthgtfull):
        global counter

        if self.width == 120 and self.height == 30:
            counter = counthgtwind
        else:
            counter = counthgtfull

        for i in range(int(self.height // 3.75)):
            if self.width == 120 and self.height == 30:
                goto(wdtwind, counter)
            else:
                goto(wdtfull, counter)
            self.color.print(f'{self.third_color}│{self.width // 4 * " "}│')
            counter += 1

    def get_start_screen(self):
        sys('cls')

        self.get_coordinates(0, 7, 0, int(self.height // 3.3))
        self.color.print(f'{self.first_color}{(self.width - 1) * "─"}')

        self.get_coordinates(
            45, 10, int(self.width // 2.66), int(self.height // self.get_symbol_resolution(2.76, 2.64))
        )
        self.color.print(f'{self.third_color}┌{self.width // 4 * "─"}┐')

        self.get_vertical_bar(45, 11, int(self.width // 2.66), int(self.height // 2.61))

        self.get_coordinates(50, 13, int(self.width // 2.25), int(self.height // 2.15))
        self.color.print(
            f'{self.first_color}{machine()}, {self._get_user_name()}'
            f'{self.change_language("-ЭВМ", "-PC")}'
        )
        self.get_coordinates(50, 16, int(self.width // 2.25), int(self.height // 1.80))
        self.color.print(
            f'{self.first_color}'
            f'{self.change_language(self.tui_neon_shell_ru, self.tui_neon_shell_eng)}'
            f'{self.ver}'
        )
        self.get_coordinates(45, 19, int(self.width // 2.66), int(self.height // 1.54))
        self.color.print(f'{self.third_color}└{self.width // 4 * "─"}┘')
        self.get_coordinates(0, 22, 0, int(self.height // 1.42))
        self.color.print(f'{self.first_color}{(self.width - 1) * "─"}')

        if self.width == 120 and self.height == 30:
            Matrix().get_matrix_move(-1, self.height // 4.61, float(f'{0.0}{randint(6, 9)}'))
            Matrix().get_matrix_move(22, self.height // 4.61, float(f'{0.0}{randint(6, 9)}'))
            press_and_release('enter')
            Thread(target=Matrix().break_function).start()
            sleep(3.5)
            input()
        else:
            Matrix().get_matrix_move(0, self.height // 4, float(f'{0.0}{randint(6, 9)}'))
            Matrix().get_matrix_move(int(self.height // 1.38), self.height // 4,
                                     float(f'{0.0}{randint(6, 9)}'))
            press_and_release('enter')
            Thread(target=Matrix().break_function).start()
            sleep(6)
            input()

    def get_settings(self):
        self.get_taskbar()

        self.get_coordinates(self.middle_width, self.middle_height - 2, self.middle_width, self.middle_height - 1)
        self.color.print(f'{self._get_user_name()}{self.change_language("-ЭВМ", "-PC")}')
        self.get_coordinates(self.middle_width, self.middle_height - 1, self.middle_width, self.middle_height)
        self.color.print(
            f'{self.first_color}{self.change_language("Процессор: ", "CPU: ")}'
            f'{self.second_color}{machine()}'
        )
        self.get_coordinates(self.middle_width, self.middle_height, self.middle_width, self.middle_height + 1)
        self.color.print(
            f'{self.first_color}{self.change_language("Разрешение: ", "Resolution: ")}'
            f'{self.second_color}{self.width} x {self.height}'
        )
        self.get_coordinates(self.middle_width, self.middle_height + 1, self.middle_width, self.middle_height + 2)
        self.color.print(
            f'{self.first_color}'
            f'{self.change_language("Текстовый интерфейс: ", "Text interface: ")}'
            f'{self.second_color}{self.change_language(self.tui_neon_shell_ru, self.tui_neon_shell_eng)}{self.ver}'
        )
        self.get_coordinates(self.middle_width, self.middle_height + 2, self.middle_width, self.middle_height + 3)
        self.color.print(
            f'{self.first_color}'
            f'{self.change_language("Операционная система: ", "Operating system: ")}'
            f'{self.second_color}'
            f'{system()} {os_release()} ({self.change_language("Версия ", "Version ")}'
            f'{version()}{self.second_color})'
        )

    def get_battery(self):
        self.get_coordinates(
            2, 24, int(self.width // self.width + 1), int(self.height - self.height // 4.27)
        )
        try:
            self.color.print(
                self.second_color + self.change_language(
                    "Аккумулятор заряжен на ", "The battery is charged for "
                ) + f'{sensors_battery()[0]}%'
            )
        except:
            print('')

    def get_loading_point(self, language_one, language_two, taskbar):
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
            self.get_coordinates(self.middle_width, self.middle_height, self.middle_width, self.middle_height)
            self.color.print(
                self.first_color + self.change_language(
                    f'{language_one}{zero}', f'{language_two}{zero}'
                )
            )
            sleep(0.3)

    def get_taskbar(self):
        sys('cls')
        self.get_coordinates(1, 0, 1, 0)

        if self.width == 120 and self.height == 30:
            value = 1.03
        else:
            value = 1.02

        self.color.print(f'{self.third_color}┌{(int(self.width // value)) * "─"}┐')
        self.get_coordinates(1, 1, 1, 1)
        self.color.print(f'{self.third_color}│')

        if self.get_system_language() == 'russian' or self.get_system_language() == 'русский':
            self.get_coordinates(4, 1, int(self.width // 6), 1)
            self.color.print(f"{self.first_color}Инфо")
            self.get_coordinates(11, 1, int(self.width // 4.8), 1)
            self.color.print(f"{self.first_color}Опции")
            self.get_coordinates(19, 1, int(self.width // 3.90), 1)
            self.color.print(f"{self.first_color}Каталог")
            self.get_coordinates(29, 1, int(self.width // 3.12), 1)
            self.color.print(f"{self.first_color}Команды")
            self.get_coordinates(39, 1, int(self.width // 2.63), 1)
            self.color.print(f"{self.first_color}Заметки")
            self.get_coordinates(49, 1, int(self.width // 2.30), 1)
            self.color.print(f"{self.first_color}Программы")
            self.get_coordinates(61, 1, int(self.width // 1.97), 1)
            self.color.print(f"{self.first_color}YouTube")
            self.get_coordinates(71, 1, int(self.width // 1.76), 1)
            self.color.print(f"{self.first_color}Погода")
            self.get_coordinates(80, 1, int(self.width // 1.61), 1)
            self.color.print(f"{self.first_color}Календарь")
            self.get_coordinates(92, 1, int(self.width // 1.44), 1)
            self.color.print(f'{self.first_color}{datetime.now():{f"Время"} %H:%M}')
            self.get_coordinates(106, 1, int(self.width // 1.29), 1)
            self.color.print(f'{self.first_color}{datetime.now():%d.%m.%Y}')
        else:
            self.get_coordinates(4, 1, int(self.width // 6), 1)
            self.color.print(f"{self.first_color}Info")
            self.get_coordinates(11, 1, int(self.width // 4.8), 1)
            self.color.print(f"{self.first_color}Settings")
            self.get_coordinates(22, 1, int(self.width // 3.65), 1)
            self.color.print(f"{self.first_color}Catalog")
            self.get_coordinates(32, 1, int(self.width // 3), 1)
            self.color.print(f"{self.first_color}Сommands")
            self.get_coordinates(43, 1, int(self.width // 2.50), 1)
            self.color.print(f"{self.first_color}Notes")
            self.get_coordinates(51, 1, int(self.width // 2.23), 1)
            self.color.print(f"{self.first_color}Programs")
            self.get_coordinates(62, 1, int(self.width // 1.95), 1)
            self.color.print(f"{self.first_color}YouTube")
            self.get_coordinates(72, 1, int(self.width // 1.75), 1)
            self.color.print(f"{self.first_color}Weather")
            self.get_coordinates(82, 1, int(self.width // 1.58), 1)
            self.color.print(f"{self.first_color}Сalendar")
            self.get_coordinates(93, 1, int(self.width // 1.43), 1)
            self.color.print(f'{self.first_color}{datetime.now():{f"Time"} %H:%M}')
            self.get_coordinates(106, 1, int(self.width // 1.29), 1)
            self.color.print(f'{self.first_color}{datetime.now():%d.%m.%Y}')

        self.get_coordinates(self.width - 2, 1, int(self.width // 1.01), 1)
        self.color.print(f'{self.third_color}│')
        self.get_coordinates(1, 2, 1, 2)
        self.color.print(f'{self.third_color}└{(int(self.width // value)) * "─"}┘')


class CommandsConfig(WidgetsConfig):
    def get_enter_action(self, language_one, language_two):
        self.get_coordinates(self.under_height, self.under_width, self.under_height, self.under_width + 1)
        return self.change_commands_input_language(language_one, language_two)

    def get_exit_or_reboot(self, language_one, language_two):
        self.get_loading_point(language_one, language_two, sys('cls'))

    def get_message_handler(self, language_one, language_two):
        self.get_taskbar()
        self.get_coordinates(self.middle_width, self.middle_height, self.middle_width, self.middle_height)
        self.color.print(self.first_color + self.change_language(language_one, language_two))
