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


def main():
    filename = 'mid.txt'

    tokens = get_tokens_file('./texts/' + filename)

    analyzer = Parser(tokens)
    analyzer.parse_core_words()

    save(analyzer, {'output': filename})
    save_tokens(tokens, f'{filename}-tokens.txt')


if __name__ == "__main__":
    main()
