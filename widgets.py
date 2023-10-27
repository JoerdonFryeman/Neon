from bext import goto
from time import sleep
from random import randint
from datetime import datetime
from os import system as sys
from threading import Thread
from psutil import sensors_battery
from keyboard import press_and_release
from platform import system, machine, version, release as os_release
from matrix import Matrix
from system import System


class Widgets(System, Matrix):
    def get_vertical_bar(self, wdt_wind, count_hgt_wind, wdt_full, count_hgt_full):
        global counter

        if self.width == 120 and self.height == 30:
            counter = count_hgt_wind
        else:
            counter = count_hgt_full

        for i in range(int(self.height // 3.75)):
            if self.width == 120 and self.height == 30:
                goto(wdt_wind, counter)
            else:
                goto(wdt_full, counter)
            self.color.print(f'{self.third_color}│{self.width // 4 * " "}│')
            counter += 1

    def get_start_screen(self):
        sys(self.get_system_command())

        self.get_coordinates(0, 7, 0, int(self.height // 3.3))
        self.color.print(f'{self.first_color}{(self.width - 1) * "─"}')

        self.get_coordinates(
            45, 10, int(self.width // 2.66),
            int(self.height // self.get_symbol_resolution(2.76, 2.64))
        )
        self.color.print(f'{self.third_color}┌{self.width // 4 * "─"}┐')

        self.get_vertical_bar(45, 11, int(self.width // 2.66), int(self.height // 2.61))

        self.get_coordinates(50, 13, int(self.width // 2.25), int(self.height // 2.15))
        self.color.print(
            f'{self.first_color}{machine()}, {self.get_user_data(self._name)}'
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
            Matrix().get_matrix_move(
                22, self.height // 4.61, float(f'{0.0}{randint(6, 9)}')
            )
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
        self.color.print(f'{self.get_user_data(self._name)}{self.change_language("-ЭВМ", "-PC")}')
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

    def get_taskbar(self):
        sys(self.get_system_command())
        self.get_coordinates(1, 0, 1, 0)

        if self.width == 120 and self.height == 30:
            value = 1.03
        else:
            value = 1.02

        self.color.print(f'{self.third_color}┌{(int(self.width // value)) * "─"}┐')
        self.get_coordinates(1, 1, 1, 1)
        self.color.print(f'{self.third_color}│')

        if self.get_user_data(self._language) == 'russian' or self.get_user_data(self._language) == 'русский':
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

    def get_shutdown_or_reboot(self, download_text):
        count = 0
        while count < 4:
            sys(self.get_system_command())
            self.get_coordinates(self.middle_width, self.middle_height, self.middle_width, self.middle_height)
            self.color.print(self.first_color + self.get_loading_points(download_text, count))
            count += 1
            sleep(0.3)
