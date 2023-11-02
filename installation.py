from time import sleep
from colorama import Fore
from getpass import getpass
from bext import goto, hide
from os import system as sys
from rich.console import Console
from pykeplib import PyKepLib, Descriptor


class Installation(PyKepLib):
    install_width = Descriptor()
    install_height_first = Descriptor()
    install_height_second = Descriptor()
    install_height_third = Descriptor()
    edit_user_name = Descriptor()
    edit_user_city = Descriptor()
    edit_user_login = Descriptor()
    edit_user_password = Descriptor()
    edit_system_language = Descriptor()
    edit_weather_key = Descriptor()
    edit_system_resolution = Descriptor()
    edit_system_color = Descriptor()
    edit_system_transparency = Descriptor()
    edit_note_file = Descriptor()

    __slots__ = (
        '_install_width', '_install_height_first', '_install_height_second', '_install_height_third', '_edit_user_name',
        '_edit_user_city', '_edit_user_login', '_edit_user_password', '_edit_system_language', '_edit_weather_key',
        '_edit_system_resolution', '_edit_system_color', '_edit_system_transparency', '_edit_note_file'
    )

    def __init__(self):
        self._install_width = 24
        self._install_height_first = 14
        self._install_height_second = 15
        self._install_height_third = 16

        self.install_get_hide = hide()
        self.install_first_color = '[bold blue]'
        self.install_console_color = Console()

        self.install_data = self.get_installation()

        self._edit_user_name = self.install_data[0]
        self._edit_user_city = self.install_data[1]
        self._edit_user_login = self.install_data[2]
        self._edit_user_password = self.install_data[3]
        self._edit_system_language = self.install_data[4]
        self._edit_weather_key = 'f90efe966671bc256131e56a0cf9a5e7'
        self._edit_system_resolution = '120, 30'
        self._edit_system_color = "'[bold blue]', '[purple]', '[purple]'"
        self._edit_system_transparency = 2
        self._edit_note_file = '*2#)7%('

    def get_install_message_handler(self, language_one, language_two):
        sys(self.get_system_command())
        goto(self.install_width, self.install_height_first)
        self.install_console_color.print(self.install_first_color + language_one)
        goto(self.install_width, self.install_height_second)
        self.install_console_color.print(self.install_first_color + language_two)

    def get_install_input(self, language_one, language_two):
        self.get_install_message_handler(language_one, language_two)
        goto(self.install_width, self.install_height_third)
        data = input(Fore.GREEN)
        return data

    def get_install_password(self, language_one, language_two):
        self.get_install_message_handler(language_one, language_two)
        goto(self.install_width, self.install_height_third)
        data = getpass('')
        return data

    def verify_install_data(self, data, value, value_two, mess_first, mess_second, mess_third, mess_four):
        if data == '':
            self.get_install_message_handler(mess_first, mess_second)
            input()
            return False
        if len(data) < value or len(data) > value_two:
            self.get_install_message_handler(mess_third, mess_four)
            input()
            return False
        else:
            return True

    def verify_install_language(self, data):
        if (
                data.lower() == 'russian' or data.lower() == 'русский' or
                data.lower() == 'english' or data.lower() == 'английский'
        ):
            return True
        else:
            self.get_install_message_handler(
                "Необходимо ввести название языка буквами — русский или английский...",
                "You must enter the name of the language in letters — russian or english..."
            )
            input()
            return False

    def get_installation(self):
        install_data_list = []
        self.get_install_message_handler(
            "Спасибо, что выбрали Неон!", "Thank you for choosing Neon!"
        )
        input()

        while True:
            user_name = self.get_install_input(
                "Как можно к Вам обращаться?", "How do I address you?"
            )
            if self.verify_install_data(
                    user_name, 2, 11, "Необходимо ввести имя!", "Name required!",
                    "Имя не может быть меньше 2 или больше 11 символов!",
                    "The name must not be less than 2 or more than 11 letters!"
            ):
                install_data_list.append(user_name)
                while True:
                    user_city = self.get_install_input(
                        "Введите Ваш город (Необходимо для предоставления сведений о погоде)",
                        "Enter your city (Required to provide weather information)"
                    )
                    if self.verify_install_data(
                            user_city, 2, 20, "Необходимо ввести название города!",
                            "You must enter the name of your city!",
                            "Название города не может быть меньше 2 или больше 20 символов!",
                            "The name of the city must not be less than 2 or more than 20 letters!"
                    ):
                        install_data_list.append(user_city)
                        while True:
                            user_login = self.get_install_input(
                                "Придумайте логин", "Create a login"
                            )
                            if self.verify_install_data(
                                    user_login, 2, 15, "Необходимо ввести логин!",
                                    "Login required!",
                                    "Логин не может быть меньше 2 или больше 15 символов!",
                                    "Login must not be less than 2 or more than 15 letters!"
                            ):
                                install_data_list.append(user_login)
                                while True:
                                    user_password = self.get_install_password(
                                        "Придумайте пароль (ввод не отображается...)",
                                        "Create a password (input is not displayed...)"
                                    )
                                    if self.verify_install_data(
                                            user_password, 7, 25, "Необходимо ввести пароль!",
                                            "You have to enter a password!",
                                            "Пароль не может быть меньше 7 или больше 25 символов!",
                                            "Password must not be less than 7 or more than 15 letters!"
                                    ):
                                        user_password_retry = self.get_install_password(
                                            "Повторите пароль (ввод не отображается...)",
                                            "Repeat your password (input is not displayed...)"
                                        )
                                        if user_password != user_password_retry:
                                            self.get_install_message_handler(
                                                "Подтверждение не совпадает с паролем!",
                                                "Confirmation doesn't match the password!"
                                            )
                                            input()
                                        else:
                                            install_data_list.append(user_password)
                                            while True:
                                                system_language = self.get_install_input(
                                                    "Выберите язык — русский или английский",
                                                    "Select a language — russian or english"
                                                )
                                                if self.verify_install_data(
                                                        system_language, 2, 1000,
                                                        "Необходимо выбрать язык!",
                                                        "You have to enter language!",
                                                        "Название языка не может быть меньше 2 символов!",
                                                        "The name of the language must not be less than 2 letters!"
                                                ):
                                                    if self.verify_install_language(system_language):
                                                        install_data_list.append(system_language)
                                                        self.get_install_message_handler(
                                                            "Ввод персональных данных завершен...",
                                                            "Entering personal data is completed..."
                                                        )
                                                        sleep(1)
                                                        self.get_install_message_handler(
                                                            "Установка завершена!",
                                                            "Installation is completed!"
                                                        )
                                                        sleep(1)
                                                        break
                                            break
                                break
                        break
                break

        return install_data_list
