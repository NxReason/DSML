import nxcli
from src.input import filter_valid
from src.output import cli, file
from src.tokenizer import tokenize_file
from src.parser import Parser
from src.ignore.db import IgnoreDB

args_map = {
    "no_ignore": bool
}


def main():
    cmd = nxcli.parse_args(args_map)

    inputs, errors = filter_valid(cmd.inputs)
    cli.inputs_summary(inputs, errors)

    tokens_dict = {}
    for input in inputs:
        tokens_dict[input] = tokenize_file(input)

    # conditionally add ignore list
    ignore_words = set()
    if not cmd.no_ignore:
        ignore_db = IgnoreDB()
        ignore_words = set(w[1] for w in ignore_db.get_words())

    for path, tokens in tokens_dict.items():
        parser = Parser(tokens)
        parser.parse_core_words()

        core_words = parser.core_words.keys()
        out_words = parser.core_words.keys() - ignore_words
        diff_count = len(core_words) - len(out_words)

        print(path)
        print(
            f'Total core words: {len(core_words)}, ignored: {diff_count}, out: {len(out_words)}')
        file.save_core_words(path, out_words)


if __name__ == "__main__":
    main()
