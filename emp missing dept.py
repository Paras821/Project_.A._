
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

mycursor.execute("SELECT * FROM employees WHERE dept IS NULL")

myresult = mycursor.fetchall()

if myresult:
    print("Employee(s) with dept info missing:\n")
    for x in myresult:
        print(f" ID: {x[0]} | Name: {x[1]}")
else:
    print(" All employees have their respective dept info filled ")

