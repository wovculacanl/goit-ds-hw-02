
import sqlite3

DATABASE = "users_tasks.db"

def get_tasks_by_specific_user_domain(user_domain: str) -> list:
    """Отримує всі завдання, які належать користувачам з певним доменом email"""
    sql = """
    SELECT t.id, t.title, t.description, s.name AS status, u.fullname AS user_name, u.email
    FROM tasks AS t
    JOIN status AS s ON t.status_id = s.id
    JOIN users AS u ON t.user_id = u.id
    WHERE u.email LIKE ?;
    """

    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute(sql, (f"%@{user_domain}",))
        return cur.fetchall()

if __name__ == "__main__":
    target_domain = "example.com"  # gmail.com /ukr.net / example.org / example.com

    tasks = get_tasks_by_specific_user_domain(target_domain)
    if tasks:
        print(f"Tasks for users with email domain '{target_domain}':")
        for task in tasks:
            print(f"- ID: {task[0]} | Task: {task[1]} | Description: {task[2]} | Status: {task[3]} | User: {task[4]} | Email: {task[5]}")
    else:
        print(f"No tasks found for users with email domain '{target_domain}'.")


"""
For DBeaver:

SELECT 
    t.id, 
    t.title, 
    t.description, 
    s.name AS status, 
    u.fullname AS user_name, 
    u.email
FROM tasks AS t
JOIN status AS s ON t.status_id = s.id
JOIN users AS u ON t.user_id = u.id
WHERE u.email LIKE '%@example.com';

"""


