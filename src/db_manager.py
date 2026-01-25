import textwrap
from typing import Any

import psycopg2

from config import config


class DBManager:
    """Класс для получения данных с БД"""

    def __init__(self) -> None:
        self.database_name = "hh_ru"
        self.params = config()

    def get_companies_and_vacancies_count(self) -> list[dict[str, int]]:
        """Получает список всех компаний и количество вакансий у каждой компании"""

        conn = psycopg2.connect(dbname=self.database_name, **self.params)
        with conn.cursor() as cur:
            cur.execute(textwrap.dedent(
                """
    SELECT employers.name, COUNT(vacancy_id) AS vacancies_count
    FROM employers
    JOIN vacancies USING(employer_id)
    GROUP BY employer_id, employers.name
    """
            ))
            rows = cur.fetchall()

        response = []
        for row in rows:
            response.append({"company": row[0], "vacancies_amount": row[1]})
        conn.commit()
        conn.close()
        return response

    def get_all_vacancies(self) -> list[tuple[Any, ...]]:
        """Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки
        на вакансию"""

        conn = psycopg2.connect(dbname=self.database_name, **self.params)
        with conn.cursor() as cur:
            cur.execute(
                """SELECT employers.name, vacancies.name, salary, url
                            FROM vacancies
                            JOIN employers USING(employer_id)"""
            )
            rows = cur.fetchall()

        conn.commit()
        conn.close()
        return rows

    def get_avg_salary(self) -> int:
        """Получает среднюю зарплату по вакансиям"""

        conn = psycopg2.connect(dbname=self.database_name, **self.params)
        with conn.cursor() as cur:
            cur.execute(
                """SELECT AVG(salary) AS avg_salary
                            FROM vacancies"""
            )
            rows = cur.fetchone()[0]

        conn.commit()
        conn.close()
        return rows

    def get_vacancies_with_higher_salary(self) -> list[tuple[Any, ...]]:
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""

        conn = psycopg2.connect(dbname=self.database_name, **self.params)
        with conn.cursor() as cur:
            cur.execute(
                """SELECT *
                            FROM vacancies
                            WHERE salary > (SELECT AVG(salary) FROM vacancies)"""
            )

            rows = cur.fetchall()
        conn.commit()
        conn.close()
        return rows

    def get_vacancies_with_keyword(self, key_word: str) -> list[tuple[Any, ...]]:
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python"""

        conn = psycopg2.connect(dbname=self.database_name, **self.params)
        with conn.cursor() as cur:
            cur.execute(
                f"""SELECT *
                            FROM vacancies
                            WHERE vacancies.name LIKE '%{key_word[1:]}%'"""
            )
            rows = cur.fetchall()

        conn.commit()
        conn.close()
        return rows

manager = DBManager()
print(manager.get_companies_and_vacancies_count())
