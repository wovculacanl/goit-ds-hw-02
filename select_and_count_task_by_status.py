import sqlite3

DATABASE = "users_tasks.db"


def get_tasks_count_by_status() -> list[tuple]:
   
    sql = """
    SELECT s.name, COUNT(t.id) AS task_count
    FROM status s
    LEFT JOIN tasks t ON s.id = t.status_id
    GROUP BY s.id, s.name;
    """

    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


if __name__ == "__main__":
    status_counts = get_tasks_count_by_status()

    if status_counts:
        print(" Numbers of tasks by status:")
        for status_name, count in status_counts:
            print(f"- {status_name}: {count}")
    else:
        print("_statuses not found.")


"""
For DBeaver:

SELECT 
    s.name AS status_name, 
    COUNT(t.id) AS task_count
FROM status s
LEFT JOIN tasks t ON s.id = t.status_id
GROUP BY s.id, s.name;

"""