
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT id, name, salary, ROUND((salary / total.total_salary) * 100, 2) AS salary_percentage FROM employees, (SELECT SUM(salary) AS total_salary FROM employees) AS total"

mycursor.execute(sql)

myresult = mycursor.fetchall()

print("Employee Salary Percentages:")

for x in myresult:
    print(f" ID: {x[0]} | Name: {x[1]} | Salary: Rs.{x[2]} -- {x[3]}%")

