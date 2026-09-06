import sqlite3

DATABASE = "users_tasks.db"  


def get_tasks_status(status: str ) -> list:
    sql = """
    SELECT id, title, description, status_id, user_id
    FROM tasks
    WHERE status_id = (
    Select id
    FROM status
    WHERE name = ?
    );
    """

    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute(sql, (status,))
        return cur.fetchall()


if __name__ == "__main__":
    
    target_status = "new"  

    tasks = get_tasks_status(target_status)
    if tasks:
        print(f" Task with status={target_status}:")
        for task in tasks:
            print(f"- ID: {task[0]} | Task: {task[1]} | Description: {task[2]}")
    else:
        print(f"For status {target_status} no tasks found.")


"""
For DBeaver:

SELECT id, title, description, status_id, user_id
FROM tasks
WHERE status_id = (
    SELECT id 
    FROM status 
    WHERE name = 'new'
);

"""