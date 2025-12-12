import requests
from typing import Any
from config import employers


# params = {"text": "IT", "page": 1, "per_page": 70, "only_with_vacancies": True}
# response = requests.get("https://api.hh.ru/employers", params)
# json_response = response.json().get("items")
# count_ = 0
# employers = []
# for res in json_response:
#     if res["open_vacancies"] > 4:
#         # print(res)
#         count_ += 1
#         employers.append({"id": res["id"]})
# print(count_)
# print(employers)
# for employer in employers:
#     params = {"employer_id": employer["id"]}
#     response_vac = requests.get("https://api.hh.ru/vacancies", params)
#     js_response = response_vac.json()["items"]
# print(js_response)

# print(json_response)
# for vacancy in json_response:
#     print(vacancy["employer"])
# def get_employers():
#     params = {"text": "IT", "page": 1, "per_page": 50, "only_with_vacancies": True}
#     response = requests.get("https://api.hh.ru/employers", params)
#     json_response = response.json()["items"]
#     return json_response



# print(get_employers())
#
def get_vacancies(employer_list: list[dict[str, Any]]):
    vacancies_list = []
    for employer in employer_list:
        params = {"employer_id": employer["id"]}
        response = requests.get("https://api.hh.ru/vacancies", params)
        json_response = response.json()["items"]
        vacancies_list.extend(json_response)
    return vacancies_list

vacancies = get_vacancies(employers)
for vac in vacancies:
    print({"vac_id": vac["id"], "emp_id": vac["employer"]["id"]})
