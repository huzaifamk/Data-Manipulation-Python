# Import connection from cmd/app.py
from . import conn


def createTable():
    # Create a table
    conn.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 email TEXT NOT NULL,
                 username TEXT NOT NULL,
                 password TEXT NOT NULL,
                 created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                 updated_at DATETIME DEFAULT CURRENT_TIMESTAMP);''')
    # Close connection
    conn.close()
