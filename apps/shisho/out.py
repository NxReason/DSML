from translation_table import translate_pos


def save_core_words_list(words: list[str]):
    save_file('core_words.txt', [f'{w}\n' for w in words])


def save_tokens(tokens, filename):
    lines = []
    for t in tokens:
        lines.append(
            f'{t.surface()} ({t.dictionary_form()}, {t.reading_form()})\n')
        pos = t.part_of_speech()
        lines.append(f'\t{translate_pos(t)}\n')
        lines.append(f'\t{pos}\n\n')

    save_file(filename, lines)


def save(analyzer, params):
    lines = []

    sorted_by_count = dict(sorted(
        analyzer.core_words.items(), key=lambda cw: cw[1].count,
        reverse=True))

    for dict_form, cw in sorted_by_count.items():
        lines.append(f'{dict_form} ({cw.count})\n')
        for compound in cw.compounds:
            lines.append(
                f'\t{compound.word} ({compound.reading}) position: {compound.begin}\n')

    save_file(params['output'], lines)


def gen_meta(filename: str = '', words: list[str] = []):
    unique = set(words)
    meta = f'''
Filename: {filename}
Total words: {len(words)}, unique: {len(unique)}\n'''
    return meta[1:]


def save_file(filename: str, lines: list[str]):
    with open('./output/' + filename, 'w', encoding='utf-8') as f:
        f.writelines(lines)
