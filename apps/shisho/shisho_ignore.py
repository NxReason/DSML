from data_store import save_ignore_words, read_ignore_list


def read_ignore_file(filename: str = 'ignore.txt') -> list[str]:
    out = []
    with open('./texts/' + filename, 'r', encoding='utf-8') as f:
        for line in f:
            out.append(line.strip())
    return out


if __name__ == '__main__':
    words = read_ignore_file()
    save_ignore_words(words)
