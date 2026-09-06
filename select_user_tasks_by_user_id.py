import sqlite3

DATABASE = "users_tasks.db"  


def get_tasks_by_user_id(user_id: int) -> list:
    sql = """
    SELECT id, title, description, status_id, user_id
    FROM tasks
    WHERE user_id = ?;
    """

    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute(sql, (user_id,))
        return cur.fetchall()


if __name__ == "__main__":
    target_user_id = 2  

    tasks = get_tasks_by_user_id(target_user_id)

    if tasks:
        print(f" Task of user with id={target_user_id}:")
        for task in tasks:
            print(f"- ID: {task[0]} | Task: {task[1]} | Description: {task[2]}")
    else:
        print(f"For user with id {target_user_id} no tasks found.")



"""

For DBeaver:

SELECT 
    t.id AS task_id,
    t.title,
    t.description,
    s.name AS status,
    u.fullname AS user_name
FROM tasks AS t
JOIN status AS s ON t.status_id = s.id
JOIN users AS u ON t.user_id = u.id
WHERE t.user_id = 1;

"""       