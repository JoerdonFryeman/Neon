import sqlite3 as sq
from installation import Installation


class DataBase(Installation):
    @staticmethod
    def get_value_list():
        with sq.connect('system_data.db') as db:
            cur = db.cursor()
            cur.execute(
                'SELECT '
                'system54, system17, system23, system41, system36, '
                'system62, system30, system89, system98, system32 '
                'FROM neon'
            )
            return cur.fetchall()[0]
