
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = " SELECT DISTINCT employees.name AS emplyee_name, departments.name AS department_name FROM employees INNER JOIN departments ON employees.dept = departments.name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for employee_name,department_name in myresult:
    print(f"{employee_name} works in the {department_name} dept")

