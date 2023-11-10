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

    __slots__ = (
        'get_hide', 'get_green', 'console_color', '_install_width', '_install_height_first',
        '_install_height_second', '_install_height_third', 'install_first_color'
    )

    def __init__(self):
        self.get_hide = hide()
        self.get_green = Fore.GREEN
        self.console_color = Console()
        self._install_width = 24
        self._install_height_first = 14
        self._install_height_second = 15
        self._install_height_third = 16
        self.install_first_color = '[bold blue]'

    def get_install_message_handler(self, language_one, language_two):
        sys(self.get_system_command())
        goto(self.install_width, self.install_height_first)
        self.console_color.print(self.install_first_color + language_one)
        goto(self.install_width, self.install_height_second)
        self.console_color.print(self.install_first_color + language_two)

    def get_install_input(self, language_one, language_two):
        self.get_install_message_handler(language_one, language_two)
        goto(self.install_width, self.install_height_third)
        data = input(self.get_green)
        return data

    def get_install_password(self, language_one, language_two):
        self.get_install_message_handler(language_one, language_two)
        goto(self.install_width, self.install_height_third)
        data = getpass('')
        return data

    def verify_install_data(self, data, value_one, value_two, mess_first, mess_second, mess_third, mess_four):
        if data == '':
            self.get_install_message_handler(mess_first, mess_second)
            input()
            return False
        if len(data) < value_one or len(data) > value_two:
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
        install_data_list_first = []
        install_data_list_second = [
            'f90efe966671bc256131e56a0cf9a5e7', '120, 30', "'[bold blue]', '[purple]', '[purple]'", 2, '*2#)7%('
        ]
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
                install_data_list_first.append(user_name)
                while True:
                    user_city = self.get_install_input(
                        "Введите Ваш город (Необходимо для предоставления сведений о погоде)",
                        "Enter your city (Required to provide weather information)"
                    )
                    if self.verify_install_data(
                            user_city, 2, 100000, "Необходимо ввести название города!",
                            "You must enter the name of your city!",
                            "Название города не может быть меньше 2 символов!",
                            "The name of the city must not be less than 2 letters!"
                    ):
                        install_data_list_first.append(user_city)
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
                                install_data_list_first.append(user_login)
                                while True:
                                    user_password = self.get_install_password(
                                        "Придумайте пароль (ввод не отображается...)",
                                        "Create a password (input is not displayed...)"
                                    )
                                    if self.verify_install_data(
                                            user_password, 7, 100000, "Необходимо ввести пароль!",
                                            "You have to enter a password!",
                                            "Пароль не может быть меньше 7 символов!",
                                            "Password must not be less than 7 letters!"
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
                                            install_data_list_first.append(user_password)
                                            while True:
                                                system_language = self.get_install_input(
                                                    "Выберите язык — русский или английский",
                                                    "Select a language — russian or english"
                                                )
                                                if self.verify_install_data(
                                                        system_language, 2, 100000,
                                                        "Необходимо выбрать язык!",
                                                        "You have to enter language!",
                                                        "Название языка не может быть меньше 2 символов!",
                                                        "The name of the language must not be less than 2 letters!"
                                                ):
                                                    if self.verify_install_language(system_language):
                                                        install_data_list_first.append(system_language)
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

        return install_data_list_first + install_data_list_second
