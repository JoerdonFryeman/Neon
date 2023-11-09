from bext import width
from bext import height
from getpass import getpass
from widgets import Widgets
from keyboard import press_and_release


class Settings(Widgets):
    def get_command(self):
        while True:
            self.get_taskbar()
            self.get_coordinates(self.middle_width - 6, self.middle_height, self.middle_width, self.middle_height)
            self.get_message_handler(
                "Имя, город, логин, пароль, язык, цвет, режим экрана, прозрачность, погода",
                "Name, city, login, password, language, color, window mode, transparency, weather"
            )
            cmd = self.get_enter_action("Введите действие: ", "Enter action: ")
            if cmd == '':
                break
            while True:
                if cmd.lower() == "имя" or cmd.lower() == "name" or cmd.lower() == "и" or cmd.lower() == "n":
                    self.edit_name()
                    break
                elif cmd.lower() == "город" or cmd.lower() == "city" or cmd.lower() == "г" or cmd.lower() == "c":
                    self.edit_city()
                    break
                elif cmd.lower() == "логин" or cmd.lower() == "login" or cmd.lower() == "л" or cmd.lower() == "l":
                    self.edit_login()
                    break
                elif cmd.lower() == "пароль" or cmd.lower() == "password" or cmd.lower() == "п" or cmd.lower() == "p":
                    self.edit_password()
                    break
                elif cmd.lower() == "язык" or cmd.lower() == "language" or cmd.lower() == "л" or cmd.lower() == "l":
                    self.edit_language()
                    break
                elif cmd.lower() == "цвет" or cmd.lower() == "color" or cmd.lower() == "ц" or cmd.lower() == "co":
                    self.edit_color()
                    break
                elif cmd.lower() == "экрана" or cmd.lower() == "window" or cmd.lower() == "э" or cmd.lower() == "w":
                    self.edit_window_mode()
                    break
                elif cmd.lower() == "погода" or cmd.lower() == "weather" or cmd.lower() == "по" or cmd.lower() == "we":
                    self.edit_weather_key()
                    break
                elif (
                        cmd.lower() == "прозрачность" or cmd.lower() == "transparency"
                        or cmd.lower() == "пр" or cmd.lower() == "t"
                ):
                    self.edit_transparency()
                    break
                else:
                    self.get_message_handler("Неверная команда!", "Wrong command!")

    @staticmethod
    def verify_color(color):
        if color == 'белый': color = 'white'
        if color == 'красный': color = 'red'
        if color == 'зелёный' or color == 'зеленый': color = 'green'
        if color == 'синий' or color == 'голубой' or color == 'blue': color = 'bold blue'
        if color == 'жёлтый' or color == 'желтый': color = 'yellow'
        if color == 'фиолетовый' or color == 'сиреневый' or color == 'лиловый': color = 'purple'
        return color

    def get_taskbar_and_coordinates(self):
        self.get_taskbar()
        self.get_coordinates(self.middle_width, self.middle_height, self.middle_width, self.middle_height)

    def edit_name(self):
        self.get_taskbar_and_coordinates()
        get_user_name = self.get_enter_action("Введите новое имя: ", "Enter new username: ")
        if get_user_name == '':
            return self.get_enter_action("Неверная команда!", "Wrong command!")
        elif len(get_user_name) < 2 or len(get_user_name) > 11:
            self.get_taskbar_and_coordinates()
            return self.get_enter_action(
                "Имя не должно быть меньше 2-х или больше 11-ти символов!",
                "The name must not be less than 2 or more than 11 letters!"
            )
        else:
            self.get_enter_action("Изменения сохранены!", "Changes saved!")
            return get_user_name

    def edit_city(self):
        self.get_taskbar_and_coordinates()

    def edit_login(self):
        self.get_taskbar_and_coordinates()

    def edit_password(self):
        self.get_taskbar_and_coordinates()

    def edit_language(self):
        self.get_taskbar_and_coordinates()

    def edit_color(self):
        counter = 0
        colorlist = []

        for i in range(3):
            self.get_taskbar_and_coordinates()

    def edit_window_mode(self):
        self.get_taskbar_and_coordinates()

    def edit_weather_key(self):
        self.get_taskbar_and_coordinates()

    def edit_transparency(self):
        self.get_taskbar_and_coordinates()
