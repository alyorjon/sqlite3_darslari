
import sqlite3 as sql
# Syntax
# Following is the basic syntax of UPDATE query with WHERE clause.

# UPDATE table_name
# SET column1 = value1, column2 = value2...., columnN = valueN
# WHERE [condition];
connect = sql.connect('database.db')
cursor = connect.cursor()
data = []
for  i in range(21,24):
    data1 = []
    data1.append(f"Ism {i}")
    data1.append(f"Familya {i}")
    data1.append(20+i)
    data.append(data1)
for k,i in enumerate(data):
    cursor.execute("INSERT INTO table1 (first_name,last_name,age)VALUES (:a,:s,:d) ",{'a':i[0],'s':i[1],'d':i[2]})
    cursor.execute("UPDATE table1 SET first_name=(:a),last_name=(:s),age=(:d) WHERE user_id=(:f) ",{'a':i[0],'s':i[1],'d':i[2],'f':k})
# cursor.execute()
connect.commit()