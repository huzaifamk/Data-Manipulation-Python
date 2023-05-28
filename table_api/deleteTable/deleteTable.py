def deleteTable(conn):
    table_name = input('*** DELETE TABLE ***\n' + 'Enter table name: ')

    if table_name:
        # Delete a table
        conn.execute('''DROP TABLE IF EXISTS {table_name}'''.format(
            table_name=table_name))
        print('Table deleted successfully.' + '\n')
    else:
        print('No table name provided, no table deleted.' + '\n')
