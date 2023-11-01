from time import sleep
from colorama import Fore
from getpass import getpass
# from bext import goto, hide
from os import system as sys
from rich.console import Console
from pykeplib import Enigma


class Installation(Enigma):
    # hide()
    __install_width = 24
    __install_height_first = 14
    __install_height_second = 15
    __install_height_third = 16
    __install_first_color = '[bold blue]'
    __install_console_color = Console()

    def get_install_message_handler(self, language_one, language_two):
        sys(self.get_system_command())
        # goto(self.__install_width, self.__install_height_first)
        self.__install_console_color.print(self.__install_first_color + language_one)
        # goto(self.__install_width, self.__install_height_second)
        self.__install_console_color.print(self.__install_first_color + language_two)

    def get_install_input(self, language_one, language_two):
        self.get_install_message_handler(language_one, language_two)
        # goto(self.__install_width, self.__install_height_third)
        data = input(Fore.GREEN)
        return data

    def get_install_password(self, language_one, language_two):
        self.get_install_message_handler(language_one, language_two)
        # goto(self.__install_width, self.__install_height_third)
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

    @staticmethod
    def verify_install_language(data):
        if (
                data.lower() == 'russian' or data.lower() == 'русский' or
                data.lower() == 'english' or data.lower() == 'английский'
        ):
            install.get_install_message_handler(
                "Ввод персональных данных завершен...",
                "Entering personal data is completed..."
            )
            sleep(1)
            install.get_install_message_handler(
                "Установка завершена!",
                "Installation is completed!"
            )
            sleep(1)
            return True
        else:
            install.get_install_message_handler(
                "Необходимо ввести название языка буквами — русский или английский...",
                "You must enter the name of the language in letters — russian or english..."
            )
            input()
            return False


install = Installation()

install.get_install_message_handler(
    "Спасибо, что выбрали Неон!", "Thank you for choosing Neon!"
)
input()

while True:
    user_name = install.get_install_input(
        "Как можно к Вам обращаться?", "How do I address you?"
    )
    if install.verify_install_data(
            user_name, 2, 11, "Необходимо ввести имя!", "Name required!",
            "Имя не может быть меньше 2 или больше 11 символов!",
            "The name must not be less than 2 or more than 11 letters!"
    ):
        while True:
            user_city = install.get_install_input(
                "Введите Ваш город (Необходимо для предоставления сведений о погоде)",
                "Enter your city (Required to provide weather information)"
            )
            if install.verify_install_data(
                    user_city, 2, 20, "Необходимо ввести название города!",
                    "You must enter the name of your city!",
                    "Название города не может быть меньше 2 или больше 20 символов!",
                    "The name of the city must not be less than 2 or more than 20 letters!"
            ):
                while True:
                    user_login = install.get_install_input(
                        "Придумайте логин", "Create a login"
                    )
                    if install.verify_install_data(
                            user_login, 2, 15, "Необходимо ввести логин!",
                            "Login required!",
                            "Логин не может быть меньше 2 или больше 15 символов!",
                            "Login must not be less than 2 or more than 15 letters!"
                    ):
                        while True:
                            user_password = install.get_install_password(
                                "Придумайте пароль (ввод не отображается...)",
                                "Create a password (input is not displayed...)"
                            )
                            if install.verify_install_data(
                                    user_password, 7, 25, "Необходимо ввести пароль!",
                                    "You have to enter a password!",
                                    "Пароль не может быть меньше 7 или больше 25 символов!",
                                    "Password must not be less than 7 or more than 15 letters!"
                            ):
                                user_password_retry = install.get_install_password(
                                    "Повторите пароль (ввод не отображается...)",
                                    "Repeat your password (input is not displayed...)"
                                )
                                if user_password != user_password_retry:
                                    install.get_install_message_handler(
                                        "Подтверждение не совпадает с паролем!",
                                        "Confirmation doesn't match the password!"
                                    )
                                    input()
                                else:
                                    while True:
                                        system_language = install.get_install_input(
                                            "Выберите язык — русский или английский",
                                            "Select a language — russian or english"
                                        )
                                        if install.verify_install_data(
                                                system_language, 2, 1000,
                                                "Необходимо выбрать язык!",
                                                "You have to enter language!",
                                                "Название языка не может быть меньше 2 символов!",
                                                "The name of the language must not be less than 2 letters!"
                                        ):
                                            if install.verify_install_language(system_language):
                                                break
                                    break
                        break
                break
        break

weather_key = 'f90efe966671bc256131e56a0cf9a5e7'
system_resolution = '120, 30'
system_color = "'[bold blue]', '[purple]', '[purple]'"
system_transparency = 2
note_file = '*2#)7%('
