import csv
from const import PHONE_GUIDE_CSV


def update_csv(rewrite_data):
    data_for_csv = [['Фамилия', 'Имя', 'Отчество', 'Номер телефона']]
    for line in rewrite_data:
        data_for_csv.append(line.strip().split())
    with open(PHONE_GUIDE_CSV, 'w', encoding='utf-8', newline='') as rewrite_csv:
        writer = csv.writer(rewrite_csv, quoting=csv.QUOTE_NONNUMERIC)
        for data in data_for_csv:
            writer.writerow(data)

