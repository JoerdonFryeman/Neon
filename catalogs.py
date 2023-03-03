from os import stat
from os import listdir
from os import scandir
from interface import Visual
from interface import Widgets
from configuration import Config


class Catalogs:
    __slots__ = ('bit', 'wrongcoords')

    def __init__(self):
        if Config().language() == 'russian' or Config().language() == 'русский':
            self.bit = "бит"
            self.wrongcoords = "Система не может отобразить все файлы!"
        else:
            self.bit = "bit"
            self.wrongcoords = "The system cannot display all files!!"

    def showalldir(self):
        Widgets().showtaskbar()

        try:
            Visual().coordinates(50, 6, int(Visual().widthread // 2.33), int(Visual().heightread // 4.7))
            Visual().color.print(Visual().firstcolor + ', '.join(listdir(f'{Config().part()}/TUI/')))

            self.directory(Visual().secondcolor, f'{Config().part()}/TUI/Programs', 2, 10,
                           int(Visual().widthread // 14),
                           int(Visual().heightread // 2.61))
            self.directory(Visual().secondcolor, f'{Config().part()}/TUI/System', 2, 12, int(Visual().widthread // 14),
                           int(Visual().heightread // 2.34))
            self.scandirectory(f'{Config().part()}/TUI/User/Contacts/', 22, 10, int(Visual().widthread // 4.42),
                               int(Visual().heightread // 2.61))
            self.scandirectory(f'{Config().part()}/TUI/User/Notes/', 47, 10, int(Visual().widthread // 2.4),
                               int(Visual().heightread // 2.61))
            self.scandirectory(f'{Config().part()}/TUI/User/Passwords/', 69, 10, int(Visual().widthread // 1.69),
                               int(Visual().heightread // 2.61))
            self.scandirectory(f'{Config().part()}/TUI/User/Downloads/', 94, 10, int(Visual().widthread // 1.27),
                               int(Visual().heightread // 2.61))
            input()

        except BaseException:
            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            Visual().color.input(f"{Visual().firstcolor}{self.wrongcoords}")

    def verifylong(self, file):
        if Visual().widthread == 120 and Visual().heightread == 30:
            valuebit = ''
        else:
            valuebit = f': {stat(file).st_size} {self.bit}'
        if len(str(file.name)) > 15:
            point = '...'
        else:
            point = ''
        return point, valuebit

    def directory(self, clr, link, wdtwind, hgtwind, wdtfull, hgtfull):
        counter = 0
        Visual().coordinates(wdtwind, hgtwind, wdtfull, hgtfull)
        print(link)
        with scandir(f'{link}') as catalog:
            for i in catalog:
                Visual().coordinates(wdtwind, hgtwind + 1 + counter, wdtfull, hgtfull + 1 + counter)
                Visual().color.print(f'{clr}{i.name[0:15]}{self.verifylong(i)[0]}{self.verifylong(i)[1]}')
                counter += 1

    def scandirectory(self, link, wdtwind, hgtwind, wdtfull, hgtfull):
        counter = 0
        if listdir(link) != ([]):
            Visual().coordinates(wdtwind, hgtwind, wdtfull, hgtfull)
            print(link)

            with scandir(f'{link}') as catalog:
                for file in catalog:
                    Visual().coordinates(wdtwind, hgtwind + 1 + counter, wdtfull, hgtfull + 1 + counter)
                    Visual().color.print(f'{Visual().secondcolor}{file.name[0:15]}'
                                         f'{self.verifylong(file)[0]}{self.verifylong(file)[1]}')
                    counter += 1
            print('')
        else:
            self.directory(Visual().firstcolor, link, wdtwind, hgtwind, wdtfull, hgtfull)
