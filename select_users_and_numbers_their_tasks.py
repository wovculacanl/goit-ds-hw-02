import sqlite3

DATABASE = "users_tasks.db"

#  def get_users_and_task_numbers() -> list[tuple]:
#     """Отримує список користувачів та кількість їхніх завдань"""
#     sql = """
#     SELECT u.id, u.fullname, u.email, COUNT(t.id) AS task_count
#     FROM users u
#     LEFT JOIN tasks t ON u.id = t.user_id
#     GROUP BY u.id, u.fullname, u.email;
#     """

#     with sqlite3.connect(DATABASE) as con:
#         cur = con.cursor()
#         cur.execute(sql)
#         return cur.fetchall()


# Ordered by task count

def get_users_and_task_numbers(descending: bool = True) -> list[tuple]:
   
    order = "DESC" if descending else "ASC"

    
    sql = f"""
    SELECT u.id, u.fullname, u.email, COUNT(t.id) AS task_count
    FROM users u
    LEFT JOIN tasks t ON u.id = t.user_id
    GROUP BY u.id, u.fullname, u.email
    ORDER BY task_count {order};
    """

    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


if __name__ == "__main__":
    users_with_task_counts = get_users_and_task_numbers()
    if users_with_task_counts:
        print("Users and their task counts:")
        for user_id, fullname, email, task_count in users_with_task_counts:
            print(f"- User: {fullname} (ID: {user_id}, Email: {email}) | Task Count: {task_count}")
    else:
        print("No users found.")



        

"""For DBeaver:


SELECT 
    u.id AS user_id, 
    u.fullname, 
    u.email, 
    COUNT(t.id) AS task_count
FROM users u
LEFT JOIN tasks t ON u.id = t.user_id
GROUP BY u.id, u.fullname, u.email
ORDER BY task_count DESC;

"""