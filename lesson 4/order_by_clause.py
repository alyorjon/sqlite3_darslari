# LIMIT clause
# Following is the basic syntax of ORDER BY clause.

# SELECT column-list
# FROM table_name
# [WHERE condition]
# [ORDER BY column1, column2, .. columnN] [ASC | DESC];
#  ASC osib borish tartibida
# DESC kamayib borish tartibida
import sqlite3 as sql
con = sql.connect('database.db')
cur = con.cursor()
data = cur.execute("SELECT first_name FROM table1 ORDER BY age ASC")
print(data.fetchall())


data = cur.execute("SELECT first_name FROM table1 ORDER BY age DESC")
print(data.fetchall())