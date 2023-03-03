from os import path
from os import rmdir
from os import remove
from os import startfile
from interface import Action
from interface import Visual
from interface import Widgets
from configuration import Config


class Compiler:
    __slots__ = ('filename', 'namelink', 'iconname', 'iconlink',
                 'compcomplete', 'pyinstall', 'filenotfound', 'compfailed')

    def __init__(self):
        if Config().language() == 'russian' or Config().language() == 'русский':
            self.filename = "Введите имя py-файла: "
            self.namelink = "Введите путь к файлу (путь не должен содержать пробелы!): "
            self.iconname = "Введите имя ico-файла иконки: "
            self.iconlink = "Введите путь к иконке (путь не должен содержать пробелы!): "
            self.compcomplete = "Компиляция выполнена!"
            self.pyinstall = "Ошибка модуля! Попробуйте снова!"
            self.filenotfound = "Не удается найти указанный файл!"
            self.compfailed = "Компиляция не удалась!"
        else:
            self.filename = "Enter the name of the py file: "
            self.namelink = "Enter the link to the file (the path must not contain spaces!): "
            self.iconname = "Enter the name of the ico file of the icon: "
            self.iconlink = "Enter icon link (the path must not contain spaces!): "
            self.compcomplete = "Compilation done!"
            self.pyinstall = "Module error! Try again!"
            self.filenotfound = "The specified file cannot be found!"
            self.compfailed = "Compilation failed!"

    def commandbuild(self):
        mode = ''

        while True:
            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            name = Visual().color.input(f'{Visual().firstcolor}{self.filename}')
            if name == '':
                Action().invalidanswer()
                break

            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            link = Visual().color.input(f'{Visual().firstcolor}{self.namelink}')
            if link == '':
                Action().invalidanswer()
                break

            if not path.isfile(f'{link}\\{name}.py'):
                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                Visual().color.input(f'{Visual().firstcolor}{self.filenotfound}')
                break

            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            iconname = Visual().color.input(f'{Visual().firstcolor}{self.iconname}')
            if iconname == '':
                mode = '-F'

            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            iconlink = Visual().color.input(f'{Visual().firstcolor}{self.iconlink}')
            if iconlink == '':
                mode = '-F'

            if iconname != '' or iconlink != '':
                mode = f'-F -i {iconlink}\\{iconname}.ico'

                if not path.isfile(f'{iconlink}\\{iconname}.ico'):
                    Widgets().showtaskbar()
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    Visual().color.input(f'{Visual().firstcolor}{self.filenotfound}')
                    break

            try:
                with open('system67.bat', 'w') as batfile:
                    batfile.write(
                        f'START pyinstaller {mode} --distpath {Config().part()}/TUI/User/Downloads/ {link}\\{name}.py'
                    )

            except ModuleNotFoundError:
                with open('system67.bat', 'w') as batfile:
                    batfile.write(f'START pip install pyinstaller')

                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                Visual().color.input(f'{Visual().firstcolor}{self.pyinstall}')
                break

            startfile('system67.bat')

            while True:
                if not f'{Config().part()}/TUI/User/Downloads/{name}.exe':
                    pass

                else:
                    try:
                        Widgets().showtaskbar()
                        Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                        Visual().color.input(f'{Visual().firstcolor}{self.compcomplete}')

                        remove(f'{Config().part()}/TUI/System/build/{name}/localpycs/pyimod01_archive.pyc')
                        remove(f'{Config().part()}/TUI/System/build/{name}/localpycs/pyimod02_importers.pyc')
                        remove(f'{Config().part()}/TUI/System/build/{name}/localpycs/pyimod03_ctypes.pyc')
                        remove(f'{Config().part()}/TUI/System/build/{name}/localpycs/struct.pyc')
                        rmdir(f'{Config().part()}/TUI/System/build/{name}/localpycs')

                        remove(f'{Config().part()}/TUI/System/build/{name}/Analysis-00.toc')
                        remove(f'{Config().part()}/TUI/System/build/{name}/base_library.zip')
                        remove(f'{Config().part()}/TUI/System/build/{name}/EXE-00.toc')
                        remove(f'{Config().part()}/TUI/System/build/{name}/PKG-00.toc')
                        remove(f'{Config().part()}/TUI/System/build/{name}/PYZ-00.pyz')
                        remove(f'{Config().part()}/TUI/System/build/{name}/PYZ-00.toc')
                        remove(f'{Config().part()}/TUI/System/build/{name}/{name}.exe.manifest')
                        remove(f'{Config().part()}/TUI/System/build/{name}/{name}.pkg')
                        remove(f'{Config().part()}/TUI/System/build/{name}/warn-{name}.txt')
                        remove(f'{Config().part()}/TUI/System/build/{name}/xref-{name}.html')

                        rmdir(f'{Config().part()}/TUI/System/build/{name}')
                        rmdir(f'{Config().part()}/TUI/System/build')
                        remove(f'{Config().part()}/TUI/System/{name}.spec')
                        remove(f'{Config().part()}/TUI/System/system67.bat')
                        break

                    except FileNotFoundError:
                        Widgets().showtaskbar()
                        Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                        Visual().color.input(f'{Visual().firstcolor}{self.compfailed}')
                        break
            break
