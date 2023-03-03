from os import system
from time import sleep
from random import randint
from interface import Visual


class Neo:
    wakeup = (
        'W', 'Wa', 'Wak', 'Wake', 'Wake ', 'Wake u', 'Wake up', 'Wake up,', 'Wake up, ', 'Wake up, N',
        'Wake up, Ne', 'Wake up, Neo', 'Wake up, Neo.', 'Wake up, Neo..', 'Wake up, Neo...'
    )

    thematrix = (
        'T', 'Th', 'The', 'The ', 'The M', 'The Ma', 'The Mat', 'The Matr', 'The Matri', 'The Matrix', 'The Matrix ',
        'The Matrix h', 'The Matrix ha', 'The Matrix has', 'The Matrix has ', 'The Matrix has y', 'The Matrix has yo',
        'The Matrix has you', 'The Matrix has you.', 'The Matrix has you..', 'The Matrix has you...'
    )

    follow = (
        'F', 'Fo', 'Fol', 'Foll', 'Follo', 'Follow', 'Follow ', 'Follow t', 'Follow th', 'Follow the', 'Follow the ',
        'Follow the w', 'Follow the wh', 'Follow the whi', 'Follow the whit', 'Follow the white', 'Follow the white ',
        'Follow the white r', 'Follow the white ra', 'Follow the white rab', 'Follow the white rabb',
        'Follow the white rabbi', 'Follow the white rabbit', 'Follow the white rabbit.'
    )

    @staticmethod
    def textgenerator(word, pauseone, pausetwo, speedone, speedtwo):
        count = 0
        system('cls')

        for i in range(len(word)):
            count += 1
            sleep(float(f'0.{randint(speedone, speedtwo)}'))
            Visual().coordinates(2, 1, 4, 2)
            print(word[count - 1])

        sleep(pauseone)
        Visual().coordinates(2, 1, 4, 2)
        print(24 * ' ')
        sleep(pausetwo)

    def neo(self):
        self.textgenerator(self.wakeup, 4.4, 1.2, 1, 2)
        self.textgenerator(self.thematrix, 4.2, 0.7, 2, 4)
        self.textgenerator(self.follow, 4, 0.2, 1, 3)
        Visual().coordinates(2, 1, 4, 2)
        print('Knock, knock, Neo.')
        sleep(4.2)
