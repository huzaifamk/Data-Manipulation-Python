def deleteTable(conn):
    # Delete a table
    conn.execute('''DROP TABLE IF EXISTS users;''')
    print('Table deleted successfully.')
