import sqlite3
from pathlib import Path
from .model import Model


class DB:
    def __init__(self, name: str | Path, models: list[Model]):
        self.name = name
        self.models = models

        self.conn = sqlite3.connect(f'{self.name}.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute("PRAGMA foreign_keys = ON;")
        self.conn.commit()

        self._init_models()

    def _init_models(self):
        for m in self.models:
            m.set_conn(self.conn)
            m.create_table()

    def share_conn(self, models: list[Model]):
        for m in models:
            m.set_conn(self.conn)

    def raw(self, query, values=[]):
        cursor = self.conn.cursor()
        cursor.execute(query, values)
        return cursor.fetchall()
