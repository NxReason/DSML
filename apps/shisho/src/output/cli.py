from pathlib import Path
from ..input import Error


def inputs_summary(valid: list[Path], invalid: list[Error]):
    if len(invalid) != 0:
        print('Error(s):')
    for inv_input in invalid:
        print(inv_input[0], '-', inv_input[1])

    if len(valid) == 0:
        print('No inputs provided')
        exit()
