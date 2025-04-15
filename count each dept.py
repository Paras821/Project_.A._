
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

mycursor.execute("SELECT COUNT(id) AS NumberOfEmployees FROM employees WHERE dept = 'IT'")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

mycursor.execute("SELECT COUNT(id) AS NumberOfEmployees FROM employees WHERE dept = 'HR'")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

mycursor.execute("SELECT COUNT(id) AS NumberOfEmployees FROM employees WHERE dept = 'Finance'")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

