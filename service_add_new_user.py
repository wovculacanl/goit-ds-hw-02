import sqlite3

DATABASE = "users_tasks.db"


def add_new_user(fullname: str, email: str) -> int | None:
    """
    Add a new user to the database.
   
    """
    sql = """
    INSERT INTO users (fullname, email)
    VALUES (?, ?);
    """

    try:
        with sqlite3.connect(DATABASE) as con:
            cur = con.cursor()
            cur.execute(sql, (fullname, email))
            con.commit()
            return cur.lastrowid
    except sqlite3.IntegrityError:
        print(f"User with email '{email}' already exists!")
        return None
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None


if __name__ == "__main__":
    print("=== Adding New User ===")
    user_name = input("Enter full name (fullname): ").strip()
    user_email = input("Enter email: ").strip()

    if not user_name or not user_email:
        print(" Error: name and email cannot be empty.")
    else:
        new_id = add_new_user(user_name, user_email)
        if new_id:
            print(f"User created successfully! Assigned ID: {new_id}")