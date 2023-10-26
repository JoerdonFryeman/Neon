from time import sleep
from getpass import getpass
from os import system as sys
from configuration import CommandsConfig


class Authentication(CommandsConfig):
    def get_authentication(self):
        while True:
            sys('cls')
            self.get_coordinates(self.middle_width, self.middle_height, self.middle_width, self.middle_height)
            self.color.print(
                self.first_color + self.change_language(
                    "Введите логин (ввод не отображается)",
                    "Enter login (input isn't displayed)"
                )
            )
            login = getpass('')

            if login != '':
                if login == self._get_user_login():
                    sys('cls')
                    self.get_coordinates(self.middle_width, self.middle_height, self.middle_width, self.middle_height)
                    self.color.print(
                        self.first_color + self.change_language(
                            "Введите пароль (ввод не отображается)",
                            "Enter password (input isn't displayed)"
                        )
                    )
                    password = getpass('')

                    if password != '':
                        if password == self._get_user_password():
                            sys('cls')
                            self.get_coordinates(
                                self.middle_width, self.middle_height, self.middle_width, self.middle_height
                            )
                            self.color.print(
                                self.first_color + self.change_language(
                                    f"Добро пожаловать, {self._get_user_name()}!",
                                    f"Welcome, {self._get_user_name()}!"
                                )
                            ), sleep(2)
                            break
                        else:
                            sys('cls')
                            self.get_coordinates(
                                self.middle_width, self.middle_height, self.middle_width, self.middle_height
                            )
                            self.color.print(
                                self.first_color + self.change_language(
                                    "Неверный пароль!", "Invalid password!"
                                )
                            )
                            self.get_enter_action(
                                "Нажмите действие для возврата...", "Press to return..."
                            )
                    else:
                        sys('cls')
                        self.get_coordinates(
                            self.middle_width, self.middle_height, self.middle_width, self.middle_height
                        )
                        self.color.print(
                            self.first_color + self.change_language(
                                "Вы ничего не ответили!", "You did not answer!"
                            )
                        )
                        self.get_enter_action(
                            "Нажмите действие для возврата...", "Press to return..."
                        )
                else:
                    sys('cls')
                    self.get_coordinates(self.middle_width, self.middle_height, self.middle_width, self.middle_height)
                    self.color.print(
                        self.first_color + self.change_language(
                            "Неверный логин!", "Invalid login!"
                        )
                    )
                    self.get_enter_action(
                        "Нажмите действие для возврата...", "Press to return..."
                    )
            else:
                sys('cls')
                self.get_coordinates(self.middle_width, self.middle_height, self.middle_width, self.middle_height)
                self.color.print(
                    self.first_color + self.change_language(
                        "Вы ничего не ответили!", "You did not answer!"
                    )
                )
                self.get_enter_action(
                    "Нажмите действие для возврата...", "Press to return..."
                )
