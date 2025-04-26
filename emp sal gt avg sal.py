
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT AVG(salary) FROM employees"

mycursor.execute(sql)

myresult = mycursor.fetchall()[0]

for x in myresult:
    print("Average Salary = Rs.",int(x))



import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT name,salary FROM employees WHERE salary > (SELECT AVG(salary) FROM employees)"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(f"{x[0]}'s Salary = RS.{x[1]}")

