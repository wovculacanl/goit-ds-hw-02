import sqlite3
from random import randint
from faker import Faker

NUMBER_OF_USERS = 10
NUMBER_OF_TASKS = 50


def generate_fake_data(number_of_users: int, number_of_tasks: int) -> tuple:
    fake_data = Faker()

    fake_users = []
    for _ in range(number_of_users):
        fake_users.append((fake_data.name(), fake_data.unique.email()))

    # Fixed recommended statuses for tasks
    statuses = [("new",), ("in progress",), ("completed",)]

    fake_tasks = []
    for _ in range(number_of_tasks):
        title = fake_data.catch_phrase()
        description = fake_data.text(max_nb_chars=200)
        status_id = randint(1, len(statuses))
        user_id = randint(1, number_of_users)
        fake_tasks.append((title, description, status_id, user_id))

    return fake_users, statuses, fake_tasks


def insert_data_to_db(conn, users, statuses, tasks):
    """Вставка згенерованих даних за допомогою executemany"""
    sql_insert_users = "INSERT INTO users (fullname, email) VALUES (?, ?);"
    sql_insert_status = "INSERT INTO status (name) VALUES (?);"
    sql_insert_tasks = "INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?);"

    cur = conn.cursor()
    try:
        cur.executemany(sql_insert_users, users)
        cur.executemany(sql_insert_status, statuses)
        cur.executemany(sql_insert_tasks, tasks)
        conn.commit()
        print("Data inserted successfully.")
    except sqlite3.Error as e:
        conn.rollback()
        print(f"Failed to insert data: {e}")