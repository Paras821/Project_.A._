
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT name, salary, SUM(salary) OVER(ORDER BY salary DESC) AS cumulative_salary FROM employees"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(f"Name: {x[0]}, Salary: Rs.{x[1]}, Cumulative Salary: Rs.{x[2]}")

