import requests
from typing import Any


# params = {"text": "IT", "page": 1, "per_page": 70, "only_with_vacancies": True}
# response = requests.get("https://api.hh.ru/employers", params)
# json_response = response.json().get("items")
# count_ = 0
# employers = []
# for res in json_response:
#     if res["open_vacancies"] > 4:
#         count_ += 1
#         employers.append(res)
# print(employers)
emp_id  = ['5591530', '3147167', '11181389', '3655078', '733972', '3669216', '11321953', '10438633', '3407499', '5046934', '4568254', '217918', '1062788', '9593424', '2910384']
# for id in emp_id:
#     response = requests.get(f"https://api.hh.ru/employers/{id}")
#     data = response.json()
#     print(data)

def get_employers(employer_ids):
    result_list = []
    for employer_id in employer_ids:
        response = requests.get(f"https://api.hh.ru/employers/{employer_id}")
        data = response.json()
        result_list.append(data)
    return result_list

# print(get_employers(emp_id))

def get_vacancies(employer_ids):
    vacancies_list = []
    for employer_id in employer_ids:
        page = 0
        while True:
            params = {"employer_id": employer_id, "per_page": 100, "page": page}
            response = requests.get("https://api.hh.ru/vacancies", params=params)
            json_response = response.json()
            vacancies_list.extend(json_response["items"])
            if page >= json_response["pages"] - 1:
                break

            page += 1
    return vacancies_list

print(get_vacancies(emp_id))
    # print(json_response)
# vacancies = get_vacancies(['5591530', '3147167', '11181389', '3655078', '733972', '3669216', '11321953', '10438633', '3407499', '5046934', '4568254', '217918', '1062788', '9593424', '2368']

# vacancies = get_vacancies(["2368"])
# num = 0
# for vacancy in vacancies:
#     num += 1
# print(num)
# num_ = 0
# employers_list = ['5591530', '3147167', '11181389', '3655078', '733972', '3669216', '11321953', '10438633', '3407499', '5046934', '4568254', '217918', '1062788', '9593424', '2368']
# employers = get_employers(['5591530', '3147167', '11181389', '3655078', '733972', '3669216', '11321953', '10438633', '3407499', '5046934', '4568254', '217918', '1062788', '9593424', '2368'])
# for employer in employers:
#     num_ += employer["open_vacancies"]
# print(num_)