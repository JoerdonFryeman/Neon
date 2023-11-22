from os import mkdir
from pytube import YouTube, Playlist, exceptions
from pytube.helpers import DeferredGeneratorList
from widgets import Widgets


class YouTubeLoader(Widgets):
    def get_video_links(self) -> list:
        """
        Links of video entering function
        :return: list
        """
        list_of_links = []
        while True:
            link = self.console_color.input(
                self.get_message_handler(
                    self.get_taskbar(),
                    "Введи ссылку на видео с YouTube: ",
                    "Enter a link to a YouTube video: "
                )
            )
            if self.verify_void(
                    link, self.get_taskbar(),
                    "Вы ничего не ответили!", "You didn't answer!",
                    "Нажмите действие для возврата...", "Press to return..."
            ):
                break
            list_of_links.append(link)
        return list_of_links

    def get_playlist_links(self) -> DeferredGeneratorList:
        """
        Links of playlist entering function
        :return: DeferredGeneratorList
        """
        link = Playlist(
            self.console_color.input(
                self.get_message_handler(
                    self.get_taskbar(),
                    "Введи ссылку на плейлист YouTube: ", "Enter a link to a YouTube playlist: "
                )
            )
        )
        return link.video_urls

    def download_choose_method(self) -> list | DeferredGeneratorList:
        """
        Function to choose between downloading videos or a playlist
        :return: list | DeferredGeneratorList
        """
        video_or_playlist = self.console_color.input(
            self.get_message_handler(
                self.get_taskbar(),
                "Скачать отдельные видео или плейлист? ",
                "Download individual videos or a playlist? "
            )
        )
        if video_or_playlist.lower() == 'видео' or video_or_playlist.lower() == 'в':
            return self.get_video_links()
        if video_or_playlist.lower() == 'плейлист' or video_or_playlist.lower() == 'п':
            return self.get_playlist_links()
        self.console_color.print(
            self.get_message_handler(
                self.get_taskbar(), "Неверная команда!", "Wrong command!"
            )
        )
        self.get_enter_action("Нажмите действие для возврата...", "Press to return...")

    def download_video(self) -> None:
        """
        The function takes a list of links and downloads the video for each of them
        :return: None
        """
        try:
            mkdir('Download')
        except FileExistsError:
            pass
        try:
            for i in self.download_choose_method():
                youtube = YouTube(i)

                self.console_color.print(
                    self.get_message_handler(
                        self.get_taskbar(),
                        f"Идёт загрузка видео: {youtube.title}",
                        f"The video is downloading: {youtube.title}"
                    )
                )
                youtube.streams.get_highest_resolution().download('Download/')
                self.console_color.print(
                    self.get_message_handler(
                        self.get_taskbar(),
                        f"Автор: {youtube.author}\nОписание: {youtube.description}",
                        f"Autor: {youtube.author}\nDescription: {youtube.description}"
                    )
                )
                self.get_enter_action(
                    "Загрузка завершена! Нажмите действие для возврата...",
                    " Download is done! Press to return..."
                )

        except exceptions.RegexMatchError:
            self.console_color.print(
                self.get_message_handler(
                    self.get_taskbar(), "Битая ссылка...", "Broken link..."
                )
            )
            self.get_enter_action("Нажмите действие для возврата...", "Press to return...")
        except exceptions.AgeRestrictedError:
            self.console_color.print(
                self.get_message_handler(
                    self.get_taskbar(),
                    "Видос имеет возрастные ограничения!", "The video has an age restriction!"
                )
            )
            self.get_enter_action("Нажмите действие для возврата...", "Press to return...")
        except exceptions.LiveStreamError:
            self.console_color.print(
                self.get_message_handler(
                    self.get_taskbar(),
                    "Попробуй скачать видео после завершения прямого эфира...",
                    "Try downloading the video after the live stream is over..."
                )
            )
            self.get_enter_action("Нажмите действие для возврата...", "Press to return...")
        except exceptions.VideoUnavailable:
            self.console_color.print(
                self.get_message_handler(
                    self.get_taskbar(),
                    "Данный видос больше не доступен...", "This vid is no longer available..."
                )
            )
            self.get_enter_action("Нажмите действие для возврата...", "Press to return...")
        except KeyboardInterrupt:
            self.console_color.print(
                self.get_message_handler(
                    self.get_taskbar(),
                    "Программа прервана!", "Program interrupted!"
                )
            )
            self.get_enter_action("Нажмите действие для возврата...", "Press to return...")
        except:
            pass
