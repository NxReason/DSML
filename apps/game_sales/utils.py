from enum import Enum


class Report:
    def __init__(self, avg, median, mode):
        self.avg = avg
        self.median = median
        self.mode = mode


class SortingOrder(Enum):
    NONE = 'none'
    ASC = 'asc'
    DESC = 'desc'


def save_report(filename, data):
    with open(f'./output/{filename}', mode='w', encoding='utf-8') as f:
        for title, section in data.items():
            f.write(f'--- {title} ---\n')
            for key, value in section.items():
                f.write(f'{key:<20.20}: {value}\n')
            f.write('\n')
