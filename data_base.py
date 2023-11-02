import sqlite3 as sq
from pykeplib import Enigma
from installation import Installation


class DataBase(Enigma, Installation):
    def add_db_value(self) -> None:
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
                    self.coding(self.edit_user_name), self.coding(self.edit_user_city),
                    self.coding(self.edit_user_login), self.coding(self.edit_user_password),
                    self.coding(self.edit_system_language), self.coding(self.edit_weather_key),
                    self.edit_system_resolution, self.edit_system_color, self.edit_system_transparency,
                    self.edit_note_file
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
