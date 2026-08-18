from .Args import Args
from sys import argv


def parse_args(desc: dict = {}):
    args = argv[1:]
    res = Args()

    if len(args) == 0:
        return res

    args_idx = [i for (i, a) in enumerate(args) if a.startswith('-')]

    # return all args as inputs if no "-args"
    if len(args_idx) == 0:
        res.inputs = args
        return res

    # split "-args" from regular inputs
    if 0 in args_idx:
        res.inputs = args[args_idx[-1] + 2:]
    else:
        res.inputs = args[:args_idx[0]]

    for idx in args_idx:
        arg = args[idx][1:]
        if (arg not in desc):
            res.errors.append(f'Unknown arg: -{arg}')
            continue

        t = desc[arg].get('type') if type(desc[arg]) == dict else desc[arg]

        if (t == bool):
            setattr(res, arg, True)
            continue

        try:
            value = t(args[idx + 1])
            setattr(res, arg, value)
        except ValueError:
            res.errors.append(f'Could not convert -{arg} to type {t}')
        except:
            res.errors.append(f'Could not parse -{arg}')

    diff = desc.keys() - {args[i][1:] for i in args_idx}

    for d in diff:
        is_dict = type(desc[d]) == dict
        t = desc[d].get('type') if is_dict else desc[d]

        if t == bool:
            setattr(res, d, False)
            continue

        if not is_dict:
            res.errors.append(f'-{d} was not provided')
            continue

        if 'default' in desc[d]:
            def_value = desc[d].get('default')
            setattr(res, d, t(def_value))
            continue

        if 'required' in desc[d] and desc[d].get('required') == False:
            continue

        res.errors.append(f'-{d} was not provided')

    return res
