
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT AVG(salary) FROM employees"

mycursor.execute(sql)

myresult = mycursor.fetchall()[0]

for x in myresult:
    print("Average Salary = Rs.",int(x))


sql = "SELECT id,name,salary FROM employees WHERE salary > (SELECT AVG(salary) FROM employees)"

mycursor.execute(sql)

myresult = mycursor.fetchall()

if myresult:
    print("\nEmployee(s) with salary greater than the average:")
    for x in myresult:
        print(f" ID: {x[0]} | Name: {x[1]} | Salary: Rs.{x[2]}")
else:
    print("No employees have a salary greater than the average")

