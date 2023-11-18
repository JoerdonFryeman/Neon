from getpass import getpass
from os import system as sys
from widgets import Widgets


class Authentication(Widgets):
    def get_invalid_answer(self, language_one, language_two):
        self.console_color.print(
            self.get_message_handler(sys(self.get_system_command()), language_one, language_two)
        )
        self.get_enter_action("Нажмите действие для возврата...", "Press to return...")

    def get_authentication(self):
        while True:
            self.console_color.print(
                self.get_message_handler(
                    sys(self.get_system_command()),
                    "Введите логин (ввод не отображается)", "Enter login (input isn't displayed)"
                )
            )
            login = getpass('')
            if login != '':
                if login == self.get_user_data(self.login):
                    self.console_color.print(
                        self.get_message_handler(
                            sys(self.get_system_command()),
                            "Введите пароль (ввод не отображается)", "Enter password (input isn't displayed)"
                        )
                    )
                    password = getpass('')
                    if password != '':
                        if password == self.get_user_data(self.password):
                            break
                        else:
                            self.get_invalid_answer("Неверный пароль!", "Invalid password!")
                    else:
                        self.get_invalid_answer("Вы ничего не ответили!", "You did not answer!")
                else:
                    self.get_invalid_answer("Неверный логин!", "Invalid login!")
            else:
                self.get_invalid_answer("Вы ничего не ответили!", "You did not answer!")
