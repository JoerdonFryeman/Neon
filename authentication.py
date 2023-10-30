from time import sleep
from getpass import getpass
from os import system as sys
from widgets import Widgets


class Authentication(Widgets):
    def get_invalid_answer(self, language_one, language_two):
        sys(self.get_system_command())
        self.get_message_handler(language_one, language_two)
        self.get_enter_action("Нажмите действие для возврата...", "Press to return...")

    def get_authentication(self):
        while True:
            sys(self.get_system_command())
            self.get_message_handler(
                "Введите логин (ввод не отображается)",
                "Enter login (input isn't displayed)"
            )
            login = getpass('')
            if login != '':
                if login == self.get_user_data(self.login):
                    sys(self.get_system_command())
                    self.get_message_handler(
                        "Введите пароль (ввод не отображается)",
                        "Enter password (input isn't displayed)"
                    )
                    password = getpass('')
                    if password != '':
                        if password == self.get_user_data(self.password):
                            sys(self.get_system_command())
                            self.get_message_handler(
                                f"Добро пожаловать, {self.get_user_data(self.name)}!",
                                f"Welcome, {self.get_user_data(self.name)}!"
                            ), sleep(2)
                            break
                        else:
                            self.get_invalid_answer("Неверный пароль!", "Invalid password!")
                    else:
                        self.get_invalid_answer("Вы ничего не ответили!", "You did not answer!")
                else:
                    self.get_invalid_answer("Неверный логин!", "Invalid login!")
            else:
                self.get_invalid_answer("Вы ничего не ответили!", "You did not answer!")
