from pathlib import Path
from sqlite3 import IntegrityError
from src.ignore.db import IgnoreDB


class Actions:
    def __init__(self, db: IgnoreDB):
        self.db = db

    def show_count(self):
        count = self.db.get_count()
        print(f'Ignore word count: {count}')

    def ignore_from_file(self, filepath: str):
        # gen final file path
        path = Path(filepath)
        if not path.is_absolute():
            path = Path(f'{Path.cwd()}{filepath}')

        with open(path, 'r', encoding='utf-8') as f:
            # clean the input
            words = [line.strip() for line in f.readlines()]

            # print ignore info msg
            print(f'Ignoring {len(words)} words:')
            print(', '.join(words[:10]), end='')
            if len(words) > 10:
                print(f', ... {len(words) - 10} others ...', end='')
            print('')

            self._save_ignore_words(words)

    def show_all(self):
        words = [word_row[1] for word_row in self.db.get_words()]
        print(words)

    def _save_ignore_words(self, words: list[str]):
        for w in words:
            try:
                self.db.add_word(w)
            except IntegrityError:
                print(f'Skipping {w}. Was already in DB probably')
