from const import PHONE_GUIDE
from src.data_processing.search_menu import s_menu


def print_guide() -> None:
    with open(PHONE_GUIDE, 'r', encoding='utf-8') as print_g:
        for line in print_g:
            print(line.strip())


def search_subscriber() -> None:
    var, sub = s_menu()
    if var == 0:
        return
    with open(PHONE_GUIDE, 'r', encoding='utf-8') as search_sub:
        count = 0
        for line in search_sub:
            if sub == line.split()[var - 1]:
                count += 1
                print(*line.split())
        if count == 0:
            print('\nАбонент с указанными данными в справочнике отсутствует.')

