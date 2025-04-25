
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

mycursor.execute("CREATE TABLE employees_backup AS SELECT * FROM employees")

myresult = mycursor.fetchall()

for x in myresult:
    print(x, "The data has been copied")

