
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT name, dept, salary FROM employees e WHERE salary = (SELECT MIN(salary) FROM employees WHERE dept = e.dept)"

mycursor.execute(sql)

myresult = mycursor.fetchall()

if myresult:
    print("Employees who earn the least in each dept:")
    for x in myresult:
        print(f"Name: {x[0]}, Dept: {x[1]}, Salary: Rs.{x[2]}")
else:
    print("No employee data found")

