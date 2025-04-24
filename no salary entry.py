
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

mycursor.execute("SELECT * FROM employees WHERE salary = 0")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

print(" None \n All employees have their salaries entried ")

