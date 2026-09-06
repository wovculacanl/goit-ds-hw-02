import sqlite3

DATABASE = "users_tasks.db"


def get_users_and_tasks_by_status(status_name: str) -> list:
   
    sql = """
    SELECT 
        u.id, 
        u.fullname, 
        u.email, 
        t.id, 
        t.title, 
        t.description
    FROM users u
    INNER JOIN tasks t ON u.id = t.user_id
    INNER JOIN status s ON t.status_id = s.id
    WHERE s.name = ?;
    """

    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute(sql, (status_name,))
        return cur.fetchall()


if __name__ == "__main__":
    status = "in progress"

    results = get_users_and_tasks_by_status(status)
    if results:
        print(f"Tasks with status '{status}' and their assignees:")
        for row in results:
            user_id, fullname, email, task_id, title, description = row
            print(f"- User: {fullname} (ID: {user_id}) | Task [{task_id}]: '{title}'")
    else:
        print(f"No tasks found with status '{status}'.")


"""
For DBeaver:

SELECT 
    u.id AS user_id, 
    u.fullname, 
    u.email, 
    t.id AS task_id, 
    t.title AS task_title, 
    t.description AS task_description
FROM users u
INNER JOIN tasks t ON u.id = t.user_id
INNER JOIN status s ON t.status_id = s.id
WHERE s.name = 'in progress';

"""
