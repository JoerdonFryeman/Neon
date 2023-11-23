from getpass import getpass
from os import system as sys
from widgets import Widgets


class Authentication(Widgets):
    def get_authentication(self):
        while True:
            self.get_message(
                sys(self.get_system_command()), print,
                "Введите логин (ввод не отображается)", "Enter login (input isn't displayed)"
            )
            login = getpass('')
            if login != '':
                if login == self.get_user_data(self.login):
                    self.get_message(
                        sys(self.get_system_command()), print,
                        "Введите пароль (ввод не отображается)", "Enter password (input isn't displayed)"
                    )
                    password = getpass('')
                    if password != '':
                        if password == self.get_user_data(self.password):
                            break
                        else:
                            self.get_message(sys(self.get_system_command()), print, "Неверный пароль!",
                                             "Invalid password!")
                            self.get_enter_action("Нажмите действие для возврата...", "Press to return...")
                    else:
                        self.get_message(sys(self.get_system_command()), print, "Вы ничего не ответили!",
                                         "You did not answer!")
                        self.get_enter_action("Нажмите действие для возврата...", "Press to return...")
                else:
                    self.get_message(sys(self.get_system_command()), print, "Неверный логин!", "Invalid login!")
                    self.get_enter_action("Нажмите действие для возврата...", "Press to return...")
            else:
                self.get_message(sys(self.get_system_command()), print, "Вы ничего не ответили!", "You did not answer!")
                self.get_enter_action("Нажмите действие для возврата...", "Press to return...")
