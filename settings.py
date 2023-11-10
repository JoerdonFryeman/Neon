from bext import width
from bext import height
from getpass import getpass
from widgets import Widgets
from keyboard import press_and_release
from authentication import Authentication


class Settings(Authentication, Widgets):
    @staticmethod
    def verify_color(color):
        if color == 'белый': color = 'white'
        if color == 'красный': color = 'red'
        if color == 'зелёный' or color == 'зеленый': color = 'green'
        if color == 'синий' or color == 'голубой' or color == 'blue': color = 'bold blue'
        if color == 'жёлтый' or color == 'желтый': color = 'yellow'
        if color == 'фиолетовый' or color == 'сиреневый' or color == 'лиловый': color = 'purple'
        return color

    def get_task_and_coords(self):
        self.get_taskbar()
        self.get_coordinates(self.middle_width, self.middle_height, self.middle_width, self.middle_height)

    def get_data(self, mess_first, mess_second):
        self.get_taskbar()
        self.get_coordinates(self.middle_width - 6, self.middle_height, self.middle_width, self.middle_height)
        return self.console_color.input(self.first_color + self.change_language(mess_first, mess_second))

    def edit_data(self, data, value_one, value_two, mess_first, mess_second):
        if data == '':
            return self.get_data("Неверная команда!", "Wrong command!")
        elif len(data) < value_one or len(data) > value_two:
            return self.get_data(mess_first, mess_second)
        else:
            self.get_data("Изменения сохранены!", "Changes saved!")
            return data

    def edit_password(self):
        new_password = self.edit_data(
            getpass(
                self.get_data(
                    "Введите новый пароль (ввод не отображается...)",
                    "Enter the new password (input not displayed...)"
                )
            ), 7, 100000,
            "Пароль не может быть меньше 7 символов!",
            "Password must not be less than 7 letters!"
        )
        new_password_retry = getpass(
            self.get_data(
                "Повторите пароль (ввод не отображается...)",
                "Repeat the password (input not displayed...)"
            )
        )
        if new_password_retry == '':
            return self.get_data("Неверная команда!", "Wrong command!")
        elif new_password_retry != new_password:
            return self.get_data(
                "Подтверждение не совпадает с паролем!",
                "Confirmation does not match the password!"
            )
        else:
            return new_password

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
                    self.edit_data(
                        self.get_data("Введите новое имя: ", "Enter new username: "),
                        2, 11, "Имя не должно быть меньше 2-х или больше 11-ти символов!",
                        "The name must not be less than 2 or more than 11 letters!"
                    )
                    break
                elif cmd.lower() == "город" or cmd.lower() == "city" or cmd.lower() == "г" or cmd.lower() == "c":
                    self.edit_data(
                        self.get_data(
                            "Введите Ваш город (Необходимо для предоставления сведений о погоде)",
                            "Enter your city (Required to provide weather information)"
                        ), 2, 100000,
                        "Название города не может быть меньше 2 символов!",
                        "The name of the city must not be less than 2 letters!"
                    )
                    break
                elif cmd.lower() == "логин" or cmd.lower() == "login" or cmd.lower() == "л" or cmd.lower() == "l":
                    self.get_authentication()
                    self.edit_data(
                        self.get_data("Придумайте логин", "Create a login"),
                        2, 15,
                        "Логин не может быть меньше 2 или больше 15 символов!",
                        "Login must not be less than 2 or more than 15 letters!"
                    )
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

    def edit_language(self):
        self.get_task_and_coords()

    def edit_color(self):
        counter = 0
        colorlist = []

        for i in range(3):
            self.get_task_and_coords()

    def edit_window_mode(self):
        self.get_task_and_coords()

    def edit_weather_key(self):
        self.get_task_and_coords()

    def edit_transparency(self):
        self.get_task_and_coords()
