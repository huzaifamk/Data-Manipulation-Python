import sqlite3
from api.createDB import createDB as db
from api.createTable import createTable as ct
from api.deleteTable import deleteTable as dt
from database.connection import createConnection as cc

# Create a connection object
conn = cc.createConnection()

# Create table
ct.createTable(conn)

# # Delete table
# dt.deleteTable()
