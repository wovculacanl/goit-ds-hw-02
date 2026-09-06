import sqlite3

DATABASE = "users_tasks.db"


def get_not_completed_tasks(completed_status_name: str = "completed") -> list:
    """Отримує всі завдання, статус яких відмінний від 'completed' (або відсутній)"""
    sql = """
    SELECT id, title, description, status_id, user_id
    FROM tasks
    WHERE status_id != (
        SELECT id FROM status WHERE name = ?
    ) OR status_id IS NULL;
    """

    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute(sql, (completed_status_name,))
        return cur.fetchall()


if __name__ == "__main__":
    tasks = get_not_completed_tasks()
    if tasks:
        print("Not completed tasks:")
        for task in tasks:
            print(f"- ID: {task[0]} | Task: {task[1]} | Description: {task[2]}")
    else:
        print("No uncompleted tasks found.")


"""
For DBeaver:

SELECT id, title, description, status_id, user_id
FROM tasks
WHERE status_id != (
    SELECT id FROM status WHERE name = 'completed'
) OR status_id IS NULL;

"""