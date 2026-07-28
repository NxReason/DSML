from enum import Enum

from PIL import Image


def desc_image(img):
    print(img.filename, end=': ')
    print(img.format, img.size, img.mode)


def split(img):
    w, h = img.size[0], img.size[1]
    w_mid, h_mid = w // 2, h // 2
    quadrants = [
        (0, 0, w_mid, h_mid),
        (w_mid, 0, w, h_mid),
        (0, h_mid, w_mid, h),
        (w_mid, h_mid, w, h),
    ]
    regions = [img.crop(q) for q in quadrants]
    return regions


def merge_ver(images):
    w = sum([img.size[0] for img in images])
    h = max([img.size[1] for img in images])
    out = Image.new('RGBA', (w, h))

    offset = 0
    for img in images:
        out.paste(img, (offset, 0))
        offset += img.size[0]

    return out


def merge_hor(images):
    w = max([img.size[0] for img in images])
    h = sum([img.size[1] for img in images])
    out = Image.new('RGBA', (w, h))

    offset = 0
    for img in images:
        out.paste(img, (0, offset))
        offset += img.size[1]

    return out


def pick_col(matrix, col_i):
    col = []
    for row in matrix:
        col.append(row[col_i])
    return col


def merge_grid(images, layout: list[list[int]]):
    lines = []
    for row in layout:
        lines.append(merge_ver([images[i] for i in row]))

    return merge_hor(lines)


class RGB(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2


def pick_channel(values, target: RGB):
    match target:
        case RGB.RED:
            return values[0]
        case RGB.GREEN:
            return values[1]
        case RGB.BLUE:
            return values[2]


def swap_channels(img, new_channels: tuple[RGB, RGB, RGB]):
    old_channels = img.split()
    swapped = (
        pick_channel(old_channels, new_channels[0]),
        pick_channel(old_channels, new_channels[1]),
        pick_channel(old_channels, new_channels[2]),
    )
    return Image.merge('RGB', swapped)


def gen_swapped_variants(img):
    img = Image.open('ei.jpg')

    rgb_perms = [(RGB(r), RGB(g), RGB(b))
                 for r in range(3)
                 for g in range(3)
                 for b in range(3)]

    def get_perm_name(p): return f'{p[0].name}_{p[1].name}_{p[2].name}'
    r = RGB(1)

    for p in rgb_perms:
        copy = swap_channels(img, p)
        copy.save(f'out/copy {get_perm_name(p)}.png')


def resize(img, factor: float):
    w, h = img.size
    resized = img.resize((int(w * factor), int(h * factor)))
    return resized


def main():
    img = Image.open('sample.jpg')
    img.show()


if __name__ == "__main__":
    main()
