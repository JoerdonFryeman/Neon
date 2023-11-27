from time import sleep
from random import randint
from threading import Thread
from os import system as sys, startfile
from apps.clock import ClockWork
from apps.images import Images
from apps.notes import Notes
from apps.neo import Neo
from apps.youtube import YouTubeLoader
from settings import Settings
from widgets import Widgets
from matrix import Matrix


class Commands(
    Settings, ClockWork, Images, Notes, YouTubeLoader, Widgets, Matrix, Neo
):
    def get_programs_commands(self):
        while True:
            self.get_message(self.get_taskbar(), print, "Контакты, пароли, кнб", "Contacts, passwords, rps")
            cmd = self.get_enter_action("Введите действие: ", "Enter action: ")
            if cmd.lower() == '#':
                pass
            elif cmd == '':
                break
            else:
                self.get_message(self.get_taskbar(), print, "Неверная команда!", "Wrong command!")

    def get_main_commands(self):
        cmd = self.get_enter_action("Введите действие: ", "Enter action: ")
        if cmd.lower() == 'выход' or cmd.lower() == 'вхд' or cmd.lower() == 'exit' or cmd.lower() == 'ext':
            self.get_shutdown_or_reboot(self.change_language("Завершение работы", "Shutdown"))
            exit()
        elif cmd.lower() == 'перезагрузка' or cmd.lower() == 'прз' or cmd.lower() == 'reboot' or cmd.lower() == 'reb':
            self.get_shutdown_or_reboot(self.change_language("Перезагрузка", "Reboot"))
            startfile(self.neon)
            exit()
        elif cmd.lower() == 'опции' or cmd.lower() == 'о' or cmd.lower() == 'settings' or cmd.lower() == 's':
            self.get_settings()
            input()
            self.get_command()
        elif cmd.lower() == 'заметки' or cmd.lower() == 'з' or cmd.lower() == 'notes' or cmd.lower() == 'n':
            self.open_note()
        elif cmd.lower() == 'ютьюб' or cmd.lower() == 'ю' or cmd.lower() == 'youtube' or cmd.lower() == 'y':
            self.download_video()
        elif cmd.lower() == 'программы' or cmd.lower() == 'п' or cmd.lower() == 'programs' or cmd.lower() == 'p':
            self.get_programs_commands()
        elif cmd.lower() == 'нео' or cmd.lower() == 'н' or cmd.lower() == 'neo' or cmd.lower() == 'n':
            self.run_text()
        elif cmd.lower() == 'матрица' or cmd.lower() == 'matrix' or cmd.lower() == 'м' or cmd.lower() == 'm':
            sys(self.get_system_command())
            Thread(target=Matrix().run_function).start()
            Matrix().get_matrix_move(-1, self.height - 1, float(f'{0.0}{randint(6, 9)}'))
            Thread(target=Matrix().break_function).start()
            input()
        elif cmd.lower() == 'время' or cmd.lower() == 'в' or cmd.lower() == 'time' or cmd.lower() == 't':
            sys(self.get_system_command())
            Thread(target=self.run_function).start()
            Thread(target=self.command_time).start()
            Thread(target=self.break_function).start()
            input()
            sleep(0.3)
        elif cmd == '':
            self.get_message(self.get_taskbar(), print, "Вы ничего не ответили!", "You didn't answer!")
            self.get_enter_action("Нажмите действие для возврата...", "Press to return...")
        else:
            self.get_message(self.get_taskbar(), print, "Неверная команда!", "Wrong command!")
            self.get_enter_action("Нажмите действие для возврата...", "Press to return...")
