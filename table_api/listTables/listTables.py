# Create a listTables function which will list all tables in the database named myapp
def listTables(conn):
    # Create a cursor object
    cursor = conn.cursor()
    # Get all tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    # Get all rows in the result set
    tables = cursor.fetchall()
    # Print all rows in the result set
    for table in tables:
        print(table)
    # Close cursor
    cursor.close()
