import nxcli
from src.input import filter_valid
from src.output import cli, file
from src.tokenizer import tokenize_file
from src.parser import Parser


def main():
    args = nxcli.parse_args()

    inputs, errors = filter_valid(args.inputs)
    cli.inputs_summary(inputs, errors)

    tokens_dict = {}
    for input in inputs:
        tokens_dict[input] = tokenize_file(input)

    for path, tokens in tokens_dict.items():
        parser = Parser(tokens)
        parser.parse_core_words()
        file.save_core_words(path, parser.core_words.keys())


if __name__ == "__main__":
    main()
