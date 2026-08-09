from translator import lookup
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

    filename = 'tiny.txt'

    tokens = get_tokens_file('./texts/' + filename)
    print('tokenized')

    parser = Parser(tokens)
    parser.parse_core_words()
    print('parsed')

    for word in parser.core_words.keys():
        print(word)
        print('-' * 20)

    # save(analyzer, {'output': filename})
    # save_tokens(tokens, f'{filename}-tokens.txt')


def main():
    id = lookup('力')
    print(id)


if __name__ == "__main__":
    main()
