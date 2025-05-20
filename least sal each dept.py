
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT id, name, dept, salary FROM employees e WHERE salary = (SELECT MIN(salary) FROM employees WHERE dept = e.dept)"

mycursor.execute(sql)

myresult = mycursor.fetchall()

if myresult:
    print("Employees who earn the least in each dept:")
    for x in myresult:
        print(f" Dept: {x[2]} | ID: {x[0]} | Name: {x[1]} | Salary: Rs.{x[3]}")
else:
    print("No employee data found")

