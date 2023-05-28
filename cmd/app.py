import sqlite3
from api.createTable import createTable as api


# Check if database exists
# If not, create it
def createDB():
    try:
        conn = sqlite3.connect('./db/database.db')
        print("Database created successfully")
        api.createTable()
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


createDB()
api.createTable()
