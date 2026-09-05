import faker
from random import randint
import sqlite3

NUMBER_OF_USERS = 10
NUMBER_OF_TASKS = 50
NUMBER_OF_STATUSES = 3

def generate_fake_data(number_of_users: int, number_of_tasks: int) -> tuple:
    fake_data = faker.Faker

    fake_users = []
    for _ in range(number_of_users):
        fake_users.append((fake_data.name(), fake_data.unique.email()))

    # Recomended statuses for tasks
    
    statuses = [("new",), ("in progress",), ("completed",)]

    fake_tasks = []
    for _ in range(number_of_tasks):
        title = fake_data.catch_phrase()
        description = fake_data.text(max_nb_chars=200)
        status_id = randint(1, len(statuses))
        user_id = randint(1, number_of_users)
        fake_tasks.append((title, description, status_id, user_id))

    return fake_users, statuses, fake_tasks
