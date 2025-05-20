
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

mycursor.execute("SELECT * FROM employees WHERE salary IS NULL")

myresult = mycursor.fetchall()

if myresult:
    print("Employee(s) without salary entries:\n")
    for x in myresult:
        print(f" ID: {x[0]} | Name: {x[1]}")
else:
    print(" All employees have their salaries filed ")

