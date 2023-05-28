def deleteTable(conn):

    # Ask user if they want to delete a table
    delete_table = input('Delete a table? (y/n): ')

    if delete_table == 'y' or delete_table == 'Y':

        table_name = input('*** DELETE TABLE ***\n' + 'Enter table name: ')

        if table_name:
            # Delete the table
            conn.execute('''DROP TABLE IF EXISTS {table_name}'''.format(
                table_name=table_name))
            print('Table deleted successfully.' + '\n')
        else:
            print('No table name provided, no table deleted.' + '\n')

    elif delete_table == 'n' or delete_table == 'N':
        print('OK, moving forward.' + '\n')
