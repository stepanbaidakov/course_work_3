import psycopg2
from typing import Any


def create_database(database_name: str, params: dict) -> None:
    """Создание БД и таблиц"""

    conn = psycopg2.connect(dbname="postgres", **params)
    conn.autocommit = True
    with conn.cursor() as cur:
        cur.execute(
            """SELECT pg_terminate_backend(pid)
                        FROM pg_stat_activity
                        WHERE datname = 'hh_ru'
                        AND pid <> pg_backend_pid();"""
        )
        cur.execute(f"DROP DATABASE {database_name}")
        cur.execute(f"CREATE DATABASE {database_name}")

    conn.close()

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        cur.execute(
            """CREATE TABLE employers (
                        employer_id INT PRIMARY KEY,
                        name TEXT)
                        """
        )

    with conn.cursor() as cur:
        cur.execute(
            """CREATE TABLE vacancies (
                        vacancy_id INT PRIMARY KEY,
                        employer_id INT REFERENCES employers(employer_id),
                        name TEXT,
                        salary INT,
                        url TEXT)
                        """
        )

    conn.commit()
    conn.close()


def save_to_database(
    data: list[dict[str, Any]], database_name: str, params: dict
) -> None:
    """Заполнение таблиц БД данными"""

    conn = psycopg2.connect(dbname=database_name, **params)
    with conn.cursor() as cur:
        for employer in data:
            employer_data = employer["employer"]
            cur.execute(
                """INSERT INTO employers (employer_id, name)
                        VALUES (%s, %s)
                        RETURNING employer_id""",
                (employer_data["id"], employer_data["name"]),
            )

            employer_id = cur.fetchone()[0]
            vacancies_data = employer["vacancies"]
            for vacancy in vacancies_data:
                if vacancy["salary"] is None:
                    cur.execute(
                        """INSERT INTO vacancies (vacancy_id, employer_id, name, salary, url)
                                    VALUES (%s, %s, %s, %s, %s)""",
                        (
                            vacancy["id"],
                            employer_id,
                            vacancy["name"],
                            None,
                            vacancy["url"],
                        ),
                    )
                elif vacancy["salary"]["from"] is None:
                    cur.execute(
                        """INSERT INTO vacancies (vacancy_id, employer_id, name, salary, url)
                                    VALUES (%s, %s, %s, %s, %s)""",
                        (
                            vacancy["id"],
                            employer_id,
                            vacancy["name"],
                            int(vacancy["salary"]["to"]),
                            vacancy["url"],
                        ),
                    )
                elif vacancy["salary"]["to"] is None:
                    cur.execute(
                        """INSERT INTO vacancies (vacancy_id, employer_id, name, salary, url)
                                                        VALUES (%s, %s, %s, %s, %s)""",
                        (
                            vacancy["id"],
                            employer_id,
                            vacancy["name"],
                            int(vacancy["salary"]["from"]),
                            vacancy["url"],
                        ),
                    )
                elif vacancy["salary"]["to"] and vacancy["salary"]["from"]:
                    salary = int(
                        (vacancy["salary"]["to"] + vacancy["salary"]["from"]) / 2
                    )
                    cur.execute(
                        """INSERT INTO vacancies (vacancy_id, employer_id, name, salary, url)
                                                                            VALUES (%s, %s, %s, %s, %s)""",
                        (
                            vacancy["id"],
                            employer_id,
                            vacancy["name"],
                            salary,
                            vacancy["url"],
                        ),
                    )
    conn.commit()
    conn.close()
