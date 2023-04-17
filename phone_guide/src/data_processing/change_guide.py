from const import PHONE_GUIDE
from src.data_processing.rewrite import rewrite_guide


def change_subscriber(sign=0) -> None:
    sub = input('Введите фамилию, имя, отчество или телефонный номер интересующего абонента: ')
    with open(PHONE_GUIDE, 'r', encoding='utf-8') as change_sub:
        lines = change_sub.readlines()
        for i in range(len(lines)):
            if sub in lines[i]:
                print(lines[i].strip('\n'))
                ch = input('Вы искали именно этого абанента? 1 - "Да"/2 - "Нет": ')
                if ch == '1' and sign == 0:
                    new_data = input('Введите новые данные абонента: ')
                    lines[i] = new_data + '\n'
                    rewrite_guide(lines)
                    print('\nИзменения в телефонный справочник успешно внесены.')
                    return
                elif ch == '1' and sign == 1:
                    del lines[i]
                    rewrite_guide(lines)
                    print('\nУказанный абонент успешно удален.')
                    return
        print('\nАбонент с указанными данными в справочнике отсутствует.')


def del_subscriber() -> None:
    change_subscriber(1)


def add_subscriber() -> None:
    with open(PHONE_GUIDE, 'a', encoding='utf-8') as add_sub:
        new_sub = input('Введите данные нового абонента: ')
        add_sub.write(new_sub)

