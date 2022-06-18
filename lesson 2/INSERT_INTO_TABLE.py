import sqlite3 as sql
# Syntax
# Following is the basic syntax of INSERT INTO statement.
# INSERT INTO TABLE_NAME [(column1, column2, column3,...columnN)]
# VALUES (value1, value2, value3,...valueN);

connect = sql.connect('database.db')
cursor = connect.cursor()

#  Birinchi usul
cursor.execute("INSERT INTO family (first_name,last_name,age) VALUES (:a,:s,:d)",{'a':"Alyorjon",'s':'Aminboyev','d':25})
connect.commit()

#  Ikkinchi usul
def func(ism,familya,yoshi):
    cursor.execute("INSERT INTO family (first_name,last_name,age) VALUES (:a,:s,:d)",{'a':ism,'s':familya,'d':yoshi})
    connect.commit()
    return True

func('Donyor','Aminboyev',20)




#  Vazifa
# Oila a'zolaringizni hammasini jadvalga kiriting.