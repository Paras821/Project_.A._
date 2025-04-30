
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT e.name, d.name, d.location FROM employees e JOIN departments d ON e.dept = d.name WHERE location = 'Paris' LIMIT 1"

mycursor.execute(sql)

myresults = mycursor.fetchall()

if not myresults:
    print("No result found")
else:
    for x in myresults:
        employee_name, departments_name, departments_location = x
        print(f"Employee: {employee_name}, Department: {departments_name}, Located: {departments_location}")

