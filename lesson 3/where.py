import sqlite3 as sql
# Syntax
# Following is the basic syntax of SQLite SELECT statement with WHERE clause.

# SELECT column1, column2, columnN
# FROM table_name
# WHERE [condition]
connect = sql.connect('database.db')
cursor = connect.cursor()


data = cursor.execute("SELECT last_name FROM table1 WHERE age = 25")

print(data.fetchall())

data = cursor.execute("SELECT first_name FROM table1 WHERE age = 25 and age = 20")

print(data.fetchall())
data = cursor.execute("SELECT * FROM table1 WHERE age BETWEEN 28 and 18")

print(data.fetchall())

data = cursor.execute("SELECT * FROM table1 WHERE age =28 or age = 18")

print(data.fetchall())

data = cursor.execute("SELECT * FROM table1 WHERE age IS NOT NULL")

print(data.fetchall())

data = cursor.execute("SELECT * FROM table1 WHERE last_name LIKE 'Ami%' ")

print(data.fetchall())

data = cursor.execute("SELECT * FROM table1 WHERE last_name LIKE 'Ami%' ")

print(data.fetchall())

data = cursor.execute("SELECT * FROM table1 WHERE age IN (25) ")

print(data.fetchall())

data = cursor.execute("SELECT * FROM table1 WHERE age NOT IN (25) ")

print(data.fetchall())

data = cursor.execute("SELECT * FROM table1 WHERE age > (SELECT age FROM table1 WHERE first_name = 'Alyor' ) ")

print(data.fetchall())