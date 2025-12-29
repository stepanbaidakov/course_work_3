from typing import Any
import psycopg2
import os
from config import config


class DBManager:
    def __init__(self):
        self.database_name = "hh_ru"
        self.params = config()

    def get_companies_and_vacancies_count(self):
        conn = psycopg2.connect(dbname=self.database_name, **self.params)
        with conn.cursor() as cur:
            cur.execute(
                """SELECT employers.name, COUNT(vacancy_id) AS vacancies_count
                            FROM employers
                            JOIN vacancies USING(employer_id)
                            GROUP BY employer_id, employers.name
                            """
            )
            rows = cur.fetchall()

        response = []
        for row in rows:
            response.append({row[0]: row[1]})
        conn.commit()
        conn.close()
        return response

    def get_all_vacancies(self):
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

    def get_avg_salary(self):
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

    def get_vacancies_with_higher_salary(self):
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

    def get_vacancies_with_keyword(self, key_word):
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


if __name__ == "__main__":
    manager = DBManager()
    print(manager.get_vacancies_with_keyword("Аккаунт"))
