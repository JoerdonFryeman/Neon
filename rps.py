from os import system
from random import randrange
from interface import Visual
from configuration import Config


class RPS:
    __slots__ = ('enteractionrps', 'rock', 'scissors', 'paper', 'computeranswer', 'draw', 'youlost', 'youwon')

    def __init__(self):
        if Config().language() == 'russian' or Config().language() == 'русский':
            self.enteractionrps = "Камень, ножницы, бумага... Введите действие: "
            self.rock = "Камень"
            self.scissors = "Ножницы"
            self.paper = 'Бумага'
            self.computeranswer = "Ответ ЭВМ: "
            self.draw = "Ничья!"
            self.youlost = "Вы проиграли!"
            self.youwon = "Вы выиграли!"
        else:
            self.enteractionrps = "Rock, paper, scissors... Enter action: "
            self.rock = "Rock"
            self.scissors = "Scissors"
            self.paper = 'Paper'
            self.computeranswer = "Computer answer: "
            self.draw = "Draw!"
            self.youlost = "You lost!"
            self.youwon = "You won!"

    def cmdchoice(self, cmpinpt, a, b, c, d, e, f, g, j, cmdinpt, result):
        if cmpinpt == a and cmdinpt.lower() == e or \
                cmpinpt == b and cmdinpt.lower() == f or \
                cmpinpt == c and cmdinpt.lower() == g or \
                cmpinpt == d and cmdinpt.lower() == j:
            system('cls')
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            Visual().color.print(f'{Visual().firstcolor}{self.computeranswer}{cmpinpt}...')
            Visual().coordinates(Visual().mtw, Visual().mth + 1, Visual().mtw, Visual().mth + 1)
            Visual().color.input(result)

    def commandrps(self):
        while True:
            system('cls')
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            commandinput = Visual().color.input(f"{Visual().firstcolor}{self.enteractionrps}")

            game = (self.rock, self.scissors, self.paper)

            if commandinput.lower() == 'камень' or commandinput.lower() == 'ножницы' or \
                    commandinput.lower() == 'бумага' or commandinput.lower() == 'rock' or \
                    commandinput.lower() == 'scissors' or commandinput.lower() == 'paper' or \
                    commandinput.lower() == 'к' or commandinput.lower() == 'н' or commandinput.lower() == 'б' or \
                    commandinput.lower() == 'r' or commandinput.lower() == 's' or commandinput.lower() == 'p':
                computerinput = (game[randrange(0, 3)])

                self.cmdchoice(computerinput, 'Камень', 'Камень', 'Rock', 'Rock', 'камень', 'к', 'rock', 'r',
                               commandinput, self.draw)
                self.cmdchoice(computerinput, 'Ножницы', 'Ножницы', 'Scissors', 'Scissors', 'ножницы', 'н', 'scissors',
                               's', commandinput, self.draw)
                self.cmdchoice(computerinput, 'Бумага', 'Бумага', 'Paper', 'Paper', 'бумага', 'б', 'paper', 'p',
                               commandinput, self.draw)
                self.cmdchoice(computerinput, 'Камень', 'Камень', 'Rock', 'Rock', 'ножницы', 'н', 'scissors', 's',
                               commandinput, self.youlost)
                self.cmdchoice(computerinput, 'Ножницы', 'Ножницы', 'Scissors', 'Scissors', 'бумага', 'б', 'paper', 'p',
                               commandinput, self.youlost)
                self.cmdchoice(computerinput, 'Бумага', 'Бумага', 'Paper', 'Paper', 'камень', 'к', 'rock', 'r',
                               commandinput, self.youlost)
                self.cmdchoice(computerinput, 'Камень', 'Камень', 'Rock', 'Rock', 'бумага', 'б', 'paper', 'p',
                               commandinput, self.youwon)
                self.cmdchoice(computerinput, 'Ножницы', 'Ножницы', 'Scissors', 'Scissors', 'камень', 'к', 'rock', 'r',
                               commandinput, self.youwon)
                self.cmdchoice(computerinput, 'Бумага', 'Бумага', 'Paper', 'Paper', 'ножницы', 'н', 'scissors', 's',
                               commandinput, self.youwon)

            if commandinput == '':
                break
