from const import PHONE_GUIDE
from src.data_processing.rewrite_csv import update_csv


def rewrite_guide(rewrite_data):
    with open(PHONE_GUIDE, 'w', encoding='utf-8') as rewrite_guide:
        for line in rewrite_data:
            rewrite_guide.write(line)
    update_csv(rewrite_data)

