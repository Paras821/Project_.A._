
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT id, name, salary FROM employees WHERE salary >= 1.2 * (SELECT AVG(salary) FROM employees)"

mycursor.execute(sql)

myresult = mycursor.fetchall()

if myresult:
    print("Employee(s) earning at least 20% more than the avg salary:")
    for x in myresult:
        print(f" ID: {x[0]} | Name: {x[1]} | Salary: Rs.{x[2]}")
else:
    print("No employee earns at least 20% more than the avg salary")

