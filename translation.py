from ast import literal_eval
from interface import Action
from interface import Visual
from interface import Widgets
from configuration import Config


class Translation:
    __slots__ = ('enteraword', 'translatesas', 'wordnotfound', 'issaved')

    def __init__(self):
        if Config().language() == 'russian' or Config().language() == 'русский':
            self.enteraword = "Введи слово: "
            self.translatesas = " переводится как "
            self.wordnotfound = "Слово не найдено... Введите перевод: "
            self.issaved = " сохранено!"
        else:
            self.enteraword = "Enter a word: "
            self.translatesas = " translates as "
            self.wordnotfound = "Word not found... Enter translation: "
            self.issaved = " is saved!"

    def translate(self):
        while True:
            wordtransfer = []

            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            wordinput = Visual().color.input(f"{Visual().firstcolor}{self.enteraword}")

            if wordinput == '':
                Action().invalidanswer()
                break

            wordtransfer.append(wordinput)

            try:
                with open(f'{Config().part()}/TUI/Programs/system13.spec', 'r') as dictionarylist:
                    diction = literal_eval('{' + f'{dictionarylist.read()}' + '}')

                    Widgets().showtaskbar()
                    for i in wordtransfer:
                        Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                        Visual().color.input(
                            f"{Visual().firstcolor}\"{wordtransfer[0]}\"{self.translatesas}\"{diction[i]}\"")

            except KeyError:
                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                wordtransfer = Visual().color.input(f"{Visual().firstcolor}{self.wordnotfound}")

                if wordtransfer == '':
                    Action().invalidanswer()
                    break

                else:
                    Widgets().showtaskbar()
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    Visual().color.input(f"{Visual().firstcolor}Слово \"{wordtransfer}\"{self.issaved}")

                translateread = open(f'{Config().part()}/TUI/Programs/system13.spec', 'r')
                translatewrite = open(f'{Config().part()}/TUI/Programs/system13.spec', 'a')

                if translateread.read() != '':
                    translatewrite.write(',')
                    translatewrite.write('\n')
                else:
                    pass

                translatewrite.write(f'\'{wordinput}\': \'{wordtransfer}\',\n')
                translatewrite.write(f'\'{wordtransfer}\': \'{wordinput}\'')
                translateread.close()
                translatewrite.close()
