import sqlite3 as sq
from installation import InstallData


class DataBase(InstallData):
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
                    self.coding(self.user_name), self.coding(self.user_city), self.coding(self.user_login),
                    self.coding(self.user_password), self.coding(self.system_language), self.coding(self.weather_key),
                    self.system_resolution, self.system_color, self.system_transparency, self.note_file
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
