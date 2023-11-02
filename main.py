from time import sleep
from random import randint
from threading import Thread
from os import system as sys, startfile
from matrix import Matrix
from widgets import Widgets
from authentication import Authentication
from apps.images import Images
from apps.clock import ClockWork

at = Authentication()
wd = Widgets()
im = Images()
cl = ClockWork()
mx = Matrix()


def get_programs_commands():
    while True:
        wd.get_taskbar()
        wd.get_message_handler("Контакты, пароли, кнб", "Contacts, passwords, rps")
        cmd = wd.get_enter_action("Введите действие: ", "Enter action: ")
        if cmd.lower() == '#':
            pass
        elif cmd == '':
            break
        else:
            wd.get_taskbar()
            wd.get_message_handler("Неверная команда!", "Wrong command!")


def get_main_commands():
    cmd = wd.get_enter_action("Введите действие: ", "Enter action: ")
    if cmd.lower() == 'выход' or cmd.lower() == 'вхд' or cmd.lower() == 'exit' or cmd.lower() == 'ext':
        wd.get_shutdown_or_reboot(wd.change_language("Завершение работы", "Shutdown"))
        exit()
    elif cmd.lower() == 'перезагрузка' or cmd.lower() == 'прз' or cmd.lower() == 'reboot' or cmd.lower() == 'reb':
        wd.get_shutdown_or_reboot(wd.change_language("Перезагрузка", "Reboot"))
        startfile('neon.exe')
        exit()
    elif cmd.lower() == 'программы' or cmd.lower() == 'п' or cmd.lower() == 'programs' or cmd.lower() == 'p':
        get_programs_commands()
    elif cmd.lower() == 'матрица' or cmd.lower() == 'matrix' or cmd.lower() == 'м' or cmd.lower() == 'm':
        sys(wd.get_system_command())
        Thread(target=mx.run_function).start()
        mx.get_matrix_move(-1, wd.height - 1, float(f'{0.0}{randint(6, 9)}'))
        Thread(target=mx.break_function).start()
        input()
    elif cmd.lower() == 'время' or cmd.lower() == 'в' or cmd.lower() == 'time' or cmd.lower() == 't':
        sys(wd.get_system_command())
        Thread(target=cl.run_function).start()
        Thread(target=cl.command_time).start()
        Thread(target=cl.break_function).start()
        input()
        sleep(0.3)
    elif cmd == '':
        wd.get_taskbar()
        wd.get_message_handler("Вы ничего не ответили!", "You didn't answer!")
        wd.get_enter_action("Нажмите действие для возврата...", "Press to return...")
    else:
        wd.get_taskbar()
        wd.get_message_handler("Неверная команда!", "Wrong command!")
        wd.get_enter_action("Нажмите действие для возврата...", "Press to return...")


def get_home_screen():
    while True:
        wd.get_taskbar()
        wd.get_weather()
        wd.get_coordinates(0, 8, 0, int(wd.height // 2.47))
        print(f'{wd.get_green}{wd.get_month_calendar()}')
        im.get_wallpaper(wd.first_color, wd.second_color)
        wd.get_battery()
        get_main_commands()


def main():
    """Entry point"""
    wd.get_screen_mode()
    wd.verify_transparency()
    wd.get_start_screen()
    at.get_authentication()
    get_home_screen()
    sys(wd.get_system_command())


if __name__ == '__main__':
    main()
