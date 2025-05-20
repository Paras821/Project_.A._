
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT * FROM employees WHERE salary BETWEEN 50000 AND 70000"

mycursor.execute(sql)

myresult = mycursor.fetchall()
print("Employee(s) with salary between Rs.50,000 and Rs.70,000:")

for x in myresult:
    print(f" ID: {x[0]} | Name: {x[1]} | Salary: Rs.{x[4]}")

