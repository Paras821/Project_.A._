
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

mycursor.execute("SELECT e.* FROM employees e LEFT JOIN departments d ON e.dept = d.name WHERE d.name IS NULL")

myresult = mycursor.fetchall()

if myresult:
    print("Employee(s) without a department:")
    for x in myresult:
        print(f" ID: {x[0]} | Name: {x[1]}")
else:
    print(" All employees belong to their respective departments ")

