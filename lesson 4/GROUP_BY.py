# GROUP BY clause
# Following is the basic syntax of GROUP BY clause. GROUP BY clause must follow the conditions in the WHERE clause and must precede ORDER BY clause if one is used.

# SELECT column-list
# FROM table_name
# WHERE [ conditions ]
# GROUP BY column1, column2....columnN
# ORDER BY column1, column2....columnN
#  ASC osib borish tartibida
# DESC kamayib borish tartibida
import sqlite3 as sql
con = sql.connect('database.db')
cur = con.cursor()
data = cur.execute("SELECT first_name FROM table1 GROUP BY last_name ")
print(data.fetchall())