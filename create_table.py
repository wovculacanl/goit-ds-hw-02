from sqlite3 import Error
from connect import create_connection, database
from seed import NUMBER_OF_TASKS, NUMBER_OF_USERS, generate_fake_data, insert_data_to_db


def create_table(conn, create_table_sql):
    """create a table from the create_table_sql statement"""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # users table
    sql_create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     fullname VARCHAR(100) NOT NULL,
     email VARCHAR(100) NOT NULL UNIQUE
    );
    """

    # status table
    sql_create_status_table = """
    CREATE TABLE IF NOT EXISTS status (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     name VARCHAR(50) NOT NULL UNIQUE
    );
    """

    # tasks table
    sql_create_tasks_table = """
    CREATE TABLE IF NOT EXISTS tasks (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     title VARCHAR(100) NOT NULL,
     description TEXT,
     status_id INTEGER,
     user_id INTEGER,
     FOREIGN KEY (status_id) REFERENCES status (id),
     FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
    );
    """

    with create_connection(database) as conn:
        if conn is not None:
            
            conn.execute("PRAGMA foreign_keys = ON;")

            # Table creation
            create_table(conn, sql_create_users_table)
            create_table(conn, sql_create_status_table)
            create_table(conn, sql_create_tasks_table)
            print("Tables created successfully.")

            # Data generation and insertion
            users, statuses, tasks = generate_fake_data(NUMBER_OF_USERS, NUMBER_OF_TASKS)
            insert_data_to_db(conn, users, statuses, tasks)
        else:
            print("Error! Cannot create the database connection.")