import sqlite3 as sql
# Syntax
# Following is the basic syntax of SELECT  statement.
#SELECT column1, column2, columnN FROM table_name;

#  Hammasini bitta belgilash
# SELECT * FROM table_name;
connect = sql.connect('database.db')
cursor = connect.cursor()

data = cursor.execute("SELECT first_name,last_name,age FROM table1")
print(data.fetchall())

data2 = cursor.execute("SELECT first_name,last_name,age FROM table1 WHERE age = 20")

print(data2.fetchall())

data2 = cursor.execute("SELECT first_name,last_name,age FROM table1 WHERE age BETWEEN 18 and 30")

print(data2.fetchall())



# Vazifa
#  1.oila azolaringizni yoshidan kelib chiqib chiqarib bering.
# 2. Mustaqil ravishda moshina, davlat ,shahar jadvalini yarating. Va ma'lumotlar bilan ishlang.