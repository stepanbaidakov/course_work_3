from config import config
from src.db_creation import save_to_database, setup_database
from src.db_manager import DBManager
from src.hh_api import get_data

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


def main():
    params = config()
    data = get_data(employer_ids)
    setup_database("hh_ru", params)
    save_to_database(data, "hh_ru", params)
    db_manager = DBManager()

    user_input = input(
        "Вы хотите получить список всех компаний и количество вакансий у каждой компании? да/нет: "
    ).lower()
    if user_input == "да":
        return_list = db_manager.get_companies_and_vacancies_count()
        for company in return_list:
            print(
                f"Компания: {company["company"]}, количество вакансий: {company["vacancies"]}"
            )

    user_input = input(
        "Хотите получить список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки"
        " на вакансию? да/нет: "
    )
    if user_input == "да":
        return_list = db_manager.get_all_vacancies()
        for vacancy in return_list:
            print(
                f"Компания: {vacancy[0]}, {vacancy[1]}, {vacancy[2]} руб. , {vacancy[3]}"
            )

    user_input = input("Хотите получить среднюю зарплату по вакансиям? да/нет: ")
    if user_input == "да":
        print(f"{db_manager.get_avg_salary()} руб.")

    user_input = input(
        "Хотите получить список всех вакансий, у которых зарплата выше средней по всем вакансиям? да/нет: "
    )
    if user_input == "да":
        return_list = db_manager.get_vacancies_with_higher_salary()
        for vacancy in return_list:
            print(
                f"ID компании: {vacancy[0]}, ID вакансии: {vacancy[1]}, {vacancy[2]}, {vacancy[3]} руб. , {vacancy[4]}"
            )

    user_input = input(
        "Хотите получить список всех вакансий, в названии которых содержатся переданные в метод слова, например "
        "python? да/нет: "
    )
    if user_input == "да":
        word_input = input("Введите слово для фильтрации: ").lower()
        return_list = db_manager.get_vacancies_with_keyword(word_input)
        for vacancy in return_list:
            if vacancy[3] is None:
                print(
                    f"ID компании: {vacancy[0]}, ID вакансии: {vacancy[1]}, {vacancy[2]}, {vacancy[3]}, {vacancy[4]}"
                )
            else:
                print(
                    f"ID компании: {vacancy[0]}, ID вакансии: {vacancy[1]}, {vacancy[2]}, {vacancy[3]} руб. , "
                    f"{vacancy[4]}"
                )


main()

# for ma in main:
#     for m in ma["vacancies"]:
#         print(m["salary"])
