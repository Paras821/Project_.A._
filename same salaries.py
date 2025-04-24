
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT name,salary FROM employees WHERE salary IN (SELECT salary FROM employees GROUP BY salary HAVING COUNT(salary) > 1)"

mycursor.execute(sql)

myresult = mycursor.fetchall()

if myresult:
    for name,salary in myresult:
        print(f"{name} earns a salary of {salary}")
else:
    print("No employees earning the same amount of salaries")

