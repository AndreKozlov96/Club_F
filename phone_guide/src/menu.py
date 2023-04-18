import data_processing
from data_processing import update

def main_menu() -> None:
    while True:
        update()
        var = int(input('\nВведите требуемый пункт меню:'
                        '\n1) Распечатать справочник'
                        '\n2) Поиск по справочнику'
                        '\n3) Удалить запись из справочника'
                        '\n4) Изменить запись в справочнике'
                        '\n5) Добавить запись в справочник'
                        '\n6) Выход'
                        '\n---> '))

        if var == 1:
            data_processing.print_guide()
        elif var == 2:
            data_processing.search_subscriber()
        elif var == 3:
            data_processing.del_subscriber()
        elif var == 4:
            data_processing.change_subscriber()
        elif var == 5:
            data_processing.add_subscriber()
        else:
            break

