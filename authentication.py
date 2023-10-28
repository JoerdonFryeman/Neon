from time import sleep
from getpass import getpass
from os import system as sys
from widgets import Widgets


class Authentication(Widgets):
    def get_user_login(self):
        self.get_message_handler(
            "Введите логин (ввод не отображается)", "Enter login (input isn't displayed)"
        )
        login = getpass('')
        return login

    def get_user_password(self):
        self.get_message_handler(
            "Введите пароль (ввод не отображается)", "Enter password (input isn't displayed)"
        )
        password = getpass('')
        return password

    def get_invalid_answer(self, language_one, language_two):
        sys(self.get_system_command())
        self.get_message_handler(language_one, language_two)
        self.get_enter_action("Нажмите действие для возврата...", "Press to return...")

    def get_authentication(self):
        while True:
            sys(self.get_system_command())
            self.get_user_login()
            if self.get_user_login() != '':
                if self.get_user_login() == self.get_user_data(self._login):
                    sys(self.get_system_command())
                    self.get_user_password()
                    if self.get_user_password() != '':
                        if self.get_user_password() == self.get_user_data(self._password):
                            sys(self.get_system_command())
                            self.get_message_handler(
                                f"Добро пожаловать, {self.get_user_data(self._name)}!",
                                f"Welcome, {self.get_user_data(self._name)}!"
                            ), sleep(2)
                            break
                        self.get_invalid_answer("Неверный пароль!", "Invalid password!")
                    self.get_invalid_answer("Вы ничего не ответили!", "You did not answer!")
                self.get_invalid_answer("Неверный логин!", "Invalid login!")
            self.get_invalid_answer("Вы ничего не ответили!", "You did not answer!")
