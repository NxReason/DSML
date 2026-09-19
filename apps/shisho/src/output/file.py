from pathlib import Path


def save_tokens(path: Path, tokens):
    out_path = path.with_stem(path.stem + '_tokens')

    with open(out_path, 'w', encoding='utf-8') as f:
        for token in tokens:
            f.write(token.dictionary_form() + '\n')


def save_core_words(path: Path, core_words):
    out_path = path.with_stem(path.stem + '_core_words')

    with open(out_path, 'w', encoding='utf-8') as f:
        for cw in core_words:
            f.write(cw + '\n')
