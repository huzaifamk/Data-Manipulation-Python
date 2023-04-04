import sqlite3

conn = sqlite3.connect('./db/data.db')

conn.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             email TEXT NOT NULL,
             username TEXT NOT NULL,
             password TEXT NOT NULL,
             created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
             updated_at DATETIME DEFAULT CURRENT_TIMESTAMP);''')

conn.close()
