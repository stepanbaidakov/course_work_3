from typing import Any

import requests


def get_data(employer_ids: list[str]) -> list[dict[str, Any]]:
    """Получает список словарей с вакансиями для каждого работодателя"""

    data = []
    for employer_id in employer_ids:
        page = 0
        employer_data = requests.get(f"https://api.hh.ru/employers/{employer_id}")
        employer_data_json = employer_data.json()
        employer_data.raise_for_status()
        vacancies_data = []
        while True:
            params = {"employer_id": employer_id, "per_page": 100, "page": page}
            vacancies_response = requests.get(
                "https://api.hh.ru/vacancies", params=params
            )
            vacancies_response.raise_for_status()
            vacancies_json = vacancies_response.json()
            vacancies_data.extend(vacancies_json["items"])

            if page >= vacancies_json.get("pages") - 1:
                break
            page += 1
        data.append({"employer": employer_data_json, "vacancies": vacancies_data})
    return data

    # emp = ['1005196', '3147167']
    # print(get_data(emp))
    # emp_list = ["1852940"]
    # data = get_data(emp)
    # for dat in data:
    #     for vac in dat["vacancies"]:
    #         print(dat["employer"]["id"], vac["id"], vac["salary"])

    # count_ = 0
    # params = {"vacancy_id": "11321953", "per_page": 40}
    # vacancy_id = "128959015"
    # response = requests.get(f"https://api.hh.ru/vacancies/{vacancy_id}")
    # rjs = response.json()["salary"]
    # print(rjs)

    # emp_id = 1966364
    # emp_response = requests.get(f"https://api.hh.ru/employers/{emp_id}")
    # response_js = emp_response.json()
    # print(response_js)

    # params = {"text": "business", "per_page": 50, "page": 0}
    # emp_response = requests.get("https://api.hh.ru/employers", params).json()["items"]
    # for emp in emp_response:
    #     if emp["open_vacancies"] > 4:
    #         print(emp)
