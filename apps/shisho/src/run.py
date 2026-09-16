def run():
    args = parse_args()

    if len(args.inputs) == 0:
        print('Error: Specify inputs to parse')
        exit()

    filename = args.inputs[0]

    tokens = get_tokens_file('./texts/' + filename)

    parser = Parser(tokens)
    parser.parse_core_words()

    core_words = set(parser.core_words.keys())
    ignore_words = set(iw[1] for iw in read_ignore_list())

    new_words = core_words - ignore_words

    save_core_words_list(list(new_words))
