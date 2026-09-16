from pathlib import Path
from nxcli import parse_args

from src.ignore.db import IgnoreDB
from src.ignore.actions import Actions


def repl(actions: Actions):
    actions_names = ['exit', 'count', 'show all']
    while True:
        print('> ', end='')
        user_input = input()

        match user_input:
            case 'exit':
                break
            case 'count':
                actions.show_count()
            case 'show all':
                actions.show_all()
            case _:
                print(
                    f'Unknown action. Try something from this list: {actions_names}')


def run():
    args = parse_args()
    db = IgnoreDB()
    actions = Actions(db)

    if len(args.inputs) == 0:
        repl(actions)
    else:
        actions.show_count()
        actions.ignore_from_file(args.inputs[0])
        actions.show_count()


if __name__ == '__main__':
    run()
