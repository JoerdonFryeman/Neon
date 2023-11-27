from os import listdir, scandir, stat

from widgets import Widgets


# Create your tests here.

class Tests(Widgets):
    def show_all_dir(self):
        self.get_taskbar()
        try:
            self.get_coordinates(50, 6, int(self.width // 2.33), int(self.height // 4.7))
            self.color.print(self.first_color + ', '.join(listdir()))
            self.directory(self.second_color, '/', 2, 10, int(self.width // 14), int(self.height // 2.61))
            self.directory(self.second_color, '/', 2, 12, int(self.width // 14), int(self.height // 2.34))
            self.scan_directory('/', 22, 10, int(self.width // 4.42), int(self.height // 2.61))
            self.scan_directory('/', 47, 10, int(self.width // 2.4), int(self.height // 2.61))
            self.scan_directory('/', 69, 10, int(self.width // 1.69), int(self.height // 2.61))
            self.scan_directory('/', 94, 10, int(self.width // 1.27), int(self.height // 2.61))
            input()
        except BaseException:
            self.get_message(
                self.get_taskbar(), input,
                "Система не может отобразить все файлы!",
                "The system cannot display all files!!"
            )

    def get_verify_long(self, file):
        if self.width == 120 and self.height == 30:
            value_bit = ''
        else:
            value_bit = f': {stat(file).st_size} {self.get_message(self.get_taskbar(), print, "бит", "bit")}'
        if len(str(file.name)) > 15:
            point = '...'
        else:
            point = ''
        return point, value_bit

    def directory(self, clr, link, wdt_wind, hgt_wind, wdt_full, hgt_full):
        counter = 0
        self.get_coordinates(wdt_wind, hgt_wind, wdt_full, hgt_full)
        print(link)
        with scandir(f'{link}') as catalog:
            for i in catalog:
                self.get_coordinates(wdt_wind, hgt_wind + 1 + counter, wdt_full, hgt_full + 1 + counter)
                self.console_color.print(f'{clr}{i.name[0:15]}{self.get_verify_long(i)[0]}{self.get_verify_long(i)[1]}')
                counter += 1

    def scan_directory(self, link, wdt_wind, hgt_wind, wdt_full, hgt_full):
        counter = 0
        if listdir(link) != ([]):
            self.get_coordinates(wdt_wind, hgt_wind, wdt_full, hgt_full)
            print(link)

            with scandir(f'{link}') as catalog:
                for file in catalog:
                    self.get_coordinates(wdt_wind, hgt_wind + 1 + counter, wdt_full, hgt_full + 1 + counter)
                    self.console_color.print(
                        f'{self.second_color}{file.name[0:15]}'
                        f'{self.get_verify_long(file)[0]}{self.get_verify_long(file)[1]}'
                    )
                    counter += 1


t = Tests()
t.show_all_dir()
