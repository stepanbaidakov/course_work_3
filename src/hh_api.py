import requests
from typing import Any


def get_data(employer_ids: list[str]) -> list[dict[str, Any]]:
    data = []

    for employer_id in employer_ids:
        page = 0
        employer_data = requests.get(
            f"https://api.hh.ru/employers/{employer_id}"
        ).json()
        vacancies_data = []
        while True:
            params = {"employer_id": employer_id, "per_page": 100, "page": page}
            vacancies_json = requests.get(
                "https://api.hh.ru/vacancies", params=params
            ).json()
            vacancies_data.extend(vacancies_json["items"])
            page += 1
            if page <= vacancies_json.get("pages"):
                break

        data.append({"employer": employer_data, "vacancies": vacancies_data})
    return data


if __name__ == "__main__":
    emp = [
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
