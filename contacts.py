from os import remove
from os import listdir
from interface import Visual
from interface import Action
from interface import Widgets
from configuration import Config


class Contacts:
    __slots__ = (
        'open', 'firstname', 'lastname', 'contact', 'notfound', 'addcontact', 'addlastname', 'contactname',
        'alreadyexist', 'phonenumber', 'emailaddress', 'houseaddress', 'newcontactadded', 'added', 'phone',
        'email', 'address', 'contactdelete', 'lastnamedelete', 'hasbeendeleted', 'wasntfound', 'wrongname'
    )

    def __init__(self):
        if Config().language() == 'russian' or Config().language() == 'русский':
            self.open = "Открыть, новый, удалить"
            self.firstname = "Введите имя: "
            self.lastname = "Введите фамилию: "
            self.contact = "Контакт"
            self.notfound = "не найден!"
            self.addcontact = "Добавьте имя нового контакта: "
            self.addlastname = "Добавьте фамилию: "
            self.contactname = "Контакт с именем"
            self.alreadyexist = "уже существует!"
            self.phonenumber = "Добавьте номер телефона: "
            self.emailaddress = "Добавьте адрес электронной почты: "
            self.houseaddress = "Добавьте домашний адрес: "
            self.newcontactadded = f"Новый контакт"
            self.added = "добавлен!"
            self.phone = "телефон: "
            self.email = "электронная почта: "
            self.address = "адрес: "
            self.contactdelete = "Введите имя удаляемого контакта: "
            self.lastnamedelete = "Введите фамилию удаляемого контакта: "
            self.hasbeendeleted = "удалён!"
            self.wasntfound = "не найден!"
            self.wrongname = 'Имя файла не должно содержать: \\/:*?"<>|'
        else:
            self.open = "Open, new, delete"
            self.firstname = "Enter first name: "
            self.lastname = "Enter last name: "
            self.contact = "Contact"
            self.notfound = "not found!"
            self.addcontact = "Add the first name of the new contact: "
            self.addlastname = "Add the last name: "
            self.alreadyexist = "already exist!"
            self.contactname = "A contact with the name"
            self.phonenumber = "Add a phone number: "
            self.emailaddress = "Add an email address: "
            self.houseaddress = "Add house address: "
            self.newcontactadded = "New contact"
            self.added = "added!"
            self.phone = "phone: "
            self.email = "email: "
            self.address = "address: "
            self.contactdelete = "Enter the first name of the contact you want to delete: "
            self.lastnamedelete = "Enter the last name: "
            self.hasbeendeleted = "has been deleted!"
            self.wasntfound = "wasn't found!"
            self.wrongname = 'The file name must not contain: \\/:*?"<>|'

    def commandcontacts(self):
        counterone = 0
        countertwo = 0

        while True:
            contactsdirectory = listdir(f'{Config().part()}/TUI/User/Contacts/')

            Widgets().showtaskbar()
            if not contactsdirectory:
                Action().nothinghere()
                break

            elif contactsdirectory:
                Widgets().showtaskbar()
                for i in contactsdirectory:
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

                    Visual().color.print(f'{Visual().firstcolor}{" ".join(i.split("_"))[0:-5]}')
                    counterone += 1
                    countertwo += 1

                input()
                break

        while True:
            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            Visual().color.print(f'{Visual().firstcolor}{self.open}')

            commandcontact = Action().enteraction()
            if commandcontact == '':
                break

            while True:
                if commandcontact.lower() == 'новый' or commandcontact.lower() == 'new' or \
                        commandcontact.lower() == 'н' or commandcontact.lower() == 'n':
                    self.newcontact()
                    break
                elif commandcontact.lower() == 'открыть' or commandcontact.lower() == 'open' or \
                        commandcontact.lower() == 'о' or commandcontact.lower() == 'o':
                    self.opencontact()
                    break
                elif commandcontact.lower() == 'удалить' or commandcontact.lower() == 'delete' or \
                        commandcontact.lower() == 'у' or commandcontact.lower() == 'd':
                    self.deletecontact()
                    break
                else:
                    Action().invalidinput()
                    break

    def opencontact(self):
        while True:
            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            openfirstname = Visual().color.input(f'{Visual().firstcolor}{self.firstname}')

            if openfirstname == '':
                Action().invalidanswer()
                break

            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            openlastname = Visual().color.input(f'{Visual().firstcolor}{self.lastname}')

            if openlastname == '':
                Action().invalidanswer()
                break

            try:
                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                word = f'{Visual().firstcolor}{Config().decoding(f"{Config().part()}/TUI/User/Contacts/{openlastname}_{openfirstname}.spec")}'

                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                Visual().color.input(
                    f'{Visual().firstcolor}{openfirstname} {openlastname}\n\n{int(Visual().widthread // 5) * " "}' +
                    f'\n{int(Visual().widthread // 5) * " "}'.join(word.split(' #)7%*(2 '))
                )
                break

            except FileNotFoundError:
                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                Visual().color.input(
                    f"{Visual().firstcolor}{self.contact} \"{openfirstname} {openlastname}\" {self.notfound}")

    def newcontact(self):
        while True:
            contactsdirectory = listdir(f'{Config().part()}/TUI/User/Contacts/')

            try:
                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                firstname = Visual().color.input(f'{Visual().firstcolor}{self.addcontact}')

                if firstname == '':
                    Action().invalidanswer()
                    break

                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                lastname = Visual().color.input(f'{Visual().firstcolor}{self.addlastname}')

                if lastname == '':
                    Widgets().showtaskbar()
                    break

                if f'{lastname}_{firstname}.spec' in contactsdirectory:
                    Widgets().showtaskbar()
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    Visual().color.input(
                        f"{Visual().firstcolor}{self.contactname} \"{firstname} {lastname}\" {self.alreadyexist}")
                    break

                else:
                    Widgets().showtaskbar()
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    phone = Visual().color.input(f'{Visual().firstcolor}{self.phonenumber}')

                    if phone == '':
                        Action().invalidanswer()
                        break

                    Widgets().showtaskbar()
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    email = Visual().color.input(f'{Visual().firstcolor}{self.emailaddress}')

                    if email == '':
                        Action().invalidanswer()
                        break

                    Widgets().showtaskbar()
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    address = Visual().color.input(f'{Visual().firstcolor}{self.houseaddress}')

                    if address == '':
                        Action().invalidanswer()
                        break

                    Config().coding(f'{Config().part()}/TUI/User/Contacts/{lastname}_{firstname}.spec',
                                    f'{self.phone}{phone} #)7%*(2 {self.email}{email} #)7%*(2 {self.address}{address}')

                    Widgets().showtaskbar()
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    Visual().color.input(
                        f"{Visual().firstcolor}{self.newcontactadded} \"{firstname} {lastname}\" {self.added}")
                    break

            except OSError:
                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                Visual().color.input(f'{Visual().firstcolor}{self.wrongname}')
                break

    def deletecontact(self):
        while True:
            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            firstnamedelete = Visual().color.input(f'{Visual().firstcolor}{self.contactdelete}')

            if firstnamedelete == '':
                Action().invalidanswer()
                break

            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            lastnamedelete = Visual().color.input(f'{Visual().firstcolor}{self.lastnamedelete}')

            if lastnamedelete == '':
                Action().invalidanswer()
                break

            try:
                remove(f'{Config().part()}/TUI/User/Contacts/{lastnamedelete}_{firstnamedelete}.spec')
                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                Visual().color.input(f"{Visual().firstcolor}{self.contact} \"{firstnamedelete} {lastnamedelete}\" "
                                     f"{self.hasbeendeleted}")
                break

            except FileNotFoundError:
                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                Visual().color.input(f"{Visual().firstcolor}{self.contact} \"{firstnamedelete} {lastnamedelete}\" "
                                     f"{self.wasntfound}")
                break
