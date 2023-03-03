from pytube import YouTube
from interface import Visual
from interface import Action
from pytube import exceptions
from interface import Widgets
from configuration import Config


class YouTubeSaver:
    __slots__ = ('link', 'name', 'author', 'views', 'description', 'loading', 'youtubelink', 'linknotfound', 'neterror')

    def __init__(self):
        if Config().language() == 'russian' or Config().language() == 'русский':
            self.link = "Введите ссылку на видео с Youtube: "
            self.youtubelink = 'Введите ссылку на видео в формате: "https://www.youtube.com/watch?v=jNQXAC9IVRw"'
            self.name = "Название: "
            self.author = "Автор: "
            self.views = "Просмотры: "
            self.description = "Описание: "
            self.loading = "Загрузка завершена!"
            self.linknotfound = "Ссылка не найдена!"
            self.neterror = "Отсутствует подключение к интернету!"
        else:
            self.link = "Enter the link to the video from Youtube: "
            self.youtubelink = 'Enter the video link in the format: "https://www.youtube.com/watch?v=jNQXAC9IVRw"'
            self.name = "Name: "
            self.author = "Author: "
            self.views = "Views: "
            self.description = "Description: "
            self.loading = "Loading is complete!"
            self.linknotfound = "Link is not found!"
            self.neterror = "No internet connection!"

    def savevideo(self):
        while True:
            Widgets().showtaskbar()
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)

            try:
                link = Visual().color.input(f"{Visual().firstcolor}{self.link}")

                if link == '':
                    break

                if link[0:23] == 'https://www.youtube.com' \
                        or link[0:15] == 'www.youtube.com' \
                        or link[0:11] == 'youtube.com':

                    youtube = YouTube(link)
                    Widgets().showtaskbar()
                    Visual().color.print(f"\n{Visual().firstcolor}{self.name}{youtube.title}\n")
                    Visual().color.print(f"{Visual().firstcolor}{self.author}{youtube.author}\n")
                    Visual().color.print(f"{Visual().firstcolor}{self.views}{youtube.views}\n")
                    Visual().color.input(f"{Visual().firstcolor}{self.description}{youtube.description}\n")

                    Action().loadingpoint("Идёт загрузка", "Download", Widgets().showtaskbar())

                    youtube.streams.get_highest_resolution().download(f'{Config().part()}/TUI/User/Downloads/')

                    Widgets().showtaskbar()
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    Visual().color.print(f"{Visual().firstcolor}{self.loading}")
                    Action().presstoreturn()

                else:
                    Widgets().showtaskbar()
                    Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                    Visual().color.input(f"{Visual().firstcolor}{self.youtubelink}")

            except exceptions.RegexMatchError:
                Widgets().showtaskbar()
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                Visual().color.input(f'{Visual().firstcolor}{self.linknotfound}')

            except:
                Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
                Visual().color.input(f'{Visual().firstcolor}{self.neterror}')
