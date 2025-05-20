
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT id, name, salary, SUM(salary) OVER (ORDER BY salary DESC, id ASC) AS cumulative_salary FROM employees"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(f" ID: {x[0]} | Name: {x[1]} | Salary: Rs.{x[2]} | Cumulative Salary: Rs.{x[3]}")

