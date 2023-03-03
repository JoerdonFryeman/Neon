from os import system
from calendar import month
from calendar import weekday
from interface import Visual
from interface import Action
from calendar import calendar
from datetime import datetime
from interface import Widgets
from configuration import Config


class Calendarium:
    year = f'{datetime.now():%Y}'
    month = f'{datetime.now():%m}'
    day = f'{datetime.now():%d}'
    dayoftheweek = weekday(int(year), int(month), int(day))

    __slots__ = ('presstoreturn', 'weeknow', 'monthnow')

    def __init__(self):
        if Config().language() == 'russian' or Config().language() == 'русский':
            self.presstoreturn = "  Нажмите действие для возврата..."
            self.weeknow = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
            self.monthnow = ('', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь',
                             'Октябрь', 'Ноябрь', 'Декабрь')
        else:
            self.presstoreturn = "  Press to return..."
            self.weeknow = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
            self.monthnow = ('', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                             'October', 'November', 'December')

    def calendarday(self):
        Visual().color.print(
            f'{Visual().firstcolor}{self.weeknow[self.dayoftheweek]}, {self.day}. {self.monthnow[int(self.month)]}'
        )

    def calendarmonth(self):
        return f'{month(int(self.year), int(self.month), 3, 2)}'

    def calendaryear(self):
        Visual().color.print('\n', f'{Visual().firstcolor}{calendar(int(self.year), 3, 2)}')

    def commandcalendar(self):
        system('cls')
        Widgets().showtaskbar()
        Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
        self.calendarday()
        Action().presstocontinue()

        system('cls')
        Widgets().showtaskbar()
        Visual().coordinates(0, 8, 0, int(Visual().heightread // 2.47))
        Visual().color.print(f'{Visual().firstcolor}{self.calendarmonth()}')
        Action().presstocontinue()

        system('cls')
        Widgets().showtaskbar()
        self.calendaryear()
        input()
