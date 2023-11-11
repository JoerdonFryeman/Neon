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

    def get_data(self, mess_first, mess_second):
        self.get_taskbar()
        self.get_coordinates(self.middle_width, self.middle_height, self.middle_width, self.middle_height)
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
        while True:
            self.get_taskbar()
            self.get_coordinates(self.middle_width - 6, self.middle_height, self.middle_width, self.middle_height)
            self.console_color.print(
                self.first_color + self.change_language(
                    "Введите новый пароль (ввод не отображается...)",
                    "Enter the new password (input not displayed...)"
                )
            )
            new_password = getpass('')
            if new_password == '':
                return self.get_data("Неверная команда!", "Wrong command!")
            if len(new_password) < 7:
                return self.get_data(
                    "Пароль не может быть меньше 7-ми символов!",
                    "Password must not be less than 7 letters!"
                )
            self.console_color.print(
                self.first_color + self.change_language(
                    "Повторите пароль (ввод не отображается...)",
                    "Repeat the password (input not displayed...)"
                )
            )
            new_password_retry = getpass('')
            if new_password != new_password_retry:
                self.get_taskbar()
                self.get_coordinates(self.middle_width - 6, self.middle_height, self.middle_width, self.middle_height)
                return self.get_data(
                    "Подтверждение не совпадает с паролем!",
                    "Confirmation does not match the password!"
                )
            return new_password

    def edit_language(self, data):
        if data == "русский" or data == "russian" or data == "английский" or data == "english":
            self.get_data("Изменения сохранены!", "Changes saved!")
            return data
        else:
            self.get_data(
                "Введите название языка буквами — русский или английский...",
                "Enter the name of the language in letters — russian or english..."
            )

    def edit_color(self):
        counter = 0
        color_list = []

        for i in range(3):
            data = self.get_data(
                f"Выберите цвет номер {counter + 1}... Красный, зелёный, синий, белый, жёлтый, сиреневый: ",
                f"Change color number {counter}... Red, green, blue, white, yellow, purple: "
            )
            if data == '':
                return self.get_data("Неверная команда!", "Wrong command!")
            color_list.append(f'[{self.verify_color(data)}]')
            if self.verify_color(data) == 'red' or self.verify_color(data) == 'green' or \
                    self.verify_color(data) == 'bold blue' or self.verify_color(data) == 'yellow' or \
                    self.verify_color(data) == 'purple' or self.verify_color(data) == 'white':
                counter += 1
                if counter == 3:
                    self.get_data("Изменения сохранены!", "Changes saved!")
                    return color_list
            else:
                return self.get_data("Неверная команда!", "Wrong command!")

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
                        self.get_data("Введите новое имя: ", "Enter new username: "), 2, 11,
                        "Имя не должно быть меньше 2-х или больше 11-ти символов!",
                        "The name must not be less than 2 or more than 11 letters!"
                    )
                    break
                elif cmd.lower() == "город" or cmd.lower() == "city" or cmd.lower() == "г" or cmd.lower() == "c":
                    self.edit_data(
                        self.get_data("Обновите Ваш город: ", "Change your city: "), 2, 100000,
                        "Название города не может быть меньше 2 символов!",
                        "The name of the city must not be less than 2 letters!"
                    )
                    break
                elif cmd.lower() == "логин" or cmd.lower() == "login" or cmd.lower() == "л" or cmd.lower() == "l":
                    self.get_authentication()
                    self.edit_data(
                        self.get_data("Придумайте логин", "Create a login"), 2, 15,
                        "Логин не может быть меньше 2 или больше 15 символов!",
                        "Login must not be less than 2 or more than 15 letters!"
                    )
                    break
                elif cmd.lower() == "пароль" or cmd.lower() == "password" or cmd.lower() == "п" or cmd.lower() == "p":
                    self.get_authentication()
                    self.edit_password()
                    break
                elif cmd.lower() == "язык" or cmd.lower() == "language" or cmd.lower() == "л" or cmd.lower() == "l":
                    self.edit_language(
                        self.get_data(
                            "Выберите язык — русский или английский: ",
                            "Select a language — russian or english: "
                        ).lower()
                    )
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

    def edit_window_mode(self):
        pass

    def edit_weather_key(self):
        pass

    def edit_transparency(self):
        pass
