from math import pi
from os import system
from interface import Visual
from interface import Action
from interface import Widgets
from configuration import Config


class Calculator:
    __slots__ = (
        'enteractionone', 'enteractiontwo', 'enterthevalue', 'circumference', 'pinumber', 'factorial', 'enterthenumber',
        'inbinary', 'inbinary', 'procent', 'fromnumber', 'firstnumber', 'secondnumber', 'answer', 'singularity'
    )

    def __init__(self):
        if Config().language() == 'russian' or Config().language() == 'русский':
            self.enteractionone = "Введите действие "
            self.enteractiontwo = "+, -, *, /, **, %, 1/x, пи, факториал, двоичный, процент: "
            self.enterthevalue = "Введите значение \"x\""
            self.circumference = "Введите длинну окружности: "
            self.pinumber = "Число pi = "
            self.factorial = "Факториал от числа: "
            self.enterthenumber = "Введите число: "
            self.inbinary = " в двоичной системе = "
            self.procent = "Процент: "
            self.fromnumber = "От: "
            self.firstnumber = "Введите первое число: "
            self.secondnumber = "Введите второе число: "
            self.answer = "Ответ: "
            self.singularity = "Сингулярность, бессердечная ты сука!"
        else:
            self.enteractionone = "Enter the action "
            self.enteractiontwo = "+, -, *, /, **, %, 1/x, pi, factorial, binary, procent: "
            self.enterthevalue = "Enter the value \"x\""
            self.circumference = "Enter circumference: "
            self.pinumber = "pi number = "
            self.factorial = "Factorial of a number: "
            self.enterthenumber = "Enter the number: "
            self.inbinary = " in binary = "
            self.procent = "Procent: "
            self.fromnumber = "From: "
            self.firstnumber = "Enter the first number: "
            self.secondnumber = "Enter the second number: "
            self.answer = "Answer: "
            self.singularity = "Singularity, you heartless bitch!"

    def commandcalculator(self):
        while True:
            try:
                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                Visual().color.print(f"{Visual().firstcolor}{self.enteractionone}\n")

                Visual().coordinates(Visual().mtw, Visual().mth + 1, Visual().mtw, Visual().mth + 1)
                operation = Visual().color.input(f"{Visual().firstcolor}{self.enteractiontwo}")

                if operation == '':
                    Action().invalidanswer()
                    break

                if operation.lower() == '1/x' or operation.lower() == 'x':
                    function = lambda x: print(1 / x)
                    Widgets().showtaskbar()
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    Visual().color.print(f"{Visual().firstcolor}{self.enterthevalue}")
                    example1 = lambda: float(input())
                    function(example1())
                    input()

                if operation.lower() == 'pi' or operation.lower() == 'пи':
                    functionpi = lambda x: print(x / 3.141592653589793)
                    Widgets().showtaskbar()
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    Visual().color.print(f"{Visual().firstcolor}{self.circumference}")
                    example2 = lambda: (float(input()))
                    functionpi(example2())
                    Visual().color.input(f"{Visual().firstcolor}{self.pinumber}{pi}")

                if operation.lower() == 'factorial' or operation.lower() == 'факториал' or \
                        operation.lower() == 'f' or operation.lower() == 'ф':

                    def factorial(f):
                        if f == 1:
                            return 1
                        return factorial(f - 1) * f

                    Widgets().showtaskbar()
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    input(factorial(int(Visual().color.input(f"{Visual().firstcolor}{self.factorial}\n"))))

                if operation.lower() == 'двоичный' or operation.lower() == 'binary' or \
                        operation.lower() == 'д' or operation.lower() == 'b':
                    Widgets().showtaskbar()
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    Visual().color.print(f"{Visual().firstcolor}{self.enterthenumber}")
                    decimalbinary = int(input())
                    Widgets().showtaskbar()
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    Visual().color.input(f"{Visual().firstcolor}"
                                         f"{decimalbinary}{self.inbinary}{decimalbinary:b}")

                if operation.lower() == 'процент' or operation.lower() == 'procent' or \
                        operation.lower() == 'п' or operation.lower() == 'p':
                    Widgets().showtaskbar()
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    Visual().color.print(f"{Visual().firstcolor}{self.procent}")
                    real = float(input())
                    Visual().color.print(f"{Visual().firstcolor}{self.fromnumber}")
                    full = float(input())
                    Visual().color.input(f'{Visual().firstcolor}{real / full:.2%}')

                if operation.lower() == '+' or operation.lower() == '-' or operation.lower() == '*' or \
                        operation.lower() == '/' or operation.lower() == '**' or operation.lower() == '%':

                    Widgets().showtaskbar()
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    a = float(Visual().color.input(f"{Visual().firstcolor}{self.firstnumber}"))

                    system('cls')
                    Widgets().showtaskbar()
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    b = float(Visual().color.input(f"{Visual().firstcolor}{self.secondnumber}"))

                    if operation == '+':
                        system('cls')
                        Widgets().showtaskbar()
                        Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                        Visual().color.input(f'{Visual().firstcolor}{self.answer}{a + b}')

                    elif operation == '-':
                        system('cls')
                        Widgets().showtaskbar()
                        Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                        Visual().color.input(f'{Visual().firstcolor}{self.answer}{a - b}')

                    elif operation == '*':
                        system('cls')
                        Widgets().showtaskbar()
                        Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                        Visual().color.input(f'{Visual().firstcolor}{self.answer}{a * b}')

                    elif operation == '/':
                        system('cls')
                        Widgets().showtaskbar()
                        Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                        Visual().color.input(f'{Visual().firstcolor}{self.answer}{a / b}')

                    elif operation == '**':
                        system('cls')
                        Widgets().showtaskbar()
                        Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                        Visual().color.input(f'{Visual().firstcolor}{self.answer}{a ** b}')

                    elif operation == '%':
                        system('cls')
                        Widgets().showtaskbar()
                        Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                        Visual().color.input(f'{Visual().firstcolor}{self.answer}{a % b}')

                    else:
                        Action().invalidinput()

            except ZeroDivisionError:
                system('cls')
                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                Visual().color.input(f"{Visual().firstcolor}{self.singularity}")

            except ValueError:
                Action().invalidinput()
