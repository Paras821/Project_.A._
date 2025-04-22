
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = " SELECT employees.name FROM employees JOIN mydatabase.departments ON dept = name "

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

##

