from time import sleep
from os import system as sys
from commands import Commands


class Application(Commands):
    def get_home_screen(self):
        while True:
            self.get_taskbar()
            self.get_weather()
            self.get_coordinates(0, 8, 0, int(self.height // 2.47))
            print(f'{self.get_green}{self.get_month_calendar()}')
            self.get_wallpaper(self.first_color, self.second_color)
            self.get_battery()
            self.get_main_commands()

    def main(self):
        """Entry point"""
        self.get_screen_mode()
        self.verify_transparency()
        self.get_start_screen()
        self.get_authentication()
        self.get_message(
            sys(self.get_system_command()), print,
            f"Добро пожаловать, {self.get_user_data(self.name)}!", f"Welcome, {self.get_user_data(self.name)}!"
        ), sleep(2)
        self.get_home_screen()


if __name__ == '__main__':
    try:
        app = Application()
        app.main()
    except AttributeError:
        pass
