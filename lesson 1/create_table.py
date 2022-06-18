import sqlite3 as sql
# Syntax
# Following is the basic syntax of CREATE TABLE statement.

# CREATE TABLE database_name.table_name(
# column1 datatype PRIMARY KEY(one or more columns),
# column2 datatype,
# column3 datatype,
# .....
# columnN datatype
# );
#  connect with database

connect = sql.connect('database.db')
cursor = connect.cursor()

#  Create table
cursor.execute("CREATE TABLE family (user_id INTEGER PRIMARY KEY AUTOINCREMENT,first_name TEXT,last_name TEXT, age INTEGER)")

#  Tasdiqlaymiz.
connect.commit()



# Agar jadval mavjud bolsa quyidagicha boladi.
# Syntax
# Following is the basic syntax of CREATE TABLE statement.

# CREATE TABLE IF NOT EXISTS database_name.table_name(
# column1 datatype PRIMARY KEY(one or more columns),
# column2 datatype,
# column3 datatype,
# .....
# columnN datatype
# );
#  connect with database
cursor.execute("CREATE TABLE IF NOT EXISTS family (user_id INTEGER PRIMARY KEY AUTOINCREMENT,first_name TEXT,last_name TEXT, age INTEGER)")
#  Tasdiqlaymiz.
connect.commit()
connect.close()
