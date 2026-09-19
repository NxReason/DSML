from pathlib import Path
from typing import NamedTuple


# validating
class Error(NamedTuple):
    path: str
    msg: str


def filter_valid(inputs: list[str]) -> tuple[list[Path], list[Error]]:
    valid, invalid = [], []
    for input in inputs:
        path = Path(input)

        # only files allowed (might change later)
        if path.is_dir():
            invalid.append((input, 'Directories are not allowed'))
            continue

        if not path.exists():
            invalid.append((input, "Doesn't exist"))
            continue

        abs_path = path if path.is_absolute() else Path(f"{Path.cwd()}/{path}")
        valid.append(abs_path)

    return valid, invalid
