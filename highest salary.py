
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT * FROM employees WHERE salary = (SELECT MAX(salary) FROM employees)"

mycursor.execute(sql)

myresult = mycursor.fetchall()
print("Highest salary in the company:")

for x in myresult:
    print(f" Salary: Rs.{x[4]} | Name: {x[1]} | ID: {x[0]}")

