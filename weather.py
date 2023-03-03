from pyowm import OWM
from interface import Visual
from interface import Action
from interface import Widgets
from configuration import Config


class Weather(Config):
    try:
        owm = OWM(Config().weatherkey())
        city = (Config().city())
        temperature = owm.weather_manager().weather_at_place(city).weather.temperature('celsius')
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(city)
        w = observation.weather
    except:
        pass


class WeatherNow:
    __slots__ = (
        'degrees', 'max', 'min', 'feelslike', 'windspeed', 'humidity', 'threatening', 'bittercold', 'neterror', 'temp',
        'terriblycold', 'frostoutside', 'cold', 'lukewarm', 'warm', 'verywarm', 'prettyhot', 'hot', 'terriblyhot',
        'usercity'
    )

    def __init__(self):
        if Config().language() == 'russian' or Config().language() == 'русский':
            self.temp = "Температура "
            self.usercity = "в городе "
            self.degrees = " градусов по Цельсию"
            self.max = "Макс.: "
            self.min = ", мин.: "
            self.feelslike = ", чувствуется как: "
            self.windspeed = "Сила ветра: "
            self.humidity = " м/с, влажность: "

            self.threatening = "На улице холод опасный для жизни"
            self.bittercold = "На улице трескучие морозы"
            self.terriblycold = "На улице жуткий дубак"
            self.frostoutside = "На улице морозы"
            self.cold = "На улице заморозки"
            self.lukewarm = "На улице прохладно"
            self.warm = "На улице тепло"
            self.verywarm = "На улице очень тепло"
            self.prettyhot = "На улице жарко"
            self.hot = "На улице очень жарко"
            self.terriblyhot = "На улице жуткая жарища"
            self.neterror = "Отсутствует подключение к интернету или другая непредвиденная ошибка!"
        else:
            self.temp = "Temperature "
            self.usercity = "in "
            self.degrees = " degrees Celsius"
            self.max = "Max.: "
            self.min = ", min.: "
            self.feelslike = ", feels like: "
            self.windspeed = "Wind speed: "
            self.humidity = " m/s, humidity: "

            self.threatening = "It's life-threatening cold outside"
            self.bittercold = "It's bitter cold outside"
            self.terriblycold = "It's terribly cold outside"
            self.frostoutside = "Frost outside"
            self.cold = "It's cold outside"
            self.lukewarm = "It's lukewarm outside"
            self.warm = "It's warm outside"
            self.verywarm = "It's very warm outside"
            self.prettyhot = "It's pretty hot outside"
            self.hot = "It's very hot outside"
            self.terriblyhot = "It's terribly hot outside"
            self.neterror = "No internet connection or other unexpected error!"

    def weatherview(self):
        try:
            Visual().coordinates(24, 14, int(Visual().widthread // 5.09), int(Visual().heightread // 2.23))
            Visual().color.print(
                f'{Visual().firstcolor}{self.temp}{self.usercity}{Config().city()}: {Visual().secondcolor}'
                f'{Weather.temperature["temp"]}{Visual().firstcolor}{self.degrees}'
            )
            Visual().coordinates(24, 15, int(Visual().widthread // 5.09), int(Visual().heightread // 2.13))
            Visual().color.print(
                f'{Visual().firstcolor}{self.max}{Visual().secondcolor}{str(Weather.temperature["temp_max"])}°'
                f'{Visual().firstcolor}{self.min}{Visual().secondcolor}{str(Weather.temperature["temp_min"])}°'
                f'{Visual().firstcolor}{self.feelslike}{Visual().secondcolor}{str(Weather.temperature["feels_like"])}°')

            Visual().coordinates(24, 16, int(Visual().widthread // 5.09),
                                 int(Visual().heightread // Visual().symbolresolution(2.04, 2.07)))
            Visual().color.print(
                f'{Visual().firstcolor}{self.windspeed}{Visual().secondcolor}{str(Weather.w.wind()["speed"])}'
                f'{Visual().firstcolor}{self.humidity}{Visual().secondcolor}{Weather.w.humidity}%')
        except:
            Visual().coordinates(Visual().mtw, Visual().mth, Visual().mtw, Visual().mth)
            Visual().color.print(f'{Visual().firstcolor}{self.neterror}')

    @staticmethod
    def detailedstatus():
        if Config().language() == 'russian' or Config().language() == 'русский':
            if Weather.w.detailed_status == str('clear sky'):
                Weather.w.detailed_status = str('ясно')
            if Weather.w.detailed_status == str('few clouds'):
                Weather.w.detailed_status = str('облачно')
            if Weather.w.detailed_status == str('overcast clouds'):
                Weather.w.detailed_status = str('пасмурно')  # полотемнота, сделана облаком
            if Weather.w.detailed_status == str('heavy intensity shower rain'):
                Weather.w.detailed_status = str('проливной дождь')
            if Weather.w.detailed_status == str('broken clouds'):
                Weather.w.detailed_status = str('облачно с прояснениями')
            if Weather.w.detailed_status == str('light rain'):
                Weather.w.detailed_status = str('лёгкий дождь')
            if Weather.w.detailed_status == str('scattered clouds'):
                Weather.w.detailed_status = str('кучевые облака')
            if Weather.w.detailed_status == str('light intensity shower rain'):
                Weather.w.detailed_status = str('лёгкий, но интенсивный дождь')
            if Weather.w.detailed_status == str('light intensity drizzle rain'):
                Weather.w.detailed_status = str('лёгкий, но интенсивный моросящий дождь')
            if Weather.w.detailed_status == str('light intensity drizzle'):
                Weather.w.detailed_status = str('моросящий дождь')
            if Weather.w.detailed_status == str('moderate rain'):
                Weather.w.detailed_status = str('небольшой дождь')
            if Weather.w.detailed_status == str('mist') or \
                    Weather.w.detailed_status == str('fog'):
                Weather.w.detailed_status = str('туман')
            if Weather.w.rain == 'rain':
                Weather.w.rain = ', дождь'
        else:
            f'{Weather.w.detailed_status}'

    def detailedweather(self, gradone, gradtwo, status):
        try:
            self.detailedstatus()

            Visual().coordinates(24, 17, int(Visual().widthread // 5.09),
                                 int(Visual().heightread // Visual().symbolresolution(1.95, 2.02)))
            if int(gradone) <= Weather.temperature['feels_like'] <= int(gradtwo):
                Visual().color.print(f"{Visual().firstcolor}{status}, {Weather.w.detailed_status}")
        except:
            pass

    def commandweather(self):
        Widgets().showtaskbar()

        self.weatherview()
        self.detailedweather(-60, -51, self.threatening)
        self.detailedweather(-50, -41, self.bittercold)
        self.detailedweather(-40, -31, self.terriblycold)
        self.detailedweather(-30, -21, self.terriblycold)
        self.detailedweather(-20, -11, self.frostoutside)
        self.detailedweather(-10, -1, self.cold)
        self.detailedweather(0, 10, self.lukewarm)
        self.detailedweather(11, 20, self.warm)
        self.detailedweather(21, 30, self.verywarm)
        self.detailedweather(31, 40, self.prettyhot)
        self.detailedweather(41, 50, self.hot)
        self.detailedweather(51, 60, self.terriblyhot)

        Action().presstoreturn()
