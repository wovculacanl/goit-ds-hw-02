
import sqlite3

DATABASE = "users_tasks.db"

def get_tasks_without_description() -> list:
   
    sql = """
    SELECT id, title, description, status_id, user_id
    FROM tasks
    WHERE description IS NULL OR description = '';
    """

    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
if __name__ == "__main__":
    tasks = get_tasks_without_description()
    if tasks:
        print("Tasks without description:")
        for task in tasks:
            print(f"- ID: {task[0]} | Task: {task[1]} | Description: {task[2]}")
    else:
        print("No tasks found without description.")


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
LEFT JOIN status AS s ON t.status_id = s.id
LEFT JOIN users AS u ON t.user_id = u.id
WHERE t.description IS NULL OR TRIM(t.description) = ''; 

"""