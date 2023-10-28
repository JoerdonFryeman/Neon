from time import sleep
from random import randint
from threading import Thread
from bext import BextException
from os import startfile, system as sys
from apps.notes import Notes
from matrix import Matrix
from apps.clock import ClockWork
from settings import Settings
from widgets import Widgets
from authentication import Authentication

wd = Widgets()
at = Authentication()


def get_home_screen():
    while True:
        wd.get_taskbar()
        wd.get_weather()
        wd.get_coordinates(0, 8, 0, int(wd.height // 2.47))
        print(f'{wd.get_green}{wd.get_month_calendar()}')
        wd.get_coordinates(wd.width // 2, wd.middle_height + 6, wd.width // 2, wd.middle_height + 7)
        print(wd.get_wallpaper(wd.first_color, wd.second_color))
        wd.get_battery()


def main():
    """Entry point"""
    try:
        wd.get_screen_mode()
        wd.verify_transparency()
        wd.get_start_screen()
        if at.get_authentication():
            get_home_screen()
        else:
            sys(wd.get_system_command())
            wd.get_message_handler("Что-то пошло не так...", "Something's gone wrong...")
    except (FileNotFoundError, BextException):
        sys(wd.get_system_command())
        wd.get_message_handler("Что-то пошло не так...", "Something's gone wrong...")


if __name__ == '__main__':
    main()
