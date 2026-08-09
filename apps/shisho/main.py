from data_store import read_translations, read_words_file, load_jmdict
import translator
from tokens import get_tokens_file
from parser import Parser
from out import save, save_tokens

# input:
# single / multiple files
# ncode / generic html parser
# youtube subs
# subtitles files (srt, ass)

# stats
# sentences
# total
# avg length
# min / max
# words
# total / unique
# counts

# word format
# dict / reading / rebuilded / count

# ignore list

# separate kanji parser / translator


def run():
    translator.load_dict()
    print('dict loaded')

    filename = 'tiny.txt'

    tokens = get_tokens_file('./texts/' + filename)
    print('tokenized')

    parser = Parser(tokens)
    parser.parse_core_words()
    print('parsed')

    for word in parser.core_words.keys():
        print(word)
        print(translator.lookup(word))
        print('-' * 20)

    # save(analyzer, {'output': filename})
    # save_tokens(tokens, f'{filename}-tokens.txt')


def main():
    expressions, *_ = read_translations()
    word = '力'
    for id, exp in expressions:
        if exp == word:
            print('found')


if __name__ == "__main__":
    main()
