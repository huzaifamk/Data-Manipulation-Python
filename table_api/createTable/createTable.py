def createTable(conn):

    # import os
    # Get table name from environment variable
    # table_name = os.getenv('TABLE_NAME')

    # Or get table name from user input
    table_name = input('*** CREATE TABLE ***\n' + 'Enter table name: ')
    print("Creating table: {table_name}".format(table_name=table_name))

    if table_name:
        # Create a table
        conn.execute('''CREATE TABLE IF NOT EXISTS {table_name}
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL,
                        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP);'''.format(
            table_name=table_name))
        print('Table created successfully.' + '\n')
    else:
        print('No table name provided, no table created.' + '\n')
