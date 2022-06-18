# LIMIT clause
# Following is the basic syntax of SELECT statement with LIMIT clause.

# SELECT column1, column2, columnN
# FROM table_name
# LIMIT [no of rows]

import sqlite3 as sql
con = sql.connect('database.db')
cur = con.cursor()

data = cur.execute("SELECT first_name FROM table1 WHERE age = 42 LIMIT 2")
print(data.fetchall())