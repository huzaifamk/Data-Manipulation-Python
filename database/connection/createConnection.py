import sqlite3
import os


def createConnection():

    # Get database name from environment variable
    # database_name = os.getenv('DATABASE_NAME')
    # print(database_name)

    # Or get database name from user input
    database_name = input(
        '*** DATABASE CONNECTION ***\n' + 'Enter database name: ')
    print("Connecting to database: {database_name}".format(
        database_name=database_name))

    if database_name:
        # Create a connection object
        conn = sqlite3.connect('./db/{database_name}.db'.format(
            database_name=database_name))
        print('Database connected successfully.' + '\n')
        return conn
    else:
        print('Database name is necessary to connect to database. You can enter database name even if it does not exist yet, and it will be created for you.' + '\n')
        createConnection()
