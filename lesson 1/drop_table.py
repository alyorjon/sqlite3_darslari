import sqlite3 as sql
# Syntax
# Following is the basic syntax of DROP TABLE statement. You can optionally specify the database name along with table name as follows −

# DROP TABLE database_name.table_name;
connect = sql.connect('database.db')
cursor = connect.cursor()

#  Create table
cursor.execute("DROP TABLE family")

#  Tasdiqlaymiz.
connect.commit()
connect.close()


