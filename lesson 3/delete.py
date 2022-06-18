import sqlite3 as sql
# Syntax
# Following is the basic syntax of DELETE query with WHERE clause.

# DELETE FROM table_name
# WHERE [condition];
connect = sql.connect('database.db')
cursor = connect.cursor()

cursor.execute("DELETE FROM table1 WHERE first_name ='Alyorjon' ")
connect.commit()