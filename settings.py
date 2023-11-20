from getpass import getpass
from os import system as sys
from keyboard import press_and_release
from widgets import Widgets
from authentication import Authentication


class Settings(Authentication, Widgets):
    def get_command(self):
        while True:
            self.console_color.print(
                self.get_message_handler(
                    self.get_taskbar(),
                    "Имя, город, логин, пароль, язык, цвет, режим экрана, прозрачность, погода",
                    "Name, city, login, password, language, color, window mode, transparency, weather"
                )
            )
            cmd = self.get_enter_action("Введите действие: ", "Enter action: ")
            if cmd == '':
                break

            while True:
                if cmd.lower() == 'имя' or cmd.lower() == 'name' or cmd.lower() == 'и' or cmd.lower() == 'n':
                    self.edit_name()
                    break
                if cmd.lower() == 'город' or cmd.lower() == 'city' or cmd.lower() == 'г' or cmd.lower() == 'c':
                    self.edit_city()
                    break
                if cmd.lower() == 'логин' or cmd.lower() == 'login' or cmd.lower() == 'л' or cmd.lower() == 'l':
                    self.edit_login()
                    break
                if cmd.lower() == 'пароль' or cmd.lower() == 'password' or cmd.lower() == 'п' or cmd.lower() == 'p':
                    self.get_authentication()
                    self.edit_password()
                    break
                if cmd.lower() == 'язык' or cmd.lower() == 'language' or cmd.lower() == 'я' or cmd.lower() == 'la':
                    self.edit_language()
                    break
                if cmd.lower() == 'цвет' or cmd.lower() == 'color' or cmd.lower() == 'ц' or cmd.lower() == 'co':
                    self.edit_color()
                    break
                if cmd.lower() == 'экран' or cmd.lower() == 'window' or cmd.lower() == 'э' or cmd.lower() == 'w':
                    self.edit_window_mode()
                    break
                if cmd.lower() == 'погода' or cmd.lower() == 'weather' or cmd.lower() == 'по' or cmd.lower() == 'we':
                    self.edit_weather_key()
                    break
                if (
                        cmd.lower() == 'прозрачность' or cmd.lower() == 'transparency' or
                        cmd.lower() == 'пр' or cmd.lower() == 't'
                ):
                    self.edit_transparency()
                    break
                else:
                    self.console_color.print(
                        self.get_message_handler(
                            self.get_taskbar(), "Неверная команда!", "Wrong command!"
                        )
                    )
                    self.get_enter_action("Нажмите действие для возврата...", "Press to return...")
                    break

    def edit_name(self):
        while True:
            name = self.console_color.input(
                self.get_message_handler(
                    self.get_taskbar(), "Введите новое имя: ", "Enter new username: "
                )
            )
            if self.verify_void(
                    name, self.get_taskbar(),
                    "Нажмите действие для возврата...", "Press to return..."
            ):
                break
            if self.verify_length(
                    name, self.get_taskbar(), 2, 11,
                    "Имя не должно быть меньше 2-х или больше 11-ти символов!",
                    "The name must not be less than 2 or more than 11 letters!",
                    "Нажмите ввод для продолжения...", "Press to continue..."
            ):
                break
            self.console_color.print(
                self.get_message_handler(
                    self.get_taskbar(), "Изменения сохранены!", "Changes saved!"
                )
            )
            self.get_enter_action("Нажмите действие для продолжения...", "Press to continue...")
            return name

    def edit_city(self):
        while True:
            city = self.console_color.input(
                self.get_message_handler(
                    self.get_taskbar(), "Обновите Ваш город: ", "Change your city: "
                )
            )
            if self.verify_void(
                    city, self.get_taskbar(),
                    "Нажмите действие для возврата...", "Press to return..."
            ):
                break
            if self.verify_length(
                    city, self.get_taskbar(), 2, 10000,
                    "Название города не может быть меньше 2-х символов!",
                    "The name of the city must not be less than 2 letters!",
                    "Нажмите ввод для продолжения...", "Press to continue..."

            ):
                break
            self.console_color.print(
                self.get_message_handler(
                    self.get_taskbar(), "Изменения сохранены!", "Changes saved!"
                )
            )
            self.get_enter_action("Нажмите действие для продолжения...", "Press to continue...")
            return city

    def edit_login(self):
        while True:
            login = self.console_color.input(
                self.get_message_handler(
                    self.get_taskbar(), "Придумайте логин: ", "Create a login: "
                )
            )
            if self.verify_void(
                    login, self.get_taskbar(),
                    "Нажмите действие для возврата...", "Press to return..."
            ):
                break
            if self.verify_length(
                    login, self.get_taskbar(), 2, 15,
                    "Логин не может быть меньше 2-х или больше 15-ти символов!",
                    "Login must not be less than 2 or more than 15 letters!",
                    "Нажмите ввод для продолжения...", "Press to continue..."
            ):
                break
            self.console_color.print(
                self.get_message_handler(
                    self.get_taskbar(), "Изменения сохранены!", "Changes saved!"
                )
            )
            self.get_enter_action("Нажмите действие для продолжения...", "Press to continue...")
            return login

    def edit_password(self):
        while True:
            self.console_color.print(
                self.get_message_handler(
                    sys(self.get_system_command()),
                    "Введите новый пароль (ввод не отображается...)",
                    "Enter the new password (input not displayed...)"
                )
            )
            new_password = getpass('')
            if self.verify_void(
                    new_password, sys(self.get_system_command()),
                    "Нажмите действие для возврата...", "Press to return..."
            ):
                break
            if self.verify_length(
                    new_password, sys(self.get_system_command()), 7, 10000,
                    "Пароль не может быть меньше 7-ми символов!",
                    "Password must not be less than 7 letters!",
                    "Нажмите ввод для продолжения...", "Press to continue..."
            ):
                break
            self.console_color.print(
                self.get_message_handler(
                    sys(self.get_system_command()),
                    "Повторите пароль (ввод не отображается...)",
                    "Repeat the password (input not displayed...)"
                )
            )
            new_password_retry = getpass('')
            if new_password != new_password_retry:
                self.console_color.input(
                    self.get_message_handler(
                        sys(self.get_system_command()),
                        "Подтверждение не совпадает с паролем!",
                        "Confirmation does not match the password!"
                    )
                )
                break
            return new_password

    def edit_language(self):
        while True:
            language = self.console_color.input(
                self.get_message_handler(
                    self.get_taskbar(),
                    "Выберите язык — русский или английский: ",
                    "Select a language — russian or english: "
                )
            )
            if self.verify_void(
                    language, self.get_taskbar(),
                    "Нажмите действие для возврата...", "Press to return..."
            ):
                break
            if language == "русский" or language == "russian" or language == "английский" or language == "english":
                self.console_color.print(
                    self.get_message_handler(
                        self.get_taskbar(), "Изменения сохранены!", "Changes saved!"
                    )
                )
                self.get_enter_action("Нажмите действие для продолжения...", "Press to continue...")
                return language
            self.console_color.input(
                self.get_message_handler(
                    self.get_taskbar(),
                    "Введите название языка буквами — русский или английский...",
                    "Enter the name of the language in letters — russian or english..."
                )
            )

    @staticmethod
    def verify_color(color):
        if color == 'белый': color = 'white'
        if color == 'красный': color = 'red'
        if color == 'зелёный' or color == 'зеленый': color = 'green'
        if color == 'синий' or color == 'голубой' or color == 'blue': color = 'bold blue'
        if color == 'жёлтый' or color == 'желтый': color = 'yellow'
        if color == 'фиолетовый' or color == 'сиреневый' or color == 'лиловый': color = 'purple'
        return color

    def edit_color(self):
        counter = 0
        color_list = []

        for i in range(3):
            number = counter + 1
            color = self.console_color.input(
                self.get_message_handler(
                    self.get_taskbar(),
                    f"Выберите цвет номер {number}... Красный, зелёный, синий, белый, жёлтый, сиреневый: ",
                    f"Change color number {number}... Red, green, blue, white, yellow, purple: "
                )
            )
            if self.verify_void(
                    color, self.get_taskbar(),
                    "Нажмите действие для возврата...", "Press to return..."
            ):
                break
            color_list.append(f'[{self.verify_color(color)}]')
            if self.verify_color(color) == 'red' or self.verify_color(color) == 'green' or \
                    self.verify_color(color) == 'bold blue' or self.verify_color(color) == 'yellow' or \
                    self.verify_color(color) == 'purple' or self.verify_color(color) == 'white':
                counter += 1
                if counter == 3:
                    self.console_color.print(
                        self.get_message_handler(
                            self.get_taskbar(),
                            "Изменения сохранены!", "Changes saved!"
                        )
                    )
                    self.get_enter_action("Нажмите действие для продолжения...", "Press to continue...")
                    return color_list
            self.console_color.print(
                self.get_message_handler(
                    self.get_taskbar(), "Неверная команда!", "Wrong command!"
                )
            )
            self.get_enter_action("Нажмите действие для возврата...", "Press to return...")
            break

    def edit_window_mode(self):
        while True:
            res = self.console_color.input(
                self.get_message_handler(
                    self.get_taskbar(),
                    "Выберите \"Оконный режим\" или \"Полный экран\": ",
                    "Select \"Window Mode\" or \"Full Screen\": "
                )
            )
            if res.lower() == "оконный" or res.lower() == "window" or res.lower() == "о" or res.lower() == "w":
                self.console_color.print(
                    self.get_message_handler(
                        self.get_taskbar(), "Изменения сохранены!", "Changes saved!"
                    )
                )
                self.get_enter_action("Нажмите действие для продолжения...", "Press to continue...")
                return "[120, 30]"
            elif res.lower() == "полный" or res.lower() == "full" or res.lower() == "п" or res.lower() == "f":
                press_and_release('alt+enter')
                f"[{self.width()}, {self.height() - 1}]"
                self.console_color.print(
                    self.get_message_handler(
                        self.get_taskbar(), "Изменения сохранены!", "Changes saved!"
                    )
                )
                self.get_enter_action("Нажмите действие для продолжения...", "Press to continue...")
                return press_and_release('alt+enter')
            self.console_color.print(
                self.get_message_handler(
                    self.get_taskbar(), "Неверная команда!", "Wrong command!"
                )
            )
            self.get_enter_action("Нажмите действие для возврата...", "Press to return...")
            break

    def edit_weather_key(self):
        while True:
            weather_key = self.console_color.input(
                self.get_message_handler(
                    self.get_taskbar(),
                    "Введите ключ погоды (https://openweathermap.org/): ",
                    "Enter weather key (https://openweathermap.org/): "
                )
            )
            if self.verify_void(
                    weather_key, self.get_taskbar(), "Нажмите действие для возврата...", "Press to return..."
            ):
                break
            self.console_color.print(
                self.get_message_handler(
                    self.get_taskbar(), "Изменения сохранены!", "Changes saved!"
                )
            )
            self.get_enter_action("Нажмите действие для продолжения...", "Press to continue...")
            return weather_key

    def edit_transparency(self):
        while True:
            transparency = self.console_color.input(
                self.get_message_handler(
                    self.get_taskbar(),
                    "Уровень прозрачности терминала (1, 2, 3, 4, 5, 6): ",
                    "Terminal transparency level (1, 2, 3, 4, 5, 6): "
                )
            )
            if self.verify_void(
                    transparency, self.get_taskbar(),
                    "Нажмите действие для возврата...", "Press to return..."
            ):
                break
            try:
                if 0 < int(transparency) < 7:
                    self.console_color.print(
                        self.get_message_handler(
                            self.get_taskbar(), "Изменения сохранены!", "Changes saved!"
                        )
                    )
                    self.get_enter_action("Нажмите действие для продолжения...", "Press to continue...")
                    return transparency
                self.console_color.print(
                    self.get_message_handler(
                        self.get_taskbar(), "Неверная команда!", "Wrong command!"
                    )
                )
                self.get_enter_action("Нажмите действие для возврата...", "Press to return...")
                break
            except ValueError:
                self.console_color.print(
                    self.get_message_handler(
                        self.get_taskbar(), "Неверная команда!", "Wrong command!"
                    )
                )
                self.get_enter_action("Нажмите действие для возврата...", "Press to return...")
                break
