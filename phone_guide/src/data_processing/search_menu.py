def s_menu():
    var = int(input('\nУкажите вариант поиска:'
                    '\n1) Поиск по фамилии абонента'
                    '\n2) Поиск по имени абонента'
                    '\n3) Поиск по отчеству абонента'
                    '\n4) Поиск по номеру телефона абонента'
                    '\n5) Выход в основное меню'
                    '\n---> '))
    if var == 1:
        sub = input('Введите фамилию: ')
    if var == 2:
        sub = input('Введите имя: ')
    if var == 3:
        sub = input('Введите отчество: ')
    if var == 4:
        sub = input('Введите номер телефона: ')
    if var == 5:
        return (0, '0')
    return (var, sub)
