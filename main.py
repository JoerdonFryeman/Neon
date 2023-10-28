from time import sleep
from random import randint
from threading import Thread
from bext import title, BextException
from os import startfile, system as sys
from apps.notes import Notes
from matrix import Matrix
from apps.images import Images
from apps.clock import ClockWork
from settings import Settings
from widgets import Widgets
from apps.weather import WeatherNow
from apps.calendarium import Calendarium
from authentication import Authentication

wdg = Widgets()
atc = Authentication()


def get_home_screen():
    while True:
        pass


def main():
    """Entry point"""
    try:
        pass
    except (FileNotFoundError, BextException):
        pass


if __name__ == '__main__':
    main()
