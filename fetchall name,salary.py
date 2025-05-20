
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

mycursor.execute("SELECT name, salary FROM employees")

myresult = mycursor.fetchall()

print("Employees' names and their salaries:")

for x in myresult:
    print(f" {x[0]} | Rs.{x[1]}")

