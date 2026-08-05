from sudachipy import Dictionary, SplitMode


def get_tokens_file(filename):
    tokens = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
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
