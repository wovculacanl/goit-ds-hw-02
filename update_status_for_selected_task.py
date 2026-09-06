import sqlite3

DATABASE = "users_tasks.db"


def update_task_status(task_id: int, new_status: str) -> None:
    sql = """
    UPDATE tasks
    SET status_id = (
        SELECT id FROM status WHERE name = ?
    )
    WHERE id = ?;
    """

    try:
        with sqlite3.connect(DATABASE) as con:
            cur = con.cursor()
            cur.execute(sql, (new_status, task_id))
            con.commit()

            
            if cur.rowcount > 0:
                print(f"Status ID {task_id} successfully updated to '{new_status}'.")
            else:
                print(f"Task with ID {task_id} not found.")
    except sqlite3.Error as e:
        print(f"Error occurred while updating status: {e}")


if __name__ == "__main__":
    target_task_id = 4
    target_status = "in progress"  # 'new', 'in progress', 'completed'

    update_task_status(target_task_id, target_status)