import sqlite3

DATABASE = "users_tasks.db"


def add_new_task(
    title: str, description: str, user_id: int, status_name: str = "new"
) -> int | None:
    """Adds a new task for a specific user.

    Task ID is generated automatically (AUTOINCREMENT).
    Status is determined by a subquery based on its textual name ('new', 'in progress', 'completed').
    Returns the ID of the created task or None in case of an error.
    """
    sql = """
    INSERT INTO tasks (title, description, status_id, user_id)
    VALUES (
        ?,
        ?,
        (SELECT id FROM status WHERE name = ?),
        ?
    );
    """

    try:
        with sqlite3.connect(DATABASE) as con:
            # Enabling foreign key constraint checking (to ensure user_id exists)
            con.execute("PRAGMA foreign_keys = ON;")
            cur = con.cursor()
            cur.execute(sql, (title, description, status_name, user_id))
            con.commit()
            return cur.lastrowid
    except sqlite3.IntegrityError as e:
        print(
            f"Foreign key error: user with ID {user_id} does not exist or status '{status_name}' is invalid. ({e})"
        )
        return None
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None


if __name__ == "__main__":
    print("=== Adding New Task ===")
    task_title = input("Enter task title: ").strip()
    task_desc = input("Enter task description: ").strip()
    target_user_id = input("Enter user ID: ").strip()
    task_status = (
        input("Enter task status (default 'new'): ").strip() or "new"
    )

    if not task_title or not target_user_id.isdigit():
        print("Error: title is required, and user ID must be a number.")
    else:
        new_task_id = add_new_task(
            task_title, task_desc, int(target_user_id), task_status
        )
        if new_task_id:
            print(
                f"Task added successfully! New task ID: {new_task_id} (assigned to user ID {target_user_id})"
            )



"""

For DBeaver:
SELECT t.id, t.title, t.description, s.name AS status, u.fullname AS user
FROM tasks t
JOIN status s ON t.status_id = s.id
JOIN users u ON t.user_id = u.id
WHERE t.user_id = 1;

"""           