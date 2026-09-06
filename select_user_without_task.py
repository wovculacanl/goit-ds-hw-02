import sqlite3

DATABASE = "users_tasks.db"

def get_users_without_tasks() -> list:
    sql = """
    SELECT id, fullname, email
    FROM users
    WHERE id NOT IN (
        SELECT user_id
        FROM tasks
        WHERE user_id IS NOT NULL
    );
    """

    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

if __name__ == "__main__":
    users = get_users_without_tasks()
    if users:
        print("Users without tasks:")
        for user in users:
            print(f"- ID: {user[0]} | Name: {user[1]} | Email: {user[2]}")
    else:
        print("No users found without tasks.")


"""
For DBeaver:

SELECT id, fullname, email
FROM users
WHERE id NOT IN (
    SELECT user_id
    FROM tasks
    WHERE user_id IS NOT NULL
);

"""