from sudachipy import Dictionary, SplitMode
from pathlib import Path
from subs import clean_subs


def get_tokens_file(filename):
    filepath = Path(filename)
    # check if file is valid
    if not filepath.exists():
        print(f'File {filename} does not exist')
        return []

    tokens = []
    with open(filename, 'r', encoding='utf-8') as f:
        # check file type and process if necessary
        if filepath.suffix == '.srt':
            lines = clean_subs(f)
        else:
            lines = f.readlines()

        # tokenize line by line
        for line in lines:
            tokens += get_tokens(line)
    return tokens


def get_tokens(text: str | list[str]):
    if type(text) == str:
        text = [text]

    tokenizer = Dictionary().create(SplitMode.A)
    tokens = []
    for line in text:
        tokens += tokenizer.tokenize(line)

    return tokens
