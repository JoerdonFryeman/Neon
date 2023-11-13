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

    def edit_name_city_login(self, data, value_one, value_two, mess_first, mess_second):
        self.verify_void(data, "Неверная команда!", "Wrong command!", 6)
        self.verify_length(data, value_one, value_two, mess_first, mess_second, 6)
        self.console_color.input(
            self.get_message_handler(
                "Изменения сохранены!", "Changes saved!", 6, self.get_taskbar
            )
        )
        return data

    def edit_password(self):
        while True:
            new_password = getpass(
                self.console_color.print(
                    self.get_message_handler(
                        "Введите новый пароль (ввод не отображается...)",
                        "Enter the new password (input not displayed...)", 6, self.get_taskbar
                    )
                )
            )
            self.verify_void(new_password, "Неверная команда!", "Wrong command!", 6)
            self.verify_length(
                new_password, 7, 100000,
                "Пароль не может быть меньше 7-ми символов!",
                "Password must not be less than 7 letters!", 6
            )
            new_password_retry = getpass(
                self.console_color.print(
                    self.get_message_handler(
                        "Повторите пароль (ввод не отображается...)",
                        "Repeat the password (input not displayed...)", 6, self.get_taskbar
                    )
                )
            )
            if new_password != new_password_retry:
                self.get_coordinates(self.middle_width - 6, self.middle_height, self.middle_width, self.middle_height)
                return self.console_color.input(
                    self.get_message_handler(
                        "Подтверждение не совпадает с паролем!",
                        "Confirmation does not match the password!", 6, self.get_taskbar
                    )
                )
            return new_password

    def edit_language(self, data):
        if data == "русский" or data == "russian" or data == "английский" or data == "english":
            self.console_color.input(
                self.get_message_handler(
                    "Изменения сохранены!", "Changes saved!", 6, self.get_taskbar
                )
            )
            return data
        else:
            self.console_color.input(
                self.get_message_handler(
                    "Введите название языка буквами — русский или английский...",
                    "Enter the name of the language in letters — russian or english...", 6, self.get_taskbar
                )
            )

    def edit_color(self):
        counter = 0
        color_list = []

        for i in range(3):
            data = self.console_color.input(
                self.get_message_handler(
                    f"Выберите цвет номер {counter + 1}... Красный, зелёный, синий, белый, жёлтый, сиреневый: ",
                    f"Change color number {counter}... Red, green, blue, white, yellow, purple: ", 6, self.get_taskbar
                )
            )
            if data == '':
                return self.console_color.input(
                    self.get_message_handler(
                        "Неверная команда!", "Wrong command!", 6, self.get_taskbar
                    )
                )
            color_list.append(f'[{self.verify_color(data)}]')
            if self.verify_color(data) == 'red' or self.verify_color(data) == 'green' or \
                    self.verify_color(data) == 'bold blue' or self.verify_color(data) == 'yellow' or \
                    self.verify_color(data) == 'purple' or self.verify_color(data) == 'white':
                counter += 1
                if counter == 3:
                    self.console_color.input(
                        self.get_message_handler(
                            "Изменения сохранены!", "Changes saved!", 6, self.get_taskbar
                        )
                    )
                    return color_list
            else:
                return self.console_color.input(
                    self.get_message_handler(
                        "Неверная команда!", "Wrong command!", 6, self.get_taskbar
                    )
                )

    def edit_window_mode(self):
        while True:
            res = self.console_color.input(
                self.get_message_handler(
                    "Выберите \"Оконный режим\" или \"Полный экран\": ",
                    "Select \"Window Mode\" or \"Full Screen\": ", 0, self.get_taskbar
                )
            )
            self.verify_void(res, "Неверная команда!", "Wrong command!", 0)
            if res.lower() == 'оконный' or res.lower() == 'о' or res.lower() == 'window' or res.lower() == 'w':
                return res
            elif res.lower() == 'полный' or res.lower() == 'п' or res.lower() == 'full' or res.lower() == 'f':
                press_and_release('alt+enter')
                self.console_color.input(
                    self.get_message_handler(
                        "Изменения сохранены!", "Changes saved!", 6, self.get_taskbar
                    )
                )
                return res, press_and_release('alt+enter')
            else:
                return self.console_color.input(
                    self.get_message_handler(
                        "Неверная команда!", "Wrong command!", 6, self.get_taskbar
                    )
                )

    def edit_weather_key(self):
        while True:
            weather_key = self.console_color.input(
                self.get_message_handler(
                    "Введите ключ погоды (https://openweathermap.org/): ",
                    "Enter weather key (https://openweathermap.org/): ", 0, self.get_taskbar
                )
            )
            self.verify_void(weather_key, "Неверная команда!", "Wrong command!", 0)
            self.console_color.input(
                self.get_message_handler(
                    "Изменения сохранены!", "Changes saved!", 6, self.get_taskbar
                )
            )
            return weather_key

    def edit_transparency(self):
        while True:
            try:
                level = self.console_color.input(
                    self.get_message_handler(
                        "Уровень прозрачности терминала (1, 2, 3, 4, 5, 6): ",
                        "Terminal transparency level (1, 2, 3, 4, 5, 6): ", 0, self.get_taskbar
                    )
                )
                self.verify_void(int(level), "Неверная команда!", "Wrong command!", 0)
                self.verify_length(level, "Неверная команда!", "Wrong command!", 0, 7, 0)
                return level
            except ValueError:
                return self.console_color.input(
                    self.get_message_handler(
                        "Неверная команда!", "Wrong command!", 6, self.get_taskbar
                    )
                )

    def get_command(self):
        while True:
            self.get_coordinates(self.middle_width - 6, self.middle_height, self.middle_width, self.middle_height)
            self.console_color.print(
                self.get_message_handler(
                    "Имя, город, логин, пароль, язык, цвет, режим экрана, прозрачность, погода",
                    "Name, city, login, password, language, color, window mode, transparency, weather",
                    0, self.get_taskbar
                )
            )
            cmd = self.get_enter_action("Введите действие: ", "Enter action: ")
            if cmd == '':
                break

            while True:
                if cmd.lower() == "имя" or cmd.lower() == "name" or cmd.lower() == "и" or cmd.lower() == "n":
                    try:
                        self.edit_name_city_login(
                            self.console_color.input(
                                self.get_message_handler(
                                    "Введите новое имя: ", "Enter new username: ", 6, self.get_taskbar
                                )
                            ), 2, 11,
                            "Имя не должно быть меньше 2-х или больше 11-ти символов!",
                            "The name must not be less than 2 or more than 11 letters!"
                        )
                    except ValueError:
                        break
                    break
                elif cmd.lower() == "город" or cmd.lower() == "city" or cmd.lower() == "г" or cmd.lower() == "c":
                    try:
                        self.edit_name_city_login(
                            self.console_color.input(
                                self.get_message_handler(
                                    "Обновите Ваш город: ", "Change your city: ", 6, self.get_taskbar
                                )
                            ), 2, 100000,
                            "Название города не может быть меньше 2 символов!",
                            "The name of the city must not be less than 2 letters!"
                        )
                    except ValueError:
                        break
                    break
                elif cmd.lower() == "логин" or cmd.lower() == "login" or cmd.lower() == "л" or cmd.lower() == "l":
                    try:
                        self.get_authentication()
                        self.edit_name_city_login(
                            self.console_color.input(
                                self.get_message_handler(
                                    "Придумайте логин", "Create a login", 6, self.get_taskbar
                                )
                            ), 2, 15,
                            "Логин не может быть меньше 2 или больше 15 символов!",
                            "Login must not be less than 2 or more than 15 letters!"
                        )
                    except ValueError:
                        break
                    break
                elif cmd.lower() == "пароль" or cmd.lower() == "password" or cmd.lower() == "п" or cmd.lower() == "p":
                    self.get_authentication()
                    self.edit_password()
                    break
                elif cmd.lower() == "язык" or cmd.lower() == "language" or cmd.lower() == "л" or cmd.lower() == "l":
                    self.edit_language(
                        self.console_color.input(
                            self.get_message_handler(
                                "Выберите язык — русский или английский: ",
                                "Select a language — russian or english: ", 6, self.get_taskbar
                            ).lower()
                        )
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
                    self.console_color.print(
                        self.get_message_handler("Неверная команда!", "Wrong command!", 0, self.get_taskbar)
                    )
