from pathlib import Path
from nxorm import DB, Model, Column


class Word(Model):
    table_name = 'words'

    id: Column = Column(int, primary=True)
    word: Column = Column(str, required=True, unique=True)


class IgnoreDB:
    def __init__(self, db_name: str = 'ignore_list'):
        self.db_name = db_name

        script_path = Path(__file__).parent.resolve()
        db_path = Path(f'{script_path}/../../store/{self.db_name}').resolve()

        self.words = Word()

        self.db = DB(db_path, [self.words])

    def get_count(self):
        sql_data = self.db.raw(f'SELECT COUNT(*) FROM {self.words._name}')
        return sql_data[0][0]

    def add_word(self, word: str):
        self.words.create({'word': word})

    def add_words(self, words: list[str]):
        for w in words:
            self.words.create({'word': w})

    def get_words(self):
        sql_data = self.words.read_all()
        return sql_data
