import sqlite3 as sql
con = sql.connect('database.db')
cur = con.cursor()
data = cur.execute("SELECT * FROM table1 WHERE last_name LIKE 'A%'")
print(data.fetchall())


data = cur.execute("SELECT * FROM table1 WHERE last_name LIKE '%boy%'")
print(data.fetchall())

data = cur.execute("SELECT * FROM table1 WHERE last_name LIKE 'Aminboye_'")
print(data.fetchall())


data = cur.execute("SELECT * FROM table1 WHERE last_name LIKE '_minboye_'")
print(data.fetchall())

data = cur.execute("SELECT * FROM table1 WHERE last_name LIKE '__inboyev'")
print(data.fetchall())