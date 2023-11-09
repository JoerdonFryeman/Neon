from time import sleep
from widgets import Widgets
from os import system as sys
from ast import literal_eval
from pykeplib import GetRandomData


class Images(Widgets, GetRandomData):
    switch = False

    @classmethod
    def break_function(cls) -> None:
        """
        Switch function
        :return: bool
        """
        input()
        cls.switch = True

    @classmethod
    def run_function(cls):
        cls.switch = False

    @staticmethod
    def open_image():
        with open('apps/images.spec') as img:
            image = literal_eval(img.read())
        return image

    def get_image(self):
        while not self.switch:
            image = self.get_random_data(self.open_image())
            if not image:
                continue
            print(image)
            sleep(2)
            sys(self.get_system_command())

    def get_wallpaper(self, fc, sc):
        self.get_coordinates(self.width // 2, self._middle_height - 7, self.width // 2, self._middle_height - 6)
        self.console_color.print(f'{fc}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')
        self.get_coordinates(self.width // 2, self._middle_height - 6, self.width // 2, self._middle_height - 5)
        self.console_color.print(f'{fc}░░░░░░░░░░░░░░░░▄{sc}▄▄█▄██▄▄{fc}░░░░░░░░░░░░░░░░░░')
        self.get_coordinates(self.width // 2, self._middle_height - 5, self.width // 2, self._middle_height - 4)
        self.console_color.print(f'{fc}░░░▄█▀███▄▄█████{sc}███████████████▄▄███▀█{fc}░░░░░')
        self.get_coordinates(self.width // 2, self._middle_height - 4, self.width // 2, self._middle_height - 3)
        self.console_color.print(f'{fc}░░░░█{sc}░░{fc}▀█████{sc}██████████████████████{fc}█{sc}░░█{fc}░░░░')
        self.get_coordinates(self.width // 2, self._middle_height - 3, self.width // 2, self._middle_height - 2)
        self.console_color.print(f'{fc}░░░░░█▄{sc}░░{fc}▀█████{sc}████████{fc}███{sc}███████{fc}█{sc}░░░▄▀{fc}░░░░')
        self.get_coordinates(self.width // 2, self._middle_height - 2, self.width // 2, self._middle_height - 1)
        self.console_color.print(f'{fc}░░░░░░▀█▄▄████▀▀▀{sc}░░░░█{fc}█{sc}░░░{fc}▀▀▀{sc}█████▄▄█▀{fc}░░░░░')
        self.get_coordinates(self.width // 2, self._middle_height - 1, self.width // 2, self._middle_height)
        self.console_color.print(f'{fc}░░░░░░▄███▀▀{sc}░░░░░░░░░█{fc}█{sc}░░░░░░░░░▀███▄{fc}░░░░░░')
        self.get_coordinates(self.width // 2, self._middle_height, self.width // 2, self._middle_height + 1)
        self.console_color.print(f'{fc}░░░░░▄██▀{sc}░░░░░▄▄▄██▄▄██░▄██▄▄▄░░░░░▀██▄{fc}░░░░')
        self.get_coordinates(self.width // 2, self._middle_height + 1, self.width // 2, self._middle_height + 2)
        self.console_color.print(f'{fc}░░░▄██▀{sc}░░░▄▄▄███ ▄█████████ ▄██▄▄▄{sc}░░░▀█▄{fc}░░░')
        self.get_coordinates(self.width // 2, self._middle_height + 2, self.width // 2, self._middle_height + 3)
        self.console_color.print(f'{fc}░░░▀██▄▄████{sc}██████▀░███▀▀▀█████████▄▄▄█▀{fc}░░░')
        self.get_coordinates(self.width // 2, self._middle_height + 3, self.width // 2, self._middle_height + 4)
        self.console_color.print(f'{fc}░░░░░▀█████████{sc}█▀░░░█{fc}█{sc}█░░░▀███████████▀{fc}░░░░')
        self.get_coordinates(self.width // 2, self._middle_height + 4, self.width // 2, self._middle_height + 5)
        self.console_color.print(f'{fc}░░░░░░░▀▀▀██████{sc}░░░{fc}██{sc}███▄░░▀██████▀▀{fc}░░░░░░░')
        self.get_coordinates(self.width // 2, self._middle_height + 5, self.width // 2, self._middle_height + 6)
        self.console_color.print(f'{fc}░░░░░░░░░░░░▀▀▀▀▄{sc}░░█{fc}██{sc}██▀░▄█▀▀▀{fc}░░░░░░░░░░░░')
        self.get_coordinates(self.width // 2, self._middle_height + 6, self.width // 2, self._middle_height + 7)
        self.console_color.print(f'{fc}░░░░░░░░░░░░░░░░░▀▀▄▄▄▄▄▀▀{fc}░░░░░░░░░░░░░░░░░')
        self.get_coordinates(self.width // 2, self._middle_height + 7, self.width // 2, self._middle_height + 8)
        self.console_color.print(f'{fc}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')
