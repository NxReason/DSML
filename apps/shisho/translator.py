import json
from pathlib import Path

jp_en = {}


def load_dict():
    for file in Path('jmdict').glob('term_bank_*.json'):
        with open(file, encoding='utf-8') as f:
            entries = json.load(f)

        for entry in entries:
            expression = entry[0]
            reading = entry[1]
            definitions = entry[5]

            jp_en.setdefault(expression, []).append({
                'reading': reading,
                'definitions': definitions
            })


def lookup(word):
    return jp_en.get(word)
