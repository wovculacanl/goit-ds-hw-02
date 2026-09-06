
import sqlite3

DATABASE = "users_tasks.db"


def get_users_by_email_pattern(email_pattern: str) -> list:
    
    sql = """
    SELECT id, fullname, email
    FROM users
    WHERE email LIKE ?;
    """

    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute(sql, (email_pattern,))
        return cur.fetchall()


if __name__ == "__main__":
    
    target_pattern = "%@example.org"   # %@gmail.com / %@yahoo.com / %@example.org

    users = get_users_by_email_pattern(target_pattern)

    if users:
        print(f"Users found with email pattern '{target_pattern}':")
        for user in users:
            print(f"- ID: {user[0]} | Name: {user[1]} | Email: {user[2]}")
    else:
        print("No users found with this email pattern.")


"""
For DBeaver:

SELECT id, fullname, email
FROM users
WHERE email LIKE '%@example.org';



SELECT id, fullname, email
FROM users
WHERE email LIKE 'nelsonchristopher@example.org';


"""