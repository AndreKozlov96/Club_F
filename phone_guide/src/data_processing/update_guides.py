''' Функция предназначена для удаления лишних пустых строк в справочнике,
которые могли появиться при введении лишних пробелов и т.д.,
а также для приведения справочника *.CSV в соответствие со справочником *.txt '''

from const import PHONE_GUIDE
from src.data_processing.rewrite import rewrite_guide


def update():
    lines = []
    with open(PHONE_GUIDE, 'r', encoding='utf-8') as update:
        for line in update:
            if line.strip() != '':
                lines.append(line.strip() + '\n')
        rewrite_guide(lines)

