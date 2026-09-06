import sqlite3

DATABASE = "users_tasks.db"


def delete_task_by_id(task_id: int) -> bool:
   
    sql = "DELETE FROM tasks WHERE id = ?;"

    try:
        with sqlite3.connect(DATABASE) as con:
            cur = con.cursor()
            cur.execute(sql, (task_id,))
            con.commit()

            if cur.rowcount > 0:
                print(f"Task with ID {task_id} successfully deleted.")
                return True
            else:
                print(f"Task with ID {task_id} not found.")
                return False
    except sqlite3.Error as e:
        print(f"Error occurred while deleting task: {e}")
        return False


if __name__ == "__main__":
    task_id_input = input("Enter task ID to delete: ").strip()

    if task_id_input.isdigit():
        delete_task_by_id(int(task_id_input))
    else:
        print("Error: Task ID must be a number.")