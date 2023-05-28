import sqlite3

# Create a function that will connect to the database and return the connection object


def createConnection():
    conn = sqlite3.connect('./db/database.db')
    print("Connection created successfully")
    return conn
