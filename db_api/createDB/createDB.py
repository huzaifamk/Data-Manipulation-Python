import sqlite3


def createDB():
    try:
        conn = sqlite3.connect('./db/database.db')
        print("Database created successfully")
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
