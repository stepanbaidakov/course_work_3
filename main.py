from src.hh_api import get_data
from src.db_creation import create_database, save_to_database
from config import config


employer_ids = [
    "5591530",
    "3147167",
    "11181389",
    "3655078",
    "3669216",
    "3407499",
    "5046934",
    "217918",
    "1062788",
    "2910384",
    "18071",
    "2235",
    "1852940",
]

# emp = ['1005196', '3147167']


def main():
    params = config()
    data = get_data(employer_ids)
    create_database("hh_ru", params)
    save_to_database(data, "hh_ru", params)


main()

# for ma in main:
#     for m in ma["vacancies"]:
#         print(m["salary"])
