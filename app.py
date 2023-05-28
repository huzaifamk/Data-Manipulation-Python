from database.connection import createConnection as cc
from table_api.createTable import createTable as ct
from table_api.deleteTable import deleteTable as dt
from table_api.listTables import listTables as lt
from users_api.insertUsers import insertUsers as iu

# Create a connection object
conn = cc.createConnection()

# List tables
lt.listTables(conn)

# Create table
ct.createTable(conn)

# Delete table
dt.deleteTable(conn)

# Insert users
iu.insertUsers(conn)

# Close connection
conn.close()
