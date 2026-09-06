# goit-ds-hw-02

Task management database built with SQLite. It contains three tables — `users`,
`status` and `tasks` — and a set of SQL query scripts.

## Requirements

- Python 3.14+
- [Poetry](https://python-poetry.org/)

## Setup

```bash
poetry install
```

Run every command below with `poetry run` (e.g. `poetry run python create_table.py`)
or activate the virtual environment first.

## Create and seed the database

This creates the tables and fills them with random data (Faker):

```bash
python create_table.py
```

The database file `users_tasks.db` appears in the project root.

## Run the queries

Each script runs one query and prints the result. Edit the target value
(user id, status, email pattern, …) at the bottom of the file if needed.

| Script | What it does |
| --- | --- |
| `select_user_tasks_by_user_id.py` | All tasks of a given user |
| `select_user_tasks_by_task_status.py` | Tasks with a given status (subquery) |
| `update_status_for_selected_task.py` | Change the status of one task |
| `select_user_without_task.py` | Users with no tasks (`NOT IN`) |
| `service_add_new_task_for_specific_user.py` | Add a new task (interactive) |
| `select_not_completed_tasks.py` | Tasks that are not completed |
| `service_delete_specific_task.py` | Delete a task by id (interactive) |
| `select_user_by_specific_email.py` | Find users by email (`LIKE`) |
| `service_update_username.py` | Rename a user (interactive) |
| `select_and_count_task_by_status.py` | Task count per status |
| `select_tasks_by_cpecific_user_domain.py` | Tasks of users with a given email domain |
| `select_tasks_without_description.py` | Tasks without a description |
| `select_user_in_task_filtred_by_task_status.py` | Users and their `in progress` tasks (INNER JOIN) |
| `select_users_and_numbers_their_tasks.py` | Users and their task count (LEFT JOIN) |
| `service_add_new_user.py` | Add a new user (interactive) |

Example:

```bash
python select_user_tasks_by_user_id.py
```
