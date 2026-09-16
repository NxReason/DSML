import re

artifacts = [
    r'{\an8}',
    r'♪～'
]


def clean_subs(file) -> list[str]:
    out = []
    num_pattern = r"^\d+$"
    timestamp_pattern = r"^.* --> .*$"
    for line in file:
        # skip empty line, order numbers and timestamps
        if line.strip() == '':
            continue
        if re.match(num_pattern, line):
            continue
        if re.match(timestamp_pattern, line):
            continue

        # replace junk
        clean_line = line
        for art in artifacts:
            clean_line = clean_line.replace(art, '')
        clean_line = clean_line.strip()
        if clean_line != '':
            out.append(clean_line)

    return out
