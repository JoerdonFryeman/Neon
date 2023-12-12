from os import mkdir
from os import system as sys
from pytube import YouTube, Playlist, exceptions
from pytube.helpers import DeferredGeneratorList
from widgets import Widgets


class YouTubeLoader(Widgets):
    def get_video_links(self) -> list:
        """
        Links of video entering function
        :return: list
        """
        one_more = None
        counter = 0
        list_of_links = []
        while True:
            if counter == 0:
                one_more = ''
            if counter > 0:
                one_more = f"{self.change_language('ещё одну ', 'one more ')}"
            link = self.get_message(
                sys(self.get_system_command()), input,
                f"Введите {one_more}ссылку на видео с YouTube или нажмите ввод для продолжения: ",
                f"Enter a {one_more}link to a YouTube video or enter to continue: "
            )
            if link == '':
                break
            list_of_links.append(link)
            counter += 1
        return list_of_links

    def get_playlist_links(self) -> DeferredGeneratorList:
        """
        Links of playlist entering function
        :return: DeferredGeneratorList
        """
        link = Playlist(
            self.get_message(
                sys(self.get_system_command()), input,
                "Введи ссылку на плейлист YouTube: ", "Enter a link to a YouTube playlist: "
            )
        )
        return link.video_urls

    def download_choose_method(self) -> list | DeferredGeneratorList:
        """
        Function to choose between downloading videos or a playlist
        :return: list | DeferredGeneratorList
        """
        video_or_playlist = self.get_message(
            sys(self.get_system_command()), input,
            "Скачать отдельные видео или плейлист? ", "Download individual videos or a playlist? "
        )
        if video_or_playlist.lower() == 'видео' or video_or_playlist.lower() == 'в':
            return self.get_video_links()
        if video_or_playlist.lower() == 'плейлист' or video_or_playlist.lower() == 'п':
            return self.get_playlist_links()
        self.get_message(sys(self.get_system_command()), print, "Неверная команда!", "Wrong command!")
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
                self.get_message(
                    sys(self.get_system_command()), print,
                    f"Идёт загрузка видео: {youtube.title}", f"The video is downloading: {youtube.title}"
                )
                youtube.streams.get_highest_resolution().download('Download/')
                self.get_coordinates(
                    self.middle_width, self.middle_height + 1, self._middle_width, self.middle_height + 1
                )
                self.get_message(
                    sys(self.get_system_command()), print,
                    "Загрузка завершена!", "Download is done!"
                )
            self.get_enter_action(
                "Нажмите действие для возврата...",
                "Press to return..."
            )
        except exceptions.RegexMatchError:
            self.get_message(sys(self.get_system_command()), print, "Битая ссылка...", "Broken link...")
            self.get_enter_action("Нажмите действие для возврата...", "Press to return...")
        except exceptions.AgeRestrictedError:
            self.get_message(
                sys(self.get_system_command()), print,
                "Видос имеет возрастные ограничения!", "The video has an age restriction!"
            )
            self.get_enter_action("Нажмите действие для возврата...", "Press to return...")
        except exceptions.LiveStreamError:
            self.get_message(
                sys(self.get_system_command()), print,
                "Попробуй скачать видео после завершения прямого эфира...",
                "Try downloading the video after the live stream is over..."
            )
            self.get_enter_action("Нажмите действие для возврата...", "Press to return...")
        except exceptions.VideoUnavailable:
            self.get_message(
                sys(self.get_system_command()), print,
                "Данный видос больше не доступен...", "This vid is no longer available..."
            )
            self.get_enter_action("Нажмите действие для возврата...", "Press to return...")
        except KeyboardInterrupt:
            self.get_message(sys(self.get_system_command()), print, "Программа прервана!", "Program interrupted!")
            self.get_enter_action("Нажмите действие для возврата...", "Press to return...")
        except:
            pass
