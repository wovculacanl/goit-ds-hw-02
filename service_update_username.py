import sqlite3

DATABASE = "users_tasks.db"

def update_username(user_id: int, new_fullname: str) -> bool:

    sql = "UPDATE users SET fullname = ? WHERE id = ?;"

    try:
        with sqlite3.connect(DATABASE) as con:
            cur = con.cursor()
            cur.execute(sql, (new_fullname, user_id))
            con.commit()
            return cur.rowcount > 0  # Returns True if a row was updated, False otherwise
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False

if __name__ == "__main__":
    user_id_input = input("Enter user ID to update: ").strip()
    new_fullname_input = input("Enter new full name: ").strip()

    if not user_id_input.isdigit():
        print("Error: User ID must be a number.")
    elif not new_fullname_input:
        print("Error: New full name cannot be empty.")
    else:
        success = update_username(int(user_id_input), new_fullname_input)
        if success:
            print(f"User ID {user_id_input} updated successfully to '{new_fullname_input}'.")
        else:
            print(f"User ID {user_id_input} not found or update failed.")