
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT * FROM employees WHERE salary > 60000"

mycursor.execute(sql)

myresult = mycursor.fetchall()

print("Employee(s) whose salary is greater than Rs.60,000:")

for x in myresult:
    print(f" ID: {x[0]} | {x[1]} | Rs.{x[4]} salary | {x[3]} dept")

