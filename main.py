from src.hh_api import get_vacancies, get_employers
from config import config


employer_ids = ['5591530', '3147167', '11181389', '3655078', '733972', '3669216', '11321953', '10438633', '3407499', '5046934', '4568254', '217918', '1062788', '9593424', '2910384']

def main():
    params = config()
    employers = get_employers(employer_ids)
    vacancies = get_vacancies(employer_ids)

    print(employers)
    print(vacancies)

print(main())