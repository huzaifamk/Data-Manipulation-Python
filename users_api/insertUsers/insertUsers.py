def insertUsers(conn):

    # Get user input
    table_name = input('*** INSERT USERS ***\n' +
                       'Enter table name to insert users(Leave blank to skip): ')

    if not table_name:
        print('No table name provided, no users inserted.' + '\n')
        exit()

    name = input('Enter name: ')
    email = input('Enter email: ')
    username = input('Enter username: ')
    password = input('Enter password: ')

    if table_name:
     # Create a cursor object
        cur = conn.cursor()
        # Insert user
        cur.execute('''INSERT INTO {table_name} (name, email, username, password, created_at, updated_at)
        VALUES ('{name}', '{email}', '{username}', '{password}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);'''.format(table_name=table_name, name=name, email=email, username=username, password=password))

        # Commit changes
        conn.commit()

    # Ask user if they want to insert another user
    insert_another = input('Insert another user? (y/n): ')

    # If user enters 'y' or 'Y', call insertUsers() again
    if insert_another == 'y' or insert_another == 'Y':
        insertUsers(conn)
    # If user enters 'n' or 'N', exit the program
    elif insert_another == 'n' or insert_another == 'N':
        print('Exiting program.')
        exit()
    # If user enters anything else, exit the program
    else:
        print('Invalid input, exiting program.')
        exit()
