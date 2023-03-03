from os import remove
from os import rename
from os import listdir
from interface import Visual
from interface import Action
from interface import Widgets
from configuration import Config


class Notes:
    __slots__ = (
        'notesmenu', 'notename', 'notenotfound', 'existsone', 'existstwo', 'notetext', 'newnoteone', 'newnotetwo',
        'notedelete', 'note', 'deletedtwo', 'currentnote', 'newnotename', 'renamed', 'widgetquestion', 'wrongname',
        'wrongnotename'
    )

    def __init__(self):
        if Config().language() == 'russian' or Config().language() == 'русский':
            self.notesmenu = "Открыть, новая, переименовать, удалить, убрать"
            self.notename = "Введите название заметки: "
            self.notenotfound = "не найдена!"
            self.existsone = "Заметка"
            self.existstwo = "уже существует!"
            self.notetext = "Введите текст заметки: "
            self.newnoteone = "Новая заметка"
            self.newnotetwo = "сохранена!"
            self.notedelete = "Введите название удаляемой заметки: "
            self.note = "Заметка"
            self.deletedtwo = "была удалена!"
            self.currentnote = "Введите текущее название заметки: "
            self.newnotename = "Введите новое название заметки: "
            self.renamed = "была переименована в"
            self.widgetquestion = "Показать заметку на главном экране? Да/нет: "
            self.wrongname = 'Имя файла не должно содержать: \\/:*?"<>|'
            self.wrongnotename = "Имя не может быть больше 15 символов!"
        else:
            self.notesmenu = "Open, new, rename, delete, remove"
            self.notename = "Enter note name: "
            self.notenotfound = "not found!"
            self.existsone = "A note with the name"
            self.existstwo = "already exists!"
            self.notetext = "Enter note text: "
            self.newnoteone = "New note"
            self.newnotetwo = "saved!"
            self.notedelete = "Enter the name of the note you want to delete: "
            self.note = "Note"
            self.deletedtwo = "has been deleted!"
            self.currentnote = "Enter the name of the current note: "
            self.newnotename = "Enter a new note name: "
            self.renamed = "has been renamed as"
            self.widgetquestion = "Show note on home screen? Yes/no: "
            self.wrongname = 'The file name must not contain: \\/:*?"<>|'
            self.wrongnotename = "The name must not be more than 15 letters!"

    def commandnote(self):
        counterone = 0
        countertwo = 0

        while True:
            notesdirectory = listdir(f'{Config().part()}/TUI/User/Notes/')

            Widgets().showtaskbar()
            if not notesdirectory:
                Action().nothinghere()
                break

            elif notesdirectory:
                Widgets().showtaskbar()
                for i in notesdirectory:
                    if counterone % 5 == 0:
                        countertwo = 0

                    if 0 <= counterone <= 4:
                        Visual().coordinates(Visual().mtw - 5, Visual().mth + countertwo, Visual().mtw - 5,
                                             Visual().mth + countertwo)
                    elif 5 <= counterone <= 9:
                        Visual().coordinates(Visual().mtw + 16, Visual().mth + countertwo, Visual().mtw + 20,
                                             Visual().mth + countertwo)
                    elif 10 <= counterone <= 14:
                        Visual().coordinates(Visual().mtw + 36, Visual().mth + countertwo, Visual().mtw + 45,
                                             Visual().mth + countertwo)
                    elif 15 <= counterone <= 19:
                        Visual().coordinates(Visual().mtw + 56, Visual().mth + countertwo, Visual().mtw + 70,
                                             Visual().mth + countertwo)
                    elif 20 <= counterone <= 24:
                        Visual().coordinates(Visual().mtw + 76, Visual().mth + countertwo, Visual().mtw + 95,
                                             Visual().mth + countertwo)
                    elif counterone == 25:
                        break

                    Visual().color.print(f'{Visual().firstcolor}{i[0:-5]}')
                    counterone += 1
                    countertwo += 1

                input()
                break

        while True:
            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            Visual().color.print(f'{Visual().firstcolor}{self.notesmenu}')

            commandnote = Action().enteraction()
            if commandnote == '':
                break

            while True:
                if commandnote.lower() == 'новая' or commandnote.lower() == 'new' or \
                        commandnote.lower() == 'н' or commandnote.lower() == 'n':
                    self.newnote()
                    break
                elif commandnote.lower() == 'открыть' or commandnote.lower() == 'open' or \
                        commandnote.lower() == 'о' or commandnote.lower() == 'o':
                    self.opennote()
                    break
                elif commandnote.lower() == 'удалить' or commandnote.lower() == 'delete' or \
                        commandnote.lower() == 'у' or commandnote.lower() == 'd':
                    self.deletenote()
                    break
                elif commandnote.lower() == 'убрать' or commandnote.lower() == 'remove' or \
                        commandnote.lower() == 'уб' or commandnote.lower() == 're':
                    self.removefromhomescreen()
                    break
                elif commandnote.lower() == 'переименовать' or commandnote.lower() == 'rename' or \
                        commandnote.lower() == 'п' or commandnote.lower() == 'r':
                    self.renamenote()
                    break
                else:
                    Action().invalidinput()
                    break

    @staticmethod
    def widgetnote():
        with open(f'{Config().part()}/TUI/System/system32.spec') as system32:
            link = str(system32.read())

            if link == '*2#)7%(':
                pass
            else:
                Visual().coordinates(2, 26, int(Visual().widthread // Visual().widthread + 1),
                                     int(Visual().heightread - Visual().heightread // 5.87))
                try:
                    Visual().color.print(f'{Visual().secondcolor}'
                                         f'{Config().decoding(f"{Config().part()}{link}")}')
                except OSError:
                    with open(f'{Config().part()}/TUI/System/system32.spec', 'w') as system32:
                        system32.write('*2#)7%(')
                    pass

    @staticmethod
    def removefromhomescreen():
        with open(f'{Config().part()}/TUI/System/system32.spec', 'w') as system32:
            system32.write('*2#)7%(')
        Action().dataupdate()

    def opennote(self):
        while True:
            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            nt = Visual().color.input(f'{Visual().firstcolor}{self.notename}')

            if nt == '':
                Action().invalidanswer()
                break

            try:
                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                Visual().color.input(f'{Visual().firstcolor}'
                                     f'{Config().decoding(f"{Config().part()}/TUI/User/Notes/{nt}.spec")}')
                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                question = Visual().color.input(f"{Visual().firstcolor}{self.widgetquestion}")

                if question.lower() == "да" or question.lower() == "yes":
                    with open(f'{Config().part()}/TUI/System/system32.spec', 'w') as system32:
                        system32.write(f'/TUI/User/Notes/{nt}.spec')
                    break
                elif question.lower() == "нет" or question.lower() == "no":
                    break
                else:
                    break

            except FileNotFoundError:
                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                Visual().color.input(f'{Visual().firstcolor}{self.note} \"{nt}\" {self.notenotfound}')
                break

    def newnote(self):
        while True:
            notesdirectory = listdir(f'{Config().part()}/TUI/User/Notes/')

            try:
                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                notefilename = Visual().color.input(f'{Visual().firstcolor}{self.notename}')

                if notefilename == '':
                    Action().invalidanswer()
                    break

                if len(notefilename) > 15:
                    Widgets().showtaskbar()
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    Visual().color.input(f'{Visual().firstcolor}{self.wrongnotename}')
                    break

                if f'{notefilename}.spec' in notesdirectory:
                    Widgets().showtaskbar()
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    Visual().color.input(f'{Visual().firstcolor}{self.existsone} \"{notefilename}\" {self.existstwo}')
                    break

                else:
                    Widgets().showtaskbar()
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    notefileinput = Visual().color.input(f'{Visual().firstcolor}{self.notetext}')

                    if notefileinput == '':
                        Action().invalidanswer()
                        break

                    Config().coding(f'{Config().part()}/TUI/User/Notes/{notefilename}.spec', notefileinput)

                    Widgets().showtaskbar()
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    Visual().color.input(f"{Visual().firstcolor}{self.newnoteone} \"{notefilename}\" {self.newnotetwo}")
                    break

            except OSError:
                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                Visual().color.input(f'{Visual().firstcolor}{self.wrongname}')
                break

    def deletenote(self):
        while True:
            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            notefiledelete = Visual().color.input(f'{Visual().firstcolor}{self.notedelete}')

            if notefiledelete == '':
                Action().invalidanswer()
                break

            try:
                remove(f'{Config().part()}/TUI/User/Notes/{notefiledelete}.spec')

                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                Visual().color.input(f"{Visual().firstcolor}{self.note} \"{notefiledelete}\" {self.deletedtwo}")
                break

            except FileNotFoundError:
                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                Visual().color.input(f"{Visual().firstcolor}{self.note} \"{notefiledelete}\" {self.notenotfound}")
                break

    def renamenote(self):
        while True:
            notesdirectory = listdir(f'{Config().part()}/TUI/User/Notes/')

            try:
                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                notefilename = Visual().color.input(f'{Visual().firstcolor}{self.currentnote}')

                if notefilename == '':
                    Action().invalidanswer()
                    break

                if f'{notefilename}.spec' not in notesdirectory:
                    Widgets().showtaskbar()
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    Visual().color.input(f"{Visual().firstcolor}{self.note} \"{notefilename}\" {self.notenotfound}")
                    break

                else:
                    Widgets().showtaskbar()
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    notefilerename = Visual().color.input(f'{Visual().firstcolor}{self.newnotename}')

                    if notefilerename == '':
                        Action().invalidanswer()
                        break

                    rename(f'{Config().part()}/TUI/User/Notes/{notefilename}.spec',
                           f'{Config().part()}/TUI/User/Notes/{notefilerename}.spec')

                    Widgets().showtaskbar()
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    Visual().color.input(f"{Visual().firstcolor}{self.note} \"{notefilename}\" "
                                         f"{self.renamed} \"{notefilerename}\"!")
                    break

            except OSError:
                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                Visual().color.input(f'{Visual().firstcolor}{self.wrongname}')
                break
