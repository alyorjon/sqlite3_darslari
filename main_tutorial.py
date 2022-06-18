import sqlite3 as sql

#  Ma'lumotlar omboriga bog'lanamiz.
connect = sql.connect('database.db')
cursor = connect.cursor()

# Jadval yaratish
cursor.execute("CREATE TABLE IF NOT EXISTS table_name_1 (column_1 INTEGER PRIMARY KEY,column_2 TEXT)")
connect.commit()


#  SELECT COLUMN FROM TABLE WHERE CONDITION TRUE

jadval = cursor.execute("SELECT column_1 FROM table_name_1")

#


