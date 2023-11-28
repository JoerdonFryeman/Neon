import sqlite3 as sq
from installation import Installation
from pykeplib import Enigma, Descriptor


class DataBase(Enigma, Installation):
    name = Descriptor()
    city = Descriptor()
    login = Descriptor()
    password = Descriptor()
    language = Descriptor()
    weather_key = Descriptor()
    resolution = Descriptor()
    color = Descriptor()
    transparency = Descriptor()
    note_file = Descriptor()

    __slots__ = (
        '_name', '_city', '_login', '_password', '_language',
        '_weather_key', '_resolution', '_color', '_transparency', '_note_file'
    )

    def __init__(
            self, name=0, city=1, login=2, password=3, language=4,
            weather_key=5, resolution=6, color=7, transparency=8, note_file=9
    ):
        super().__init__()
        self._name = name
        self._city = city
        self._login = login
        self._password = password
        self._language = language
        self._weather_key = weather_key
        self._resolution = resolution
        self._color = color
        self._transparency = transparency
        self._note_file = note_file

    def add_db_value(self) -> None:
        edit_data = self.get_installation()
        with sq.connect('system_data.db') as db:
            cur = db.cursor()
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS system
                (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                system54 TEXT, system17 TEXT, system23 TEXT, system41 TEXT, system62 TEXT, 
                system36 TEXT, system30 TEXT, system89 TEXT, system98 INTEGER, system32 TEXT
                )
                """
            )
            cur.execute(
                "INSERT INTO system VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    self.coding(edit_data[self.name]), self.coding(edit_data[self.city]),
                    self.coding(edit_data[self.login]), self.coding(edit_data[self.password]),
                    self.coding(edit_data[self.language]), self.coding(edit_data[self.weather_key]),
                    edit_data[self.resolution], edit_data[self.color], edit_data[self.transparency],
                    edit_data[self.note_file]
                )
            )

    @staticmethod
    def get_value_list() -> list:
        with sq.connect('system_data.db') as db:
            cur = db.cursor()
            cur.execute(
                'SELECT '
                'system54, system17, system23, system41, system62, '
                'system36, system30, system89, system98, system32 '
                'FROM system'
            )
            return cur.fetchall()[0]
