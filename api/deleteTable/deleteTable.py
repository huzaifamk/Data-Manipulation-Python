import sqlite3


def deleteTable():
    conn = sqlite3.connect('./db/database.db')
    # Delete a table
    conn.execute('''DROP TABLE IF EXISTS users''')
    # Close connection
    conn.close()
